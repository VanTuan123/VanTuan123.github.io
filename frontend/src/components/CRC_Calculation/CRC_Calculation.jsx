import React, { useState, useEffect } from "react";
import './CRC_Calculation.css'

function CRC_Calculation(){
    const [Value, SetValue] = useState('');
    const [count, SetCount] = useState(0);
    const JsonObject = {title:'React POST request',
    data: ''};
    const requestOpition = {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({JsonObject})
    };  
    useEffect(()=>{
        /*This is for easy check*/
        document.title = 'Calculate '+ count +' times';
        /*Make POST request to backend API*/
        if (count !== 0)
        {;
            myfetch();
        }
    });
    /*Make POST request to backend API*/
    async function myfetch()
    {
        var datastring;
        var result;
        JsonObject.data = Value.toString();
        requestOpition.body = JSON.stringify(JsonObject);
        await fetch('http://127.0.0.1:8000/request',requestOpition)
        .then((res)=>res.json())
        .then((data)=>{
            result = data;
        })
        .catch((err)=>{
            console.log(err.message);
        });
        var element = document.getElementById('resultCRC');
        if (null !== element)
        {
            element.innerHTML = result.CRC_Result;
        }
    }
    function myClick()
    {
        var datastring;
        var element = document.getElementById('datachain');
        if (null !== element)
        {
            datastring = element.value;
        }
        SetValue(datastring);
        SetCount(count + 1);
    }
    return(
        <div>
            <div className="textinput">
                <textarea id="datachain"></textarea>
                <button onClick={() => myClick()}>Calculate</button>
            </div>
            <div className="CRCresult">
                <h3>CRC Result</h3>
                <textarea id='resultCRC'></textarea>
            </div>
        </div>
    )
    
}

export default CRC_Calculation;