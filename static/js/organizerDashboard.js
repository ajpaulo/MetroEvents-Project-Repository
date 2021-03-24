$.fn.modal.Constructor.prototype._enforceFocus = function() {};

function disableBeforeToday(input_date_id) {
  var dateToday = new Date().toISOString().slice(0, 10);
  document.getElementById(input_date_id).setAttribute("min",dateToday);
}

$(document).ready(function() {
  var eventListDataTable = $('#eventList').DataTable( {
    'columnDefs': [ {
      'targets': [3], 
      'orderable': false, // set orderable false for buttons col
    }],
  } );

} );