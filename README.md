# Python-Telegram-Bot-TripAdvisor
This Bot can help you to find best hotel for your trip.
<h1>Too Easy Travel</h1>

## Description

**How to start**
<p>Use following commands to start searching hotels:</p>

<br><b>/start</b> - the structure of the request will be:
<div><em>General request [LowPrice/HighPrice].</em></div>
    <ul>
        <li>City</li>
        <li>Date</li>
        <li>Mode[LowPrice/HighPrice]</li>
        <li>Number of hotels</li>
        <li>Show pictures</li>
        <li>Show pictures</li>
        <li>Show pictures[Yes/No]</li>
            <ul>
                <li>Number of pictures</li>
            </ul>
        <li>Location(Region)</li>
    </ul>

<div><em>Example:</em></div>

    ***[Chosen request]***
    🎯 Direction: Paris
    🛫 Check in: 2023-02-08
    🛬 Check out: 2023-02-17
    💥 Command: lowprice
    🏨 Number of hotels: 6
    📷 Send photo: yes
    🧮 Count of photos: 5
    📍 Location: Paris
    

<div><em>General request [BestDeal].</em></div>
    <ul>
        <li>City</li>
        <li>Date</li>
        <li>Mode[BestDeal]</li>
        <li>Minimum price</li>
        <li>Maximum price</li>
        <li>Distance from the center</li>
        <li>Number of hotels</li>
        <li>Show pictures[Yes/No]</li>
            <ul>
                <li>Number of pictures</li>
            </ul>
        <li>Location(Region)</li>
    </ul>

<div><em>Example:</em></div>

    ***[Chosen request]***
    🎯 Direction: Dubai
    🛫 Check in: 2023-02-08
    🛬 Check out: 2023-02-16
    💥 Command: bestdeal
    🤏 Minimum price: 100
    👐 Maximum price: 300
    🎢 Distance from the center: 30
    🏨 Number of hotels: 5
    📷 Send photo: yes
    🧮 Count of photos: 7
    📍 Location: Dubai Marina

<br><b>/lowprice</b> - the structure of the request will be: 
<div><em>The lowest price request.</em></div>
    <ul>
        <li>City</li>
        <li>Date</li>
        <li>Number of hotels</li>
        <li>Show pictures</li>
        <li>Show pictures</li>
        <li>Show pictures[Yes/No]</li>
            <ul>
                <li>Number of pictures</li>
            </ul>
        <li>Location(Region)</li>
    </ul>
<br><b>/highprice</b> - the structure of the request will be: 
<div><em>The highest price request.</em></div>
    <ul>
        <li>City</li>
        <li>Date</li>
        <li>Number of hotels</li>
        <li>Show pictures</li>
        <li>Show pictures</li>
        <li>Show pictures[Yes/No]</li>
            <ul>
                <li>Number of pictures</li>
            </ul>
        <li>Location(Region)</li>
    </ul>

<br><b>/bestdeal</b> - the structure of the request will be: 
<div><em>The best deal request.</em></div>
    <ul>
        <li>City</li>
        <li>Date</li>
        <li>Minimum price</li>
        <li>Maximum price</li>
        <li>Distance from the center</li>
        <li>Number of hotels</li>
        <li>Show pictures[Yes/No]</li>
            <ul>
                <li>Number of pictures</li>
            </ul>
        <li>Location(Region)</li>
    </ul>

<br><b>/history</b> - the structure of the request will be: 
<div><em>The history of 5 last request.</em></div>

<div><em>Example:</em></div>

    [#2] lowprice from 2023-01-31 - 10:05:08 Hotels: 4
            -IT Time Hotel Price: 33.82
            -StudioMinsk in Historic Centre Price: 31.04
            -StudioMinsk Apartments in Centre Price: 30.73
            -StudioMinsk Spa Apartments in Centre Price: 30.73
    
    [#1] bestdeal from 2023-01-31 - 09:40:46 Hotels: 6
            -Imperial Palace Hotel Price: 186.67
            -Hot Tub VIP SMART ApartHotel Price: 34.39625
            -Belarus Hotel Price: 112
            -East Time Hotel Price: 37.5
            -Willing Hotel Price: 152.83
            -The Basilian Minsk, Curio Collection By Hilton Price: 126.22

<br><b>/help</b> - the structure of the request will be: 
<div><em>Help request will show you all available commands.</em></div>

<div><em>Example:</em></div>

    /help - Информация о боте
    /start - Запустить бота
    /lowprice - Минимальная цена
    /highprice - Максимальная цена
    /bestdeal - Лучшее предложение, цена и расположение
    /history - История поиска(5 последних)

<br><b>/clean</b> - the structure of the request will be: 
<div><em>Clean request will clean conversation with bot.</em></div>

<div><em>Example:</em></div>

    ...
    There is no message with such ID: {} next 14734
    There is no message with such ID: {} next 14735
    There is no message with such ID: {} next 14736
    There is no message with such ID: {} next 14737
    There is no message with such ID: {} next 14738
    There is no message with such ID: {} next 14739
    There is no message with such ID: {} next 14740
    There is no message with such ID: {} next 14741
    There is no message with such ID: {} next 14742
    There is no message with such ID: {} next 14743
    There is no message with such ID: {} next 14744
    There is no message with such ID: {} next 14745
    ...
