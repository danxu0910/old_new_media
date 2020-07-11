window.onload = () => {

    const generate = () => {
        const title_slider = document.querySelector("#title_slider");
        const people_slider = document.querySelector("#people_slider");
        const project_slider = document.querySelector("#project_slider");

        const formdata = new FormData();
        formdata.append("title_slider", title_slider.value);
        formdata.append("people_slider", people_slider.value);
        formdata.append("project_slider", project_slider.value);

        fetch("/generate", {
            method: "POST", 
            body: formdata
        }).then((res) => {
            return res.json();
        }).then((data) => {
            const title = document.querySelector("#title");
            const people = document.querySelector("#people");
            const project = document.querySelector("#project");

            title.innerHTML = "&nbsp;// " + data["new_title"] + " //&nbsp;";
            people.innerHTML = "By " + data["new_people"];
            project.innerHTML = data["new_project"];

            console.log(data);
        });
    };

    const art_value = document.querySelector("#art_value");
    const sci_value = document.querySelector("#sci_value");
    const tech_value = document.querySelector("#tech_value");

    const art_update = document.querySelector("#art_update");
    const sci_update = document.querySelector("#sci_update");
    const tech_update = document.querySelector("#tech_update");

    const about = () => {
        const formdata = new FormData();
        formdata.append("art_value", art_value.value);
        formdata.append("sci_value", sci_value.value);
        formdata.append("tech_value", tech_value.value);

        const sums = parseInt(art_value.value) + parseInt(sci_value.value) + parseInt(tech_value.value);
        console.log(sums)
        if (sums != 0){
            const art_perc = parseInt(art_value.value) * 100 / sums;
            const sci_perc = parseInt(sci_value.value) * 100 / sums;
            const tech_perc = parseInt(tech_value.value) * 100 / sums;

            art_update.innerHTML = art_perc.toFixed(0) + "%";
            sci_update.innerHTML = sci_perc.toFixed(0) + "%";
            tech_update.innerHTML = tech_perc.toFixed(0) + "%";
        } else {
            art_update.innerHTML = "";
            sci_update.innerHTML = "";
            tech_update.innerHTML = "";
        }

        fetch("/about", {
            method: "POST",
            body: formdata
        }).then((res) => {
            return res.text();
        }).then((data) => {
            const newabout = document.querySelector("#newabout");
            newabout.innerHTML = data;

            console.log(data);
        });
    };

    const button = document.querySelector("#button1");

    button.onclick = generate;
    generate();

    art_value.oninput = about;
    sci_value.oninput = about;
    tech_value.oninput = about;
    about();
};