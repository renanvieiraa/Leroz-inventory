const {app, BrowserWindow} = require('electron')
    const url = require('url');
    const path = require('path');

    let mainWindow

    function createWindow() {
        mainWindow = new BrowserWindow({
            width: 800,
            height: 600,
            webPreferences:{
                nodeIntegration: true
            }
        })

        mainWindow.loadURL(
            url.format({
                pathname: path.join(__dirname, `/dist/Leroz-IM/index.html`),
                protocol: "file",
                slashes: true
            })
        );

        // Abre a DevTools.
        mainWindow.webContents.openDevTools()

        mainWindow.on('close', ()=>{
            mainWindow = null
        })
    }

    app.on('ready', createWindow)

    app.on('window-all-closed', ()=>{
        if (process.platform !== 'darwin') app.quit()
    })

    app.on('activate', ()=>{
        if(mainWindow === null) createWindow()
    })