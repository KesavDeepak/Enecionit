document.getElementById('fileInput').addEventListener('change', function(event) {
    const file = event.target.files[0];
    if (file && file.name.endsWith('.ipynb')) {
        const reader = new FileReader();
        reader.onload = function(e) {
            const content = e.target.result;
            displayNotebook(content);
        };
        reader.readAsText(file);
    } else {
        alert('Please upload a valid .ipynb file');
    }
});

function displayNotebook(content) {
    const notebook = JSON.parse(content);
    const outputDiv = document.getElementById('output');
    outputDiv.innerHTML = ''; // Clear previous output

    notebook.cells.forEach(cell => {
        if (cell.cell_type === 'code') {
            const codeBlock = document.createElement('pre');
            codeBlock.textContent = cell.source.join('');
            outputDiv.appendChild(codeBlock);

            // Display the output if available
            if (cell.outputs && cell.outputs.length > 0) {
                cell.outputs.forEach(output => {
                    const outputBlock = document.createElement('div');
                    outputBlock.className = 'outputBlock';

                    // Check the type of output and display accordingly
                    if (output.output_type === 'execute_result' && output.data['text/plain']) {
                        outputBlock.textContent = output.data['text/plain'].join('\n');
                    } else if (output.output_type === 'stream' && output.text) {
                        outputBlock.textContent = output.text.join('');
                    } else if (output.output_type === 'display_data' && output.data['text/html']) {
                        outputBlock.innerHTML = output.data['text/html'].join('');
                    }

                    outputDiv.appendChild(outputBlock);
                });
            }
        } else if (cell.cell_type === 'markdown') {
            const markdownBlock = document.createElement('div');
            markdownBlock.innerHTML = marked(cell.source.join('')); // Convert Markdown to HTML
            outputDiv.appendChild(markdownBlock);
        }
    });
}
