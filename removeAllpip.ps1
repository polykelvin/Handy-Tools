Add-Type -AssemblyName System.Windows.Forms
$response = [System.Windows.Forms.MessageBox]::Show('Do you want to uninstall all pip packages?', 'Confirmation', [System.Windows.Forms.MessageBoxButtons]::YesNo)

if ($response -eq 'Yes') {
    pip freeze | % { pip uninstall -y $_ }
}
