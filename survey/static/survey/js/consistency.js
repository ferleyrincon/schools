$(document).ready(function () {
    $('.items1').click(
        function () {
            var clickedRadio = this;
            var afterClickedRadio = false;

            var radios = $('.items1');
            var i_clicked = -1;

            for (i = 0; i < radios.length; ++i) {
                var radio = radios[i];

                if (!afterClickedRadio && clickedRadio.value === 'B' && radio.value === 'B') {
                    radio.checked = true;
                }

                if (!afterClickedRadio && clickedRadio.value === 'A' && radio.value === 'A') {
                    radio.checked = true;
                }

                if (!afterClickedRadio && clickedRadio.value === 'A' && radio.value === 'A' && radio === clickedRadio) {
                    radio.checked = true;
                }

                if (afterClickedRadio && clickedRadio.value === 'A' && radio.value === 'B' && i_clicked != (i-1)) {
                    radio.checked = true;
                }

                if (afterClickedRadio && clickedRadio.value === 'B' && radio.value === 'A') {
                    radio.checked = true;
                }

                if (radio === clickedRadio) {
                    afterClickedRadio = true;
                    i_clicked = i;
                    continue;
                }
            }
        }
    );
});

$(document).ready(function () {
    $('.items2').click(
        function () {
            var clickedRadio = this;
            var afterClickedRadio = false;

            var radios = $('.items2');

            for (i = 0; i < radios.length; ++i) {
                var radio = radios[i];

                if(clickedRadio.value === 'B'){
                    if (!afterClickedRadio && radio.value === 'B') {
                        radio.checked = true;
                    }
                    if (afterClickedRadio && radio.value === 'A') {
                        radio.checked = true;
                    }
                    if (radio === clickedRadio) {
                        afterClickedRadio = true;
                        i_clicked = i;
                        continue;
                    }
                }
            }
        }
    );
});

$(document).ready(function () {
    $('.items3').click(
        function () {
            var clickedRadio = this;
            var afterClickedRadio = false;

            var radios = $('.items3');

            for (i = 0; i < radios.length; ++i) {
                var radio = radios[i];

                if(clickedRadio.value === 'B'){
                    if (!afterClickedRadio && radio.value === 'B') {
                        radio.checked = true;
                    }
                    if (afterClickedRadio && radio.value === 'A') {
                        radio.checked = true;
                    }
                    if (radio === clickedRadio) {
                        afterClickedRadio = true;
                        i_clicked = i;
                        continue;
                    }
                }
            }
        }
    );
});

$(document).ready(function () {
    $('.slider_dinero').change(
        function (event) {
            var slider_id = event.target.id;
            var parent_slider = document.getElementById(slider_id).parentElement.parentElement;
            var childs = parent_slider.children;

            var dinero_pa = childs[0].firstElementChild;
            var slider_max = childs[1].firstElementChild.max;
            var slider_value = childs[1].firstElementChild.value;
            var dinero_pb = childs[2].firstElementChild;

            var check_sli = childs[1].lastElementChild;

            dinero_pa.innerHTML = "$ "+numberWithPoints(slider_value);
            dinero_pb.innerHTML = "$ "+numberWithPoints(slider_max-slider_value);
            check_sli.value = 1;

            var next_button = document.getElementsByClassName('otree-btn-next');
            next_button[0].style.cssText += 'display: block !important;';
        }
    );
});

$(document).ready(function () {
    $('.slider_tiempo').change(
        function (event) {
            var slider_id = event.target.id;
            var parent_slider = document.getElementById(slider_id).parentElement.parentElement;
            var childs = parent_slider.children;

            var dinero_pa = childs[0].firstElementChild;
            var slider_max = childs[1].firstElementChild.max;
            var slider_value = childs[1].firstElementChild.value;
            var dinero_pb = childs[2].firstElementChild;

            var check_sli = childs[1].lastElementChild;

            dinero_pa.innerHTML = "Horas: "+slider_value;
            dinero_pb.innerHTML = "Horas: "+(slider_max-slider_value);
            check_sli.value = 1;

            var next_button = document.getElementsByClassName('otree-btn-next');
            next_button[0].style.cssText += 'display: block !important;';
        }
    );
});

function numberWithPoints(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".");
}

$(document).ready(function () {
    $('.otree-btn-next').click(
        function () {
            var radios = $('.items1');
            for (i = 0; i < radios.length; ++i) {
                var radio = radios[i];
                radio.disabled = false;
            }
            var radios = $('.items2');
            for (i = 0; i < radios.length; ++i) {
                var radio = radios[i];
                radio.disabled = false;
            }
            var radios = $('.items3');
            for (i = 0; i < radios.length; ++i) {
                var radio = radios[i];
                radio.disabled = false;
            }
        }
    );
});




