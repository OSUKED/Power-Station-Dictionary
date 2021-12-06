function strtrunc(str, max, add){
   add = add || '...';
   return (typeof str === 'string' && str.length > max ? str.substring(0, max) + add : str);
};

$(document).ready(function() {
    $('#dictionary').DataTable({
        "scrollX": true,
        targets: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
        render: function(data, type, full, meta){
            if(type === 'display'){
                data = strtrunc(data, 35);
            }
            return data;
        }
    });
});