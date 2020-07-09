window.onload = () => {
    const title_slider = document.querySelector("#title_slider");
    const people_slider = document.querySelector("#people_slider");
    const project_slider = document.querySelector("#project_slider");

    const button = document.querySelector("#button1");

    const title = document.querySelector("#title");
    const people = document.querySelector("#people");
    const project = document.querySelector("#project");

    button.onclick = () => {
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
            title.innerHTML = data["new_title"];
            people.innerHTML = data["new_people"];
            project.innerHTML = data["new_project"];

            console.log(data);
        });
        // console.log(title_slider.value);
    };
};