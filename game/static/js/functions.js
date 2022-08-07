document.getElementById("a1").addEventListener('change', function() {
    let v = parseInt(this.value);
    if (v < 0) this.value = 0;
    if (v > 20000) this.value = 20000;
});

document.getElementById("a2").addEventListener('change', function() {
    let v = parseInt(this.value);
    if (v < 0) this.value = 0;
    if (v > 20000) this.value = 20000;
});


function enviar() {
    var all_inputs = document.getElementsByClassName('input_number');
    console.log(all_inputs);
    var inversion = Number(20000);
    var sum_inversion = Number(0);
    for(const ai of all_inputs) {
        console.log(ai);
        sum_inversion = Number(sum_inversion) + Number(ai.value);
        console.log("Inversion:", ai.value);
    }
    console.log("Suma", sum_inversion);
    if(sum_inversion == inversion) {
        document.getElementById("form").submit();
    } else {
        alert('La suma de ambas inversiones no da $ 20.000, por favor revise');
    }
}
