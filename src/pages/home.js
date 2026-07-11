import { renderWelcome } from './welcome.js';
import { renderTopic } from './topic.js';

const appDiv = document.getElementById('app');
let clickHandler = null; // 1. Variabile dichiarata correttamente nel modulo

async function loadApp() {
    const hash = window.location.hash.substring(1);

    // Pulizia di vecchi listener
    if (clickHandler) {
        document.removeEventListener('click', clickHandler);
        clickHandler = null;
    }
    
    if (!hash) {
        appDiv.innerHTML = "<h1>In attesa di scansione...</h1>";
        return;
    }

    try {
        // fetch guests data
        const guestResponse = await fetch('./resources/data/guests.json');
        if (!guestResponse.ok) throw new Error("Errore nel caricamento dei dati");
        const data = await guestResponse.json();
        const guest = data.guests[hash];

        // fetch page content data
        const contentResponse = await fetch('./resources/data/content.json');
        if (!contentResponse.ok) throw new Error("Errore nel caricamento dei dati");
        const content = await contentResponse.json();

        if (guest) {
                appDiv.innerHTML = renderWelcome(guest.name, content.welcome);

                // handle screen click function to transition to topic page
                clickHandler = () => {
                    appDiv.innerHTML = renderTopic(guest, content.topic);
                    document.removeEventListener('click', clickHandler);
                    clickHandler = null;
                };
                setTimeout(() => {
                    document.addEventListener('click', clickHandler);
                }, 50);

            } else {
                appDiv.innerHTML = "<h1>Ospite non trovato</h1>";
            }

    } catch (error) {
        console.error(error);
        appDiv.innerHTML = "<h1>Errore di sistema. Riprovare.</h1>";
    }
}

window.addEventListener('load', loadApp);
window.addEventListener('hashchange', loadApp);