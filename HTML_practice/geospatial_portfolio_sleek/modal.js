const projects = [
  {
    title: "Urban Growth Change Map",
    category: "Remote Sensing",
    tools: "ArcGIS Pro, Landsat imagery, Excel",
    details:
      "This project compares two land cover snapshots to show where suburban growth expanded over time. The modal highlights the main workflow, map purpose, and a short summary instead of a long case study.",
    link_text: "View placeholder case study",
    href: "https://example.com/urban-growth-change-map",
  },
  {
    title: "Trail Accessibility Audit",
    category: "Public Planning",
    tools: "ArcGIS Online, Survey123, Google Sheets",
    details:
      "This project maps sidewalks, curb ramps, and trail links to identify barriers that affect access to community parks. The final layout focuses on quick findings that a visitor can scan in a few seconds.",
    link_text: "Open placeholder project page",
    href: "https://example.com/trail-accessibility-audit",
  },
  {
    title: "Flood Risk Story Map",
    category: "Hazard Analysis",
    tools: "ArcGIS StoryMaps, DEM data, stream buffers",
    details:
      "This project combines elevation, water features, and flood-prone areas into a short story map summary. It is designed to explain flood risk clearly to a general audience using concise text and a single call to action.",
    link_text: "Read placeholder story map",
    href: "https://example.com/flood-risk-story-map",
  },
  {
    title: "Campus Tree Inventory",
    category: "Field Data",
    tools: "Collector, ArcGIS Pro, attribute tables",
    details:
      "This project organizes campus tree points by species, condition, and maintenance needs. The modal keeps the details brief while still showing the main tools and the purpose of the inventory.",
    link_text: "Visit placeholder inventory page",
    href: "https://example.com/campus-tree-inventory",
  },
  {
    title: "Transit Stop Service Area",
    category: "Network Analysis",
    tools: "Network Analyst, census data, service areas",
    details:
      "This project measures walking access around bus stops to see which neighborhoods have stronger transit coverage. The modal explains the analysis method and gives visitors a quick project link.",
    link_text: "View placeholder service area map",
    href: "https://example.com/transit-stop-service-area",
  },
  {
    title: "Habitat Suitability Model",
    category: "Environmental GIS",
    tools: "Raster calculator, slope analysis, land cover layers",
    details:
      "This project uses environmental layers such as slope, water distance, and land cover to estimate suitable habitat zones. The modal shows the core tools and a short description that stays concise and beginner-friendly.",
    link_text: "Open placeholder habitat model",
    href: "https://example.com/habitat-suitability-model",
  },
];

const modal = document.querySelector("#project-modal");
const modal_title = document.querySelector("#modal-title");
const modal_category = document.querySelector("#modal-category");
const modal_tools = document.querySelector("#modal-tools-text");
const modal_details = document.querySelector("#modal-details");
const modal_link = document.querySelector("#modal-link");
const modal_close = document.querySelector("#modal-close");

const card_buttons = document.querySelectorAll(".project-card");

function openModalByIndex(index) {
  const project = projects[index];

  if (!project) return;

  modal_title.textContent = project.title;
  modal_category.textContent = project.category;
  modal_tools.textContent = project.tools;
  modal_details.textContent = project.details;
  modal_link.textContent = project.link_text;
  modal_link.href = project.href;

  modal.showModal();
  document.body.style.overflow = "hidden";
  modal.focus();
}

function onCardClicked(event) {
  const clicked_card = event.currentTarget;
  const index = Number(clicked_card.dataset.index);
  openModalByIndex(index);
}

for (let i = 0; i < card_buttons.length; i += 1) {
  card_buttons[i].addEventListener("click", onCardClicked);
}

modal_close.addEventListener("click", function () {
  modal.close();
});

modal.addEventListener("close", function () {
  document.body.style.overflow = "";
});
