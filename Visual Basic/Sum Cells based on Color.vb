'Code created by Sumit Bansal from https://trumpexcel.com/
'This VBA code created a function that can be used to sum cells based on color
Function SumByColor(SumRange As Range, SumColor As Range)
Dim SumColorValue As Integer
Dim TotalSum As Long
SumColorValue = SumColor.Interior.ColorIndex
Set rCell = SumRange
For Each rCell In SumRange
If rCell.Interior.ColorIndex = SumColorValue Then
TotalSum = TotalSum + rCell.Value
End If
Next rCell
SumByColor = TotalSum
End Function