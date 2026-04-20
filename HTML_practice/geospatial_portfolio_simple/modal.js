const projects = [
  {
    title: "Urban Growth Change Map",
    category: "Remote Sensing",
    tools: "ArcGIS Pro, Landsat imagery, Excel",
    details:
      "Compared land cover from two different years to show where development expanded. This project focuses on a short summary, main tools, and a simple project link.",
    link_text: "View placeholder project page",
    href: "https://example.com/urban-growth-change-map",
    image: "images/project-1.svg",
    image_alt: "Preview map for the urban growth change project.",
  },
  {
    title: "Trail Accessibility Audit",
    category: "Public Planning",
    tools: "ArcGIS Online, Survey123, Google Sheets",
    details:
      "Mapped sidewalks, curb ramps, and trails to identify accessibility gaps near local parks. The goal was to highlight useful planning information in a clear visual format.",
    link_text: "Open placeholder audit page",
    href: "https://example.com/trail-accessibility-audit",
    image: "images/project-2.svg",
    image_alt: "Preview map for the trail accessibility project.",
  },
  {
    title: "Flood Risk Story Map",
    category: "Hazard Analysis",
    tools: "ArcGIS StoryMaps, DEM data, stream buffers",
    details:
      "Combined elevation and water data to explain flood-prone areas in a short story map format. The modal keeps the project information concise and easy to scan.",
    link_text: "Read placeholder story map",
    href: "https://example.com/flood-risk-story-map",
    image: "images/project-3.svg",
    image_alt: "Preview map for the flood risk story map project.",
  },
  {
    title: "Campus Tree Inventory",
    category: "Field Data",
    tools: "Field Maps, ArcGIS Pro, attribute tables",
    details:
      "Organized campus tree point data by species, condition, and maintenance needs. The project card opens a modal with the core details instead of a separate page.",
    link_text: "Visit placeholder inventory page",
    href: "https://example.com/campus-tree-inventory",
    image: "images/project-4.svg",
    image_alt: "Preview map for the campus tree inventory project.",
  },
  {
    title: "Transit Stop Service Area",
    category: "Network Analysis",
    tools: "Network Analyst, census data, service areas",
    details:
      "Measured walking access around bus stops to compare transit coverage across neighborhoods. This is a placeholder example that still demonstrates the modal pattern clearly.",
    link_text: "View placeholder service area map",
    href: "https://example.com/transit-stop-service-area",
    image: "images/project-5.svg",
    image_alt: "Preview map for the transit stop service area project.",
  },
  {
    title: "Habitat Suitability Model",
    category: "Environmental GIS",
    tools: "Raster calculator, slope, land cover layers",
    details:
      "Used slope, land cover, and water distance layers to estimate suitable habitat areas. The modal shows a title, details, tools, and one project link as required.",
    link_text: "Open placeholder habitat model",
    href: "https://example.com/habitat-suitability-model",
    image: "images/project-6.svg",
    image_alt: "Preview map for the habitat suitability model project.",
  },
];

const modal = document.querySelector("#project-modal");
const modal_title = document.querySelector("#modal-title");
const modal_category = document.querySelector("#modal-category");
const modal_tools = document.querySelector("#modal-tools");
const modal_details = document.querySelector("#modal-details");
const modal_link = document.querySelector("#modal-link");
const modal_close = document.querySelector("#modal-close");
const modal_image = document.querySelector("#modal-image");

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
  modal_image.src = project.image;
  modal_image.alt = project.image_alt;

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
