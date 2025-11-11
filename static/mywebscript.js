let RunSentimentAnalysis = async () => {
    const textToAnalyze = document.getElementById("textToAnalyze").value;
    
    try {
        const response = await fetch(`sentimentAnalyzer?textToAnalyze=${textToAnalyze}`);
        const result = await response.text();
        document.getElementById("system_response").innerHTML = result;
    } catch (error) {
        console.error('Error:', error);
    }
}
