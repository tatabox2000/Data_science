var strScriptPath;
var strMoveFrom;
var strMoveTo;

//var objFileSys = new ActiveXObject("Scripting.FileSystemObject");

var obj = new ActiveXObject("WScript.Shell");
obj.CurrentDirectory = "C:/Users/analyst/Documents/Data_science/pyside_blog";
WScript.echo(obj.CurrentDirectory);
//obj.Exec("cmd pyside-uic -o pygraph_Opencv.py pygraph_Opencv.ui");
obj.Exec("pyside-uic -o pygraph_Opencv.py pygraph_Opencv.ui");

//strScriptPath = String(WScript.ScriptFullName).replace(WScript.ScriptName,"");

//strMoveFrom = objFileSys.BuildPath(strScriptPath, "dat");
//strMoveTo = objFileSys.BuildPath(strScriptPath, "backup\\dat");

//#objFileSys.MoveFolder(strMoveFrom, strMoveTo);

//WScript.echo("[dat] Ç [BackUp] Ç…à⁄ìÆÇµÇ‹ÇµÇΩÅB");

obj = null;
