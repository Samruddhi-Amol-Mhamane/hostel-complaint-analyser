console.log(
    "Hostel Complaint Analyzer website loaded successfully."
);


// ==========================================
// ACTIVE NAVIGATION LINK
// ==========================================

const sections = document.querySelectorAll("section");

const navLinks = document.querySelectorAll("nav a");


window.addEventListener("scroll", () => {

    let current = "";

    sections.forEach(section => {

        const sectionTop =
            section.offsetTop - 120;

        const sectionHeight =
            section.clientHeight;

        if (
            window.scrollY >= sectionTop &&
            window.scrollY < sectionTop + sectionHeight
        ) {

            current =
                section.getAttribute("id");

        }

    });


    navLinks.forEach(link => {

        link.classList.remove("active");

        if (
            link.getAttribute("href") ===
            "#" + current
        ) {

            link.classList.add("active");

        }

    });

});


// ==========================================
// FORM SUBMISSION MESSAGE
// ==========================================

const complaintForm =
    document.getElementById("complaintForm");


if (complaintForm) {

    complaintForm.addEventListener(
        "submit",
        () => {

            console.log(
                "Complaint submitted successfully."
            );

        }
    );

}
