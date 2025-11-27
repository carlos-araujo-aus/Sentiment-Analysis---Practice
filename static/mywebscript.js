/**
 * Analyzes the sentiment of text using Watson NLP API
 */
let RunSentimentAnalysis = async () => {
    // 1. Obtener el texto del textarea
    const textToAnalyze = document.getElementById("textToAnalyze").value;
    
    // 2. Validar que no esté vacío
    if (!textToAnalyze || !textToAnalyze.trim()) {
        alert('Please enter some text to analyze!');
        return;
    }
    
    // 3. Obtener elementos del DOM
    const loadingSpinner = document.getElementById('loadingSpinner');
    const systemResponse = document.getElementById('system_response');
    
    // 4. Mostrar spinner y limpiar resultado anterior
    if (loadingSpinner) {
        loadingSpinner.style.display = 'block';
    }
    systemResponse.innerHTML = '';
    systemResponse.classList.remove('has-result');
    
    try {
        // 5. Hacer petición fetch con URL absoluta
        const response = await fetch(`/sentimentAnalyzer?textToAnalyze=${encodeURIComponent(textToAnalyze)}`);
        
        // 6. Obtener el texto de la respuesta
        const result = await response.text();
        
        // 7. Ocultar spinner
        if (loadingSpinner) {
            loadingSpinner.style.display = 'none';
        }
        
        // 8. Verificar status code
        if (response.ok) {
            // Status 200-299: Éxito
            systemResponse.innerHTML = result;
            systemResponse.classList.add('has-result');
        } else {
            // Status 400-599: Error
            systemResponse.innerHTML = `<span style="color: red;">❌ Error: ${result}</span>`;
        }
        
    } catch (error) {
        // 9. Manejar errores de red
        console.error('Network error:', error);
        
        if (loadingSpinner) {
            loadingSpinner.style.display = 'none';
        }
        
        systemResponse.innerHTML = `<span style="color: red;">❌ Network error: ${error.message}</span>`;
    }
}
