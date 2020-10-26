## Excel Tips and Tricks

##### Author Sudeshna Bora

Started Visual basic excel development (for project : ) . Will add tips and tricks here.

#### <a name="Developer_mode">Initialise Developer Mode:</a><br>

- [] Right-Click on Ribbon. 
- [] Click Customise Ribbon.
- [] Choose Developer

#### <a name="Button">Create Button:</a><br>

- [] Click on Developer Tab
- [] Click on Insert
- [] Click on Button Sign and select the area on the sheet to place button.
- [] Right Click on the button and click on properties to change properties like button name etc.
- [] Right Click on button and click on code to load visual basic editor with function. 

A sample function is shown below : 

<pre><code>
Dim tickr, abbrev

Private Sub Welcome_Click()

Dim original_url

original_url = InputBox("Enter money control url for stock")

Split_url = Split(original_url, "/")

abbrev = Split_url(UBound(Split_url))
tickr = Split_url(UBound(Split_url) - 1)

MsgBox (abbrev)
MsgBox (tickr)

End Sub
</code></pre>

<b>Note: </b> To save such a worksheet/workflow , save it as <code>excel macro enabled</code> type
