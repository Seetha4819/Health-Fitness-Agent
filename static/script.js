
function calculateBMI(weight, height) {
    if (weight > 0 && height > 0) {
        const heightM = height / 100;
        return (weight / (heightM ** 2)).toFixed(2);
    }
    return '';
}

document.getElementById("weight").addEventListener("input", updateBMI);
document.getElementById("height").addEventListener("input", updateBMI);

function updateBMI() {
    const weight = parseFloat(document.getElementById("weight").value);
    const height = parseFloat(document.getElementById("height").value);
    const bmi = calculateBMI(weight, height);
    document.getElementById("liveBMI").innerHTML = bmi ? `Your BMI: <b>${bmi}</b>` : "";
}
document.getElementById("fitnessForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const data = {
        age: parseInt(document.getElementById("age").value),
        weight: parseInt(document.getElementById("weight").value),
        height: parseInt(document.getElementById("height").value),
        goal: document.getElementById("goal").value
    };
    

    const response = await fetch("http://127.0.0.1:5000/recommend", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    });

    const result = await response.json();

    document.getElementById("result").innerHTML = `
        <h3>Results</h3>
        <p><b>BMI:</b> ${result.bmi}</p>
        <p><b>Calories:</b> ${result.calories}</p>
        <p><b>Exercises:</b> ${result.exercises.join(", ")}</p>
        <p><b>Tips:</b> ${result.tips.join(" ")}</p>
    `;
});
