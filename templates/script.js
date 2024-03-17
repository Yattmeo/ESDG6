document.addEventListener('DOMContentLoaded', function () {
    var calendarEl = document.getElementById('calendar');

    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',
        selectable: true,
        dateClick: function (info) {
            console.log('clicked on ' + info.dateStr);
        }
    });

    calendar.render();

    var startDateInput = document.getElementById('startDate');
    var endDateInput = document.getElementById('endDate');

    startDateInput.addEventListener('change', function () {
        calendar.gotoDate(this.value);
    });

    endDateInput.addEventListener('change', function () {
        calendar.gotoDate(this.value);
    });
});