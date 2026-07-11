export function renderWelcome(guestName, content) {
    return `
        <div class="aurora-container">
            <div class="aurora-background">
                <div class="aurora-blob-1"></div>
                <div class="aurora-blob-2"></div>
            </div>

            <div class="aurora-content">
                <div class="welcome-card">
                    <h1 class="welcome-title animate-fade-in delay-1">
                        ${content.title} ${guestName}!
                    </h1>
                    
                    <p class="welcome-subtitle animate-fade-in delay-2">
                        ${content.subtitle}
                    </p>
                    
                    <p class="welcome-cta animate-fade-in delay-3">
                        <span class="pulse-text">
                            ${content.cta}
                        </span>
                    </p>
                </div>
            </div>
        </div>
    `;
}