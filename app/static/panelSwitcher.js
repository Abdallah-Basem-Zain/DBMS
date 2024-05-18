document.onkeyup = function (e) {
    if (e.key === "Escape") {
        closeNavIfOpen(Inav);
        closeNavIfOpen(Snav);
        closeNavIfOpen(Lnav);
        closeNavIfOpen(Pnav);
        closeNavIfOpen(Anav);
        closeNavIfOpen(Cnav);
        closeNavIfOpen(Conav)
    }
};


function closeNavIfOpen(navElement) {
    if (navElement.classList.contains("open")) {
        navElement.classList.remove("open");
    }
}

// Define variables for student navigation elements
let Stoggler = document.querySelector(".studente");
let Snav = document.querySelector(".studentNav");
let sClose = document.querySelector(".cStudent");

// Define variables for instructor navigation elements
let Itoggler = document.querySelector(".instructorr");
let Inav = document.querySelector(".instructorNav");
let IClose = document.querySelector(".cinstructor");

// Define variables for license navigation elements
let Ltoggler = document.querySelector(".Licencee");
let Lnav = document.querySelector(".licenseNav");
let LClose = document.querySelector(".cLicense");

// Define variables for program navigation elements
let Ptoggler = document.querySelector(".pptoggler");
let Pnav = document.querySelector(".pppnav");
let PClose = document.querySelector(".cProgram");

let Atoggler = document.querySelector(".aiutog");
let Anav = document.querySelector(".aiuNav");
let AClose = document.querySelector(".aiuc");


let Ctoggler = document.querySelector(".courseratog");
let Cnav = document.querySelector(".courseraNav");
let CClose = document.querySelector(".courserac");

let Cotoggler = document.querySelector(".coordinatorr");
let Conav = document.querySelector(".coordinatorNav");
let CoClose = document.querySelector(".ccoordinator");


Ptoggler.onclick = function () {
    Pnav.classList.add("open");
};

PClose.onclick = function () {
    Pnav.classList.remove("open");
};

Stoggler.onclick = function () {
    Snav.classList.add("open");
};

sClose.onclick = function () {
    Snav.classList.remove("open");
};

Itoggler.onclick = function () {
    Inav.classList.add("open");
};

IClose.onclick = function () {
    Inav.classList.remove("open");
};

Ltoggler.onclick = function () {
    Lnav.classList.add("open");
};

LClose.onclick = function () {
    Lnav.classList.remove("open");
};

Atoggler.onclick = function () {
    Anav.classList.add("open");
};

AClose.onclick = function () {
    Anav.classList.remove("open");
};
Ctoggler.onclick = function () {
    Cnav.classList.add("open");
};

CClose.onclick = function () {
    Cnav.classList.remove("open");
};

Cotoggler.onclick = function () {
    Conav.classList.add("open");
};

CoClose.onclick = function () {
    Conav.classList.remove("open");
};
