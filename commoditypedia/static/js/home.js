function dateConvert(reciveDate){

    var date = new Date("");
    var date = new Date(reciveDate);
    var now = new Date;
    var diffTimeToMinute = parseInt((now - date) / (1000 * 60));
    if (diffTimeToMinute < 1) {
        document.write('همین الان!');
    } else if (diffTimeToMinute < 5) {
        document.write('دقایقی قبل!');
    } else if (diffTimeToMinute < 10) {
        document.write('حدود ۵ دقیقه قبل!');
    } else if (diffTimeToMinute < 30) {
        document.write('حدود ۱۰ دقیقه قبل!');
    } else if (diffTimeToMinute < 60) {
        document.write('حدود نیم ساعت قبل!');
    } else if (diffTimeToMinute < 120) {
        document.write('حدود یک ساعت قبل!');
    } else if (diffTimeToMinute < 180) {
        document.write('حدود دو ساعت قبل!');
    } else if (diffTimeToMinute < 360) {
        document.write('حدود سه ساعت قبل!');
    } else if (diffTimeToMinute < 720) {
        document.write('حدود شش ساعت قبل!');
    } else if (diffTimeToMinute < 1440) {
        document.write('حدود دوازده ساعت قبل!');
    } else if (diffTimeToMinute < 2880) {
        document.write('دیروز!');
    } else if (diffTimeToMinute < 4320) {
        document.write('پریروز!');
    } else if (diffTimeToMinute < 10080) {
        document.write('چند روز قبل!');
    } else if (diffTimeToMinute < 43200) {
        document.write('چند هفته قبل!');
    } else if (diffTimeToMinute < 525600) {
        document.write('چند ماه قبل!');
    } else if (diffTimeToMinute < 1051200) {
        document.write('یکسال قبل!');
    } else {
        document.write('چند سال قبل!');
    }
}

function numToPersianWithCommaSeperator(enNum) {
    price = enNum;
    priceWithThousandSeperator = price.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    persianPrice = priceWithThousandSeperator.replace(/0/g, '۰').replace(/1/g, '۱').replace(/2/g, '۲').replace(/3/g, '۳').replace(/4/g, '۴').replace(/5/g, '۵').replace(/6/g, '۶').replace(/7/g, '۷').replace(/8/g, '۸').replace(/9/, '۹').replace(/9/g, '۹');
    document.write(persianPrice);
}
