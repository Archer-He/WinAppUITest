









// vOpenFile(png);
// open(new File(png));
var fileRef = new File(png);
// var png_options = new PNGSaveOptions();
app.open(fileRef);

app.preferences.rulerUnits = Units.PIXELS
app.preferences.typeUnits = TypeUnits.PIXELS;

//获取打开的文件document。
var doc = app.activeDocument;
var w = doc.width
var h = doc.height

//定义一个变量[bounds]，用来表示文档需要裁切的区域，即裁切从坐标[1,1]至[doc.width-1, doc.height-1]的区域。
// var bounds = layer.bounds;
// alert(bounds);
// var bounds = [1, 1, w-1, h-1];
// txt.size = new UnitValue(100, 'px');
//定义一个变量[angle]，用来设置裁切的旋转角度为0。
// var angle = 0;
//调用[document]对象的[crop]方法，来裁切当前文档。
// doc.crop(bounds, angle);

// var width = new UnitValue("1","px");
// doc.selection.selectBorder(width);

//裁剪区域 左上-右上-右下-左下
doc.selection.select([[1,1],[w-1,1],[w-1,h-1],[1,h-1]]);

// doc.selection.invert();
// doc.selection.cut();
// doc.paste();
// layer.copy();
// layer.duplicate();

//给中间裁剪下来的部分渲染颜色
// vSetColorToLayer(color,"图层 0")


//设置混合模式为颜色（只能设置常规的混合模式混合为颜色，叠加颜色的混合模式设置不了）
// var Layers = app.activeDocument.layers;
var c = new SolidColor();
c.rgb.hexValue = color;
doc.selection.fill(c, ColorBlendMode.COLOR, 100, true)
// Layers["图层 0"].blendMode = BlendMode.COLORBLEND;
// Layers["图层 0"].photoFilter(c,100,true);



//合并所有图层
// doc.activeLayer.merge();

//保存处理后的.9图为副本
save_path = new File(png + "副本.png");
var png_options = new PNGSaveOptions();
doc.saveAs(save_path,png_options,true,Extension.LOWERCASE);
doc.close(SaveOptions.DONOTSAVECHANGES);



/* 数组判断：包含 */
Array.prototype.contains = function (obj) {
    var index = this.length;
    while (index--) {
        if (this[index] === obj) {
            return true;
        }
    }
    return false;
}
/*
 * 基础数据操作
 *
 */
function jointPath(vRoot,vNail) {
    return vRoot + '\\' + vNail
}
function getLastItemInArray(vArray) {
    return vArray[vArray.length - 1]
}
/*
 * 文件操作
 *
 */
// 打开文件
function vOpenFile(file){
	var idOpn = charIDToTypeID( "Opn " );
    var desc5 = new ActionDescriptor();
    var idnull = charIDToTypeID( "null" );
    desc5.putPath( idnull, new File( file ) );
    var idDocI = charIDToTypeID( "DocI" );
    desc5.putInteger( idDocI, 195 );
	executeAction( idOpn, desc5, DialogModes.NO );
}
//关闭并直接保存
function vCloseAndSave(){
	vSaveFile(); // 关闭前先保存
	vCloseFile();
}

// 关闭不保存当前文档
function vCloseUnSave(){
	var idCls = charIDToTypeID( "Cls " );
    var desc96 = new ActionDescriptor();
    var idSvng = charIDToTypeID( "Svng" );
    var idYsN = charIDToTypeID( "YsN " );
    var idN = charIDToTypeID( "N   " );
    desc96.putEnumerated( idSvng, idYsN, idN );
    var idDocI = charIDToTypeID( "DocI" );
    desc96.putInteger( idDocI, 924 );
    var idforceNotify = stringIDToTypeID( "forceNotify" );
    desc96.putBoolean( idforceNotify, true );
	executeAction( idCls, desc96, DialogModes.NO );
};
// 保存当前文档
function vSaveFile(){
	var idsave = charIDToTypeID( "save" );
    var desc119 = new ActionDescriptor();
    var idIn = charIDToTypeID( "In  " );
//  desc119.putPath( idIn, new File( "C://Users//admin//Desktop//素材//icon//第三方mask.png" ) );
    var idsaveStage = stringIDToTypeID( "saveStage" );
    var idsaveStageType = stringIDToTypeID( "saveStageType" );
    var idsaveBegin = stringIDToTypeID( "saveBegin" );
    desc119.putEnumerated( idsaveStage, idsaveStageType, idsaveBegin );
    var idDocI = charIDToTypeID( "DocI" );
    desc119.putInteger( idDocI, 299 );
	executeAction( idsave, desc119, DialogModes.NO );

	var idsave = charIDToTypeID( "save" );
    var desc120 = new ActionDescriptor();
    var idIn = charIDToTypeID( "In  " );
//  desc120.putPath( idIn, new File( "C://Users//admin//Desktop//素材//icon//第三方mask.png" ) );
    var idDocI = charIDToTypeID( "DocI" );
    desc120.putInteger( idDocI, 299 );
    var idsaveStage = stringIDToTypeID( "saveStage" );
    var idsaveStageType = stringIDToTypeID( "saveStageType" );
    var idsaveSucceeded = stringIDToTypeID( "saveSucceeded" );
    desc120.putEnumerated( idsaveStage, idsaveStageType, idsaveSucceeded );
	executeAction( idsave, desc120, DialogModes.NO );
}

//关闭文档
function vCloseFile(){
    var idCls = charIDToTypeID( "Cls " );
    var desc772 = new ActionDescriptor();
    var idDocI = charIDToTypeID( "DocI" );
    desc772.putInteger( idDocI, 1024 );
    var idforceNotify = stringIDToTypeID( "forceNotify" );
    desc772.putBoolean( idforceNotify, true );
executeAction( idCls, desc772, DialogModes.NO );
};

/*
 * 导出操作
 *
 */
// 保存jpg图片
function vSaveAsJPG(pathName){
var idsave = charIDToTypeID( "save" );
    var desc37 = new ActionDescriptor();
    var idAs = charIDToTypeID( "As  " );
        var desc38 = new ActionDescriptor();
        var idEQlt = charIDToTypeID( "EQlt" );
        desc38.putInteger( idEQlt, 12 );
        var idMttC = charIDToTypeID( "MttC" );
        var idMttC = charIDToTypeID( "MttC" );
        var idNone = charIDToTypeID( "None" );
        desc38.putEnumerated( idMttC, idMttC, idNone );
    var idJPEG = charIDToTypeID( "JPEG" );
    desc37.putObject( idAs, idJPEG, desc38 );
    var idIn = charIDToTypeID( "In  " );
    desc37.putPath( idIn, new File( pathName ) );
    var idDocI = charIDToTypeID( "DocI" );
    desc37.putInteger( idDocI, 255 );
    var idCpy = charIDToTypeID( "Cpy " );
    desc37.putBoolean( idCpy, true );
    var idsaveStage = stringIDToTypeID( "saveStage" );
    var idsaveStageType = stringIDToTypeID( "saveStageType" );
    var idsaveBegin = stringIDToTypeID( "saveBegin" );
    desc37.putEnumerated( idsaveStage, idsaveStageType, idsaveBegin );
executeAction( idsave, desc37, DialogModes.NO );

// =======================================================
var idsave = charIDToTypeID( "save" );
    var desc39 = new ActionDescriptor();
    var idAs = charIDToTypeID( "As  " );
        var desc40 = new ActionDescriptor();
        var idEQlt = charIDToTypeID( "EQlt" );
        desc40.putInteger( idEQlt, 12 );
        var idMttC = charIDToTypeID( "MttC" );
        var idMttC = charIDToTypeID( "MttC" );
        var idNone = charIDToTypeID( "None" );
        desc40.putEnumerated( idMttC, idMttC, idNone );
    var idJPEG = charIDToTypeID( "JPEG" );
    desc39.putObject( idAs, idJPEG, desc40 );
    var idIn = charIDToTypeID( "In  " );
    desc39.putPath( idIn, new File( pathName ) );
    var idDocI = charIDToTypeID( "DocI" );
    desc39.putInteger( idDocI, 255 );
    var idCpy = charIDToTypeID( "Cpy " );
    desc39.putBoolean( idCpy, true );
    var idsaveStage = stringIDToTypeID( "saveStage" );
    var idsaveStageType = stringIDToTypeID( "saveStageType" );
    var idsaveSucceeded = stringIDToTypeID( "saveSucceeded" );
    desc39.putEnumerated( idsaveStage, idsaveStageType, idsaveSucceeded );
executeAction( idsave, desc39, DialogModes.NO );
}
// 另存为png图片
function vSaveAsPNG(pathName){
// =======================================================
var idsave = charIDToTypeID( "save" );
    var desc125 = new ActionDescriptor();
    var idAs = charIDToTypeID( "As  " );
        var desc126 = new ActionDescriptor();
        var idPGIT = charIDToTypeID( "PGIT" );
        var idPGIT = charIDToTypeID( "PGIT" );
        var idPGIN = charIDToTypeID( "PGIN" );
        desc126.putEnumerated( idPGIT, idPGIT, idPGIN );
        var idPNGf = charIDToTypeID( "PNGf" );
        var idPNGf = charIDToTypeID( "PNGf" );
        var idPGAd = charIDToTypeID( "PGAd" );
        desc126.putEnumerated( idPNGf, idPNGf, idPGAd );
        var idCmpr = charIDToTypeID( "Cmpr" );
        desc126.putInteger( idCmpr, 9 );
    var idPNGF = charIDToTypeID( "PNGF" );
    desc125.putObject( idAs, idPNGF, desc126 );
    var idIn = charIDToTypeID( "In  " );
    desc125.putPath( idIn, new File( pathName ) );
    var idDocI = charIDToTypeID( "DocI" );
    desc125.putInteger( idDocI, 705 );
    var idCpy = charIDToTypeID( "Cpy " );
    desc125.putBoolean( idCpy, true );
    var idsaveStage = stringIDToTypeID( "saveStage" );
    var idsaveStageType = stringIDToTypeID( "saveStageType" );
    var idsaveBegin = stringIDToTypeID( "saveBegin" );
    desc125.putEnumerated( idsaveStage, idsaveStageType, idsaveBegin );
executeAction( idsave, desc125, DialogModes.NO );

// =======================================================
var idsave = charIDToTypeID( "save" );
    var desc127 = new ActionDescriptor();
    var idAs = charIDToTypeID( "As  " );
        var desc128 = new ActionDescriptor();
        var idPGIT = charIDToTypeID( "PGIT" );
        var idPGIT = charIDToTypeID( "PGIT" );
        var idPGIN = charIDToTypeID( "PGIN" );
        desc128.putEnumerated( idPGIT, idPGIT, idPGIN );
        var idPNGf = charIDToTypeID( "PNGf" );
        var idPNGf = charIDToTypeID( "PNGf" );
        var idPGAd = charIDToTypeID( "PGAd" );
        desc128.putEnumerated( idPNGf, idPNGf, idPGAd );
        var idCmpr = charIDToTypeID( "Cmpr" );
        desc128.putInteger( idCmpr, 9 );
    var idPNGF = charIDToTypeID( "PNGF" );
    desc127.putObject( idAs, idPNGF, desc128 );
    var idIn = charIDToTypeID( "In  " );
    desc127.putPath( idIn, new File( pathName ) );
    var idDocI = charIDToTypeID( "DocI" );
    desc127.putInteger( idDocI, 705 );
    var idCpy = charIDToTypeID( "Cpy " );
    desc127.putBoolean( idCpy, true );
    var idsaveStage = stringIDToTypeID( "saveStage" );
    var idsaveStageType = stringIDToTypeID( "saveStageType" );
    var idsaveSucceeded = stringIDToTypeID( "saveSucceeded" );
    desc127.putEnumerated( idsaveStage, idsaveStageType, idsaveSucceeded );
executeAction( idsave, desc127, DialogModes.NO );

}
//导出原版（不带虚影）的图片
function vMajorCutNumbers(images_path) {

// =======================================================
var idExpr = charIDToTypeID( "Expr" );
    var desc87 = new ActionDescriptor();
    var idUsng = charIDToTypeID( "Usng" );
        var desc88 = new ActionDescriptor();
        var idOp = charIDToTypeID( "Op  " );
        var idSWOp = charIDToTypeID( "SWOp" );
        var idOpSa = charIDToTypeID( "OpSa" );
        desc88.putEnumerated( idOp, idSWOp, idOpSa );
        var idDIDr = charIDToTypeID( "DIDr" );
        desc88.putBoolean( idDIDr, true );
        var idIn = charIDToTypeID( "In  " );
        desc88.putPath( idIn, new File( images_path ) );
        var idFmt = charIDToTypeID( "Fmt " );
        var idIRFm = charIDToTypeID( "IRFm" );
        var idPNtwofour = charIDToTypeID( "PN24" );
        desc88.putEnumerated( idFmt, idIRFm, idPNtwofour );
        var idIntr = charIDToTypeID( "Intr" );
        desc88.putBoolean( idIntr, false );
        var idTrns = charIDToTypeID( "Trns" );
        desc88.putBoolean( idTrns, true );
        var idMtt = charIDToTypeID( "Mtt " );
        desc88.putBoolean( idMtt, true );
        var idEICC = charIDToTypeID( "EICC" );
        desc88.putBoolean( idEICC, false );
        var idMttR = charIDToTypeID( "MttR" );
        desc88.putInteger( idMttR, 255 );
        var idMttG = charIDToTypeID( "MttG" );
        desc88.putInteger( idMttG, 255 );
        var idMttB = charIDToTypeID( "MttB" );
        desc88.putInteger( idMttB, 255 );
        var idSHTM = charIDToTypeID( "SHTM" );
        desc88.putBoolean( idSHTM, false );
        var idSImg = charIDToTypeID( "SImg" );
        desc88.putBoolean( idSImg, true );
        var idSWsl = charIDToTypeID( "SWsl" );
        var idSTsl = charIDToTypeID( "STsl" );
        var idSLUs = charIDToTypeID( "SLUs" );
        desc88.putEnumerated( idSWsl, idSTsl, idSLUs );
        var idSWch = charIDToTypeID( "SWch" );
        var idSTch = charIDToTypeID( "STch" );
        var idCHsR = charIDToTypeID( "CHsR" );
        desc88.putEnumerated( idSWch, idSTch, idCHsR );
        var idSWmd = charIDToTypeID( "SWmd" );
        var idSTmd = charIDToTypeID( "STmd" );
        var idMDCC = charIDToTypeID( "MDCC" );
        desc88.putEnumerated( idSWmd, idSTmd, idMDCC );
        var idohXH = charIDToTypeID( "ohXH" );
        desc88.putBoolean( idohXH, false );
        var idohIC = charIDToTypeID( "ohIC" );
        desc88.putBoolean( idohIC, true );
        var idohAA = charIDToTypeID( "ohAA" );
        desc88.putBoolean( idohAA, true );
        var idohQA = charIDToTypeID( "ohQA" );
        desc88.putBoolean( idohQA, true );
        var idohCA = charIDToTypeID( "ohCA" );
        desc88.putBoolean( idohCA, false );
        var idohIZ = charIDToTypeID( "ohIZ" );
        desc88.putBoolean( idohIZ, true );
        var idohTC = charIDToTypeID( "ohTC" );
        var idSToc = charIDToTypeID( "SToc" );
        var idOCzerothree = charIDToTypeID( "OC03" );
        desc88.putEnumerated( idohTC, idSToc, idOCzerothree );
        var idohAC = charIDToTypeID( "ohAC" );
        var idSToc = charIDToTypeID( "SToc" );
        var idOCzerothree = charIDToTypeID( "OC03" );
        desc88.putEnumerated( idohAC, idSToc, idOCzerothree );
        var idohIn = charIDToTypeID( "ohIn" );
        desc88.putInteger( idohIn, -1 );
        var idohLE = charIDToTypeID( "ohLE" );
        var idSTle = charIDToTypeID( "STle" );
        var idLEzerothree = charIDToTypeID( "LE03" );
        desc88.putEnumerated( idohLE, idSTle, idLEzerothree );
        var idohEn = charIDToTypeID( "ohEn" );
        var idSTen = charIDToTypeID( "STen" );
        var idENzerozero = charIDToTypeID( "EN00" );
        desc88.putEnumerated( idohEn, idSTen, idENzerozero );
        var idolCS = charIDToTypeID( "olCS" );
        desc88.putBoolean( idolCS, false );
        var idolEC = charIDToTypeID( "olEC" );
        var idSTst = charIDToTypeID( "STst" );
        var idSTzerozero = charIDToTypeID( "ST00" );
        desc88.putEnumerated( idolEC, idSTst, idSTzerozero );
        var idolWH = charIDToTypeID( "olWH" );
        var idSTwh = charIDToTypeID( "STwh" );
        var idWHzeroone = charIDToTypeID( "WH01" );
        desc88.putEnumerated( idolWH, idSTwh, idWHzeroone );
        var idolSV = charIDToTypeID( "olSV" );
        var idSTsp = charIDToTypeID( "STsp" );
        var idSPzerofour = charIDToTypeID( "SP04" );
        desc88.putEnumerated( idolSV, idSTsp, idSPzerofour );
        var idolSH = charIDToTypeID( "olSH" );
        var idSTsp = charIDToTypeID( "STsp" );
        var idSPzerofour = charIDToTypeID( "SP04" );
        desc88.putEnumerated( idolSH, idSTsp, idSPzerofour );
        var idolNC = charIDToTypeID( "olNC" );
            var list9 = new ActionList();
                var desc89 = new ActionDescriptor();
                var idncTp = charIDToTypeID( "ncTp" );
                var idSTnc = charIDToTypeID( "STnc" );
                var idNCzerozero = charIDToTypeID( "NC00" );
                desc89.putEnumerated( idncTp, idSTnc, idNCzerozero );
            var idSCnc = charIDToTypeID( "SCnc" );
            list9.putObject( idSCnc, desc89 );
                var desc90 = new ActionDescriptor();
                var idncTp = charIDToTypeID( "ncTp" );
                var idSTnc = charIDToTypeID( "STnc" );
                var idNConenine = charIDToTypeID( "NC19" );
                desc90.putEnumerated( idncTp, idSTnc, idNConenine );
            var idSCnc = charIDToTypeID( "SCnc" );
            list9.putObject( idSCnc, desc90 );
                var desc91 = new ActionDescriptor();
                var idncTp = charIDToTypeID( "ncTp" );
                var idSTnc = charIDToTypeID( "STnc" );
                var idNCtwoeight = charIDToTypeID( "NC28" );
                desc91.putEnumerated( idncTp, idSTnc, idNCtwoeight );
            var idSCnc = charIDToTypeID( "SCnc" );
            list9.putObject( idSCnc, desc91 );
                var desc92 = new ActionDescriptor();
                var idncTp = charIDToTypeID( "ncTp" );
                var idSTnc = charIDToTypeID( "STnc" );
                var idNCtwofour = charIDToTypeID( "NC24" );
                desc92.putEnumerated( idncTp, idSTnc, idNCtwofour );
            var idSCnc = charIDToTypeID( "SCnc" );
            list9.putObject( idSCnc, desc92 );
                var desc93 = new ActionDescriptor();
                var idncTp = charIDToTypeID( "ncTp" );
                var idSTnc = charIDToTypeID( "STnc" );
                var idNCtwofour = charIDToTypeID( "NC24" );
                desc93.putEnumerated( idncTp, idSTnc, idNCtwofour );
            var idSCnc = charIDToTypeID( "SCnc" );
            list9.putObject( idSCnc, desc93 );
                var desc94 = new ActionDescriptor();
                var idncTp = charIDToTypeID( "ncTp" );
                var idSTnc = charIDToTypeID( "STnc" );
                var idNCtwofour = charIDToTypeID( "NC24" );
                desc94.putEnumerated( idncTp, idSTnc, idNCtwofour );
            var idSCnc = charIDToTypeID( "SCnc" );
            list9.putObject( idSCnc, desc94 );
        desc88.putList( idolNC, list9 );
        var idobIA = charIDToTypeID( "obIA" );
        desc88.putBoolean( idobIA, false );
        var idobIP = charIDToTypeID( "obIP" );
        desc88.putString( idobIP, """""" );
        var idobCS = charIDToTypeID( "obCS" );
        var idSTcs = charIDToTypeID( "STcs" );
        var idCSzeroone = charIDToTypeID( "CS01" );
        desc88.putEnumerated( idobCS, idSTcs, idCSzeroone );
        var idovNC = charIDToTypeID( "ovNC" );
            var list10 = new ActionList();
                var desc95 = new ActionDescriptor();
                var idncTp = charIDToTypeID( "ncTp" );
                var idSTnc = charIDToTypeID( "STnc" );
                var idNCzeroone = charIDToTypeID( "NC01" );
                desc95.putEnumerated( idncTp, idSTnc, idNCzeroone );
            var idSCnc = charIDToTypeID( "SCnc" );
            list10.putObject( idSCnc, desc95 );
                var desc96 = new ActionDescriptor();
                var idncTp = charIDToTypeID( "ncTp" );
                var idSTnc = charIDToTypeID( "STnc" );
                var idNCtwozero = charIDToTypeID( "NC20" );
                desc96.putEnumerated( idncTp, idSTnc, idNCtwozero );
            var idSCnc = charIDToTypeID( "SCnc" );
            list10.putObject( idSCnc, desc96 );
                var desc97 = new ActionDescriptor();
                var idncTp = charIDToTypeID( "ncTp" );
                var idSTnc = charIDToTypeID( "STnc" );
                var idNCzerotwo = charIDToTypeID( "NC02" );
                desc97.putEnumerated( idncTp, idSTnc, idNCzerotwo );
            var idSCnc = charIDToTypeID( "SCnc" );
            list10.putObject( idSCnc, desc97 );
                var desc98 = new ActionDescriptor();
                var idncTp = charIDToTypeID( "ncTp" );
                var idSTnc = charIDToTypeID( "STnc" );
                var idNConenine = charIDToTypeID( "NC19" );
                desc98.putEnumerated( idncTp, idSTnc, idNConenine );
            var idSCnc = charIDToTypeID( "SCnc" );
            list10.putObject( idSCnc, desc98 );
                var desc99 = new ActionDescriptor();
                var idncTp = charIDToTypeID( "ncTp" );
                var idSTnc = charIDToTypeID( "STnc" );
                var idNCzerosix = charIDToTypeID( "NC06" );
                desc99.putEnumerated( idncTp, idSTnc, idNCzerosix );
            var idSCnc = charIDToTypeID( "SCnc" );
            list10.putObject( idSCnc, desc99 );
                var desc100 = new ActionDescriptor();
                var idncTp = charIDToTypeID( "ncTp" );
                var idSTnc = charIDToTypeID( "STnc" );
                var idNCtwofour = charIDToTypeID( "NC24" );
                desc100.putEnumerated( idncTp, idSTnc, idNCtwofour );
            var idSCnc = charIDToTypeID( "SCnc" );
            list10.putObject( idSCnc, desc100 );
                var desc101 = new ActionDescriptor();
                var idncTp = charIDToTypeID( "ncTp" );
                var idSTnc = charIDToTypeID( "STnc" );
                var idNCtwofour = charIDToTypeID( "NC24" );
                desc101.putEnumerated( idncTp, idSTnc, idNCtwofour );
            var idSCnc = charIDToTypeID( "SCnc" );
            list10.putObject( idSCnc, desc101 );
                var desc102 = new ActionDescriptor();
                var idncTp = charIDToTypeID( "ncTp" );
                var idSTnc = charIDToTypeID( "STnc" );
                var idNCtwofour = charIDToTypeID( "NC24" );
                desc102.putEnumerated( idncTp, idSTnc, idNCtwofour );
            var idSCnc = charIDToTypeID( "SCnc" );
            list10.putObject( idSCnc, desc102 );
                var desc103 = new ActionDescriptor();
                var idncTp = charIDToTypeID( "ncTp" );
                var idSTnc = charIDToTypeID( "STnc" );
                var idNCtwotwo = charIDToTypeID( "NC22" );
                desc103.putEnumerated( idncTp, idSTnc, idNCtwotwo );
            var idSCnc = charIDToTypeID( "SCnc" );
            list10.putObject( idSCnc, desc103 );
        desc88.putList( idovNC, list10 );
        var idovCM = charIDToTypeID( "ovCM" );
        desc88.putBoolean( idovCM, false );
        var idovCW = charIDToTypeID( "ovCW" );
        desc88.putBoolean( idovCW, true );
        var idovCU = charIDToTypeID( "ovCU" );
        desc88.putBoolean( idovCU, true );
        var idovSF = charIDToTypeID( "ovSF" );
        desc88.putBoolean( idovSF, true );
        var idovCB = charIDToTypeID( "ovCB" );
        desc88.putBoolean( idovCB, true );
        var idovSN = charIDToTypeID( "ovSN" );
        desc88.putString( idovSN, """images""" );
    var idSaveForWeb = stringIDToTypeID( "SaveForWeb" );
    desc87.putObject( idUsng, idSaveForWeb, desc88 );
executeAction( idExpr, desc87, DialogModes.NO );
}

//导出用户切片
function vOutputUserSection(images_path){
        var idExpr = charIDToTypeID( "Expr" );
    var desc1043 = new ActionDescriptor();
    var idUsng = charIDToTypeID( "Usng" );
        var desc1044 = new ActionDescriptor();
        var idOp = charIDToTypeID( "Op  " );
        var idSWOp = charIDToTypeID( "SWOp" );
        var idOpSa = charIDToTypeID( "OpSa" );
        desc1044.putEnumerated( idOp, idSWOp, idOpSa );
        var idDIDr = charIDToTypeID( "DIDr" );
        desc1044.putBoolean( idDIDr, true );
        var idIn = charIDToTypeID( "In  " );
        desc1044.putPath( idIn, new File( images_path ) );
        var idFmt = charIDToTypeID( "Fmt " );
        var idIRFm = charIDToTypeID( "IRFm" );
        var idPNtwofour = charIDToTypeID( "PN24" );
        desc1044.putEnumerated( idFmt, idIRFm, idPNtwofour );
        var idIntr = charIDToTypeID( "Intr" );
        desc1044.putBoolean( idIntr, false );
        var idTrns = charIDToTypeID( "Trns" );
        desc1044.putBoolean( idTrns, true );
        var idMtt = charIDToTypeID( "Mtt " );
        desc1044.putBoolean( idMtt, true );
        var idEICC = charIDToTypeID( "EICC" );
        desc1044.putBoolean( idEICC, false );
        var idMttR = charIDToTypeID( "MttR" );
        desc1044.putInteger( idMttR, 255 );
        var idMttG = charIDToTypeID( "MttG" );
        desc1044.putInteger( idMttG, 255 );
        var idMttB = charIDToTypeID( "MttB" );
        desc1044.putInteger( idMttB, 255 );
        var idSHTM = charIDToTypeID( "SHTM" );
        desc1044.putBoolean( idSHTM, false );
        var idSImg = charIDToTypeID( "SImg" );
        desc1044.putBoolean( idSImg, true );
        var idSWsl = charIDToTypeID( "SWsl" );
        var idSTsl = charIDToTypeID( "STsl" );
        var idSLUs = charIDToTypeID( "SLUs" );
        desc1044.putEnumerated( idSWsl, idSTsl, idSLUs );
        var idSWch = charIDToTypeID( "SWch" );
        var idSTch = charIDToTypeID( "STch" );
        var idCHsR = charIDToTypeID( "CHsR" );
        desc1044.putEnumerated( idSWch, idSTch, idCHsR );
        var idSWmd = charIDToTypeID( "SWmd" );
        var idSTmd = charIDToTypeID( "STmd" );
        var idMDCC = charIDToTypeID( "MDCC" );
        desc1044.putEnumerated( idSWmd, idSTmd, idMDCC );
        var idohXH = charIDToTypeID( "ohXH" );
        desc1044.putBoolean( idohXH, false );
        var idohIC = charIDToTypeID( "ohIC" );
        desc1044.putBoolean( idohIC, true );
        var idohAA = charIDToTypeID( "ohAA" );
        desc1044.putBoolean( idohAA, true );
        var idohQA = charIDToTypeID( "ohQA" );
        desc1044.putBoolean( idohQA, true );
        var idohCA = charIDToTypeID( "ohCA" );
        desc1044.putBoolean( idohCA, false );
        var idohIZ = charIDToTypeID( "ohIZ" );
        desc1044.putBoolean( idohIZ, true );
        var idohTC = charIDToTypeID( "ohTC" );
        var idSToc = charIDToTypeID( "SToc" );
        var idOCzerothree = charIDToTypeID( "OC03" );
        desc1044.putEnumerated( idohTC, idSToc, idOCzerothree );
        var idohAC = charIDToTypeID( "ohAC" );
        var idSToc = charIDToTypeID( "SToc" );
        var idOCzerothree = charIDToTypeID( "OC03" );
        desc1044.putEnumerated( idohAC, idSToc, idOCzerothree );
        var idohIn = charIDToTypeID( "ohIn" );
        desc1044.putInteger( idohIn, -1 );
        var idohLE = charIDToTypeID( "ohLE" );
        var idSTle = charIDToTypeID( "STle" );
        var idLEzerothree = charIDToTypeID( "LE03" );
        desc1044.putEnumerated( idohLE, idSTle, idLEzerothree );
        var idohEn = charIDToTypeID( "ohEn" );
        var idSTen = charIDToTypeID( "STen" );
        var idENzerozero = charIDToTypeID( "EN00" );
        desc1044.putEnumerated( idohEn, idSTen, idENzerozero );
        var idolCS = charIDToTypeID( "olCS" );
        desc1044.putBoolean( idolCS, false );
        var idolEC = charIDToTypeID( "olEC" );
        var idSTst = charIDToTypeID( "STst" );
        var idSTzerozero = charIDToTypeID( "ST00" );
        desc1044.putEnumerated( idolEC, idSTst, idSTzerozero );
        var idolWH = charIDToTypeID( "olWH" );
        var idSTwh = charIDToTypeID( "STwh" );
        var idWHzeroone = charIDToTypeID( "WH01" );
        desc1044.putEnumerated( idolWH, idSTwh, idWHzeroone );
        var idolSV = charIDToTypeID( "olSV" );
        var idSTsp = charIDToTypeID( "STsp" );
        var idSPzerofour = charIDToTypeID( "SP04" );
        desc1044.putEnumerated( idolSV, idSTsp, idSPzerofour );
        var idolSH = charIDToTypeID( "olSH" );
        var idSTsp = charIDToTypeID( "STsp" );
        var idSPzerofour = charIDToTypeID( "SP04" );
        desc1044.putEnumerated( idolSH, idSTsp, idSPzerofour );
        var idolNC = charIDToTypeID( "olNC" );
            var list264 = new ActionList();
                var desc1045 = new ActionDescriptor();
                var idncTp = charIDToTypeID( "ncTp" );
                var idSTnc = charIDToTypeID( "STnc" );
                var idNCzerozero = charIDToTypeID( "NC00" );
                desc1045.putEnumerated( idncTp, idSTnc, idNCzerozero );
            var idSCnc = charIDToTypeID( "SCnc" );
            list264.putObject( idSCnc, desc1045 );
                var desc1046 = new ActionDescriptor();
                var idncTp = charIDToTypeID( "ncTp" );
                var idSTnc = charIDToTypeID( "STnc" );
                var idNConenine = charIDToTypeID( "NC19" );
                desc1046.putEnumerated( idncTp, idSTnc, idNConenine );
            var idSCnc = charIDToTypeID( "SCnc" );
            list264.putObject( idSCnc, desc1046 );
                var desc1047 = new ActionDescriptor();
                var idncTp = charIDToTypeID( "ncTp" );
                var idSTnc = charIDToTypeID( "STnc" );
                var idNCtwoeight = charIDToTypeID( "NC28" );
                desc1047.putEnumerated( idncTp, idSTnc, idNCtwoeight );
            var idSCnc = charIDToTypeID( "SCnc" );
            list264.putObject( idSCnc, desc1047 );
                var desc1048 = new ActionDescriptor();
                var idncTp = charIDToTypeID( "ncTp" );
                var idSTnc = charIDToTypeID( "STnc" );
                var idNCtwofour = charIDToTypeID( "NC24" );
                desc1048.putEnumerated( idncTp, idSTnc, idNCtwofour );
            var idSCnc = charIDToTypeID( "SCnc" );
            list264.putObject( idSCnc, desc1048 );
                var desc1049 = new ActionDescriptor();
                var idncTp = charIDToTypeID( "ncTp" );
                var idSTnc = charIDToTypeID( "STnc" );
                var idNCtwofour = charIDToTypeID( "NC24" );
                desc1049.putEnumerated( idncTp, idSTnc, idNCtwofour );
            var idSCnc = charIDToTypeID( "SCnc" );
            list264.putObject( idSCnc, desc1049 );
                var desc1050 = new ActionDescriptor();
                var idncTp = charIDToTypeID( "ncTp" );
                var idSTnc = charIDToTypeID( "STnc" );
                var idNCtwofour = charIDToTypeID( "NC24" );
                desc1050.putEnumerated( idncTp, idSTnc, idNCtwofour );
            var idSCnc = charIDToTypeID( "SCnc" );
            list264.putObject( idSCnc, desc1050 );
        desc1044.putList( idolNC, list264 );
        var idobIA = charIDToTypeID( "obIA" );
        desc1044.putBoolean( idobIA, false );
        var idobIP = charIDToTypeID( "obIP" );
        desc1044.putString( idobIP, "" );
        var idobCS = charIDToTypeID( "obCS" );
        var idSTcs = charIDToTypeID( "STcs" );
        var idCSzeroone = charIDToTypeID( "CS01" );
        desc1044.putEnumerated( idobCS, idSTcs, idCSzeroone );
        var idovNC = charIDToTypeID( "ovNC" );
            var list265 = new ActionList();
                var desc1051 = new ActionDescriptor();
                var idncTp = charIDToTypeID( "ncTp" );
                var idSTnc = charIDToTypeID( "STnc" );
                var idNCzeroone = charIDToTypeID( "NC01" );
                desc1051.putEnumerated( idncTp, idSTnc, idNCzeroone );
            var idSCnc = charIDToTypeID( "SCnc" );
            list265.putObject( idSCnc, desc1051 );
                var desc1052 = new ActionDescriptor();
                var idncTp = charIDToTypeID( "ncTp" );
                var idSTnc = charIDToTypeID( "STnc" );
                var idNCtwozero = charIDToTypeID( "NC20" );
                desc1052.putEnumerated( idncTp, idSTnc, idNCtwozero );
            var idSCnc = charIDToTypeID( "SCnc" );
            list265.putObject( idSCnc, desc1052 );
                var desc1053 = new ActionDescriptor();
                var idncTp = charIDToTypeID( "ncTp" );
                var idSTnc = charIDToTypeID( "STnc" );
                var idNCzerotwo = charIDToTypeID( "NC02" );
                desc1053.putEnumerated( idncTp, idSTnc, idNCzerotwo );
            var idSCnc = charIDToTypeID( "SCnc" );
            list265.putObject( idSCnc, desc1053 );
                var desc1054 = new ActionDescriptor();
                var idncTp = charIDToTypeID( "ncTp" );
                var idSTnc = charIDToTypeID( "STnc" );
                var idNConenine = charIDToTypeID( "NC19" );
                desc1054.putEnumerated( idncTp, idSTnc, idNConenine );
            var idSCnc = charIDToTypeID( "SCnc" );
            list265.putObject( idSCnc, desc1054 );
                var desc1055 = new ActionDescriptor();
                var idncTp = charIDToTypeID( "ncTp" );
                var idSTnc = charIDToTypeID( "STnc" );
                var idNCzerosix = charIDToTypeID( "NC06" );
                desc1055.putEnumerated( idncTp, idSTnc, idNCzerosix );
            var idSCnc = charIDToTypeID( "SCnc" );
            list265.putObject( idSCnc, desc1055 );
                var desc1056 = new ActionDescriptor();
                var idncTp = charIDToTypeID( "ncTp" );
                var idSTnc = charIDToTypeID( "STnc" );
                var idNCtwofour = charIDToTypeID( "NC24" );
                desc1056.putEnumerated( idncTp, idSTnc, idNCtwofour );
            var idSCnc = charIDToTypeID( "SCnc" );
            list265.putObject( idSCnc, desc1056 );
                var desc1057 = new ActionDescriptor();
                var idncTp = charIDToTypeID( "ncTp" );
                var idSTnc = charIDToTypeID( "STnc" );
                var idNCtwofour = charIDToTypeID( "NC24" );
                desc1057.putEnumerated( idncTp, idSTnc, idNCtwofour );
            var idSCnc = charIDToTypeID( "SCnc" );
            list265.putObject( idSCnc, desc1057 );
                var desc1058 = new ActionDescriptor();
                var idncTp = charIDToTypeID( "ncTp" );
                var idSTnc = charIDToTypeID( "STnc" );
                var idNCtwofour = charIDToTypeID( "NC24" );
                desc1058.putEnumerated( idncTp, idSTnc, idNCtwofour );
            var idSCnc = charIDToTypeID( "SCnc" );
            list265.putObject( idSCnc, desc1058 );
                var desc1059 = new ActionDescriptor();
                var idncTp = charIDToTypeID( "ncTp" );
                var idSTnc = charIDToTypeID( "STnc" );
                var idNCtwotwo = charIDToTypeID( "NC22" );
                desc1059.putEnumerated( idncTp, idSTnc, idNCtwotwo );
            var idSCnc = charIDToTypeID( "SCnc" );
            list265.putObject( idSCnc, desc1059 );
        desc1044.putList( idovNC, list265 );
        var idovCM = charIDToTypeID( "ovCM" );
        desc1044.putBoolean( idovCM, false );
        var idovCW = charIDToTypeID( "ovCW" );
        desc1044.putBoolean( idovCW, true );
        var idovCU = charIDToTypeID( "ovCU" );
        desc1044.putBoolean( idovCU, true );
        var idovSF = charIDToTypeID( "ovSF" );
        desc1044.putBoolean( idovSF, true );
        var idovCB = charIDToTypeID( "ovCB" );
        desc1044.putBoolean( idovCB, true );
        var idovSN = charIDToTypeID( "ovSN" );
        desc1044.putString( idovSN, """images""" );
    var idSaveForWeb = stringIDToTypeID( "SaveForWeb" );
    desc1043.putObject( idUsng, idSaveForWeb, desc1044 );
executeAction( idExpr, desc1043, DialogModes.NO );
}



/*
 * xml操作
 *
 */
//写xml
function writeXML(file,xml) {//---------------------------------
	try {
	file = File(file)
	file.encoding = "UTF8";
	file.open("w");
	file.write(xml);
	file.close();
	} catch (e) {
	alert("" + e.message + "\n Error write to XML " ); }
	return true;
};
//读xml
function readXML (file) {//------------------------------------
  try {
    file = File(file)
    file.encoding = "UTF8";
//    file.lineFeed = "unix";
    file.open('r');
    content = file.read();
    file.close();
    return new XML(content);
  } catch (e) {
    alert("" + e.message + "\n Error read from XML " + file );
  }
   return content;
};

/*
 * 图层操作
 *
 */
// 选择图层
function vSelectLayer(vLayerName) {
    var idslct = charIDToTypeID( "slct" );
    var desc947 = new ActionDescriptor();
    var idnull = charIDToTypeID( "null" );
        var ref209 = new ActionReference();
        var idLyr = charIDToTypeID( "Lyr " );
        ref209.putName( idLyr, vLayerName );
    desc947.putReference( idnull, ref209 );
    var idMkVs = charIDToTypeID( "MkVs" );
    desc947.putBoolean( idMkVs, false );
    var idLyrI = charIDToTypeID( "LyrI" );
        var list121 = new ActionList();
        list121.putInteger( 281 );
    desc947.putList( idLyrI, list121 );
executeAction( idslct, desc947, DialogModes.NO );
}
// 栅格化图层
function vRaserizeLayer() {
var idrasterizeLayer = stringIDToTypeID( "rasterizeLayer" );
    var desc950 = new ActionDescriptor();
    var idnull = charIDToTypeID( "null" );
        var ref210 = new ActionReference();
        var idLyr = charIDToTypeID( "Lyr " );
        var idOrdn = charIDToTypeID( "Ordn" );
        var idTrgt = charIDToTypeID( "Trgt" );
        ref210.putEnumerated( idLyr, idOrdn, idTrgt );
    desc950.putReference( idnull, ref210 );
executeAction( idrasterizeLayer, desc950, DialogModes.NO );

}
// 隐藏图层
function hideLayer(name){
    vSelectLayer (name)
// =======================================================
var idHd = charIDToTypeID( "Hd  " );
    var desc107 = new ActionDescriptor();
    var idnull = charIDToTypeID( "null" );
        var list34 = new ActionList();
            var ref45 = new ActionReference();
            var idLyr = charIDToTypeID( "Lyr " );
            var idOrdn = charIDToTypeID( "Ordn" );
            var idTrgt = charIDToTypeID( "Trgt" );
            ref45.putEnumerated( idLyr, idOrdn, idTrgt );
        list34.putReference( ref45 );
    desc107.putList( idnull, list34 );
executeAction( idHd, desc107, DialogModes.NO );
}
// 显示图层
function showLayer(name){
    vSelectLayer (name)
    var idShw = charIDToTypeID( "Shw " );
    var desc108 = new ActionDescriptor();
    var idnull = charIDToTypeID( "null" );
        var list35 = new ActionList();
            var ref46 = new ActionReference();
            var idLyr = charIDToTypeID( "Lyr " );
            var idOrdn = charIDToTypeID( "Ordn" );
            var idTrgt = charIDToTypeID( "Trgt" );
            ref46.putEnumerated( idLyr, idOrdn, idTrgt );
        list35.putReference( ref46 );
    desc108.putList( idnull, list35 );
executeAction( idShw, desc108, DialogModes.NO );
}

/*
 * 智能对象操作
 *
 */
// 打开智能对象
function vEditLayer(name){
	// 选择
    vSelectLayer(name)

	var idplacedLayerEditContents = stringIDToTypeID( "placedLayerEditContents" );
    var desc11 = new ActionDescriptor();
	executeAction( idplacedLayerEditContents, desc11, DialogModes.NO ); // 编辑
}
// 更新链接的智能对象
function vUpdateSmartLayer(vLayerName) {
    vSelectLayer(vLayerName)

    var idplacedLayerUpdateAllModified = stringIDToTypeID( "placedLayerUpdateAllModified" );
    executeAction( idplacedLayerUpdateAllModified, undefined, DialogModes.NO );
}
// 创建智能对象
function vCreateSmartObject() {
    var idnewPlacedLayer = stringIDToTypeID( "newPlacedLayer" );
    executeAction( idnewPlacedLayer, undefined, DialogModes.NO );

}


/*
 * 画布操作
 *
 */
//改变画布大小，有方向
function vChangeCanvasBySide(vWidth,vHeight,hrz_Side,vrtSide) {
    /*
        hrz_Side:
            "Left","Rght","Cntr"
        vrtSide:
            "Bttm","Top ","Cntr"
     */
var idCnvS = charIDToTypeID( "CnvS" );
    var desc247 = new ActionDescriptor();
    var idWdth = charIDToTypeID( "Wdth" );
    var idPxl = charIDToTypeID( "#Pxl" );
    desc247.putUnitDouble( idWdth, idPxl, vWidth );
    var idHght = charIDToTypeID( "Hght" );
    var idPxl = charIDToTypeID( "#Pxl" );
    desc247.putUnitDouble( idHght, idPxl, vHeight );
    var idHrzn = charIDToTypeID( "Hrzn" );
    var idHrzL = charIDToTypeID( "HrzL" );
    var idLeft = charIDToTypeID( hrz_Side );
    desc247.putEnumerated( idHrzn, idHrzL, idLeft );
    var idVrtc = charIDToTypeID( "Vrtc" );
    var idVrtL = charIDToTypeID( "VrtL" );
    var idTop = charIDToTypeID( vrtSide );
    desc247.putEnumerated( idVrtc, idVrtL, idTop );
executeAction( idCnvS, desc247, DialogModes.NO );
}


//给指定图层名，叠加指定色号的颜色
function vSetColorToLayer(vColorHex, vLayerName) {

    //先选中图层
    vSelectLayer(vLayerName);
    //再颜色叠加
    var meta_color_rgba = createColorWithHex (vColorHex)
    vColorOverlay (meta_color_rgba)

}

function createColorWithHex(vHex){
    var c = new SolidColor();
    c.rgb.hexValue = vHex;
     //要转化成rgba数组
    var metaRGBA = [c.rgb.red, c.rgb.green, c.rgb.blue, 100];
    return metaRGBA;
}

function vColorOverlay(solidColor){
    var red_sc = solidColor[0];
    var green_sc = solidColor[1];
    var blue_sc = solidColor[2];
    var vAlpha = solidColor[3];

var idsetd = charIDToTypeID( "setd" );
    var desc508 = new ActionDescriptor();
    var idnull = charIDToTypeID( "null" );
        var ref172 = new ActionReference();
        var idPrpr = charIDToTypeID( "Prpr" );
        var idLefx = charIDToTypeID( "Lefx" );
        ref172.putProperty( idPrpr, idLefx );
        var idLyr = charIDToTypeID( "Lyr " );
        var idOrdn = charIDToTypeID( "Ordn" );
        var idTrgt = charIDToTypeID( "Trgt" );
        ref172.putEnumerated( idLyr, idOrdn, idTrgt );
    desc508.putReference( idnull, ref172 );
    var idT = charIDToTypeID( "T   " );
        var desc509 = new ActionDescriptor();
        var idScl = charIDToTypeID( "Scl " );
        var idPrc = charIDToTypeID( "#Prc" );
        desc509.putUnitDouble( idScl, idPrc, 100.000000 );
        var idSoFi = charIDToTypeID( "SoFi" );
            var desc510 = new ActionDescriptor();
            var idenab = charIDToTypeID( "enab" );
            desc510.putBoolean( idenab, true );
            var idpresent = stringIDToTypeID( "present" );
            desc510.putBoolean( idpresent, true );
            var idshowInDialog = stringIDToTypeID( "showInDialog" );
            desc510.putBoolean( idshowInDialog, true );
            var idMd = charIDToTypeID( "Md  " );
            var idBlnM = charIDToTypeID( "BlnM" );
            var idNrml = charIDToTypeID( "Nrml" );
            desc510.putEnumerated( idMd, idBlnM, idNrml );
            var idClr = charIDToTypeID( "Clr " );
                var desc511 = new ActionDescriptor();
                var idRd = charIDToTypeID( "Rd  " );
                desc511.putDouble( idRd, red_sc );
                var idGrn = charIDToTypeID( "Grn " );
                desc511.putDouble( idGrn, green_sc );
                var idBl = charIDToTypeID( "Bl  " );
                desc511.putDouble( idBl, blue_sc );
            var idRGBC = charIDToTypeID( "RGBC" );
            desc510.putObject( idClr, idRGBC, desc511 );
            var idOpct = charIDToTypeID( "Opct" );
            var idPrc = charIDToTypeID( "#Prc" );
            desc510.putUnitDouble( idOpct, idPrc, vAlpha );
        var idSoFi = charIDToTypeID( "SoFi" );
        desc509.putObject( idSoFi, idSoFi, desc510 );
    var idLefx = charIDToTypeID( "Lefx" );
    desc508.putObject( idT, idLefx, desc509 );
executeAction( idsetd, desc508, DialogModes.NO );
}






