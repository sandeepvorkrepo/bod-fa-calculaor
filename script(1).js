document.getElementById('gender').addEventListener('change', function() {
    if (this.value === 'female') {
        document.getElementById('femaleFields').style.display = 'block';
        document.getElementById('hip').required = true;
    } else {
        document.getElementById('femaleFields').style.display = 'none';
        document.getElementById('hip').required = false;
    }
});

document.getElementById('calculateBtn').addEventListener('click', function() {
    const gender = document.getElementById('gender').value;
    const age = parseFloat(document.getElementById('age').value);
    const height = parseFloat(document.getElementById('height').value);
    const weight = parseFloat(document.getElementById('weight').value);
    const waist = parseFloat(document.getElementById('waist').value);
    const neck = parseFloat(document.getElementById('neck').value);
    const hip = gender === 'female' ? parseFloat(document.getElementById('hip').value) : 0;

    if (!gender || !age || !height || !weight || !waist || !neck || (gender === 'female' && !hip)) {
        document.getElementById('result').textContent = "Please fill all required fields.";
        return;
    }

    // US Navy Body Fat Formula
    let bodyFat = 0;
    if (gender === 'male') {
        // Formula for males
        bodyFat = 495 / (1.0324 - 0.19077 * Math.log10(waist - neck) + 0.15456 * Math.log10(height)) - 450;
    } else if (gender === 'female') {
        // Formula for females
        bodyFat = 495 / (1.29579 - 0.35004 * Math.log10(waist + hip - neck) + 0.22100 * Math.log10(height)) - 450;
    }

    bodyFat = Math.round(bodyFat * 10) / 10; // 1 decimal place

    let resultText = `Estimated Body Fat Percentage: <strong>${bodyFat}%</strong>`;
    document.getElementById('result').innerHTML = resultText;
});