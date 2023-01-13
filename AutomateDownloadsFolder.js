const fs = require('fs');
const path = require('path')
const os = require('os')

let absPath = os.userInfo().homedir + "\\Downloads";   // C:/Users/wycze + /Downloads + /Obrazki  

const foldery = ["Obrazki", "Dokumenty", "Programy", "Muzyka"]

const programy = fs.readdirSync(absPath)   // readdirsync zwraca array z cala zawartoscia

const obrazkiExt = ['.jpg','.jpeg','.png', '.PNG', '.svg']
const dokumentyExt = ['.doc', '.docx', '.txt', '.pdf', '.pptx']
const programyExt = ['.exe', '.msi']
const muzykaExt = ['.mp4', '.mp3', '.wav', '.aif', '.mid', '.flac', '.aac']
let len = programy.length;


foldery.map((elem) => { 
    if(!fs.existsSync(path.join(absPath, elem)))  
        fs.mkdir(path.join(absPath, elem), (err) => {})
    else console.log(`Folder ${path.join(absPath, elem)} juz istnieje`);
});
programy.map(move)

function move(elem){
    const filePath = path.join(absPath, elem)
    const ext = path.extname(filePath);

    if(obrazkiExt.includes(ext)) {
        fs.renameSync(filePath, path.join(absPath, foldery[0], elem)); 
        log(filePath);
    } else if(dokumentyExt.includes(ext)) {
        fs.renameSync(filePath, path.join(absPath, foldery[1], elem)); 
        log(filePath);
    } else if(programyExt.includes(ext)) {
        fs.renameSync(filePath, path.join(absPath, foldery[2], elem));
        log(filePath);
    } else if(muzykaExt.includes(ext)) {
        fs.renameSync(filePath, path.join(absPath, foldery[3], elem)); 
        log(filePath);
    } else console.log(`NIE PRZERZUCONO ${filePath}`)
}

function log(filePath){
    console.log("przerzucono plik " + filePath);
}

console.log(`Ilosc programow w folderze przed pracą: ${len}`);
len = fs.readdirSync(absPath).length
console.log(`Ilosc programow w folderze po pracy: ${len}`);
