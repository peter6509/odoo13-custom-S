<?xml version="1.0" encoding="UTF-8"?>
<Form xmlVersion="20170720" releaseVersion="10.0.0">
<TableDataMap>
<TableData name="ds1" class="com.fr.data.impl.DBTableData">
<Parameters>
<Parameter>
<Attributes name="地區"/>
<O>
<![CDATA[]]></O>
</Parameter>
</Parameters>
<Attributes maxMemRowCount="-1"/>
<Connection class="com.fr.data.impl.NameDatabaseConnection">
<DatabaseName>
<![CDATA[FRDemoTW]]></DatabaseName>
</Connection>
<Query>
<![CDATA[select 城市, 城市||city as 城市city from 客戶 
where 地區='${地區}' ]]></Query>
<PageQuery>
<![CDATA[]]></PageQuery>
</TableData>
<TableData name="ds2" class="com.fr.data.impl.DBTableData">
<Parameters>
<Parameter>
<Attributes name="城市"/>
<O>
<![CDATA[]]></O>
</Parameter>
<Parameter>
<Attributes name="地區"/>
<O>
<![CDATA[]]></O>
</Parameter>
</Parameters>
<Attributes maxMemRowCount="-1"/>
<Connection class="com.fr.data.impl.NameDatabaseConnection">
<DatabaseName>
<![CDATA[FRDemoTW]]></DatabaseName>
</Connection>
<Query>
<![CDATA[SELECT 公司名稱 FROM 客戶 where 城市='${城市}' and 地區='${地區}']]></Query>
<PageQuery>
<![CDATA[]]></PageQuery>
</TableData>
<TableData name="訂單" class="com.fr.data.impl.DBTableData">
<Parameters/>
<Attributes maxMemRowCount="-1"/>
<Connection class="com.fr.data.impl.NameDatabaseConnection">
<DatabaseName>
<![CDATA[FRDemoTW]]></DatabaseName>
</Connection>
<Query>
<![CDATA[select 客戶.地區,客戶.城市,客戶.City,客戶.客戶ID,客戶.公司名稱,訂單.訂單ID,訂單.訂購日期,訂單.發貨日期,訂單.到貨日期,訂單.運貨商,貨主名稱,訂單明細.產品ID,(訂單明細.單價*訂單明細.數量) AS 金額
from 客戶,S訂單 訂單 ,S訂單明細 訂單明細
where 訂單.訂單ID=訂單明細.訂單ID and 客戶.客戶ID=訂單.客戶ID]]></Query>
<PageQuery>
<![CDATA[]]></PageQuery>
</TableData>
</TableDataMap>
<FormMobileAttr>
<FormMobileAttr refresh="false" isUseHTML="false" isMobileOnly="false" isAdaptivePropertyAutoMatch="false" appearRefresh="false" promptWhenLeaveWithoutSubmit="false"/>
</FormMobileAttr>
<Parameters/>
<Layout class="com.fr.form.ui.container.WBorderLayout">
<WidgetName name="form"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<Margin top="0" left="0" bottom="0" right="0"/>
<Border>
<border style="0" color="-723724" borderRadius="0" type="0" borderStyle="0"/>
<WidgetTitle>
<O>
<![CDATA[新建标题]]></O>
<FRFont name="SimSun" style="0" size="72"/>
<Position pos="0"/>
</WidgetTitle>
<Alpha alpha="1.0"/>
</Border>
<LCAttr vgap="0" hgap="0" compInterval="0"/>
<Center class="com.fr.form.ui.container.WFitLayout">
<WidgetName name="body"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<Margin top="20" left="1" bottom="1" right="1"/>
<Border>
<border style="0" color="-723724" borderRadius="0" type="0" borderStyle="0"/>
<WidgetTitle>
<O>
<![CDATA[新建标题]]></O>
<FRFont name="SimSun" style="0" size="72"/>
<Position pos="0"/>
</WidgetTitle>
<Alpha alpha="1.0"/>
</Border>
<LCAttr vgap="0" hgap="0" compInterval="0"/>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.ui.container.WScaleLayout">
<WidgetName name="客戶"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<Margin top="0" left="0" bottom="0" right="0"/>
<Border>
<border style="0" color="-723724" borderRadius="0" type="0" borderStyle="0"/>
<WidgetTitle>
<O>
<![CDATA[新增標題]]></O>
<FRFont name="Dialog" style="0" size="72"/>
<Position pos="0"/>
</WidgetTitle>
<Alpha alpha="1.0"/>
</Border>
<LCAttr vgap="0" hgap="0" compInterval="0"/>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.ui.ComboBox">
<WidgetName name="客戶"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<Dictionary class="com.fr.data.impl.TableDataDictionary">
<FormulaDictAttr kiName="公司名稱" viName="公司名稱"/>
<TableDataDictAttr>
<TableData class="com.fr.data.impl.NameTableData">
<Name>
<![CDATA[ds2]]></Name>
</TableData>
</TableDataDictAttr>
</Dictionary>
<widgetValue>
<O>
<![CDATA[]]></O>
</widgetValue>
</InnerWidget>
<BoundsAttr x="640" y="0" width="157" height="21"/>
</Widget>
</InnerWidget>
<BoundsAttr x="640" y="0" width="157" height="50"/>
</Widget>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.ui.container.WScaleLayout">
<WidgetName name="地區"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<Margin top="0" left="0" bottom="0" right="0"/>
<Border>
<border style="0" color="-723724" borderRadius="0" type="0" borderStyle="0"/>
<WidgetTitle>
<O>
<![CDATA[新增標題]]></O>
<FRFont name="Dialog" style="0" size="72"/>
<Position pos="0"/>
</WidgetTitle>
<Alpha alpha="1.0"/>
</Border>
<LCAttr vgap="0" hgap="0" compInterval="0"/>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.ui.ComboBox">
<WidgetName name="地區"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<Dictionary class="com.fr.data.impl.DatabaseDictionary">
<FormulaDictAttr kiName="貨主地區" viName="貨主地區"/>
<DBDictAttr tableName="訂單" schemaName="" ki="-1" vi="-1" kiName="貨主地區" viName="貨主地區"/>
<Connection class="com.fr.data.impl.NameDatabaseConnection">
<DatabaseName>
<![CDATA[FRDemoTW]]></DatabaseName>
</Connection>
</Dictionary>
<widgetValue>
<O>
<![CDATA[]]></O>
</widgetValue>
</InnerWidget>
<BoundsAttr x="147" y="0" width="145" height="21"/>
</Widget>
</InnerWidget>
<BoundsAttr x="147" y="0" width="145" height="50"/>
</Widget>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.ui.container.WTitleLayout">
<WidgetName name="report0"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<Margin top="0" left="0" bottom="0" right="0"/>
<Border>
<border style="0" color="-723724" borderRadius="0" type="0" borderStyle="0"/>
<WidgetTitle>
<O>
<![CDATA[新建标题]]></O>
<FRFont name="SimSun" style="0" size="72"/>
<Position pos="0"/>
</WidgetTitle>
<Alpha alpha="1.0"/>
</Border>
<LCAttr vgap="0" hgap="0" compInterval="0"/>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.ui.ElementCaseEditor">
<WidgetName name="report0"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<Margin top="1" left="1" bottom="1" right="1"/>
<Border>
<border style="0" color="-723724" borderRadius="0" type="0" borderStyle="0"/>
<WidgetTitle>
<O>
<![CDATA[新建标题]]></O>
<FRFont name="SimSun" style="0" size="72"/>
<Position pos="0"/>
</WidgetTitle>
<Alpha alpha="1.0"/>
</Border>
<FormElementCase>
<ReportPageAttr>
<HR/>
<FR/>
<HC/>
<FC/>
</ReportPageAttr>
<ColumnPrivilegeControl/>
<RowPrivilegeControl/>
<RowHeight defaultValue="723900">
<![CDATA[723900,1485900,304800,1066800,1028700,723900,723900,723900,723900,723900,723900]]></RowHeight>
<ColumnWidth defaultValue="2743200">
<![CDATA[2743200,2743200,2743200,2743200,2743200,2743200,2743200,2743200,2743200,2743200,2743200]]></ColumnWidth>
<CellElementList>
<C c="0" r="0">
<PrivilegeControl/>
<Expand/>
</C>
<C c="0" r="1" cs="7" s="0">
<O>
<![CDATA[運貨商月訂單資訊]]></O>
<PrivilegeControl/>
<CellGUIAttr/>
<CellPageAttr/>
<Expand/>
</C>
<C c="0" r="2" s="1">
<PrivilegeControl/>
<Expand/>
</C>
<C c="1" r="2" s="1">
<PrivilegeControl/>
<Expand/>
</C>
<C c="2" r="2" s="1">
<PrivilegeControl/>
<Expand/>
</C>
<C c="3" r="2" s="1">
<PrivilegeControl/>
<Expand/>
</C>
<C c="4" r="2" s="1">
<PrivilegeControl/>
<Expand/>
</C>
<C c="5" r="2" s="1">
<PrivilegeControl/>
<Expand/>
</C>
<C c="6" r="2" s="1">
<PrivilegeControl/>
<Expand/>
</C>
<C c="0" r="3" s="2">
<O>
<![CDATA[訂單號]]></O>
<PrivilegeControl/>
<CellGUIAttr/>
<CellPageAttr/>
<Expand/>
</C>
<C c="1" r="3" s="2">
<O>
<![CDATA[客戶]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="2" r="3" s="2">
<O>
<![CDATA[訂購日期]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="3" r="3" s="2">
<O>
<![CDATA[貨主名稱]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="4" r="3" s="2">
<O>
<![CDATA[發貨日期]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="5" r="3" s="2">
<O>
<![CDATA[到貨日期]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="6" r="3" s="2">
<O>
<![CDATA[運貨商]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="0" r="4" s="3">
<O t="DSColumn">
<Attributes dsName="訂單" columnName="訂單ID"/>
<Condition class="com.fr.data.condition.ListCondition">
<JoinCondition join="0">
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[0]]></CNUMBER>
<CNAME>
<![CDATA[地區]]></CNAME>
<Compare op="0">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=if($地區 = "", nofilter, $地區)]]></Attributes>
</O>
</Compare>
</Condition>
</JoinCondition>
<JoinCondition join="0">
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[0]]></CNUMBER>
<CNAME>
<![CDATA[城市]]></CNAME>
<Compare op="0">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=if($城市 = "", nofilter, $城市)]]></Attributes>
</O>
</Compare>
</Condition>
</JoinCondition>
<JoinCondition join="0">
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[0]]></CNUMBER>
<CNAME>
<![CDATA[公司名稱]]></CNAME>
<Compare op="0">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=if($客戶 = "", nofilter, $客戶)]]></Attributes>
</O>
</Compare>
</Condition>
</JoinCondition>
</Condition>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Result>
<![CDATA[$$$]]></Result>
<Parameters/>
</O>
<PrivilegeControl/>
<CellGUIAttr/>
<CellPageAttr/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[&A4 % 2! = 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.BackgroundHighlightAction">
<Scope val="1"/>
<Background name="ColorBackground" color="-855310"/>
</HighlightAction>
</Highlight>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[条件属性2]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[&A5 % 20 = 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.PageHighlightAction">
<P i="1"/>
</HighlightAction>
</Highlight>
</HighlightList>
<Expand dir="0"/>
</C>
<C c="1" r="4" s="4">
<O t="DSColumn">
<Attributes dsName="訂單" columnName="客戶ID"/>
<Condition class="com.fr.data.condition.ListCondition"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Result>
<![CDATA[$$$]]></Result>
<Parameters/>
</O>
<PrivilegeControl/>
<CellGUIAttr/>
<CellPageAttr/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[条件属性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($客户) > 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.FRFontHighlightAction">
<FRFont name="SimSun" style="1" size="72" foreground="-16777088"/>
</HighlightAction>
</Highlight>
</HighlightList>
<Present class="com.fr.base.present.DictPresent">
<Dictionary class="com.fr.data.impl.DatabaseDictionary">
<FormulaDictAttr ki="0" vi="1"/>
<DBDictAttr tableName="客户" schemaName="" ki="0" vi="1" kiName="" viName=""/>
<Connection class="com.fr.data.impl.NameDatabaseConnection">
<DatabaseName>
<![CDATA[FRDemo]]></DatabaseName>
</Connection>
</Dictionary>
</Present>
<Expand dir="0"/>
</C>
<C c="2" r="4" s="4">
<O t="DSColumn">
<Attributes dsName="訂單" columnName="訂購日期"/>
<Condition class="com.fr.data.condition.ListCondition"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Result>
<![CDATA[$$$]]></Result>
<Parameters/>
</O>
<PrivilegeControl/>
<CellGUIAttr/>
<CellPageAttr/>
<Expand dir="0"/>
</C>
<C c="3" r="4" s="4">
<O t="DSColumn">
<Attributes dsName="訂單" columnName="貨主名稱"/>
<Condition class="com.fr.data.condition.ListCondition"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Result>
<![CDATA[$$$]]></Result>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand dir="0"/>
</C>
<C c="4" r="4" s="4">
<O t="DSColumn">
<Attributes dsName="訂單" columnName="發貨日期"/>
<Condition class="com.fr.data.condition.ListCondition"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Result>
<![CDATA[$$$]]></Result>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand dir="0"/>
</C>
<C c="5" r="4" s="4">
<O t="DSColumn">
<Attributes dsName="訂單" columnName="到貨日期"/>
<Condition class="com.fr.data.condition.ListCondition"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Result>
<![CDATA[$$$]]></Result>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand dir="0"/>
</C>
<C c="6" r="4" s="5">
<O t="DSColumn">
<Attributes dsName="訂單" columnName="運貨商"/>
<Condition class="com.fr.data.condition.ListCondition"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Result>
<![CDATA[$$$]]></Result>
<Parameters/>
</O>
<PrivilegeControl/>
<CellGUIAttr/>
<CellPageAttr/>
<Present class="com.fr.base.present.DictPresent">
<Dictionary class="com.fr.data.impl.DatabaseDictionary">
<FormulaDictAttr ki="0" vi="1"/>
<DBDictAttr tableName="运货商" schemaName="" ki="0" vi="1" kiName="" viName=""/>
<Connection class="com.fr.data.impl.NameDatabaseConnection">
<DatabaseName>
<![CDATA[FRDemo]]></DatabaseName>
</Connection>
</Dictionary>
</Present>
<Expand dir="0"/>
</C>
</CellElementList>
<ReportAttrSet>
<ReportSettings headerHeight="0" footerHeight="0">
<PaperSetting/>
<Background name="ColorBackground" color="-1"/>
</ReportSettings>
</ReportAttrSet>
</FormElementCase>
<StyleList>
<Style horizontal_alignment="2" imageLayout="1">
<FRFont name="微软雅黑" style="0" size="128" foreground="-16691295"/>
<Background name="ColorBackground" color="-855310"/>
<Border>
<Top style="5" color="-6908266"/>
<Bottom style="1" color="-1842205"/>
</Border>
</Style>
<Style imageLayout="1">
<FRFont name="微软雅黑" style="0" size="72"/>
<Background name="ColorBackground" color="-1"/>
<Border/>
</Style>
<Style horizontal_alignment="2" imageLayout="1">
<FRFont name="微软雅黑" style="0" size="88" foreground="-16691295"/>
<Background name="NullBackground"/>
<Border>
<Top style="1" color="-1"/>
<Bottom style="1" color="-4144960"/>
<Left style="1" color="-1"/>
<Right style="1" color="-2105377"/>
</Border>
</Style>
<Style horizontal_alignment="2" imageLayout="1">
<FRFont name="微软雅黑" style="0" size="72"/>
<Background name="ColorBackground" color="-1"/>
<Border>
<Top style="1" color="-2631721"/>
<Bottom style="1" color="-2631721"/>
<Right style="1" color="-2631721"/>
</Border>
</Style>
<Style horizontal_alignment="2" imageLayout="1">
<FRFont name="微软雅黑" style="0" size="72"/>
<Background name="ColorBackground" color="-1"/>
<Border>
<Top style="1" color="-2631721"/>
<Bottom style="1" color="-2631721"/>
<Left style="1" color="-2105377"/>
<Right style="1" color="-2631721"/>
</Border>
</Style>
<Style horizontal_alignment="2" imageLayout="1">
<FRFont name="微软雅黑" style="0" size="72"/>
<Background name="ColorBackground" color="-1"/>
<Border>
<Top style="1" color="-2631721"/>
<Bottom style="1" color="-2631721"/>
<Left style="1" color="-2105377"/>
</Border>
</Style>
</StyleList>
<heightRestrict heightrestrict="false"/>
<heightPercent heightpercent="0.75"/>
<IM>
<![CDATA[m<`VN;caaCaL&;V".aTbV#on@3h:;jJepffD/68+MUf-@8>:_T&Ksc"KS1VZ%T%pqVV72b5e
J8s!$OT1&u&2k"EHm5$m?ufKFgIj![0SbEfr(XCU*R-4mhFbkBe9KTdD;CBCE7c[GH,0]AsDq
UWb$\Uo;dA42Jq/TQ@JhkRVC6@"k0>CpO;O5a#dRV5FOEGg8\H%5@!b.[6PrM-#^)b+'.R:L
.9G%i'$Z!K"StA_;i0]AJi7q%?W_a/kLK=`m^R4HdI(L.?<Q`P*gh"`k16$6^"Y`PEH>>AB3M
*Db8]A`FlJYY<qOA.o'DCIOPqBJA?1g?XM4a/lQs+jBklAi.Z%)5de*:prV1"BI7i96ja"m'p
ELfV.WcL;=*5]Ae;*p[!S`GUmojg*'hM$fqrpGT/GgmsI:NmHkXVL7f+fCDU-a"]AL'4EM"!e*
Q^0B?<<k7l0Y;d*ZG!#2elsqF'C-gXlFV);rrT?X[GK]Aj3g-ah;?YMP^R`EdT7LJmm_p\t@3
ehQmAel=-]A`iHN%Gp*Y3jT$+WV,DO_5C^,LIcsL0]A_j.g=cd,-Q9eUgEW>nX(`Alkh\t(Q3[
r:U(N838AV\ls'53<?jH,CeEP!g85?[;,C;,QKWo6+N$rt1oJc-1\_5k7R,O!<k?mBLH:1-;
WrWP\2hq(?I7g0*.npUN%do<("m1K7OW]AKarY6>QLWJ_gKOg\jnK^"6U#-t\AC8]At2d36&Mr
$*n9goktfHpe?`id&F(,^N"ODmS+n?irC[('KFH$Uj"AeZmD.+[pq/!Dos2QZ*El%#W47\@Y
ct*$,9W=OSRMQ!1R4WMl:!T9O9gt:0JHTYh1'iW]AH0$)"*/==ADS^A_s=i^NI!j:*rH/GW!M
DB1<=$C8sI<]AVlH39tpBV@OPP[XU@g"`8,V%IaRM3Wqf*,aLmltji)u<2)?-.19O:b)aW5_i
H^bc'?*">rff_Fh+4e*S:,kH&g?>.X?aMZKL"2SMdT85Y)%@I7VgY*`ZJhM_E6U?1bj#fY>1
/2TEn>"*]AGbH"u.Q8?g`'ro;u*/FZ_;6D`lb-B__kZBl3QIU>pgt/tYOb*R;.<o1*tf*H73k
LgcOIGfQTZ`V$9lBlrX_c\0XAV+T=@iDpc@NVOrV-0e2g=<%tF5/n=XCXm/=lb>$K9FaH).3
$.i>s9RXZXb/?jgi?bSbCENi4uB'YP7QGmq&;K[55\J/8[stqF34mEkCsoRCZa4<?+Q$FPUr
u`oPbhDDC,aqbQW/Hf74a7M$pm-oH5#ip%WR`]Asb`O8!SUdsdi6Nd\X5qe_L+T/Ji]Ad*pQET
hpl^X8M;:QX>Snr:U#9DO1ppKP186rI1Eqs7j:J"@#A63/6.>qd.uIO8Yp>a-ReuXq4<*XTO
K1D4?L/4)RmLYD<'2EBG,^0cm%@e5mWdqt9=D3km@+$U4&]A_8B;<\Xd-b'<t@><;UXFmHWaZ
A%#1XDH1<7J@[2"W+GpOT*#4,9/L7gQfD!V(aAY@)of3*D_,"1Im(Xa1=_E+mBX>kD4N`;-H
03pMV9?S]A2)5IhilD"q`Y;,+%KXVGhZ#8"g0[/:?%?/M\JA^b(B*f'D8Dd2[;ir0(-<ce8I*
h-Ds4A58XrqQk#rgS`9G1Sfl<:9(?:,B<gea50MZ`QJ*#a`n&)9_:^e@2QjllWO9X0+:jcp^
`7c.1uC%WKCL3D2-LKH9Ge;PMI[Ys[SJ.0MRloMf.<+UoAo[)%*$l?4c=CZbLAIpH<q@1&sG
kS/CtE\Daoe-64Vs6Vf3E3eBX8ul-ao@Ou"XO)_soOMZ;CPEiT"sc&\V4E]AZmc)+`Cn]A$rs"
-=.:'W4Z.-K;E/afPY>)(BG,W0e@[uXIsUAeB5hZc/,#m$%OO..jp+U5%c@F_/6GZ(6tgJV#
9k#[r*\WbT.W7UAg5oLI=L\K5-`!JI%ZOY=/YGb<Tnr`Z&(LBpCXhOT+NtC\@gVMW+2f$p6C
&%dP04/^;[YQ+_/b:Gd03Bo*9k;#5*t'p&trJGOlh%m`c$73$M-2HA.[0N.(2ad+aqR!,R!^
l"sX]AgRfga'fnu6V0YS[RXdW3(Ws^5.pV(Y%M[A&l^o8I,oj<>_T(FS`slpDt+#hRF&@HSO5
'e4I$5NHC8?H[s<qf'MD5Fm^Z)S[;#H2d2/(Q!<S:kc]As/O-R[*F.J<=#l6UdI\!Km"6p#`F
PSPSoA8s%`1sJCt[>Xa4M'kn3IQ_ZqiXd)o&/V]A.18<qPU=h[P<;k%LD<Z-U!^u\:3-q/>ND
*EDF=70/m(hPX-(Xj+.2P98%5g25<Km9lq.81,G97P^ohkNVMXYnG2jQ<WJKmemDgn*4P*dN
oa8XXbl<`Lk^:qs$!&&#cB-`FuQoLs;er]A0n=2E3Y##AV(;ulABP,Y7JbOsQj9B0Y;T"U0&'
M;Ef,l#khV+pU,VfeN4gLp<Qp#[,7]ArgrmBPNiU@)V]AT=N7J*FQ%RP'0@QdWj[1fi!l7%K_m
Z+-jggo*,*S1ZkRGa]A0QIh^%(0WZbua,FTqpP86P'#WW"^cEJ'35JkJURVDg\uF]AH2/!u!".
Jo0'=8#VQ\;^8Rm3[c=T>=mEu4d23/?cSHhj/XO7Jh%?%'5f=3AO3GP0s=#84.rrH\Xkj?lf
#bOa+\lg6?+(0[BXp'RIS(u431C">)0"/fD!$G\c&ZQC%0iC23aNqK(!6/N\gTU<;hBaFUOH
h<"c<[5u<0AS;1n_adDg/NGkTh9EfI15c5@7]A<^?6c_Q_.N3p?'s%]AAQb^BSr6%08qB.JR`]A
bF%79_EWu5)GO.@gL2]Aa@K*RT!B5a2=mo=!sHOHZYiq5EKb=Z\=[@gkE(h*mbR_r.hiP^d%D
X_4bB+SY+GoGf/uFR`4<"h?dG+<";;gJ;<7M.=P"!l%F[PBf*%u>pq`(^e\<)8%\Nol$3j4B
A)@V&alYKaXJu+%jXL1$(1M;HiKCL>J`Y-]A3Z(6'f[gpSjuTg4jf-oiB-"BjbI/Xho,r`+$!
Gd4'JL@sjY4%!l^8Fp)/D@taK07+&#:;(-eRjuTMT`8bC,qD'.bQJDe!THeX*P54Mqjo!u-D
M[+Q;6J"qTm-P)PThd*t`JViQ%;L%5-f2G[U?t`pLQ5Z74WS5P_VdJiGX9dG2,.N;bX*^^4e
/^Ic@(UU#P363W=(q<Rn8.h%%?cVq!s=:SfdF^f_cQ,d!@.KPI%$luGn$slHDNE186neAk&i
Ws5E/A*38G"W'VV$i$mDHZ;97(Q6.fR&7A_`PF5=0eQ6FTH=R9FL$D$XjqtUENV3!Q^4[+r1
['j$L4aM@/2q\,+,=OqW.!eff4_G5B/0fLnZJ]A6cXp0i@+VQ$=fd.LFVj)*f#&^&5TI?nrAF
4dLEqg6DLQ,LD[]Ae/ucde*3HmLuNJLj(Pb_50*$Hu>T)&kA8VAgmLk=+2".PJ#\"1>:nnN'%
Vm@]A:RWJM,1JS.`3D>T^p>qQgV^Phh-5;f&6#S#EMZ;$[FS".?gZe0YM;I2bP$!P"2:I[K2?
AmB(VE4*V/%IPQGDfbtT1Of<e69NSdr+hK#78%YYZG_WGMa^LdgFeJV;=;rr?:W3L:A'OdSf
MVbdVE!d(Wdl@Q,^(EV<%",m5@Ni;O%J;FFfG[)g.e'A7cfeM)_P-dBZ`XF(P144@q9[+($^
?qT(>r6S[&n)l]A4BNoUbZ6Bdb!ai>Vlgouk)i$[QMgYPB2+Q%cKYP$em>'[X%)h(GAYM**;;
Lh7$H?531a%#:."/cGVOY_YE7nltRB^!fb"uX_D!E\+;N]AdcBNmG!S*V%6;4!MKfL&6\\l):
Ec^l;F'T4Z.lZHPSDT3^_Cga1'N#KC'$rtG1UcL)$@.du2oJe(88$nMd_k&df%4RqQUq/tDS
ZN3)oKoCFF;[aZf2X39'YW\2N'9]AfooQNTI]ABU&Q#U>I4Mg@sQB#?7Jkc'EJ[V%\q08XG]AZ9
,ueE)*>EGH"2^[N+P7jXhGqHb-1.bWG7ZB62:_q5Ct#5B]A2AZR_)11K=Uq_.B]Aku'KF4mV((
m&#U,c6XAKe5nubhn%U8GMSq&M%ig7mnA[OpUdf`\,Pk']A/;T^qH=]A#P]A[%_A9;_I2cgZ^dd
0CJQE<OhG32LC(eCqd[CAR[/;=!h.p+ci&5^QV:Kb+Kjq^0N[n(enfr8N0HTO?%J:kIZ5D@p
p+MjbJn5q#B[B.dYZ[kBfE\OsLps5bc$h#ZXFrpoplPn\Tfiof-Do_X"\;6CRMK&I\N8]A&NU
+bd9S4oJK#.Z)K!.F(8BjqSNnt%/N`$8Bg`gK)d^(?@Ljc\tEofN`V:(Z`dQWuC[#+KC01$T
)1\f.O)(@4jEjYBmCmN>]A]AHu8I6g&H&6-6gX;nWP,.==4Id&@=M2n#+\VMX^>)mb?Y7ERtAQ
>F":"XRXXG\C058eeE)?r<:tY,<\8G$N"0,MUuBY3SWTchoMI!^?@/dD,JreK"P!\kpB:O\a
cM=S5D]AG;@bB?gWYu\GDI/Jns4H:o8UE;m1s3;H>X?b\AnXZc<K7G[^b0+_g:9dmC89$;&8X
(,h&o_>tO)bP+NTYi!`HB#G9;;:fQ=*Ql'j'1AL?BFr<]Ag/iF/PPK[<m#SL3t1n8G(cRRcOW
/+e0RG+7/A[V5j=[[!M1[r[r@T$`R!>C?o&\fD/d+I,M6H.g<LWSb>o6/0h5"D?kYCRCr[7(
$9/pu-O*E*IW2X"'j!);gAs+7SmKL!8hi9[/=d*6V\\1^;$%VaH_cD&s8DmkVTpTR$F'sb'@
0]Ae]AS%DFK[12U[tqV<p'B+`2U.choR$Q'5H)np?T.+Cg$6qYA00!CI\If[G.Nm&C)jPh*Se%
HNqQo10:@UV=#bI.VSr,;g_g)L2`j-\YQNI40J`KlR7RgI-QOugN;:r!s8i2MD#'@cKQp$mo
!pRe?QP=?i4/QdB6Bt!mOW?m*JFP;n1.cnG!oi>4Ie:l]AE@Dkksdb>Ann:AFI?c1]Ai&D!C[6
2<!g-.MG`l6^Ca>-fpJZ>f<]AJ5LX$HuNO>onsJ%QbkRm)91Yo\941_O;"Sr>dM!s'YA\8>[(
[08K[F'Q'UAJXEm3@VnG!PZM`nP2fpki%PL^6(]Auqu??/78hKUF3C<1)g_(=aW*mEaBkJ_Sa
dtK<*)'_U]An="e`6sbiF*>)3i1.V/Q]A;tdtb[&Tg2C0^&TJE>cAHSN[^54X@E6'.Bbc"/;2?
[3#j?)US>UBO[(:Z[n\qRYu.Ehe\RNNWnUs,DcOV*@hp)<I-/X2Bs']Au`jef;'t)l/nbEeD-
uW^H5`jeMjAg62OXSnu_O\WHs-_-+hR@32m5rZ*Od"pf0>6$6)NB!C/%qLK$@&0gN52noGC(
`#aiUMQUMnK2S3s2]ASV4*5+rUUX["nhZ7#"KKN=kqtQ1B0s*p5uMSFB4-MV[:Cp1)d^!dO'M
]ARn8"E7F()3fTIWZU?^!)'_kRbU.Sp<Vb(F"Tf'.QbX4<i[U[:Y;-HXA3'$f4@RDaE;CoII&
2Y+(-7dL:ZcW:?U/NYc:I@t.\*Kr<kjYD=:Ed_u"bN2)h?-7nCN#/K\DgkJ"'ooml$>5"3mA
hii\fppEA!B&"g2TN+h6Ta`s(5+RJ!BtrM[6(sK1pe>/rZ5fJb3t71nY5u/q%r4HdGt[72Ia
B@'0^$48PT;-;C&I$d<\mPeBDt5>S@RXp*I4YdUN1\Fm%q&9^n)0$pRd6DX2B7k"(tA%3R-M
3^t(A7/LQ*JiDfpJmq'-RFrOXNTm'8njtCI,_OUN-X<I6L$/@+g-UQ,J9oY^L6hsbI>LJ6Ip
1j;9B@_bedGenhiBla\>8^%=4;&7CbjRVJMA=jcg(bQtD]A7NnCQ.[(H6qNu^>p#YiK"<'>j^
Nae.G]ApG(S"'CPp+(//aTRa>C[kXt_PaYJ*g?e`sb^#_Efps!=ToY8CW0Hu:I>IR5AKt8p]AP
+-GoRno^;$6qmdqGi%4\-+g</?9[c,s3?5]AeLGI7kc#1PPE<0:Ak'HCLgYA4RI]AR!(d<S!mV
4Fjm6#J+GaEQ:;8%/nY@6EgnDCo`,HW;h'Gp\)aYl/O^BO&eB>uZ^Q?Pb;`U3=Rr"M8+Q(9,
=]A3QR-ZIX*>>k=%GR9a3MMA#B"P-]A=OD1d+"kCtdG<%GiiWoPKdBb,7Ack*OR@8aT'(Q'OWT
^#FP;7Nj,K@J\7)0aoJP'&[q`''[_DBa9Wlks4@`&tWfW405`Vr"i1rK_XL0,R-4>^f'7d@X
%.NZeI18bX4ndoY!"/hoUP`lHW"!0CN1D9dlPWT%kYpn7:d)X]AC#*ILWCgE`C;0I:f5Le4@T
9UY[,($nUpTAJRnC7aZFNGo]Ao(75lnBVf&3E2-bf+`K)j(K_U&r"t#[jJd,39&MHZ?PXR]AE]A
3)/1n4p2nLN'Ct0uoCgtR95s:C!QG54.\eNTQrKHrGc/`3C=X_:Uqf0O)%\iMA,]A_DRpF</`
qhh\c>_W&0$ETonjt8;feAIF0m_"LoOg!_-Zi'QUu\4`j4BS*mu8=iSP75llu)`M.C@^[r.0
b/.Kf=%+Tn3F7@Knfc'U^mb8J$;atS@)0)698+ghf[7=CQ/&Q=fpY`<9.P")6=l1h]Ag9__a[
<[OYsdERA\0A^(^N/<'5ireDK2"%qTK=Pl$g.rLu1H(Y)W&s9]Ab;,aHUbPtbbpm83EH+V2S)
%h&qP".Vn8md[R[J^573h[.J!i)<<dVGOV!fpQhu5PhPlLA(?X[9F!3M]AZ9_i9EPliL?ol*(
f27mU&]AcHNp;F[5U0o#c>#70(p"l:+kZdG#W%#C%#P8dZk'/RFlL@i's_8:2q#,Or;@t^+]A*
c/$^VdbV!&mld$BAnU:j*r*8%-7;AT,":]AdQ"7S$+H/fZQ>SO`6.'#]A!-]AiKlU%`&?+]AS?oO
65[FqmHEfI".bMG%TidKg<KCV!/Ms@S6LasNeX\1f)YagnmOHomX\6ckqOCuQp.-6a67-Q$n
\@IF9^bP'*e@H)_;lk*2<FIh(bdTK/Tsb>!b0u-fdn(Dmhm[6KI&krL+S!1]ATM=bmT$nt?1S
3DuUpBmk.sC66Op^N+4?c@$#*k9u5Gf?CRL=l@1Znu_",rM?'+AaQF"-7&^(MoHi?%a-THPr
B'20+)?k9f\_6l#<#J0`nG?%StiXe\Z=<TuX<!jrdCO=@V"?'<6]AVQebgn@W]A)SEVLEpYui7
<1rMOH!dK</e;+c%E70q/+Q*S\maV8I%OjbGsb<E%O#<_iHTKlPNU]AlZ@^N^fh3Pcf]A83:dY
FbWZ5e^C=TZq0(tY:YRIm.Z@dil-BWkg0am8gpmq^_:5AOsZu1uVWC\+bpNUZmm;L&q5.#;`
=?qO,a1T#pdL&D3_jc&;:.2go9_kN;o=VmM>e&J&JHc]AE$s:q*r2sc1HTSd(CG9rHYU@rCbW
L/XY"VSc!>s0ti*qAABA^H<#i<58hU%HX8Xp5FIBmI:X9Sg5`YB-HD#Lm(I/Ml)YBnF6k$t@
i[]AUmt8!U[$1'^hr`1%O<IAAHNaEQRM:J+J[H3b%Y8`ZBK8HSZ)=0_DpH$n/eSpHf+gEftM0
UJAP'*31a3EWO=n3?ZZ"a*0;"qtX"m2(Op:(`)F!TPr[qA3r>@`9X@;;dU)e5;68pVoXK;L5
/:phbnu?!ND3k>irZ/p>9kgVqk=/d47=Z;r3P5G!<nhQ8W83`W?0;9O,:m?1OjU*mGbQGi12
+sFCUMp;=[6hDeH.VjYp/IN%1:N+luCAdX]AVR<-p+e1Ed$^^I1+`A@H]AB3U+7Ya3*449<35h
HFg3NmGZ08ku!Po=B3an'3RL)q;Pn%Snfc(4rYK=f5TR+i92Wfm',8i(2%+\!0@#b7[`!XIY
r$1+adbtQT?6OrAl@U)rWmcWknLfDD!%QGISqef$JJr>(Q/r,#]Ap%JEs]A*-D_KGc9G4ul8fK
RQ^k>#s/p:]AJ?fkROp8a=HO_W4D/ZR57MpC+S1NS`Z_8p-S+miK![mC(Z!J$9dpm0h20AZ?!
tE":`89?<8'@:6@BNEbR-&PRDZ"3clM"&8J)@Xo[E&X3:Vqjn?/g6?m7PrY`^/]A95I).d>NW
_[TlL:#(O[UFaG!S8U261W0mfp%2(/Y:Aa9ErNka,lQ;rSJSt%_4F=k=*t!/"fP@C=MGNkD9
Z,i#0UDW/F%DPq%EfKUV?iS#a^%\NF6e3Lo"qKJV8.Wcm@]AfArMnP?@D>NA8<s\JuN8DSp>'
/$*63@Br'(F!VYE;#*IsO>"=g<rc^i,qZ=4nb!(KJ=_fC_^oTgr.K8Fc;BP7@"T-;ZeBDRGQ
JJi,jseeg)-fA3CB4?BC8@'g3ZDq=[B3:l>i?WJfR2-/DtU9p=NfG?=$1lJbNV?g(\=E<DQB
p)ZDfk+]AiQ94WcB.ZEmLP"Qm_>uk$j_8CTC1gR%nI*YaB4m,n>hc+lm1G1sF)F#(CR+dM(t/
^<#KTN*#270+=EnL+=?ic<JqC"rPL,*ij0&*]AA=LEJuQg*qJ&BVk[#<%@@utq#(=rRCX'+1S
k!2f[Uh+q[GI*lr8oHf<\VAd?Z<t61F^U>(;i330N[DMbV&%53Jh]AW5amLlFB!CNVK[MM5+P
@<lA*eB6T)YABXf`P;jm,Q=,JaW_W(#7^JpMlnqg5F*EM<['c]A_SSh^d?g-Y+5,]A9>@bH12B
?aEk^g:J2hd.ShrSjgP6j9=RdW9BjY%\dk@r4.U22jAL`?/:O$9>VsT*`^o=QjSJBk**4.Nu
l/L)U26<7Z5@hc?Fg'n3n([%+V;N@.h5+X:g-*km*k#1Gp%,KR'[7,qkPI%@$8km8+pXMu9b
'Rm<+a'tMtVE8Gcc9V8#2WkF--$%rYC3Z'f_;/sr-e)kt'N7G!s1diE\qXQ%(rNS;)&,NUE(
]AL.-5jatkVSJD3I9P1C$?l">CP0DH6\WI%XTT#+igcAL>q<Rr(K(<Mu3/J12s'E/GNYocB#7
>h8uHp^0:TM:.=ClY3L0!gNlpL$0<_((aMqlLisn7$kNOg1k_Vf)SY'srsT4qY^@lI,aM&+`
dQK:ZpW`/=$57n(;G&$b3=&=D6.m2MgtB`27hmU*R]A@UhbP%*pqB-G&S3iIO4@-120g!/)#E
'jPn3WT_K85?fj=4Nl<Y.,Dc[2H;"jae`mD2_Z;UEbf(+VsMCoYrs.^rmDCNQ19]Ad?\[*/@h
p]A$M'OB/#&b^9,-O\LneZ>6PH5,K#Ykl'UjPW_.38YreI'3-^cp'>\<7!VShc3o0:50uiA\p
3F1\FTArI_*)Lds#`n^J7l!bbAp!G]AIm3PK.@)]AU-"-R[-Hm%RdiCFKhW4jp)]Aq?OZcoBTF,
,`k+R+Tnc"T;ts-p-Cfg6:J%WlL"PGcKL-a;?m7qa)"2-+5!%NunHX91F%$t*o?+CdB&:GAC
f7b[Q0g%CX(>_1K*3`m8u?^RIahS.[2#_DWgfEn#h2LVN3")M4)g5s\W=Puo()+)Wpc<*53*
f2pb[E[lcS+2M??ftFCJ.&2"bMop.9;(\i=P27JOC_*AkdGiq8("W`d2glEr)5+jF2tKleT)
,a?(;'F0+a5+%T1gp)UKTJ?&@d73u_b5/Tp2CO[?EI.$DBY8JBgI2&[<RIg1bNEsC2#P4q@s
_)3O^=1foFrAH6[6Q:b(:"/=0sR'n\fK8jB7O>4W`X/ie(]A<@irf31j:>S7@5pXmsZ&^E)5b
jp*3ViV$nPU[%Zbh5EudsZ0^Br"NLCkJhp[>O&L!1Wfl^QfAikk;Hs=p=$?Zs'`C-qaRD97(
=Wn)WT>ES"(u.Akl3qA#@mdI7pFRpg381+pf#RR1\SX:V>EEX/KPg+*LW/W(_&g,TK<'e;X1
\8iAJ*OW3$r`6:H,Wg=PZ7#6n$5J]AV\8[?0QiY?7Q=facI$5q@Ya'$?H6^2Kb9JsbCMi;26X
,_;C0CtWI_20n`UlLO;q#`Z)O5gY/G@;HVUl@F9R,U1Uc*B251,F',h3A>FW)D%WNp9ODljq
c,41Ei-sZP#$."tG9:[!KIUZig-N,T8W;_[*K:;M%XbT9mdceIXF>Bg(Y\:S^H8jB8G7JuT+
6/;\^FnANJ1)_$UNiEoCo8QDbKc`#sSn*&q!?H^nAIfh3-GlAa(?I<uk5G90u*BQ14Pd8',j
sLVPK#XqMc;`\'6QbQlIhWk("T7876a$--3Z=\ThJ>/#+AVb*OK##d:o&2#"o`4GqVbS"QQi
T^LtdU4[!SP\DG#:bbVh@Gj.I07(:Wj.\E5`Fcr!(UU/Jh1N^gV4JpN#kM+CVk;H.=)<Z20.
*%lF@NMcPbWkUo<EB^'cg*<ELYb"e]A!>hR"po3m*/8]Ai6/YCb=j!mgf^`saZ(\abDCFS@ThO
sk.G]Aee#CD,%@Z\BC_gFlUnn0l>@$dD1+CBh8@")!Qdoao8B"m4]A*6!57'4raGO`j<#^Q/a?
d;#QGm\TciRF&2f"\(Cc"Ju0n_=q9G4D)9C=$\`/d-A1p?g;#2;#[?u"8CYY5B7OBl#l>c[=
0&@T+Y]A<tj;"^ZEiH[54qk%JEpV[(#'t0#!>OKH1)"O)s0)3rlE#khW\Y`3)>N`lo34ETf"9
/p539fiR:#pd#[=57'kHLIE'ahmBMGf?4E%#([:OV7-mhqF7G#<[\P;]A.9fB#"4dAq9Lm]AoL
G%mOnasm?H:(cNcCdqbSC-2;RR9D?P&%%AZY$LSV2)c:/Tsc"sE^'4`r\O^>K@6?]AL!,4S8K
EM+#DuDWa9k_Z5,_(g's6M<imZH^MXTOs57\qK+jHtE[qDRA4"&76Lt]AS5loh`1q)WoaUCmh
5rVOWIWo"uJE_lkn+[*+sk/]A?To,bk'_K#519;%q\I)c9(n>G:+pPKKEPTg&GC(f/2.uW.=?
\Ei,cgq`CKr":hja)%:+1b/#I`gRXW_kOi1.'O\d&_:Lr)+43R2cJ8P>T<b\$"'iV:qW)dB7
@8Km1P.Em4P&a2f+jR4o*3';)g%n"?#4;Y?%5\48@!\5i5',kj[dJGfp]A]A.3U'eFI)tg=PU!
IR)nfQ9SG,.?kJg"o[Kso&KZJG,T/rh;%mgn$;pQrR5J@5KfCrqQT>b%:B)V~
]]></IM>
<ElementCaseMobileAttrProvider horizontal="1" vertical="0" zoom="true" refresh="false" isUseHTML="false" isMobileCanvasSize="false" appearRefresh="false" allowFullScreen="false"/>
</InnerWidget>
<BoundsAttr x="0" y="0" width="956" height="490"/>
</Widget>
<body class="com.fr.form.ui.ElementCaseEditor">
<WidgetName name="report0"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<Margin top="1" left="1" bottom="1" right="1"/>
<Border>
<border style="0" color="-723724" borderRadius="0" type="0" borderStyle="0"/>
<WidgetTitle>
<O>
<![CDATA[新建标题]]></O>
<FRFont name="SimSun" style="0" size="72"/>
<Position pos="0"/>
</WidgetTitle>
<Alpha alpha="1.0"/>
</Border>
<FormElementCase>
<ReportPageAttr>
<HR/>
<FR/>
<HC/>
<FC/>
</ReportPageAttr>
<ColumnPrivilegeControl/>
<RowPrivilegeControl/>
<RowHeight defaultValue="723900">
<![CDATA[723900,1485900,304800,1066800,1028700,723900,723900,723900,723900,723900,723900]]></RowHeight>
<ColumnWidth defaultValue="2743200">
<![CDATA[2743200,2743200,2743200,2743200,2743200,2743200,2743200,2743200,2743200,2743200,2743200]]></ColumnWidth>
<CellElementList>
<C c="0" r="0">
<PrivilegeControl/>
<Expand/>
</C>
<C c="0" r="1" cs="7" s="0">
<O>
<![CDATA[运货商月订单信息]]></O>
<PrivilegeControl/>
<CellGUIAttr/>
<CellPageAttr/>
<Expand/>
</C>
<C c="0" r="2" s="1">
<PrivilegeControl/>
<Expand/>
</C>
<C c="1" r="2" s="1">
<PrivilegeControl/>
<Expand/>
</C>
<C c="2" r="2" s="1">
<PrivilegeControl/>
<Expand/>
</C>
<C c="3" r="2" s="1">
<PrivilegeControl/>
<Expand/>
</C>
<C c="4" r="2" s="1">
<PrivilegeControl/>
<Expand/>
</C>
<C c="5" r="2" s="1">
<PrivilegeControl/>
<Expand/>
</C>
<C c="6" r="2" s="1">
<PrivilegeControl/>
<Expand/>
</C>
<C c="0" r="3" s="2">
<O>
<![CDATA[订单号]]></O>
<PrivilegeControl/>
<CellGUIAttr/>
<CellPageAttr/>
<Expand/>
</C>
<C c="1" r="3" s="2">
<O>
<![CDATA[客户]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="2" r="3" s="2">
<O>
<![CDATA[订购日期]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="3" r="3" s="2">
<O>
<![CDATA[货主名称]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="4" r="3" s="2">
<O>
<![CDATA[发货日期]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="5" r="3" s="2">
<O>
<![CDATA[到货日期]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="6" r="3" s="2">
<O>
<![CDATA[运货商]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="0" r="4" s="3">
<O t="DSColumn">
<Attributes dsName="订单" columnName="订单ID"/>
<Condition class="com.fr.data.condition.ListCondition">
<JoinCondition join="0">
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[1]]></CNUMBER>
<CNAME>
<![CDATA[地区]]></CNAME>
<Compare op="0">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=if($地区 = "", nofilter, $地区)]]></Attributes>
</O>
</Compare>
</Condition>
</JoinCondition>
<JoinCondition join="0">
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[2]]></CNUMBER>
<CNAME>
<![CDATA[城市]]></CNAME>
<Compare op="0">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=if($城市 = "", nofilter, $城市)]]></Attributes>
</O>
</Compare>
</Condition>
</JoinCondition>
<JoinCondition join="0">
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[5]]></CNUMBER>
<CNAME>
<![CDATA[公司名称]]></CNAME>
<Compare op="0">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=if($客户 = "", nofilter, $客户)]]></Attributes>
</O>
</Compare>
</Condition>
</JoinCondition>
</Condition>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Result>
<![CDATA[$$$]]></Result>
<Parameters/>
</O>
<PrivilegeControl/>
<CellGUIAttr/>
<CellPageAttr/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[&A4 % 2! = 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.BackgroundHighlightAction">
<Scope val="1"/>
<Background name="ColorBackground" color="-855310"/>
</HighlightAction>
</Highlight>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[条件属性2]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[&A5 % 20 = 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.PageHighlightAction">
<P i="1"/>
</HighlightAction>
</Highlight>
</HighlightList>
<Expand dir="0"/>
</C>
<C c="1" r="4" s="4">
<O t="DSColumn">
<Attributes dsName="订单" columnName="客户ID"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<CellGUIAttr/>
<CellPageAttr/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[条件属性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($客户) > 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.FRFontHighlightAction">
<FRFont name="SimSun" style="1" size="72" foreground="-16777088"/>
</HighlightAction>
</Highlight>
</HighlightList>
<Present class="com.fr.base.present.DictPresent">
<Dictionary class="com.fr.data.impl.DatabaseDictionary">
<FormulaDictAttr ki="0" vi="1"/>
<DBDictAttr tableName="客户" schemaName="" ki="0" vi="1" kiName="" viName=""/>
<Connection class="com.fr.data.impl.NameDatabaseConnection">
<DatabaseName>
<![CDATA[FRDemo]]></DatabaseName>
</Connection>
</Dictionary>
</Present>
<Expand dir="0"/>
</C>
<C c="2" r="4" s="4">
<O t="DSColumn">
<Attributes dsName="订单" columnName="订购日期"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<CellGUIAttr/>
<CellPageAttr/>
<Expand dir="0"/>
</C>
<C c="3" r="4" s="4">
<O t="DSColumn">
<Attributes dsName="订单" columnName="货主名称"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand dir="0"/>
</C>
<C c="4" r="4" s="4">
<O t="DSColumn">
<Attributes dsName="订单" columnName="发货日期"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand dir="0"/>
</C>
<C c="5" r="4" s="4">
<O t="DSColumn">
<Attributes dsName="订单" columnName="到货日期"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand dir="0"/>
</C>
<C c="6" r="4" s="5">
<O t="DSColumn">
<Attributes dsName="订单" columnName="运货商"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<CellGUIAttr/>
<CellPageAttr/>
<Present class="com.fr.base.present.DictPresent">
<Dictionary class="com.fr.data.impl.DatabaseDictionary">
<FormulaDictAttr ki="0" vi="1"/>
<DBDictAttr tableName="运货商" schemaName="" ki="0" vi="1" kiName="" viName=""/>
<Connection class="com.fr.data.impl.NameDatabaseConnection">
<DatabaseName>
<![CDATA[FRDemo]]></DatabaseName>
</Connection>
</Dictionary>
</Present>
<Expand dir="0"/>
</C>
</CellElementList>
<ReportAttrSet>
<ReportSettings headerHeight="0" footerHeight="0">
<PaperSetting/>
<Background name="ColorBackground" color="-1"/>
</ReportSettings>
</ReportAttrSet>
</FormElementCase>
<StyleList>
<Style horizontal_alignment="2" imageLayout="1">
<FRFont name="微软雅黑" style="0" size="128" foreground="-16691295"/>
<Background name="ColorBackground" color="-855310"/>
<Border>
<Top style="5" color="-6908266"/>
<Bottom style="1" color="-1842205"/>
</Border>
</Style>
<Style imageLayout="1">
<FRFont name="微软雅黑" style="0" size="72"/>
<Background name="ColorBackground" color="-1"/>
<Border/>
</Style>
<Style horizontal_alignment="2" imageLayout="1">
<FRFont name="微软雅黑" style="0" size="88" foreground="-16691295"/>
<Background name="NullBackground"/>
<Border>
<Top style="1" color="-1"/>
<Bottom style="1" color="-4144960"/>
<Left style="1" color="-1"/>
<Right style="1" color="-2105377"/>
</Border>
</Style>
<Style horizontal_alignment="2" imageLayout="1">
<FRFont name="微软雅黑" style="0" size="72"/>
<Background name="ColorBackground" color="-1"/>
<Border>
<Top style="1" color="-2631721"/>
<Bottom style="1" color="-2631721"/>
<Right style="1" color="-2631721"/>
</Border>
</Style>
<Style horizontal_alignment="2" imageLayout="1">
<FRFont name="微软雅黑" style="0" size="72"/>
<Background name="ColorBackground" color="-1"/>
<Border>
<Top style="1" color="-2631721"/>
<Bottom style="1" color="-2631721"/>
<Left style="1" color="-2105377"/>
<Right style="1" color="-2631721"/>
</Border>
</Style>
<Style horizontal_alignment="2" imageLayout="1">
<FRFont name="微软雅黑" style="0" size="72"/>
<Background name="ColorBackground" color="-1"/>
<Border>
<Top style="1" color="-2631721"/>
<Bottom style="1" color="-2631721"/>
<Left style="1" color="-2105377"/>
</Border>
</Style>
</StyleList>
<heightRestrict heightrestrict="false"/>
<heightPercent heightpercent="0.75"/>
<IM>
<![CDATA[m9=j<P?5?9"W\rDAXn[tKk-&]Ag,gj._$Z@DN#`Od(;%daKs4NR;acH.KI"pa?JA\H7-u9mKk
Le#[R/-&YU*s[Jd2!BO@0^([[;^bP%[mZOQ:kA_Ka8eIG1UNrc+icnXT3!h`:.NJ+)rTh\6"
\[5dNqhlcdWO,qW0?+?6YnF9Y5oC5tZqTUd7AliU#@3;+4bH@0dIk*XZ)b"?DV<*3@pRU5:K
]AS\lhf%E!p[>kHrNhMYLS!API.Ut=cF%:%S3-Yd8_+pNh!'.hn_Wp:#Gc"mE_T?h3aR9(o\0
gYZW9eu=0"AFUE^KRb2_E)%V:s#*#$kE<,+XKe`jM]A<8HEY\1Mb"^WC0d0h(4n;\Q.VON[f/
343QXa1P(#"$Upn.YP/\'88Wl`BG]Aj1GOG[n-)jSEujr'(?=`_on\l1JaYAQn'Y(R:4aRW#L
kmb/8N.[BQ-1DMAh(.>.4?hEqu8@qVJj@e]Aj3c^d.Cl+E7"1c,Hd!_o++PZs%HG-V>am)2R\
E).-?VJ$_%EO"*)'IIW2f0H;UB?Tg.#8sp8CF3C1YYKKRM"Ek4KSiYh>2-nnoh'hC89R_)Mh
aek)HolJq-(sEhbXBbGrbdtYH9\NGl4-t[TiXDE8@3heENKH#7WEG1Zeu7kgG9F<"2'g31V%
d<p$7WE[p$-Vk:+6Kak11sl'V1<QoC>f9"fsgSqsonOha",RkP"DA(%]A=eJ"k6L*MV%"kBdu
A>=abY,MHgNE@`:[+R`bqJ+G;2BYJIT*j)i?P3Kf'fSrd.T&,5i:o&$`W7F/`f5(&o>RdFRF
P:-XfC;(jG55RPkl7`9!.AG#*cuaT+&PMiU:97Fp)+OE6+EgSDe\Eajl]A-9.*Pj!OWN$i/Z^
6"X!R!5mirm3%":F>SIrKpJ#]A\\N_3anI>?DcGZi#/kJ:'`iPkW)`Bd.*J)^=\YS]A&MKb%B:
Q<b>g;eMcm0PKQJ^hE&SaIp]AQeqJ1f["K&bq.fB]A/^ur1Aint)Q;=?0"jtes.d0rb)-&R^%>
CW5T;\s(/o'6lN3kE[su#GE$D1#5OJF2G=2RJ)6-<i[?#5F"pTaM'&YZK"uYPiQ3:5Gr;`eO
atcqaaD4[FDTXgV3dfs,E--5/44*>Fmu>`U'R'ap;#;s^PaEYe^oSE;0aHdXCjU(PaW/Y6I!
C#Y7u[h.M=:H4G4g*^>iF!=;GDi%l$ateFCY&$3KY,139TAb1rgAH"mT+=B=eC%C'ML_'Ap'
MZ)hPTps5l.N'CYHH*cf?Ls!58R!@-lk.SYC5\C_#o[U<$P\:GTGW"o_iV-+e+4KTM>`?Q4R
SOIK2=_X');Ha\JR'-$A>E9$VIfe?=d_AlkEuN:LI$=5h!"H)S:/g,MX)g::Mnifk$FSBIH4
<#(g[7C,#u1_rXJ;d*Ut?="OsEu]AK$,HE=p_"&sosN!.8nXe#^O:n+XNSICJO\Wg;=d6Z?@Q
#fo,P-"9?4K:#Bk7.69.V00+2_+oQiP'Uq]An<#_=]AuIC(AD;Iq1C*-=mIuM1mC]Ah*)nb=@ih
a.HF#om)U#dF0?AU5<Q+3*l90>2A'O3eb4t"WgGXc`1G@XuVH/)+u93KV-K07JA1#`b__Se`
&c.Q17V=u[d-Y?-L_J46\Z6YGk+KuR#9)4dRhjurY^Qup@9@m9Cflm9@L7oLL;BK3dV&fgJ0
.4Fd$!U3nX^2k^^V[eT#^t7=%jd]A89W!62W2"EHbIH`)Als1+'PKPOf/LTb<\Xs^Vnj"o^Ua
8XEi*\p!_U),FJEUJ]AJcBQ@`2Ol1c24Hk"$W"XLr<:T!m&cOhstVmI4(2D*8cX6Q"hj:o,3(
)UH/mbAI2@Z=*j`H/.1K*,_8>Uk_U.LIocU<F%bo(R*3p,r=d^oMP*#*;CK\eDn8W!)Y=(>q
6-!A_O8VeoMF!*X8>Ac,)C3d3^Nhalk_f[[ZfNeidUCX4_%`%r5+XJg2A5jM[tn2t2Z]A$<p(
\X[su^CV5sqdAUBA?FoY_i>e((K]AD9)=C)^h+m2g&\5]AEMqlW(H:"GCc8j6nO5ZDoM*$hrFc
<eA^Gp%tWqEnutpX@/=1+V8MFM,qZ1W)eA#\'^cKhZ1Cq4m$5iGl&`9P6J`KI1DVY(>0"FG2
4N*+EtUO_XfiXb>pHJo7XIdg&.=1sQ,sqo2^$SQq6&fmBo(`90sJD2Z&F%`-7PiN`W"0.U:n
VJBFh&'N?[,fRI="u6L'/a=CD3MTM[+*ONe*aGT>p,nOB[=.Hnk<EA6B&?S8/n956%_pc@$m
X3@7lLGTN'Q!34Kh/R*rR2?a?sq2bR<Lf7G(!42u9M4G_RL)m9$1W>`G%VJ4Yi$qP^u^<@_!
@8\@&BOF7OaUGA9Js-.!f?*:?O&76[h=V;F#UF2+NM6[W/`"f"I2&G&E+E.h_=*Y(cK4kPRW
)#Ud:\:;4?D;@DT2&@<L38^*-e,WZZD1>a1NA`+gNs"^*]AkH'/SU7D7dNO?5M`'j,d!LnO@U
A3m0K@D,O#cPFTi&)B[5M)0);h(C4gG,/q9&nlTkS8+mZb[Qo:HS)c#J@q<@s`G72UV2@t9)
rjI@WbP:SU6<)F45<B$S6<UeF@qU)8]AY"!=HTESfh.NtWgq3TOo>qMP00&%,"c%r\6Y%)h8,
mV9?HK8(lSnUONUf2^Ha7OeFKA($%Es[?pX,^Zm?B<[Lhbc/hD`QBHGh#"p3K,[HH3,4(AW(
N+-/V-`&QI6VXTa8;W"SY+\BOcBgEE@N6ih/IZDsR/YqGnbt2R'kQe1O%mHm(+$Mlc9m1E]A;
3LUS<VUNer'9.jN\2,6>E@"r^iRR=U[WC&f_B,W#kfc:6u^?)*p+MINZ5qF]APMGQ4?;Xen(-
f1lP*2L`07NK$rhhuBP=Lle&S?o"'[G1fM]AfMWHSd3O<i`n(0N7,FBo;R)biHFpq_<S;L6Fr
X,e@KW)tp@W)qQ&m,I#<kOhNN?]ASJFl'I4GN$t>bBcT6787WHG!A:eMI>u26<iq1"=7@QC=m
\.GiOjo02I!`NHpp%<hlLb:B6l&1Vo?dd>!.T9disjNN68!h,,on:.tp@=!n\GP1bWQXl<;F
:PS4)%2hm6LmFJoa%U=9Z.=!TmU'j'r)]A=S.B:Am*46oKCT.2E3+$9F$NA`turJMWVUA2/PC
tpp97_?&3S)eYSKf4kKXRgBeQ=ZfNSIS!HS@Z@$,b`_V^lX3m@Y:rXO@X]AiD`VHhR>Q%>g)J
R#(-_Ks*pTD,<D/<lT2%oEhDgZcZ<6Xk_2?`#X#j?-j`?X+Jhe#YG@N7j=&tt\8]ArW!l$os@
LU31(e$;ZkTsu=RpXhMp1FpLHNSoZ\[]AB4R9+QDVRjq,J[^XrF3M]ASQh6d?R]A8!T>Vk[!6P#
%3(k/TUqDlk4"+^&^<D-)rmV?9A$UZ)=t9>*Jj0&e'MFSTLn,Q^*'TD<2O5J+@7M='0aMk]Aa
%]AZG8;nMN=na^<<4#JXt7[q@*bER+`A/0rr%VlRkF/U<4KWrb::p^V7h.b%k;klep06Bc5L<
:8?4W;^C5]A1DQS1Z^[bf"!kH^!ZR<J^I9gfN0l5l:OA?'4F:+'i11'-IL?/S(=Kk\*DG[425
!gg#kJ6Dp1j=9=hb-^<G[o(,GP(r.p2k"urdh_4?p`5Qr:6QFcplP2rl&?C"@O7X?JLpWf`d
ItD;3LqqqL]AmlI8_$6JaCWO9eV/<p%W`,L2!`D$+Znh+'(0.f/=rqmC9@4\&O(%'ta0Ud?Oe
chl<tX7K`OB-gaoin)5uYi6K/ZunF&G'iO>^m%)\S'6[V+HW)\L0]A!-[RicQ:Hi(orIWnV,`
3Y"-ZfCoiG#,<6_[bNcs11IHjd%!e$hJMbYUa"QioNf;/7*9>Z6I>\Fa/jeHJOWnGS7,u+.P
*OU/d/j.,Z+`[`pEVZZdMgBCCqM5O-mTp9pm#fj]AhZoJ,RQ<Ta2ts^KIOFA%@oC\PDYnW;Bd
+_*bouW@IhtPLSI/'b%m_,SNs_6ThRc<8/s.,b7`_-nRu,ETjcg,o.g9*n%<+K^&-g@T4S,D
QbLc1r0hP6eb59K*TVr'H#Xp-fh!30YM_R%pM+D:DcN"cHSnarc2]A<8D<GXi'KUGumYiu*>"
UA"5=5oRcX;ID(qs_M^-BL`.+rrM?Xi!g"8QiOD$OP)bq-4Ag`SG`K-#%S^\_0nqCX%;N6Vb
&[ImSAgJlZUKRl%6k]ACa&BXHu&YqD</jJb[EFL:NHBI:(bTY35/'2M(Q3I"J'H?+S^6CtWpj
cScUB3XtjnB=[\!kUd<IC")+njoBsD$8(VrqC"\dUJhYWBYfA[DKj[oVV7)T0&>0kj,_aQbu
!Nrh4b%jkdbum5B4E4HE\a?F')QQ0I8enQ`KV3:onEoupg#a%<06WSh/"6-$f)<r)A1g,3R5
GiUCCp\#&`=qOa%e2CBpE2Ln=G"-_j*#b[WX%RWinSn6fRB0p><bo*h!mBNCRjnY<__Pkg'\
O*j_)T"Amg-t=L`Vgp+F#NfO!ZQXi,`'!PC48Q75[A6FFV=f>2[`H;[(H_Zc9@Oq5$nj1-kV
1mg_^"$:_*Dc6`%`f4ej?H)#aYn+of!Gqb8T*4^Q?I!`sj9`h@u2"2l*@f(8G[,+\/E$$<K4
+Z*"8\K/n==m?"6?VS7J\ZGEX5lNQhWUVHe8a1@ge5:@dhp6cR/4E]A``Ju<iT'nJ;('t%^HM
;*9Zoign3fG48>5]AB&f@10+g,mLC2&NJlW=`Lh9`<01aT+S(ThF4X%2d(Z=8B:a[Vu#el"u^
FEs=CE29.71.S6!8VcB^5_YA5IY,_5[MPC1jq$!41M`lXX!H(7;Yg0QX,P;!rZdt_!#ToX>R
'gto)g.n$*65Y%A@^^KA,F-Eg]A2pi-LH/>,*aXkCm`\7$`(4<o"2/&T,!`)S[Oi\OYq#\$T'
"167#ld]AQ1I'5/8k4BaX=dW7`oJ*MEN(jRR8BN2!s<pa7\8*LH$&L@SI;3s921@j^Dd5bq39
4Di1di0<MQ1pK"/u%pXgo;rKQ8iVDqHtDG*a'c(ZU@J=+=bb"\Ei[2Cb36[`'ZYm>]A:YDplF
DujcFOh(.AZG:JgpK#)O<nr^BSohouHW2`\FSB@Pms2;BC/j24QUcKOQ@RKDlGbS%$Y*&MgF
`/Uj=oumaA-<Sj9Hb5W:WAV<p-ej'.4\Auq79YCJ_[",s>L(-KR&O=2nHd^mW&3)9G]A&SPh:
cUb^F%1h"-KK0C:5U6J5kc,&J1/u@&UDFH\/1,QW:WWG@-,^q'fC@*U]A-70-eYrFC3;MWV<]A
dA,iL%dPfqQW[(Nl.IFgFQ3bmkMf!%`TaGl\bKi4e.2<>VZ-j6$V]A)'9=#O']A'k5;UL1WfJ=
ca,C4#r5IN&WOY&05nYVmcOUq"Z&eE&OQgWK?eMmC%8;;5WHU7\,m053$f_o]Ar%m7<7(+'d%
*1QQ%M%OY2!`*,#C(Nc9iO38NVu2eM[:/*2b4K5mCuMQ=1n*mcsc>OuNtMHCJ-!d@jJ5b!(6
VAYZ.QDkD8lZ[9U%QiI*UF##3>\f6S;$^p7j)Tg7Uhe@I$0I0!1W4T[2pM9:dDW-T)HD"12"
)I53RQkc@1&SjRulj5U>C7#=L=2.Kk[qUSdQGgO`9&k9/B#Zb>]A8*!=E-`\m8:8#5t`qT%'W
uJD2iYRFI@Ve>XgoP-MJAM7*c=r,H'0A:JAUIWol'Z8@^$'r=a1r#G>/71IFuDNLR*>7C:kN
i=<8C6>]AHGL7ln,O<F+Od`^l<ATH7-.5/^Hs\$U<>=63+[o&E%%oKl0%[5W<mO.G<Cts9Bi*
Ib$2CF0/5+L'1OI#E$g3FnaH"pUfYacC5okTbglDge0p*Q+:Ve:=Mb0!pY_j/B!Z98]Afa$MC
X8'LM?I^nWF9&GBfC,naN;fFQcQ<[,&l_M>k/rU3eh*p@&YV3Anb9u:midbbHmQop;s'Q-/4
SN30l*hGY!]AeScDlK2`<IDU-d%\oGNF<6_,Y7;-;-SLnG7O"-"%]AT\L4U_[f"Ei@MmBF4Ws1
Jq$%H"YbAt]AWqH.lW;"AW'g#TSp6MKGk`Y5egHdnI*7CWe9'=_/EkUTE0$]AW'UTkqjES,"a8
"(\'PTiO*E"O%5-S/iQiA$k+>1B:0Br1":!q!-OY:QA"hePi$*FI2U[usbScVEZ-lkl"-d2n
T$"4T>5<7\KQ5!@sNkSj4G,/;Sp1KWkh/@5;=oF_0`3ldc4/,7S`meU*!0"GsncQmIeJn,Q?
O612DRbOrf@k[.YMq'%H%NLe>0X>LLg"nXRB^ncg5\9.WG4]AC1H1R=+Q<)Gur"i;K=d:"!jJ
V:1$;s+Y\F1`>M:eOs*P5X;IT`>TAs3N_?oDuQp1?]Ajqau8!1#U3+rgMSh&UjA_?'O?o2Hd[
MAp^_-f1-dl41+2+%V]ASG\rA/1-Vh(\=,9FepOoMQoYW:(Qn/bXN.-A->#Uj\Yr!f&4P(DHZ
dmr<>gPd-iS)Vp`28BF^"&Ys35K`#$).Lg>.m5,c^"jaMnB$'#:^4`=,fIn`POGSON`E$og)
9j\V7@>.:kHVED0/7O8B+8]A(-8g_dX5cT/MgtG^C.]AXonR;$E,kuj(s9f]AgXE^e2OK4>3X9Q
*^U[T;#I`YH*:D%C<3P=Z=.$$UE$#/ma&W;=D#7K_6Vle"rH!%#k%=pRE`c.MI"[AZE@'EHr
=VI$V61>]A&i_k]Ald9Y#Na:O4J$VLi@YUTD"S(p#7KpH[Zrr.^;7PUV1hh?dC)G0bjoX=)67J
jcYbb:O$`8irr)Q3+"c9oT$?3hC8:hLNpTiMHu\lBl-.9;c+'P.Ka:oOV./#'r*tB%:RMB%p
Y;^i@Q7&O!tcP<#fSN.#PbR%I^VCl>[mm.*aR7ogE3[^qWNB%;:n4cl0eH*i7Nr2T$6a;-k#
tKWe-i(b%WXJqEZU[ZJ"Q]Ae6^pT!2Pg(S!>N(qH,B4p1'gHj5*D57JO2p&?6.7@FU!?@`.^E
4[e@:q-_/j?Oc69D!uN^+!5@&l/C:8=:e%9r__dfIn^&18L@p#+B2f-qJ('Kg:4m8/`QYB2F
:Z<&q5$'rCOQRMOt;e?GLW,#\;/_r+/nV%:9&)--*P#-8(&*R2M$KQCk?hL>m#G!O?[t%@T9
qK)%M4(@%WX^1h3rR`3i^[&1LW#"0lhK(07tHs$_M"<ko0r7PUm&59_C,.;rsfN03jI:[&gQ
K,4GAO;bfan,>]AO5lE'&Qf"#0JS?:7[9MFf"V)G\j7\LO<EhCKJY+2oCK;rNo@%\NCoq*9(t
$@&589`_6e3KL@PjB]A'n5,brFq@jB)J9EdZ@GJ^FZ$%0/`(qoAQKg3jfJm$]ACT6tD_Hh+kh:
1qc3aZ-='1CQlO&^#&+8,jV9WhZqo'2#q/\Q%)C"9mc94R+*3c@SLa02T)/hK6C30m$l_l4s
)kBBqn%jRDNZkX@40::/o=hXXP6AZ$bc9R9%eImWHl%$ZtFmUZQ\1LY1@,4d2Yn%p=\e$cD8
n&i!<>Z4EUlW,-J&JNkt61*BhHV9-o4+sB^j(CZW3IQst!'hE"LNdR5(kXS8P`q(>Fl+>=0K
Ato_Y'$XE(`E9R?M"nuXVt`Yef%(k/!e]AWd$gsWPNQ6LU_Sat2^1_^)>U53Y<q.V`WR5e:SE
4-UJ%]AC`;4XM7Xjm5[$4q(ksO.RorV+kO3m9!W+<3)QCG--We;Y?hN(8'$lW1b0:p!#KM8B#
0W[M9^gkb6(j5MW:&?ZN?ON4@>'bc?e_>S--H)ef$n/"EPJmHc'g]A/M7iM\T9'ddmdP%;-R$
NYbi\:Q?F;#G$>$>'i890@8VkG7ZH#X&ISWM5XWh^:(UD_A\f%VD`:5Gi&]AsI_1^KaPMoY$Z
"h5W%*Ca#$]A-@ro,(J>?64T6!t2p4#l^BOfRJt_7XRC;@ZGfU5+4]An:p_d;kG4/&+`?;o5'T
uf8M8!ecC,QY_5&7<"%gqN:dG5(0<`)+BrB<u5pl'<g?k3V.*-)FZlhHkQ0FXp-:J9i8kA&>
sbMg4?5KS`VN)(erq69"01K\aCK$?_=Dcc?On1Do2Hn=)UaN;SKP.=VCa`&"E:6V!A3.JVT"
D"f*46rb#/+s,-6,AY(3r5'7J4<s>Co]Ae?pGi]A4M5$g2o'2.@6HQYtNm<=t&-CZ)sI0P#!\G
?eS.;toFIErjRIWa<CiNVjL,%uH/*EHACWOK@+"^Nj?Sahg>aU>7n#$`uA\7pE3'p.h(S]A/4
P!Y),r"K7WKRD@al%tiP\42e-kQrobIroF*)OXgADnG"Kb%67aBDT>a!mluF'-19m+5JKqiD
Z~
]]></IM>
<ReportFitAttr fitStateInPC="0" fitFont="false"/>
<ElementCaseMobileAttrProvider horizontal="1" vertical="0" zoom="true" refresh="false" isUseHTML="false" isMobileCanvasSize="false" appearRefresh="false" allowFullScreen="false"/>
</body>
</InnerWidget>
<BoundsAttr x="0" y="50" width="956" height="490"/>
</Widget>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.ui.Label">
<WidgetName name="label0"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<widgetValue>
<O>
<![CDATA[地區：]]></O>
</widgetValue>
<LabelAttr textalign="4" autoline="true"/>
<FRFont name="SimSun" style="0" size="72"/>
<border style="0" color="-723724"/>
</InnerWidget>
<BoundsAttr x="0" y="0" width="147" height="50"/>
</Widget>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.ui.container.WScaleLayout">
<WidgetName name="城市"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<Margin top="0" left="0" bottom="0" right="0"/>
<Border>
<border style="0" color="-723724" borderRadius="0" type="0" borderStyle="0"/>
<WidgetTitle>
<O>
<![CDATA[新建标题]]></O>
<FRFont name="SimSun" style="0" size="72"/>
<Position pos="0"/>
</WidgetTitle>
<Alpha alpha="1.0"/>
</Border>
<LCAttr vgap="0" hgap="0" compInterval="0"/>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.ui.ComboBox">
<WidgetName name="城市"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<Dictionary class="com.fr.data.impl.TableDataDictionary">
<FormulaDictAttr kiName="城市" viName="城市city"/>
<TableDataDictAttr>
<TableData class="com.fr.data.impl.NameTableData">
<Name>
<![CDATA[ds1]]></Name>
</TableData>
</TableDataDictAttr>
</Dictionary>
<widgetValue>
<O>
<![CDATA[]]></O>
</widgetValue>
</InnerWidget>
<BoundsAttr x="394" y="0" width="141" height="21"/>
</Widget>
</InnerWidget>
<BoundsAttr x="394" y="0" width="141" height="50"/>
</Widget>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.ui.Label">
<WidgetName name="label2"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<widgetValue>
<O>
<![CDATA[客戶：]]></O>
</widgetValue>
<LabelAttr textalign="4" autoline="true"/>
<FRFont name="SimSun" style="0" size="72"/>
<border style="0" color="-723724"/>
</InnerWidget>
<BoundsAttr x="535" y="0" width="105" height="50"/>
</Widget>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.ui.Label">
<WidgetName name="label1"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<widgetValue>
<O>
<![CDATA[城市：]]></O>
</widgetValue>
<LabelAttr textalign="4" autoline="true"/>
<FRFont name="SimSun" style="0" size="72"/>
<border style="0" color="-723724"/>
</InnerWidget>
<BoundsAttr x="292" y="0" width="102" height="50"/>
</Widget>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.ui.Label">
<WidgetName name="label4"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<widgetValue/>
<LabelAttr verticalcenter="true" textalign="0" autoline="true"/>
<FRFont name="SimSun" style="0" size="72"/>
<border style="0" color="-723724"/>
</InnerWidget>
<BoundsAttr x="797" y="0" width="159" height="50"/>
</Widget>
<Sorted sorted="false"/>
<MobileWidgetList>
<Widget widgetName="label0"/>
<Widget widgetName="地區"/>
<Widget widgetName="label1"/>
<Widget widgetName="城市"/>
<Widget widgetName="label2"/>
<Widget widgetName="客戶"/>
<Widget widgetName="label4"/>
<Widget widgetName="report0"/>
</MobileWidgetList>
<WidgetZoomAttr compState="0"/>
<AppRelayout appRelayout="true"/>
<Size width="956" height="540"/>
<ResolutionScalingAttr percent="1.0"/>
<BodyLayoutType type="0"/>
</Center>
</Layout>
<DesignerVersion DesignerVersion="KAA"/>
<PreviewType PreviewType="0"/>
<TemplateIdAttMark class="com.fr.base.iofile.attr.TemplateIdAttrMark">
<TemplateIdAttMark TemplateId="9ef46a48-6fc0-4d0f-b6b0-d97967e23023"/>
</TemplateIdAttMark>
</Form>
