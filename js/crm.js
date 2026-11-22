import { createClient } from "https://esm.sh/@supabase/supabase-js@2";

const config = window.ACADEMY_SUPABASE_CONFIG;
const authScreen = document.querySelector("#auth-screen");
const authForm = document.querySelector("#auth-form");
const authMessage = document.querySelector("#auth-message");
const authSubmit = document.querySelector("#auth-submit");
const authMode = document.querySelector("#auth-mode");
const authTitle = document.querySelector("#auth-title");
const authIntro = document.querySelector(".auth-intro");
const authFootnote = document.querySelector(".auth-footnote");
const dashboard = document.querySelector("#dashboard");
const dashboardMessage = document.querySelector("#dashboard-message");
const leadsBody = document.querySelector("#leads-body");
const leadDialog = document.querySelector("#lead-dialog");
const editForm = document.querySelector("#lead-edit-form");
const statusNames = {
  new: "New",
  contacted: "Contacted",
  interested: "Interested",
  follow_up: "Follow-up",
  enrolled: "Enrolled",
  not_interested: "Not interested",
};
let supabase;
let leads = [];
let activeLeadId = null;
let creatingAccount = false;

function setMessage(node, message, isError = false) {
  node.textContent = message;
  node.classList.toggle("is-error", isError);
}

function showAuth(message = "", isError = false) {
  dashboard.hidden = true;
  authScreen.hidden = false;
  setMessage(authMessage, message, isError);
}

function showDashboard() {
  authScreen.hidden = true;
  dashboard.hidden = false;
  setMessage(dashboardMessage, "");
}

function normalizeEmail(value) {
  return value.trim().toLowerCase();
}

function formatDate(value) {
  if (!value) return "—";
  const date = new Date(value);
  if (Number.isNaN(date.getTime())) return "—";
  return new Intl.DateTimeFormat("en-IN", {
    day: "numeric",
    month: "short",
    year: "numeric",
    timeZone: "Asia/Kolkata",
  }).format(date);
}

function setCell(row, value, className = "") {
  const cell = document.createElement("td");
  cell.textContent = value;
  if (className) cell.className = className;
  row.append(cell);
  return cell;
}

function renderLeads() {
  const search = document.querySelector("#lead-search").value.trim().toLowerCase();
  const selectedStatus = document.querySelector("#status-filter").value;
  const visible = leads.filter((lead) => {
    const matchesStatus = selectedStatus === "all" || lead.status === selectedStatus;
    const searchable = [lead.name, lead.phone, lead.email, lead.course_interest, lead.message]
      .filter(Boolean)
      .join(" ")
      .toLowerCase();
    return matchesStatus && searchable.includes(search);
  });

  leadsBody.replaceChildren();
  if (!visible.length) {
    const row = document.createElement("tr");
    const cell = setCell(row, leads.length ? "No enquiries match these filters." : "No enquiries yet. Website submissions will appear here.", "table-message");
    cell.colSpan = 6;
    leadsBody.append(row);
  } else {
    visible.forEach((lead) => {
      const row = document.createElement("tr");
      const prospectCell = document.createElement("td");
      const prospectName = document.createElement("span");
      prospectName.className = "prospect-name";
      prospectName.textContent = lead.name;
      const phoneLink = document.createElement("a");
      phoneLink.className = "prospect-phone";
      phoneLink.href = `tel:${lead.phone.replace(/[^+\d]/g, "")}`;
      phoneLink.textContent = lead.phone;
      prospectCell.append(prospectName, phoneLink);
      row.append(prospectCell);

      const courseCell = setCell(row, lead.course_interest, "");
      const courseName = document.createElement("span");
      courseName.className = "course-name";
      courseName.textContent = lead.course_interest;
      courseCell.replaceChildren(courseName);

      const statusCell = document.createElement("td");
      const statusPill = document.createElement("span");
      statusPill.className = `status-pill status-${lead.status}`;
      statusPill.textContent = statusNames[lead.status] || "New";
      statusCell.append(statusPill);
      row.append(statusCell);
      setCell(row, lead.source.replaceAll("-", " "), "source-label");
      setCell(row, formatDate(lead.created_at), "date-label");
      const actionCell = document.createElement("td");
      const editButton = document.createElement("button");
      editButton.className = "row-action";
      editButton.type = "button";
      editButton.dataset.editLead = lead.id;
      editButton.setAttribute("aria-label", `Update enquiry for ${lead.name}`);
      editButton.textContent = "Update";
      actionCell.append(editButton);
      row.append(actionCell);
      leadsBody.append(row);
    });
  }

  document.querySelector("#stat-total").textContent = String(leads.length);
  document.querySelector("#stat-new").textContent = String(leads.filter((lead) => lead.status === "new").length);
  document.querySelector("#stat-follow-up").textContent = String(leads.filter((lead) => lead.status === "follow_up").length);
  document.querySelector("#stat-enrolled").textContent = String(leads.filter((lead) => lead.status === "enrolled").length);
  document.querySelector("#sidebar-lead-count").textContent = String(leads.length);
  document.querySelector("#results-count").textContent = `${visible.length} of ${leads.length} recent enquiries`;
  document.querySelector("#follow-up-summary").textContent = "Times shown in Bengaluru time · up to 1,000 recent records";
}

async function loadLeads() {
  setMessage(dashboardMessage, "Loading recent enquiries…");
  const { data, error } = await supabase
    .from("leads")
    .select("id, name, phone, email, course_interest, message, source, status, follow_up_at, notes, created_at, updated_at")
    .order("created_at", { ascending: false })
    .limit(1000);

  if (error) {
    setMessage(dashboardMessage, "Could not load enquiries. Please sign in again or contact the workspace owner.", true);
    return;
  }

  leads = data || [];
  renderLeads();
  setMessage(dashboardMessage, "");
}

async function enterDashboard(session) {
  if (!session?.user?.email) {
    showAuth("Sign in with your invited academy email to continue.");
    return;
  }

  const { data, error } = await supabase
    .from("crm_admins")
    .select("email")
    .maybeSingle();

  if (error || !data) {
    await supabase.auth.signOut();
    showAuth("This email does not have CRM access yet. Ask the academy owner to add it to the admin list.", true);
    return;
  }

  showDashboard();
  await loadLeads();
}

function updateAuthMode() {
  creatingAccount = !creatingAccount;
  authTitle.textContent = creatingAccount ? "Create your account." : "Welcome back.";
  authIntro.textContent = creatingAccount
    ? "Create an account with the email address approved by the academy owner."
    : "Sign in with an invited academy email to manage course enquiries and follow-ups.";
  authSubmit.innerHTML = creatingAccount ? 'Create account <span aria-hidden="true">→</span>' : 'Sign in <span aria-hidden="true">→</span>';
  document.querySelector("#auth-password").autocomplete = creatingAccount ? "new-password" : "current-password";
  authMode.textContent = creatingAccount ? "Already have an account? Sign in" : "Need an account? Create one";
  authMode.setAttribute("aria-pressed", String(creatingAccount));
  authFootnote.textContent = creatingAccount
    ? "Creating an account does not grant CRM access. Only emails added to the academy admin list can view enquiries."
    : "Only an email added to the academy admin list can view lead details. Admin access is not configured yet.";
  setMessage(authMessage, "");
}

function setDateTimeInput(value) {
  if (!value) return "";
  const date = new Date(value);
  if (Number.isNaN(date.getTime())) return "";
  return new Date(date.getTime() - date.getTimezoneOffset() * 60000).toISOString().slice(0, 16);
}

function openEditor(lead) {
  activeLeadId = lead.id;
  document.querySelector("#dialog-title").textContent = "Update enquiry";
  document.querySelector("#dialog-prospect").textContent = `${lead.name} · ${lead.phone}${lead.email ? ` · ${lead.email}` : ""}`;
  document.querySelector("#edit-status").value = lead.status;
  document.querySelector("#edit-source").value = lead.source;
  document.querySelector("#edit-follow-up").value = setDateTimeInput(lead.follow_up_at);
  document.querySelector("#edit-notes").value = lead.notes || "";
  setMessage(document.querySelector("#dialog-message"), "");
  leadDialog.showModal();
}

function csvValue(value) {
  return `"${String(value ?? "").replaceAll('"', '""')}"`;
}

function exportLeads() {
  const columns = ["name", "phone", "email", "course_interest", "status", "source", "follow_up_at", "notes", "created_at"];
  const rows = [columns.join(","), ...leads.map((lead) => columns.map((column) => csvValue(lead[column])).join(","))];
  const blob = new Blob(["\uFEFF", rows.join("\r\n")], { type: "text/csv;charset=utf-8" });
  const url = URL.createObjectURL(blob);
  const link = document.createElement("a");
  link.href = url;
  link.download = `academy-enquiries-${new Date().toISOString().slice(0, 10)}.csv`;
  document.body.append(link);
  link.click();
  link.remove();
  URL.revokeObjectURL(url);
}

if (!config?.url || !config?.publishableKey) {
  authSubmit.disabled = true;
  authMode.disabled = true;
  setMessage(authMessage, "CRM storage is not configured for this deployment. Please contact the site owner.", true);
} else {
  supabase = createClient(config.url, config.publishableKey, {
    auth: {
      storage: window.sessionStorage,
      persistSession: true,
      autoRefreshToken: true,
      detectSessionInUrl: true,
    },
  });

  const { data: { session } } = await supabase.auth.getSession();
  if (session) await enterDashboard(session);
}

authMode.addEventListener("click", updateAuthMode);

authForm.addEventListener("submit", async (event) => {
  event.preventDefault();
  if (!supabase) return;
  if (!authForm.reportValidity()) return;

  const email = normalizeEmail(authForm.elements.email.value);
  const password = authForm.elements.password.value;
  authSubmit.disabled = true;
  setMessage(authMessage, creatingAccount ? "Creating your account…" : "Signing in…");

  if (creatingAccount) {
    const { data, error } = await supabase.auth.signUp({
      email,
      password,
      options: { emailRedirectTo: `${window.location.origin}/crm.html` },
    });
    authSubmit.disabled = false;
    if (error) {
      setMessage(authMessage, "Could not create the account. Check the password and try again, or sign in if you already registered.", true);
      return;
    }
    if (data.session) {
      await enterDashboard(data.session);
    } else {
      setMessage(authMessage, "Check your email to confirm the account. CRM access still requires owner approval for this address.");
    }
    return;
  }

  const { data, error } = await supabase.auth.signInWithPassword({ email, password });
  authSubmit.disabled = false;
  if (error) {
    setMessage(authMessage, "Unable to sign in. Check your email and password, then try again.", true);
    return;
  }
  await enterDashboard(data.session);
});

document.querySelector("#sign-out").addEventListener("click", async () => {
  await supabase.auth.signOut();
  leads = [];
  showAuth("You are signed out.");
});

document.querySelector("#lead-search").addEventListener("input", renderLeads);
document.querySelector("#status-filter").addEventListener("change", renderLeads);
document.querySelector("#export-csv").addEventListener("click", exportLeads);

leadsBody.addEventListener("click", (event) => {
  const button = event.target.closest("[data-edit-lead]");
  if (!button) return;
  const lead = leads.find((item) => item.id === button.dataset.editLead);
  if (lead) openEditor(lead);
});

document.querySelector("#dialog-close").addEventListener("click", () => leadDialog.close());
document.querySelector("#dialog-cancel").addEventListener("click", () => leadDialog.close());

editForm.addEventListener("submit", async (event) => {
  event.preventDefault();
  const saveButton = document.querySelector("#save-lead");
  const followUpValue = document.querySelector("#edit-follow-up").value;
  const updates = {
    status: document.querySelector("#edit-status").value,
    source: document.querySelector("#edit-source").value,
    follow_up_at: followUpValue ? new Date(followUpValue).toISOString() : null,
    notes: document.querySelector("#edit-notes").value.trim(),
  };
  saveButton.disabled = true;
  setMessage(document.querySelector("#dialog-message"), "Saving updates…");
  const { error } = await supabase.from("leads").update(updates).eq("id", activeLeadId);
  saveButton.disabled = false;
  if (error) {
    setMessage(document.querySelector("#dialog-message"), "Could not save changes. Please try again.", true);
    return;
  }
  leadDialog.close();
  await loadLeads();
  setMessage(dashboardMessage, "Enquiry updated.");
});
