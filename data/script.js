const HELL = {
    "0": {
        "title": "Ghost Gate Pass",
        "subitle": "The border between the World of Light and Dark.",
        "description": "Guarded by the prison lord, anyone who is recently dead shall pass through this gate. You are all alone and by yourself, abandoned from your family and loved ones in the world of light. This is the beginning of your journey."
    },
    "1":{
        "title": "Karmascope Terrace",
        "subitle": "Mirror that shines on all people of the wrold is hung high.",
        "description":"Any good and evil, merit and misstep are shown without discrepancy. You may have a mouth of steel and deny anything, but cannot deny the obvious facts shown on the mirror. If you were filial to your ancestors, your face will be reflected on your own and virtuous light will pervade the entire world of darkness. You bypass all the purgatory and will be reborn as human again. If you lived life full of evil, never respected parents and elders, you may reborn as an animal or sink down to hell and pay your price depending on your karma."
    },
    "2":{
        "title": "Wasted Money Mountain",
        "subitle": "Mountain of paper money towers ten thousand feet",
        "description":""
    },
    "3":{
        "title": "",
        "subitle": "",
        "description":""
    },
    "4":{
        "title": "",
        "subitle": "",
        "description":""
    },
    "5":{
        "title": "",
        "subitle": "",
        "description":""
    },
    "6":{
        "title": "",
        "subitle": "",
        "description":""
    },
    "7":{
        "title": "",
        "subitle": "",
        "description":""
    },
    "8":{
        "title": "",
        "subitle": "",
        "description":""
    },
    "9":{
        "title": "",
        "subitle": "",
        "description":""
    },
    "":{
        "title": "",
        "subitle": "",
        "description":""
    },
    "":{
        "title": "",
        "subitle": "",
        "description":""
    },
    "":{
        "title": "",
        "subitle": "",
        "description":""
    },
    "":{
        "title": "",
        "subitle": "",
        "description":""
    },
    "":{
        "title": "",
        "subitle": "",
        "description":""
    },
    "":{
        "title": "",
        "subitle": "",
        "description":""
    },
    "":{
        "title": "",
        "subitle": "",
        "description":""
    },
    "":{
        "title": "",
        "subitle": "",
        "description":""
    },
    "":{
        "title": "",
        "subitle": "",
        "description":""
    },
    "":{
        "title": "",
        "subitle": "",
        "description":""
    },
    "":{
        "title": "",
        "subitle": "",
        "description":""
    },
    "":{
        "title": "",
        "subitle": "",
        "description":""
    },
    "":{
        "title": "",
        "subitle": "",
        "description":""
    }
    
}


let reload = ()=>{
    let ak = document.getElementsByClassName("idd")[0].value;
    const thisHell = HELL[ak];
    document.getElementById('title').innerHTML = thisHell['title'];
    document.getElementById('description').innerHTML = thisHell['description'];
}

reload();

document.getElementById("btn-right").addEventListener('click',()=>{
    alert("aa");
    let index = document.getElementsByClassName("idd")[0].value;
    index = (index + 1) % 30;
    document.getElementsByClassName("idd")[0].value = index;
    reload();
}, false);