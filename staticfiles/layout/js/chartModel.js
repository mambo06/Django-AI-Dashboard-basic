
// Set new default font family and font color to mimic Bootstrap's default styling
//     Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
//     Chart.defaults.global.defaultFontColor = '#858796';

//generate random color

function getRandomColor() {
    var letters = '0123456789ABCDEF';
    var color = '#';
    for (var i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}
var context = document.getElementById("data_from_django").innerHTML;
context = JSON.parse(String(context));
// console.log(context);

var data = []
for (var i =0; i <context.length;i++){
    data.push(context[i].datasets[0])
}
console.log(data)

// Bar Chart Example
    var ctx = document.getElementById("myChart");
    myChart = new Chart(ctx, {
        data: {
            datasets: data,
            // labels: ['January', 'February', 'March', 'April']
        },
        // options: options
        options: {
            animations: {
                responsive: true,
                tension: {
                    duration: 1000,
                    easing: 'linear',
                    from: 0,
                    to: 0,
                    loop: true
                }
            },
        }
    });
