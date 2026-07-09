export function renderTopic(guest, content) {
    
    const imageUrl = guest.image;

    return `
        <div class="aurora-container">
            <div class="aurora-background">
                <div class="aurora-blob-1"></div>
                <div class="aurora-blob-2"></div>
            </div>

            <div class="topic-content">
                <div class="topic-image-wrapper animate-slide-up">
                    <img src="${imageUrl}" alt="${guest.concept}" class="topic-image">
                </div>
                
                <div class="topic-text-wrapper animate-fade-in-delayed">
                    <h2 class="topic-title">${guest.concept}</h2>
                    
                    <div class="topic-section">
                        <h3>${content.description}</h3>
                        <p>${guest.explanation}</p>
                    </div>
                    
                    <div class="topic-section">
                        <h3>${content.dedication}</h3>
                        <p class="topic-dedication">${guest.dedication}</p>
                    </div>
                </div>
            </div>
        </div>
    `;
}