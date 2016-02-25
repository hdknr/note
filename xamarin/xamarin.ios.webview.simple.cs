void InitTiemTable()
{
  string contentDirectoryPath =
    System.IO.Path.Combine (NSBundle.MainBundle.BundlePath, "");
  string html = @"
  <html>
  <head>
  <style>
  body {margin: 0px;  font-family:helvetica;}
  table { width:100% }
  table td { text-align: right}
   tr:nth-child(odd) td {
    background-color: #EAF6FD;
  }
  table tr:nth-child(even) td {
    background-color: #EFEFEF;
  }
  </style>
  </head>
  <body>
   <table>
       <thead>
         <tr>
           <th >時</th>
           <th colspan='8'>分</ht>
  	   </tr>
       </thead>
       <tbody>
          <tr>
             <td> 9 </td>
             <td> 00 </td> <td> 05 </td> <td> 10 </td> <td> 15 </td> <td> 20 </td>
             <td> 25 </td> <td> 30 </td> <td> 35 </td>
          </tr>
          <tr>
             <td> 10 </td>
             <td> 00 </td> <td> 05 </td> <td> 10 </td> <td> 15 </td> <td> 20 </td>
             <td> 25 </td> <td> 30 </td> <td> 35 </td>
          </tr>
       </tbody>
   </table>
  <body>
  </html>";
  TimeTable.LoadHtmlString(html,
    new NSUrl(contentDirectoryPath, true));
}
