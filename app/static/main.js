const submitForm = document.getElementById('submit-form');
const codeInput = document.getElementById('code-input');
const output = document.getElementById('output');
const submitBtn = document.getElementById('submit-btn');
const useDistCheckbox = document.getElementById('use-dist-checkbox');
const headerGroup = document.getElementById('header-group');
const headerInput = document.getElementById('header-input');

codeInput.addEventListener('input', function() {
    submitBtn.disabled = codeInput.value.trim() === '';
});

useDistCheckbox.addEventListener('change', function() {
    headerGroup.hidden = useDistCheckbox.checked;
});

submitForm.addEventListener('submit', async function(e) {
    e.preventDefault();

    submitBtn.disabled = true;
    codeInput.disabled = true;
    headerInput.disabled = true;
    output.textContent = 'Running...';

    try {
        const response = await fetch('/submit', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                code: codeInput.value,
                header: useDistCheckbox.checked ? '' : headerInput.value
            })
        });
        const data = await response.json();
        output.textContent = data.output;
    } catch (err) {
        output.textContent = 'Error: could not reach server.';
    } finally {
        submitBtn.disabled = false;
        codeInput.disabled = false;
        headerInput.disabled = false;
    }
});
