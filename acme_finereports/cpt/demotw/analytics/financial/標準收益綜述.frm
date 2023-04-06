<?xml version="1.0" encoding="UTF-8"?>
<Form xmlVersion="20170720" releaseVersion="10.0.0">
<TableDataMap>
<TableData name="ds1" class="com.fr.data.impl.DBTableData">
<Parameters/>
<Attributes maxMemRowCount="-1"/>
<Connection class="com.fr.data.impl.NameDatabaseConnection">
<DatabaseName>
<![CDATA[FRDemoTW]]></DatabaseName>
</Connection>
<Query>
<![CDATA[SELECT * FROM `get`]]></Query>
<PageQuery>
<![CDATA[]]></PageQuery>
</TableData>
<TableData name="ds2" class="com.fr.data.impl.DBTableData">
<Parameters>
<Parameter>
<Attributes name="type"/>
<O>
<![CDATA[純收入]]></O>
</Parameter>
</Parameters>
<Attributes maxMemRowCount="-1"/>
<Connection class="com.fr.data.impl.NameDatabaseConnection">
<DatabaseName>
<![CDATA[FRDemoTW]]></DatabaseName>
</Connection>
<Query>
<![CDATA[select type,ROUND((金額/純收入)*100,2) as 百分比 from
(SELECT type,sum(sum) as 金額 FROM `get`
where type='${type}' 
AND country='China' and year1='2004' and cate='現實' group by type) a,
(select sum(sum) as 純收入 from `get` where type='純收入' and year1='2004'
AND cate='現實'  and country='China') b]]></Query>
<PageQuery>
<![CDATA[]]></PageQuery>
</TableData>
<TableData name="ds3" class="com.fr.data.impl.DBTableData">
<Parameters>
<Parameter>
<Attributes name="type"/>
<O>
<![CDATA[純收入]]></O>
</Parameter>
</Parameters>
<Attributes maxMemRowCount="-1"/>
<Connection class="com.fr.data.impl.NameDatabaseConnection">
<DatabaseName>
<![CDATA[FRDemoTW]]></DatabaseName>
</Connection>
<Query>
<![CDATA[SELECT * FROM `get`
where type='${type}'
AND country='China'and cate='現實']]></Query>
<PageQuery>
<![CDATA[]]></PageQuery>
</TableData>
<TableData name="ds4" class="com.fr.data.impl.DBTableData">
<Parameters>
<Parameter>
<Attributes name="type"/>
<O>
<![CDATA[純收入]]></O>
</Parameter>
</Parameters>
<Attributes maxMemRowCount="-1"/>
<Connection class="com.fr.data.impl.NameDatabaseConnection">
<DatabaseName>
<![CDATA[FRDemoTW]]></DatabaseName>
</Connection>
<Query>
<![CDATA[SELECT * FROM `get`
where type='${type}'
AND country='China' and cate='目標']]></Query>
<PageQuery>
<![CDATA[]]></PageQuery>
</TableData>
</TableDataMap>
<ReportFitAttr fitStateInPC="0" fitFont="false"/>
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
<Margin top="1" left="1" bottom="1" right="1"/>
<Border>
<border style="0" color="-723724" borderRadius="0" type="0" borderStyle="0"/>
<WidgetTitle>
<O>
<![CDATA[新建标题]]></O>
<FRFont name="SimSun" style="0" size="72"/>
<Position pos="0"/>
</WidgetTitle>
<Background name="ColorBackground" color="-526085"/>
<Alpha alpha="1.0"/>
</Border>
<Background name="ColorBackground" color="-526085"/>
<LCAttr vgap="0" hgap="0" compInterval="5"/>
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
<Margin top="0" left="0" bottom="0" right="0"/>
<Border>
<border style="0" color="-723724" borderRadius="0" type="0" borderStyle="0"/>
<WidgetTitle>
<O>
<![CDATA[新建标题]]></O>
<FRFont name="SimSun" style="0" size="72"/>
<Position pos="0"/>
</WidgetTitle>
<Background name="ColorBackground" color="-1"/>
<Alpha alpha="1.0"/>
</Border>
<Background name="ColorBackground" color="-1"/>
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
<![CDATA[1333500,1409700,1368000,723900,723900,723900,723900,723900,723900,723900,723900]]></RowHeight>
<ColumnWidth defaultValue="2743200">
<![CDATA[5295900,3200400,2438400,2057400,1028700,2743200,2743200,2743200,2743200,2743200,2743200]]></ColumnWidth>
<CellElementList>
<C c="0" r="0" cs="5" s="0">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[="  "+"標準收益綜述"]]></Attributes>
</O>
<PrivilegeControl/>
<CellGUIAttr/>
<CellPageAttr/>
<Expand/>
</C>
<C c="0" r="1" s="1">
<O>
<![CDATA[ABC公司（單位 千$）]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="1" r="1" s="2">
<O>
<![CDATA[2012年]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="2" r="1" s="2">
<O>
<![CDATA[2014年]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="3" r="1" cs="2" s="3">
<O>
<![CDATA[變化率]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="0" r="2" s="4">
<O t="DSColumn">
<Attributes dsName="ds1" columnName="type"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<NameJavaScriptGroup>
<NameJavaScript name="动态参数1">
<JavaScript class="com.fr.js.ParameterJavaScript">
<Parameters>
<Parameter>
<Attributes name="type"/>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=$$$]]></Attributes>
</O>
</Parameter>
</Parameters>
</JavaScript>
</NameJavaScript>
</NameJavaScriptGroup>
<CellGUIAttr/>
<CellPageAttr/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[条件属性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[row() % 2 != 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.BackgroundHighlightAction">
<Scope val="1"/>
<Background name="ColorBackground" color="-1049860"/>
</HighlightAction>
</Highlight>
</HighlightList>
<Expand dir="0"/>
</C>
<C c="1" r="2" s="5">
<O t="DSColumn">
<Attributes dsName="ds1" columnName="sum"/>
<Condition class="com.fr.data.condition.ListCondition">
<JoinCondition join="0">
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[2]]></CNUMBER>
<CNAME>
<![CDATA[type]]></CNAME>
<Compare op="0">
<ColumnRow column="0" row="2"/>
</Compare>
</Condition>
</JoinCondition>
<JoinCondition join="0">
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[1]]></CNUMBER>
<CNAME>
<![CDATA[year1]]></CNAME>
<Compare op="0">
<O>
<![CDATA[2004]]></O>
</Compare>
</Condition>
</JoinCondition>
<JoinCondition join="0">
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[3]]></CNUMBER>
<CNAME>
<![CDATA[country]]></CNAME>
<Compare op="0">
<O>
<![CDATA[China]]></O>
</Compare>
</Condition>
</JoinCondition>
<JoinCondition join="0">
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[0]]></CNUMBER>
<CNAME>
<![CDATA[season]]></CNAME>
<Compare op="0">
<O>
<![CDATA[Q1]]></O>
</Compare>
</Condition>
</JoinCondition>
<JoinCondition join="0">
<Condition class="com.fr.data.condition.CommonCondition">
<CNAME>
<![CDATA[cate]]></CNAME>
<Compare op="0">
<O>
<![CDATA[現實]]></O>
</Compare>
</Condition>
</JoinCondition>
</Condition>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.SummaryGrouper">
<FN>
<![CDATA[com.fr.data.util.function.SumFunction]]></FN>
</RG>
<Result>
<![CDATA[$$$]]></Result>
<Parameters/>
</O>
<PrivilegeControl/>
<CellGUIAttr/>
<CellPageAttr/>
<Expand/>
</C>
<C c="2" r="2" s="5">
<O t="DSColumn">
<Attributes dsName="ds1" columnName="sum"/>
<Condition class="com.fr.data.condition.ListCondition">
<JoinCondition join="0">
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[2]]></CNUMBER>
<CNAME>
<![CDATA[type]]></CNAME>
<Compare op="0">
<ColumnRow column="0" row="2"/>
</Compare>
</Condition>
</JoinCondition>
<JoinCondition join="0">
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[1]]></CNUMBER>
<CNAME>
<![CDATA[year1]]></CNAME>
<Compare op="0">
<O>
<![CDATA[2005]]></O>
</Compare>
</Condition>
</JoinCondition>
<JoinCondition join="0">
<Condition class="com.fr.data.condition.CommonCondition">
<CNAME>
<![CDATA[cate]]></CNAME>
<Compare op="0">
<O>
<![CDATA[現實]]></O>
</Compare>
</Condition>
</JoinCondition>
<JoinCondition join="0">
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[0]]></CNUMBER>
<CNAME>
<![CDATA[country]]></CNAME>
<Compare op="0">
<O>
<![CDATA[China]]></O>
</Compare>
</Condition>
</JoinCondition>
<JoinCondition join="0">
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[0]]></CNUMBER>
<CNAME>
<![CDATA[season]]></CNAME>
<Compare op="0">
<O>
<![CDATA[Q1]]></O>
</Compare>
</Condition>
</JoinCondition>
</Condition>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.SummaryGrouper">
<FN>
<![CDATA[com.fr.data.util.function.SumFunction]]></FN>
</RG>
<Result>
<![CDATA[$$$]]></Result>
<Parameters/>
</O>
<PrivilegeControl/>
<CellGUIAttr/>
<CellPageAttr/>
<Expand leftParentDefault="false" left="A3"/>
</C>
<C c="3" r="2" s="6">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=(C3 - B3) / B3]]></Attributes>
</O>
<PrivilegeControl/>
<CellGUIAttr/>
<CellPageAttr/>
<Expand leftParentDefault="false" left="A3"/>
</C>
<C c="4" r="2" s="7">
<PrivilegeControl/>
<NameJavaScriptGroup>
<NameJavaScript name="当前表单对象2">
<JavaScript class="com.fr.form.main.FormHyperlink">
<JavaScript class="com.fr.form.main.FormHyperlink">
<Parameters>
<Parameter>
<Attributes name="type"/>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=A3]]></Attributes>
</O>
</Parameter>
</Parameters>
<TargetFrame>
<![CDATA[_blank]]></TargetFrame>
<Features/>
<realateName realateValue="chart0" animateType="none"/>
<linkType type="0"/>
</JavaScript>
</JavaScript>
</NameJavaScript>
<NameJavaScript name="当前表单对象3">
<JavaScript class="com.fr.form.main.FormHyperlink">
<JavaScript class="com.fr.form.main.FormHyperlink">
<Parameters>
<Parameter>
<Attributes name="type"/>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=A3]]></Attributes>
</O>
</Parameter>
</Parameters>
<TargetFrame>
<![CDATA[_blank]]></TargetFrame>
<Features/>
<realateName realateValue="chart1" animateType="none"/>
<linkType type="0"/>
</JavaScript>
</JavaScript>
</NameJavaScript>
</NameJavaScriptGroup>
<CellGUIAttr/>
<CellPageAttr/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[条件属性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[D3 >= 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.ValueHighlightAction">
<O>
<![CDATA[↑]]></O>
</HighlightAction>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.FRFontHighlightAction">
<FRFont name="Microsoft YaHei" style="1" size="144" foreground="-8994464"/>
</HighlightAction>
</Highlight>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[条件属性2]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[D3 < 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.ValueHighlightAction">
<O>
<![CDATA[↓]]></O>
</HighlightAction>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.FRFontHighlightAction">
<FRFont name="Microsoft YaHei" style="1" size="144" foreground="-23707"/>
</HighlightAction>
</Highlight>
</HighlightList>
<Expand/>
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
<FRFont name="微软雅黑" style="0" size="80" foreground="-12961222"/>
<Background name="ColorBackground" color="-1"/>
<Border/>
</Style>
<Style horizontal_alignment="2" imageLayout="1" paddingLeft="13">
<FRFont name="微软雅黑" style="0" size="80" foreground="-1"/>
<Background name="ColorBackground" color="-13722160"/>
<Border>
<Top style="1" color="-855310"/>
<Bottom style="1" color="-855310"/>
<Left style="1" color="-855310"/>
<Right style="1" color="-855310"/>
</Border>
</Style>
<Style horizontal_alignment="2" imageLayout="1">
<FRFont name="微软雅黑" style="0" size="80" foreground="-1"/>
<Background name="ColorBackground" color="-13722160"/>
<Border>
<Top style="1" color="-855310"/>
<Bottom style="1" color="-855310"/>
<Left style="1" color="-855310"/>
<Right style="1" color="-855310"/>
</Border>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="微软雅黑" style="0" size="80" foreground="-1"/>
<Background name="ColorBackground" color="-13722160"/>
<Border>
<Top style="1" color="-855310"/>
<Bottom style="1" color="-855310"/>
<Left style="1" color="-855310"/>
<Right style="1" color="-855310"/>
</Border>
</Style>
<Style horizontal_alignment="2" imageLayout="1" paddingLeft="13">
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[$#,##0;($#,##0)]]></Format>
<FRFont name="微软雅黑" style="0" size="72" foreground="-16741173" underline="1"/>
<Background name="ColorBackground" color="-1"/>
<Border>
<Top style="1" color="-855310"/>
<Bottom style="1" color="-855310"/>
<Left style="1" color="-855310"/>
<Right style="1" color="-855310"/>
</Border>
</Style>
<Style horizontal_alignment="2" imageLayout="1">
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[$#,##0;($#,##0)]]></Format>
<FRFont name="微软雅黑" style="0" size="72" foreground="-10066330"/>
<Background name="ColorBackground" color="-1"/>
<Border>
<Top style="1" color="-855310"/>
<Bottom style="1" color="-855310"/>
<Left style="1" color="-855310"/>
<Right style="1" color="-855310"/>
</Border>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#0.0%]]></Format>
<FRFont name="微软雅黑" style="0" size="72" foreground="-10066330"/>
<Background name="ColorBackground" color="-1"/>
<Border>
<Top style="1" color="-855310"/>
<Bottom style="1" color="-855310"/>
<Left style="1" color="-855310"/>
<Right style="1" color="-855310"/>
</Border>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#0.0%]]></Format>
<FRFont name="微软雅黑" style="0" size="72" foreground="-4492536"/>
<Background name="ColorBackground" color="-1"/>
<Border>
<Top style="1" color="-855310"/>
<Bottom style="1" color="-855310"/>
<Left style="1" color="-855310"/>
<Right style="1" color="-855310"/>
</Border>
</Style>
</StyleList>
<heightRestrict heightrestrict="false"/>
<heightPercent heightpercent="0.75"/>
<IM>
<![CDATA[m(<R*;q]A_dXJ5k5MM`W)![7`&Jom*W+sK?=77E<4dZ&dA5c@PT+=a&4HZ&tB8cT0KLaYeI$%
s'Z&OI+]A:dQ9JaVSQlF6Ci-I,@$C^YJ]AMn+6%)@@s'rp0,5=eo.\(c]A1&!@D]AcHCr`DIS+o_
(S@Yq=dh^$%9g;0bj5KukKIj=]A[)r3@l)>=4+mEA"Jt>[0<R+`7:HdD^s!YA?cm+=Z1;T8BB
B,1NbS_q]A`6Do[OuaDt6]A4.flg[<0En#k^:&lXA?ZHNMq^lBNp(,c"!*_:DK5RE(EcP'r`3c
!.RVoIU_P"E6iA:md=hEmpFa7O74#F\PXtub-<`sb_$CVhO2&d&'qDG`B06UC]Ai<0'+#iPoe
)eYD#Q5-E/IRoX5Kb\b4lI\8^CAL\DZ/+k0b]A2lq0!>q72ET]AbS.f+4dQ%57o09D:JXPliC_
/nr(/(M/:JZ4uPp&?3f*?tqWZ/s%htL&eU'Qi*$RHXO1`\c8rTaRX+'G2XOKG/K5FG$X(c`n
)#,?kR0O`i2!Ua4oHkIfeXZrtu+Pb2b%.m:RbIAL(-0]A7]Ag$mXmK+SJSg39EHU%H702lo=AE
aE4u=RLrs1%Y!/1WC&.4VYB>K>G?UmUA*)d:.D9[7YYCK)!Ugdk!]Ank%:28X,(_?M[%k]A\\d
5YWBk_Xfnkhb$fQ//H`25A6[kZR'9`iel77U$S8$]ApCsojVpPCj!%A5bL2<B:;Gr4Pr"M?r9
=2mN9hon:/MS)E,W0l"^.ci7&n)InPjXmY;/JS'or>b0Aoh,8)\T0e<^.Je-Am?LdK:qg\BL
u;/II+Zt7%qX2m9VKZ7tpiQCA#f'Gf40Z[/84`#,`kN<neC":Bhk8:Zbudn1<;W&BogZqpc-
=O!s*s-$5m<3)r.Qd_-G4fhhNQBIPGR>cpp4K\gQj]AS._V?n'7rLsUbNX+sFp$s5l79Z]Ae.k
p>K#e>d<6/%IQ+mPI$DQE!9:rHXj5*uW=$n_C$;I6KNH3&V\AI/1eMk$pMGVf=B,[K9GO,%t
3KNVP==V^3S6n\bcnIX[pHEq[5Hq%<&^d057KV[uu7d&#Z!h>Y*Nncu';)NGZ"$Os(KOM+T>
[Zp@uCog_&>qqf/]A`r2qYWY_aM<h/Ve*Goiaj8[sFn9CX8[nP3f/+TKdF3K'j[*OeE_**t3(
(8aM<<'3k`D^^\NI=J8Q!/hpH>EhY!'UZ=5oHB9l7<?okEuF@A"N@oc[QX[%lk6pJHu10nul
/\%U6+R/lj,N3!0"cp2Rl-%Y<kSIFXD[\el;^"WVGd/GPc[]AC"hB4L^^@Lo9P<#btc)62/sR
tl"8WLrX\%k(/!@fbeSo7X[DU]A]AB>rVD^/Q&+Shd8l5+RHr@l^'ZLlr!i.b\XtPCq!\+Udeh
iIqg69!=$?Y:UZ3m7C2,3egA[4be]AFW&/-`6_2)AJXR,ehF5p)rT#@a.:*1K6'qnIY#q6g-G
`Vn,&:_bWLGkeA(,kFW9RprdNBY0enC<J0Rb-IeV;]A)k3@J7BrV>?_M*-r23Ln5/*GZGJ7k>
uF$k@W\\Z`(&NTo3Vp?Oc3V>r5&Dh9mEI5kMJ.0>ADB.&$qlEu5/m.V+JuMJ#YQ(m6W?EF-O
s[d@Q&'OYaRBblX5Z00I<h6I<f-L\>h*/$=7<mM$dI5Am7)4M'_#)3rY18aYXM4#N+%#]AjjL
='ckbZ[?1IL,3E!r\Qji5d=6*H6n\8=l$*ea)lJY4ABBe29=n-QV1)cnE^=Q4Z;D`ki`hX,&
^,*uX"=lPC3!>/^?-7,=.?EcG8[gppE=BoX1eCq4alBb3cG]A$`QR*Bn1sl3a(['65qp8h_B"
6.t^r6`5nham="5FuG+1%MP?A?ds]A(7=0tURHI=LH+WF4?NFn!19RRSpcojo\kU^#eXo1UWZ
qOW&K5^5!WGc`>E18?2=me;O'dhU\X9K#?$:j$"cj+WNJ&p-YX"Funu7e\jYk=d)Zdbn6@ba
;EmW[a=_@IHUV(O5-e8!j=QnI,SZ2Dur_*Pe=%\]A^B!T[IP[gF@nb((j"K\G.?#ZokdAUQ@W
MARs.E`jSJ3fOMlB_0WA+uueCCPh'^YC$rl)\(X6,"cG7X\A4GfeqP'>n5kL.@T2qNtG]ATj3
\IhqJWB>'JKT]AdaRnE8s;e.dj4k;cgrW^os&;\mqcVFF5Q4"1+)>=DCcUa`[;aWdKuLAl0c^
7fWnm7+N=l8uG$:oX`:11HWBZm[I^-+shsLiQN/T?1euN2WAg[ha3N)(s+=FD-iCc6a)5"X%
UKn7$n9^VY`Pq^bVes;GOQ?A$2;kkIK6@nDT2@r1eRPfe"XZB!+d0Cf4<K?GN$f.gE!$EA83
C1aX(oE1J*d\\C)-B.6sUlK)`!ZabHiJ#NP;`TSn/d.n3*)Id<\XRcpj",U_0qH8X4B#kt)P
jufiWaD[\Qi/r]Ae.oiN5F3[lY'Kbm1;NiHKG:o>RTY#cciq!p28t?eGe6E6.soF.?)V>i;O0
P:_)H[_F<QcP'ka4=!p'Yg/a7haE&AeSo?GM)3/P:c$>E'*_]A3H6N[Ce@`jmT:H4:/3L<3/S
i-!*/Cq0srD7,o*)=_Dn2mAeRRN9<SOo2YGg66QhMCBP#?#5=2,A-$l-FpX`4fd"VOj0Dcdt
NlrA\nd=FMCE&&)p>N4*d@d9DAY`aJ;#[cU8ctTi=G]Ai"&iK8t6>8'"S^t?WX19A@l)_EVUm
+S@%ABR6W<"Mg"qB5,T^65is\R;2RXsD'Sk<F=R4UdsSD;n*n:Q-N2@_FN\pFS4d>0(VWS6L
TQ$DcAYX^BZn+($2`F%,B5U1>Z93RERg;K3u(EKF8Aif-4BJ*LL\8F)07WOkEfc9$YR:rE]AN
dgjWT_nd?*#ndIC!g4$9eYC%lZPpJl+(rPCG?>kp/:.R_W)+,^L0*)I7`4EGq,E%nsQ2V]AB*
Zq!tB^?'a*f0BGri*r9H)Z75c,,AM@H&83a@3#s'V\R+Bn$^E)"gNQ3d45f;j\SBbGD,CD<q
@+$aeq;JV-&"tN'**,`+!?#Yfg\?Q>$rWmTb(N#LL3V'9>bKSZaK_VG(O#\=e@7je6hr6"66
Ibu?0KTsls_dPFhPUY0,*VE<luG#+N@^j]A-;R)^tBK3[uU/Zoi"]A8+F)]AF)4LgsfK5h(Is;<
8X4&btT;387L:%7F"lq\%NB/>MePh<IXUfkX%`+]Ab#OIDLj2haCsoqr2M,@6[cGm>1\V;'$G
9]AkfW<QM[RC!aKL>Aq`TVU>`?&63`0RM)M(RMqiOK^8l_'u-p%$0N,VWp7#NTP=0&dq/r)+M
Eg<Wr)[a*lV1I?Kp$UU[PF!d)d!ut91^IEj4fs$(eS8cuEKc6-^?Ke0*&:mG?EhLb&(g%i%L
<uUh3JKCZu8X<\(7>5X@a'S,qumK4:j`Zc9,1WopHL8Y<$-G[(FDS/p]AOSo@%Nu4rp"ZgYk=
F>_ItH;W.[Dg.?0T+_AL,OL:kbW4:j9n>#JS]A"u`J(O)m*$r4G'!Z(UAd(Ec9;B5!7Zt7^`>
PlW_s2nXUF^W)GMPC!]A[iP+a()\nVh0c3u9VK+D*&ZG31f#V=<FmL`@J=oS)?JqqdIph/18<
"t@R=aUBP2)=#:^g16j%J8aeI.Vd&]As32V;iLAKP,UOH":F2/VnXlq[*$3Vs,P`Ej`%Hbgl-
oCd7AesNsV?`]AI_iBFK6PZ':tU70$!=##:1G3RJB1/,NsI?OYf\>REXPc^E5;7!<TH?8QSVV
An6[F)hrZG`fkE(]AT]AJ]A<sE_mRM3]Ahc;I>dftE.^u"T$RQU=3ZG:c#:f/27m5ZKg^"ba:<Rg
P^#/(4%@OA@$!=5*WNkBT&ZeMMJc)+35P+.-\5ud>PI^_pY"@RI:D+YkC9Nddi2p+H/IVm]AG
2.94X:rEj6AM<d)kKSKW>0PNlls6+(3^-328[*jFf+.rim,Tfa7J)*Vqt3CBIta'OQ0fEC<s
BM<$C/sF1chg`4M?"FqhG]AF5Z$3du!MRd)r2IS-J>64ra0m-VQa&agN+)gKH8=_uj!]A22Wnc
U93pE/L)@hVSejI/=S30:D'u+IO:TGZ,@/hp[is\(N3->M'-Iod"+k)A=dU!l#PQj#`60\dG
_i`=6Dc39n\P(<B=&klfb+=fjqJH@qR93rp_CYjish1-C:4[!J@"$,.WkCrDCZ(=*>fQe1ge
g7+`[nU.A(D=W5q9CInqodg$"RrILs8:Y>N^FMD4kK3Phq'mbm=\>94QIKtQKgqRLcj/FA`[
SrH;k;b9p%]AUj;7,NB<[G=FG-?XDo-?.(df(-6P<b-,RWUb_$+;TUj,K07%b@GW4]Aj))*lHO
#-KO\=GQt:gl]AC\!uH@*22/,n-=l%L$Dj2)76TSbekF7/(`jJ:fp(Bs1lEb[ft()`hBSmbdV
7Gj(m.$1LpfJGu3KX77h(q-GM[R2JfNj-<A/g>0UWb#OAKQ^I7[1;+m'fAAVC&Z>p\#o0GPb
.i9,&.&5bnCL;P-R,ZkfsG(;=^bqW9=tRaO[eBmK\$FD)"9J+,+%oNuuF<Fg"ZPDWMC&2G\7
@et.W-e1sc;;BrtCN>HiQ`I\iZoK#aI6HFK`2rcC4,3.DFZr0%ZS97.L+tf<(464`1i-SUV\
Jj*I8#+<f99*HWc^Tab5nV"B]ADM9oj;4X$I*^3!i$[[KSLmrUn^V)5ee6,=,3\E+hD-fK`PH
fHr=5!G-4YqY9-/B;5qUn676j;a?I_,oo1j<kY/afE/QD<4+:^SRW*Sc>%?Z)LQbu!OQ#]A>n
gceci?ZG:rgeOhjlcLbEe=Gb`6aTAT3Q7e=df+lY"\e+'pfLK,^ddu#Kl`.L^*UI'JfY2o#8
/NV%`;ds'o2^E@9qMuHq$Ro()'pWn=!4`FO<K>,GuqNGU]AIJjCXo9.=]AuQPBMXVk`pk_<rN1
[PN>j6I?U[Td.?j<(+0e7SbuFjl["r"akr6;fqQZdb-&RPU*_<LZtp'a=]A*iI\tV!sXEZIN0
-T98`B^',BBJHI1!f8g^^JAD-ffqeaJ>flNI/88'!M=&#=lF-k3[BI=d9$Ke)?pB3_n;1Hr+
!A6f]AV%EoSL/kK9(uho]A^em#Mt\GPRb00V]AQun8+hp..cACFa!8_qfCe'>>Mn]A8/9`dI9met
I$8SYTB<=7+h$9ap4K&baqhlZFXYCXH+J[D74hVooJY]AT\VUt&?5;PE<;Mn8Ic'UmOq?#^r0
I80?U9#'.mrU:;2jDd);4!:6c%BQU"Aa1r`"q&BlD$nhgKQnAVe-Lb)s6FqV*#p5[GTJ__FJ
I+OOo3#5Dj5!A,@!`"Hi;*G[n\1Jn+K):u8"dqXAk+5(]Ab%!nBt,;a!VAqtR#k,e@hRipQ1C
0gB&ZdMETeM::7"?17V!L(JR1@Ro-36eSu+_H5ooH-jE)E/8+6'>SF=(ai,%Dq@L?/R=uc=a
Dp72RiH.sk/21MsoSfF)9<iK*.mRDH3?C*l2LqWL^\.o\#db-JkC>3`?.D,P#r(<T"dYHtP[
Mo_PG\>1:H5*GAuQ!qaV$se5E"d;Ld$RE_U`gJ]A4m3<8?`$$_'ZZ0KmI2S^lNJ%H2/1!QBm8
'?nK9"qeUu)Z'W"*U$ec2.30U=R6F\9phJ+`u+ZK$/k.27K`1FHDX\f;ir6J*BQV#"Jd^(9@
AVAt5&V,qm,SV4\R-Ak(>&I6Y+esFfK5E\(6(:mZ_Oqh<,]A+E)kAG=U[=jILV:BdOn$ZdYK$
0&4+s3GQo_N2:,1s,6V;bsUc*^`"LAXjmbFH0?QK+7`[lW>rQ2'Lgdp/^F,bY32F1Gpt1Q<:
UIn%;^s'TEr6me'LF;s%5hE@J`5#=T2G[HX+r75l`sCm>c+(02R'g)*'T-XV'Ad3PNj*3Z]A-
iiT>Z)di[olD?Ti&Vu!"X3R_HrrfEGm`Kb<A5dPg4+3FV"6Bf2l&?9/F#DqFZCYA=1XlO4#8
k\B$=$lhlI`PO1B*fR:.ch`45:oFmga&Q^+sgTi_3G/m_eWFELV`A)rfr=St.P"%;&1lEh!6
R*O/78H.("XR%u?il2'#@G$4([h[5V^eZ8#90SK92*nSF5b--:gD`\WuNH&TkVAM/@"F_XKU
)3+4lE4Wqn@H3+jSThmhCFGS;b]AFb<R&`?qM9'eOoh4[5M<FU7s(-<N.1]AaXsW?,IYqdo27L
AW423(OO*BV*VO<9rAY!lGhV@70%o\2?kL_@s:XsuZ64Em&2u#pN)S[]AS']A2bX:(*ksTP)8M
N:MfMe8/1.''f.R\620k^HTJ1$'8onGt+0/s*i`j1iK5RGhcV3`N^V<N1V:/TS\oO/16%8B%
r=[,:Q`_9:Y:ZMYF"\="bK1nR6lEc$>G8=>Y@^*<)bXM_jcfpN$!s%LOZB=M2\qnY"ZS=FBV
M,0g6I?Q^"Jk@ttTSa^5C;f4T@S]AeV=>8E^IH!0*%[la,6:OoGIC7"V`J4=jpRr@@brMfQKM
8;1S7Gb7E+.t(R!Z9P)h(ZAk1:$VuEd;qRDZ"W3n4Gro"T7ORU.'A>,nK&_)9Dj,d*pGU<((
B4?_`gK",oEom@q&ndR5=)]A^t.RU?d(g$3)_t'lN24bY^<R@*$]A1q5:EL-DL2,-8o6hHu9?L
S2JbF#CVkc!2o2"o>0as&Vh56pp#EZh"J)L8"M]ARG\%.`p(:7/=rRV3]A`jhG4]AuTtK*Jc@4Q
*OTY"+c2*_\T31\\1SEk40j`ScW&*%B^?W6I[5d81eK;DK&8)&:1$FamAY!h)d^4pYA.2P(Q
dR]A/=$WJERN'&+M%geePnibF@qfLk=mn`eRPdmCPB6g:N(eRC`81KYQHD$WLa;>R;NT<qJ09
?r4(7ca_I>*<7`?Bh.4ebt5+b,Z^ub]Al<-c?3SUJHM%,WkJmc"Gl;:b0E&HHtjO3O\u7I,,e
4ub6Ujg)kn$bX^<p,+Za'^[-ku*'J&R0S)q#g)bJ[TC>7"uH5:YUaI,T;WTKZLaT3Js6!E^G
l+2-C[`lc;OBrebo0qAkJJ1h%0(BhL!$a+P2h'0\Z7V=8$QPI=L8W*A!d51f5gtO(8$rAOVU
+<-U;D%*6nX=aA$*uq,Gf@TrM.O\XfCbK%D$?h5oQk07Hha\;c`Zs;U>Oe-Vtr\29jUG,=fm
RYkAD%HnuUh(4SNCh^kG6WlN?,pPXpAFR.LB\rr%7XN2n<Z"H/n_hBAYf7`_&^)n4d5K?o_9
L\A[4=UErH58_K17"_GW[\frUB>6/FElfE(V&1ED%oTW_bWZF[,P&,4`Dc$=K$tLi4&H]A!Xe
]AmQ^]A"MBR[WG;`4(ib'[Wd1Psh!7F*K!l4EMJP+UeE&N!#knf$NpWQHP(^r[L?:9qSt`sX7e
]A[?mWAGC42SS<6\=aW7rGgWndFuAZ@bj=."_*9:+MJaKY2I`A;SmM_[a)^HUL0VkGf]A<sH1\
bL#^DRlbPp1'.Jd5gnjY7FR[+"Xnn$'=5+Qp,A[^E@_DsLPVT'0/hollC.;FuuIf0A,AYsf&
&BYRJM*?qZe.g"G;-WQp/LSKm>/OW+T"Zq]AqW"D&*bK)&3-AodJr=R0e(,9GhpUudfA%(hc#
s]Aa0>.#@NZNl`ti5toVcC#=%U3agH)JV(l&u1<p@7$N6C&<Lq7IP*P,n``R^l%t)^VCS>DfX
Z<Ta@>qcj_aGo_H#?Yep.ig9EE@9o?/!JJ&3O%((L&l43V$GmLfJ-n^r]AHH-:k_u_%*H3`?O
QLdsZH_gR$VW`)8Fg\/b-Wp6sX]AVd(5)Y3Sdpl$1A%"PRL>DcjV4]ATt,%q6M%RPkVJK@u6p:
`tH_EFIMA6B,M(OT>k&'l\%@D?s?e0&@8AmqT:+PmT\k/O]AdN$!s,`=@(F`G95>ogh?>$[(^
$4\YQ9[:NO\g(!*&ijZVd0]AAW,P8jtBD#um32hA/q\$9ka$^5e33X6m04s';+nULd@>=!&bC
cPsDAnB0=UKi43rC#"^,@J>le92r`27_P"M@3T,\Kk8mXop84.<R<G]AQ89hVHLj%%;XIp^!d
NtRcr+tp=VZPbp9`\&,DEk6$a2+5?TTO;<Dfa4n.%3:JBK/2&17g[\sM;oe"M%MF9Li$HG-1
#LbQ*H6rMOCVhV_MmT\*b=`ZcjQki[MY'k;9gNjqNPS!T6'F[rO/jfdiRS!7%r&P7h94te"b
DE[7hNjNl'Hb,2"A&h`bnmV4$ab/TD9a(,QPF"I)(,JQ;QZaB!2OZ)E7onkj+2tE7uUQ4S(9
R1G)(8QQYTe%3%$:$^ZJlk_(us*3@4G3]AnoO_gc^Kb`PZKQXei*=D`q+dPLVU4*%pS:1b\r&
'P^3gYYu3Zp1"g(Gso#g18?9.=;'d=[rha9F`EF=+)6gSii::2I+%4Ql+QA2f%49s5Laj-\0
2a1Hq=+S+I9j0r$%VR:g2/&ANVH&NV?)7?0G9om[WI'OhMR2M^f+#2"814Mm6W(Y-!-b!_%M
\!=\DC<A:'Q'[CM<:^I6Kpq0\K#I:`I$YQG?&K-^fGFtcBt+eJ;-RZ6d=naTP7c65aemGPDI
iPGIg%@-^7N/kA4?/n0g/f")Rb$4>"2C$r6hNjh-7_QqU=il2Qg?<E=_tM@$:*h=oHg3/iuK
4V^0O3g=8A>PdMfqGhcD=R@D$/2%_;d$ErG;3SKr;&OYBRUC=I?ePhEt24`p8^668uUlC5rN
pS9\dHo`("j%aCVY:n21[=p(BFArD?0=cX?!2()kIc#jT'.4K3N>-J"'Ck]A:d8--,M`O[b5u
4ejXO,5*\/\D["<+=e23OW=h88f'/9]A&<U$iQEPt6O7UoqV6AB3b97o`6Z-HD@U&9pT&j^%e
B$.uQb=uoDAh[fq0,7p<h?)bRds^LUfF&@>K-fj[<rsFnoj'_)^C$Sm"5"Di&Y6nq6RI+UQd
iC=Y_D)qZjODoKa6SC,;g:;S_Ikk"r,e1XQIIDk>ITX"0)oeBJGD2A)rEdWd%Ca7oWem4&]An
&[!70!&"@+&mk>NH'^%?mg&*q8`UG9=C)CjUG+>?7gWhe%9=lYHR0"S@!OjXD[_XM/Pf0D+*
UgRq<"?NK)Q-alA-Vl&4?il-X))IK3'o;"Pt^N*Ck!_rf1>_:kelXQpR=+a/;RjeD-I)qgmT
!G]A4hk`r=jSYR;U""^"r-qDpOTk8p.W]A"kPb#>':Zs,,?F]AboDWMO'Q19`&4.,cd!^Ua!Z1K
l<I<M?$u3NkhlnN`-e3#U24'Yhku$Fj0C4F(J@SUK>p(6A+B5-6k/[SSR-1CTpJ7p)O#ScAP
8Ib*.#4nRTK!P48%\@R[Oen(tgM&VZ3QoB"X^D7\7no;kfVD7V/`b'+jHcb:L%.)0mfflPb[
,Xp!G@3fNZZ96l0T0Oiie2;;hR%"$#5H#_Ll5XReVZ02)K4N\"bEoKXA-255$P`*`ehBGh)i
3F>GL\S3R[>DBepRZ9Gm&sD6"WP!Dh0`:h8L+hCgB_'/g/ekBmlY!V5L:tc%V]AsQ0+`>n;rk
XIIWLjZp9^1qd%"]A0Oa$^)dZo-_cgp^"N]A1eT`r_'jMeS)b2:,.m+X%^o$A,sSf=-aE,uY$o
O1]A%jTcr]Acd8uJWV<WeM$=9uKLaJ#_9LeMRAn\Jr/9>FdN_.q8Vt"12cA/G)Q5jI0gu0L==;
/[cZB4B-79egeKF)5+G9qa6Gf:,QrV7a7i:^,4R7@`VbCU\Bf:aZYF,AS87EE[`aV'=R%AF'
fZ9W.Q\U.<p5"JL*`8:7CT=XTf;7YQ?hU?g@\0`2,O'aSpMBBqDq0_BI2_O9^/^0t>cis>4F
/8Q<C&,q2Tt;-OKm'<8aKLrbR_U_dmVPcJ)^8&;Vae1_.O8+o9#puQ5-tDcNK6eU,)=E'FtS
57kU^4.V-CQk%<=@2d#^;ldTFjjCY-:c_B/i+'^F[gH"*s.-#5F3ae/`AN"1ZIWhAO4No9@s
33Q=#ADiM/*)4-j!D@0kH6A]A!1@>eMfEM!k(_spdUP0nCjYrrmBinGjK:_?\U;*^6.El/6.^
?<::KFTj1E?W?Z<uroJ<pJ1\O8Ap;_NCBN_6B!CEUkT9UW<1@O(4XF`(q]A:BIEIDgXt,=`Y7
]AX9Vn0PtFB6YfE(,jEEH%H7ls-q0c_>[oYL]Ae`E"Y3GAtjn@2QTnn!O&M:@Qf>ga7WS%lQUJ
$%1VlDpJ*L?CVO]AUU=4.RCsU4L&1R_`i_!V"K]Ad(U%UU'TO`$CJRTF-AR\g4#6prm2OJ0_95
(G>pa)E;81]A6UFEYE-#fS2-HpLH?:Yf_EjZ[dH=*!#dIP#JSV5FZ6'fIMS9%L9DnQj)!<>@F
3.jsD^33//r+#M?>SX1fRo9="]A^:H\MT6CWkO>pde]A3B(JVMdHIjh(:T(T"m[R_;9%.!UuiB
Ee[SoJ+6W[R-r06&a7&tF(UhmH"V^R6TNY/@WP56pUANa0@u"H6S;D/VHU'%L!0'i2\u5$l0
$Tp&q^U1/GC?D?<MdYb3]A]AQ:7iL`emEi78NCEjt+QB3E8*K*,a:0/_3LmGNZ)o=q%D$HNFQj
(0/.![ZUihSVKr9lFR;:Z?j(MD^R8NdAE=7bcrVDeEcLH^UE`r[D]A&cnfLI`msYpDQH9!-1[
n([(#asO/WL3WX3=goT%e=ktX[EO[Cf;IW/D%Cu&np]AhrgcoYh5g<aL:sHhCS8%Ib.772gI?
$_`eQ5;2'S-a$;)N\b;4Yuai#h1Hd/SaRUJI%\l?YU*:D$gpafC)QBW!3m]AXaT:"5Q.g5G\f
KfOcXGu1A.p%.Z!!M5B<('5YI`]AONPcRf#ICJaO"VH0%ki%4+gb]A6No2kR%*GTj=5N%2?KZ*
gnTstNie\]A6Q6m?[A;;n^Z)s85#Tb9YU)IQU]A:-6BhCE<@A+JUO^/O*?-MEk[ebS+7cV@:$h
P!7,g?bCAd^`)6-Qk[A]Ak-'or6!P:A_cQgeK5^)_GeX6!]A=8XBH+^(<HZ8&gE+GM9mp\J#7e
Eu."$9Yn-CfJ*$:p6Z)s]AGXGAVCNq.UU-Kj[4`.n!85__D'#TXt(f/l8t0'dYfEs+p+T'k`<
\Ou`8.D2YQ!E_/Ap7fSSVkW?C0RbXg#h)D1qud0&JR0+Fm\K1Uc>9KqGU,Cn05N3q>)@A`E6
S<u>3Mb!U=?aqIs6Fk+XLBrf^n0oi=Q6\E+O8@O/8uug"`<L;\*/V&1)>4Fmcq9oM7(!&usQ
#VNdu8+>9,D7tOAQ?`:*J5%qM@i6JGULknogD-P$giK`;(l2*rjjd4\;n-or%aL6`<'.TE=f
95$\+Kj5jge7;0#j'j7MTf$7q/nO=,m`"$M9J_1Gmi-3GH?/T:Sg0Za38[C=m.,T!@'B>E9@
MW>Z]A'DZYc9]AZ,)<B&L"2e(g<e^juhJ210(3?aGV,NiqZjhK>$/m^"grXACWB!:>C2aMf\%#
9dDNq;EE-`RkT^?pB0qP/D?l-LoY,CQ1%_gB:4L$%H_SgGlVWdG(c-)pb(s3gcF:M0&Oin1m
g_=55B1\>-L2+YDD&<hpqHiMWHZN[HbTQ-QpG)?6<G@-WY?u4Y'P^*kUD$6Mte6r:9F>(dQ-
dU3Z5"[eke?:,BUBp7RSj1u!YZ+PFo-(iW!ZAo>rd0'#dZ*FO(Fl+!j6Bm4-5L&[37++J`:9
$om%qr1\C0=+T":DSl5!e`)\4!agXCY(cK5LrCk+Wefted`ILp%[d&V?Z4`5BfDE,3ZS"\n]A
O68B86FcI;rBpKDJ5\L!]AE$lSWDe]Aj+Tns+R3m5m8To@.Bm&KPb1ABsPQXIN1kq\S89eHe6a
'njuehn,cG*<>J[#^OP6*[2+LP7F+mns</4K&&Yt8$*0jOVW1Vi7_Q2k8n;',40,;R3*1gES
?LObbjbd0)XfE\]A(B*#fjKESjF]A^m`pC^PlgXgNUK'Ms1c;>lsDe^(qS;hEq<;Ih\l\dohKD
Ag.RJ_f=*h)9R8YqIe%$>ik5HKhJ"9^KeIg5l8tPI;n\F7=J82&U)@@\9fnCT2W`R,3sKi.a
&Y^l_1["6Vqqd[+ui^-Z>&J4EJ(3[nAu>G4V1sB2)`nb"&SfaV@N2XW!7e)5@3$.gtp@Q4!L
%QQ/YP%pgqWKJT!l?]AGm3B9)@N#1TmacE!SW$e7NjEq1ZG<Ol,`M2<q(2le_p&$t7$DOorG5
=^Ha$o%NH<h<PkjoZ]Af)]AVaY+5!NLT6K[P7iC'uD_<RA9o5RS[%d"gPf[c_n\'REAk/u$5K_
BF<a_HlL*s_P/b*=d#W]AZ(6$%?1VPjnNZT-$\#kSOef0G/([>0!*%Sm,QK$*Z6s+]AeoeFT_Q
^R%nbf>3E.Qh(MQ`;!ZkW#d9[CL5A)F)LbF@O9!:U,@7p'A^7`bFf"DIPqrhKj>"S(BRMIJH
+::W$%oCODZ\G>L!Wb.CM<ZJRE]Ap103r]A02c_m68MR:Gg-6%Ya\?:IXCfImIcS9a_?WJd#7T
6._HLK5r3J@u`7i!fMEPa[9:nC7.iaN.bC$Yeq/NMPq@c*PQ[Mt@WNIkfTqdJ@/7u`@[#*`Q
5X-fs.t"l/1i#"AdM;'$!Rb3I-r&VWT\c7,2A46l9"SPWI8Wg$Y[+*Yh`Go]A5\GhO^;o"(!B
G)\6A`9r!KG<T_95+:>gXAUX%8h##&P47I&p0JOk-39+fDdh$`1]Ace(_lHd.WPs&""H-%@1@
\.MU1I)DJ&Ai%AkUqC(oIBBQt:SL$sJ'WJ<tktI(46:K!LYm/4e_79(>MBdm24-es!8PsiY'
hP7NH`TDiYeC^.^"Bn/[_?TPj(T^jNbe]Am]AO//!W.LEL=NOHZr]AN?A7F,2EL[Pj2e/%a2E-d
-)E#$i#/D09S't.r!1T0FWAEN:+oF(oi%jR^)ma2=!AcTPX2-d#nU^(f(Dfk)O]Aj0JF^:n?\
*1?#,0p)nY+D2j&ZI48QD(;GIbDZjUh-:dieUSC_DrWb97[46dq:+$lPcnG<Cpe=Bp[M,20d
d3n>T)`G%c#7g&":e#>\<t;dTha-`rr..TT6,%3Q%[5_%(,C;U#j.^,DW/II:eSRqigdIs$/
cAnD=%YfDB"a%71Lp\o\]A0"a92RjbF_L+,ZC@"4)>f#[^e^=%stod8bB"EW3[3WirFZG_gV[
"G=&G0[3_BIPR[cToJbRMR;;?VJQ&-*9"<eb=;-jJFT4+@7H:YirMq`u[0mctgZ-R&T#[Y8j
6m2<=HJK-IM#8?OSGC1jQ$07stU^+Ts#pC)C*I_1$1L*d&b5QN)r#iU=+.qM/a/o5a^N8NB8
fc(;p5lp@;&8D=3;\o'qVY3Nq?S@A<Wng3_^r"P<G/5skeLjVH@[A6MIFhEVBl^u5W]Adl\;J
DVhRnV_c%lA>3%t=hPf3&`Jn]Af]AR=7G5kEIn<rULKXMQK'l7c/TiFBO+[9<'c\b:uFN@V9WR
T06sIiULX,8F#]AigPVJ5H$JL-QZ<?<^mENpG4cWc0a.k%M;kk-;^)V%X&EEmee'(BT=PjF`e
O?WZ/aEc3p`s42hCG"9rBk4PY$:DNGLUZP&H#;:7hTcklRKC>@eZKN0m,jbMmOL0MJKI(1nC
pcgZ*>.^Y[hjoTOOX8.XW1ErKL_F)D&b[F".TQ\d5`&FOIXATM:;[E(f<Rf`9/&90N'^!8V5
N8N`&"q4eZl#:a09$MXGBF4N@._2=O&a]AZ_Nhp#MH$Mq3Bicr9:RBtKJjJZs5\en?Ni&g?aB
EjBa'd=,++j;Ecd=>mlLkICpjbCEQjZKQOh`Dj4bKgJ$`,cN1?#dXij60A!niEl:1+"Ec=_.
CCm5^eZC[LcG"r+-D]AAXs`)-)`^/nHY=n.gC94f)fs(Wa=c>`o<C0<X,7eS*\.&D745PZE=T
Kbtl'>d4O105P2&p3AGa4a>8Ap_KKrF8u'X&6,)gA;4DZdRAY!WN5gcX[)CK0HVTiH.6%j[k
qefLhq"XP>UhZ)ggBUZeV'pT!AWRnj<DK9[/Kq,;Ep;lSi"F^TB(8BsQri:VrphAVY&?\c"M
;odYTOUBt40>gYT(AL/jLuHIM(?fT*<cIDg*iR#bF1gVZLi8b,;q,Rqr,0.%&jfo!Na(P%T2
LoaADb#aFcuO!DT:.pU2*QPQTa;LWUN7/.=@n^+h`qk.oaN[,`YPN?r*hh`4_fL2&B='`OkO
E#3p94N\UCbCCj'e^r[fuF?r2Yhgd_gH>N]AP3O3Me(9(LN$k8]A+WlYZSWtY\(/(W-/P90g!,
':8Yf/7rad;[Wj*oT7Dc0cf#k-EE!)`ku(X4Mr[UK,J^q&sj4@2>`.d*(]A!/Pa$b$)KfrWJ1
2^k9p0Aa;N?!Gi5[SFWLq)BR<m"n`?]A7pX>WGh66L&cRX",kjo>DMdc^Qc9FBD/SR_^m>4fA
GGRDXOWXt-)_?+NBuTtk>NjOTUUX?GISmc+N*Zg%(hm!+ng02^;i2uGq*d>>79STc:en>?HX
6eOi+PVE=3tr9#nj*lOkpOj,h:e%@PdZ5A]A<`uFk1u3(\3S8-W8/0#V9(#SCVo8Pi0mMb\NH
&iA#-e4%SO2W;`n!letl;Vdn+U_^+TLMe7m=e-XocEg$Sd=9NK4cG#Gtf/IW&\%9-K.lq0p[
]AAGYEEeRFmlJ9gl@B+(LV5BfF4&&W9@C)ZL,h9QS^KF!cbO[s30:<a/3i<k-+*F1ns."Qf@N
CE<W`FaT9@Z<Xh5h&*I\LBkSXGD[71e!KFiE[(df,(NhaS2kZon!AUQ\Ab7XE))3#IR$C&\1
8FrM6['BFnm%]A1-1>C87fclR@;6h$:#V_Kt,,Y6[P.t,2IkL'\[:hX@8-phX29gO!JBbR>7g
"OT3gW%br7&WaaE:lj'Q5E7.QZX,k7Z/]A+eq*24`&8dbrMB8.^'m^9i_$#X/i(@qO@"WAn\+
/c6t7g84?8Y9ha[i'H^<RqBa:Ka7?T[PJMltaf0ZG,VSMRX-UWZ(&Xj&CJ-!=P)eeoFca`rl
Ul^m_k!*c89Ji"dKC$Ipd7`?GGR4.HM?ogcFUqc)u+hhq2(gLm6\KH.q@;/jn^s=BX?BciP9
$fkrj*$C*m0&!^l7PnNGU3gNmJ_n(=b0:7:gQ?W6Kh6Xt\dIG('G1N>;e"(6.j=^[J(n>J\@
*\SE%e.XFEP`(9jqOX%G)\H&c>MZXs?^I_SE\bR1[<VKgSccWgTsq@qq(^?+]ARBI?B19SsKW
i"?Z"iAg`JX!S,B0uLaWd'`7cQRs,l<$\Bl-"IAZ<1K->q7hhleq";>+?!A(kSn\?Qsj`1`o
kM2A@8@3PiAk;dU(8&m*c)MW%k.=GO%3c;Bp61'7:lAj^20Y66BE$K[pGd'?E>ZW,-2",:^)
%b$?PmAS-A4>BsjrXXA_ea^l(V06WAG@-k<m[STNX:]AE/TC(+4r$I`)1)IojOf0?Z"IMJ&UI
2RZe@C[2-YaB>KE2Vre8J9/nS-X(hp8)b!T-4d?6@3jIJd2Hi*J.S.3!]As)O!W/q[J2d5f]A6
mW#F@(8qlP'F-&7/$=!9MYBU\,(!%j,2<uVfpbXFm%PoJg(n!WkG%CE!\$.(0d>U66j1q$ih
#!s4[aQ:Mo'[%700<FZV9k&o$p:u->O$bNu]AEj\S_cF):"1S5&b9'B+sdR8;eISaMu3L6E.I
^q@VY`4rIbUgr,Cq2m&,2?N7Ue+JF;XZAq75R.,n$QM_N1QC$gG@GP,QN%f#WQfuuEgoFurZ
^8it$-X[:,%eN,H'eq3O2hl`RXW3nmTK4aLuePjoh!7e6#e(lnNm+dUi%bJUGbnl1;\\F@ec
iQL`VM='rn-pLs5"Vj`\S:@:]A8Se(3'N`^(nhGFp/j-.3E*&RZu$5C!^^#G'$[B$T70brQXq
09YDdXJVo)FoA]AQh)/rB[B>u2/1Ij-`:"g,Q\e@[REXb!-^CbiB>$Ls,(Y(m;H<+$V[?qR?F
Jqq'p73_;>"OO/(5["HEK;Gqht"A<G*'T6-P-6BlW8(cV\`Pd6r4WDohRE9m&1Il8M-f*K8]A
_'->IlLA0S\`rT)MVKo`QTZ)#6>6T_FQEISZKRRfmaD+J+_=>F]AQ!@de\DI.HF(<`jYY:aq>
pZpFQ^OeuEcRWUSdAOHL.S??)jSO@$BJ1f@t;/bA<Ad2^#D_>>/jbN4KL,^Alsd52Ph!L#He
)MR@Toe;Zc0=)M1s2"K^Msfq4T\Fa<8)#PXA`m#AGJMT!g#El8#qT:Zo76R/@p'\\rQfEU]AB
7rV.rN,5\u,l-qf>%p43\GUrJqae2&qOa`ZG,6DU/@*J2qT_IH%/dUadCIjN3qTbci[(,7"-
hfhnWYi8>+XPo)qJf@.+dJ68Z^RR?AC$hd61>aLnXnfQ3\F-\*hjuZu#>i.R_rllI4Y(a(I5
iB=thKEG8fS^Vp2d;G1ADUV"[)AD01[:QjWIV4BG6@X=ar^n^Rif;l"n3\<oNhErl7WTND@<
FEjV3:6]AFk&BFG`@9Xp18\FP0X%7TUSK1#b@nRhOk9@\YSQV`a4<hER!J^KMmp0.^P"NG`-t
T0[G,Uc9#-<FjHdY_dnlTJ15s,n4*)(s>6ddSZoj$$rM/CJ'$FkGZoZ3"nnu[ad%4D,"ApCc
%i&.',2A>QIaN^8HV%3*aTK]A6l]Aq#_lB-uW<9MqjB+t#]A-+%F5,rT//jFZc@lAtPHpVnI0MW
eUs,[JZ#AL+c23nDOk9P1cPZTmFG`SPU02t78i3A?\\=jJX@&rDDMGi$5p9X%&0eH3(Iq)E(
\Fr4A*QP(M&%4,h)5R=C(Wc0@Hl]A[.4SGC\->B^ch7>*gd-3D."#m%)WMG`$l5+n12AWt6#L
%nMa0+u?W<'6?_Z9-%#S0Bi>>-ceA7/Ni>R)oPeHK(#l\qgRW?q?M<28\^3S>`$h>kTieSs0
(g+kn75%g^bY'F&m$!aAk&S6!SpIm.[b"ishV[oCi@+<dH!6!?1IgqpX(p5#qD>1jSgbbq<<
5cH2nGI*JZ]AhPbPorMoLd#=tsb;^qMT5ZX`q=[I'?a3o@IDJsLr=^7IGOq/fC[BSWG(BHgBC
V@;>l:*;k^"lYY.k(4D#uO-mRtB2?Sb$W7%nM+K&>q=e%&uc=h@B1JeG:)m_!;[5USIW[4.K
"U&FA"%+<urM<>$pSl32QZf&\">K_7h)cEA[`R4T\RD<HS6_V%OG9Y=H&+XIaVOM%%]A-qu-P
3i8bH)#(jRL`3ZHjZ7(i[Pd5FrlM`G).B807MW\R!?Uc.'>H!I!*6Qd/Y[MMY?WK><MrrP81
Pi3ft'8\Is-4ZC6s1YTFPJY+1#NIib?AM,r@qJZ:ZLVoUN@%B>Q;.171pfl!in6F8JrnDgdl
kBNfMk;scoRLp%]A\Y93hh5RpUfF&M2;\?sBQAZf%B>L5;6d5"AVT+n.BB3a3d:<9/,R:V^bK
l%#q?qa)m<-/Al+E8:p1cn3N'Id7[;0Dn^/2pYr))K23,B3?3,g8_f]AID?%n5mkIKu$0(1>K
l#+Y*'2E73@S]AGAd:S[_AiQn_kS"&*\S6>*]A)?bfnQ$sY/OV'8jc0Eu@l;X96=Y^e-?b,9=b
V>75F7NB(3U;1sS6'<u?%&]A<SaBB2>o\C'/Di[c4S&#AoD\Z>4Huo@)io0k[]AuQYJfu)J1TH
P1KLMf7=gDJ2,@&([P-o<?M!U`Lj4"N!PU5PO4-s-UJl@Vp&+(=3bo@DBQl!"A5A38^Qm(9e
E0g6Q+Fg8=Ggbk;\$&G,bIKXG5ci?Gb]A6=q1FBT!&u,0DI(HEAe[&m<Ane4dm:<b\hL/2b6@
rnKi.Xu;F3H@4]APZFKnnd.D*@[76%G57G"Q`9bfI43=L!ggXUdFq,<<Y"ebJ8[H\m\<IMc2S
cbF)JR;\)9JNB5EXk5cN#I(9i2P1Ijpb.4s$bhbl<IFkT"M"MRO=9F4HHBE[[hO5:m6PHbmD
35/a2<-]ALJ!Y/%`[kTQRto%iem*BmBJu\.cZ@1Ks(ZMmosI'r,t[:lcBf]A]AO'>1e3hd_p:S$
,ML<)(4Wb&`>'nJpBRFb=C.=cqos8+KWm%Qd".BKnFU8%Js`Hj+R=V`jV9P(OZ8qtn7/Pnpc
Ed2Z'P`?B!X=V%g$R[eRgU7G5G!*4TZq6nQL(U)[$uj>a,+!X72WbB^IsH?SU8TB9hO=2m6S
EtDR+2q\:)W</c?,V83c;8W9&[4:_82n.e`&A3,(-sf2kDs9n(Zh,$G,J]Al2GJm]AWg=EP/g`
^M_CHu-'hsmZjJor?$1O5\6i?V(29-bI,H2J.usKQ#Q-l=/3q7c.<!?en-M>LmZ6a1e;KKkB
2TU)LDgg7WnH4]AbY"iO^9AbLn?E8$gn[foa<s=-T9NR-c(j@KAn24V*Wp\c54@ns<^``Z(>l
#Q+.^K>e/ts!?^o4dkepqrF%2_<(m"#L?5Vh;>O[<S\f5Ag_g4g_mHIYc"At:m(\!tOR1$(b
>)lii9]ALpn.iXa7-cZ+m5Ha7qP>'4G/NI,d3eA+D'9i[@fZVf=Vd9$S<I8&eLC"m3amtc(T$
Ebpl^e'laONJ`,\jJ$rQ+eHA0EA+X)p\j_Q8\F@!m9J:9'(&Zhnn*M!VC<PihK;d.'bNglH0
j_5G>NZXJf)^80cp'81ZH%I-j&@/bql@dc7?mT/]A/5?I&'hsbl."upY:8`O]AYVG0Z\FXAqaX
J&?nE\g.E+bEcQ#>ae?ap8hV?0?BV1.Lf)BgSih#ms<`V]A^,6TO-5%X%".k7el>j>7sWF`n6
pio)0AEa_0fY2/Xedc@^nagMcXh+NR1<bf7Fa(\)P*P6^GgFZLDV*Bjr]An'I3GMIk&m,jjGE
eKm=t:ORNm&5H/PB!c46e!?I:H@m:;WCq9@VZrm_r!%G@'dI]AK=Z&FX+YAiNes"&7'np?`oJ
Z;A-T_abmZP(oasO>t?aP**83/;AqIV>]AhpZA9GbP`0?LoAGOrUVhqre=`8mEXs&iX=]AB>8L
b%)!@#IpR9_If#XJ25/o)=1cCC$fPLJX6kH[l=d['K,.l)V>J4bAdY&nbQDk_%5Y!hIVigC[
6*q@44-0Vp1S*0hF\`X=CoH"TZN&g$k"46,?jD%ab(^"LEYS%7o3]A=(pj6UZ_d*164jN*6YD
6:BA?BsS-)<!EUS*tQ#FO!S-jg^9kJE6%>[mAZN0-:$auQbnYnd2[6Q%)"Br?=V9Meg^`"%n
\T`<qHHbnsNIY?1.:(=VQ,Vtjc,l2AaFc_CF^P0YNNU/?QS#=`)G8J+=NI$SW]AiLpjN'0=Fq
D&G`$$Y.]AR,B,m;!&`2[ic5?A0TlGaUGd57(e\MO==G-334;ck9iABRg>hfGr$^HM@_7GF`+
#\Dk)S0!LG%6?pgZ'@!-a\E)?j;&qt1IJ;uo5ikWFQs?O!V2VP@WM?n-4QX06h=O?4@->[2R
WOCnPX"#f#KAj>hR,$';mHp*8A'5s0D\VNRD!+gpg)a)=qL6O&$(+7pM9k8(-jW6R0h6n^)k
t",b=1IObE94Ag^\BBPTGKI/L<Z\(m!?ER:.^KRJ!+Ui[m%S3Fqr_D4h_!Uf+7;"cB^F6L00
Y1HD,p@UVa0n3fZ[;O>cXX5d*-^r2/C]A+_5lL@#aFcN!l\A-"q`98m+62_G"f>*4O';`:a-f
Z^EXlUYTG5l>L`6T\'<jW0"GX;`7-l':Wk3d[/mao)C9*$,n$,Eb'M@:t3H+AdgXaFZ@kahH
2-B`L]AcPqs'c0DO-cDQ&fU>+0]Akj^&ai(Jb/me;%qgF?Q0(A-Z5U">(f.8f7mP@6XS(>o,)k
?aib"e$!#7\g61PT>KkP"t&j/I/0#Q+$7ad$'ShAoVETF\"pDRmkS(LS4giYmEQ`4-4q!U[,
L4"[Cu$DUI0d7C\*maCS[7nIh=e?)O6S5\I_"n0r7CU7\D8J'n0F;qZ?2r.fG',_NlagdgIE
-'tgc(reW#fGV>K-1i#Q0\CMUX7CFF>oZ1LD59hg0BRsOE,EpZ]A8VEa/8!79["-\Qf#R6,)a
@#fh"gj+3/qdspSm=0$WK>XbF`3Hm4r<+r[Dkse_Is5YlH:UDZ-,jcNPuH'26VSNJ3CqYG*J
Zirn&&rh,q\AH![O@\ZY("!r4HU*.K2oO$PRO!V28NT2,KEKpG;K"ijYaZVQod=WL!NnjBlm
ocZGXh2M9cTh29`PIA\$7cP-,meRJg-:Y`pnd']A+BqL;G6e5UeogN;d0RKRJ325&`m-Q_<T?
;>nbAq2*Pk9KB>Rb2Y0l\:j4"2^h"j\.jeq2Nm8q[1D4Wm`;2LU3oa?3b[XMNOM^l*pRdf(b
,DF6+JG#HjDngbirpQVV42cCIY6B;d9(Fp?9o_ehhDOACB4;kn)9I;L7m%RdVM$JR&;?^Xab
#"02^@>h&`4DkDef2W@?G</mWngp;WWqmIsm3('28F.5JDC/hR=.SD?P1`]A*S-iOo@m^]As#`
(h7H`rTD8/`iA0maJ'Y2tEju(>aiN)O?R&eGDSM_@?]A0cqr8/UNWs'rnq>M$XZm5**h>[ujp
Fcas*K8c^Z>8c_?[p9'FoDJ*DZaq\cblcF8>K?Rp@iFENN)j'p)\3#T<@j70C$5b!/t7`@0c
72Ja\D-bWkB=r;/ElD1pg3>qkGVZ_HDs\=jachGYcumf>VlFOT,%dpE"3CMGS9g&DL8n*7`J
aftecmaJY/N".rqS`'Imc8HVMIePncSPO2(]A,?&.ONTmU^Lq["*lS(O3p7mRT%LiFP(eYdr8
djSE,QYTn3;F@8,fn*dQTVi*5;Np!!\ir(>6K]As,V3>rrMubUM"N6"\G,PNM:O%N0@;dSo_r
Tpj\q5b(a>JDh+nupfJG2%C/is0\SdQNuVSj%9pQiM$KQ#r&Z6=eC]A:EHe#R@D\8%JjC`%Si
N7UUbPlA$W=!0<F6?EXinN>rafbA2g&E\ArCn+(otA8ko6WB)'-dV8,70f))opW-p]A>Mn%>#
aQX`@Y?Fm:=*mm]Ari4UNuk,MIa'2`-P5DWgi!l[(>BO31I/`V1SH.tLPIBS/pd;>Y95P3XX_
epIAu_YcV.nM#83rEI&ij;%\*cU!OQhB!^GB%-DtXGW"1ANtN0[+^bb/!P+$6PKV[+;<"=h@
7[8YVl%aebTI7ZMtsuXp(41*]A+Wn+S\,"N\O8J]ApdTWGDGh(aHn,*MA%&SXqBA1#&*^i-f"N
iU@\Bl!?Z^BE7MB3o,c")3jBjNbmHU&(.Sf;2mD=3),Q3ndIEN\m)"6r,8Yf.g$U,f28]ApXW
+LFb4LB$ZW5/!HT%k&Ca'Mb.hLBeM2nlRt7=Y.u+DPhjGCV$,YUl8<0:UBO[VQMR_:gQ57qG
WUbd.:!_&GhFNcCOjqi1M>',fc@D^(oabK''_pd@t9mGnIhB>lNT+5^lUq0fD!e"3fV:??a4
nJfMT_YC0t*QKJ?8'gnL.;RcUdCV404V9&,LU9JL_e[["eo9LS\@Vd^7#g-:d5M"Hk_n.UI1
b>'^1]A_@imR0Hhdtbo&n^Eu?"*bU*S_Rgdm6XWqg1"9g^A1mac1&fnoCLe^SP*1q_Z&463e^
qLqN?%CkK<iqjdZl]A)LU7'7QeDIej:.$LBWb.B)S"$Z@p1\Jr,EX^d6WG=Ce$O,[#0V&@@6Q
n@3RaX'&AoOOGNH:0"<2MBfJjM-Us,k1A(OL`.rKfPL0]A4c>'R!Xe1dH,TOB:\WYBq82o(,[
gD'/+dmqs^sadZ#aX1a/8j2h$kgITPpfMhWIG2sSN7..^$CD;'NLE$P>=iVJub\?*gWn\8L8
FK`.>oipHp2VN92Qe8NO]AMkVLlUH_-"gV!TpOD]A2^Dl(9R/=4%Y8fH6$(&%'nOKLfN&K(shg
[Z$6)aL4Bq[]A_2[\^'HTF96&6h).?in]APD/,m:bl`HjE<apCe22C9pcdIk,Xl7s,O9\Y"?,V
l1i?,SW4IhS#LEFs/@1HG0#F]A>p`EQ.DpE+ACSAETY'9nP]A%0:#s8T6#7o._@hV4uq/W/[ul
?(@d.XT[<CqH("F3j)5q8?4b"S-@I,qEfbp@`J:O*=0s4_JE%->):%bkmI(%"@lp/?JFOX6T
0VYUYsMH8/?:@ERGB\!FEQZ(k;'_c&G?C`A*JaYAHoQ[\`"":74u0fZ$8$lN[48gA(k8$WJp
SmPr$=6>^q(aO^gG:o;WmJP\3&6#sgeE%$C<1i]AV<-W!b:NK#=g&KAlg#ZBe+/a&6?TIH,[]A
_X7cK>6L@dj8F(,Pt6ChB5TA5=Jil,=/QB:.;=rLU\b1I$27mcQZLs)iiQem!T"3$W9)qsW4
]A>IL^u^TB801!hY;^TPaZ#X%FDJ+hd+bZhQ[V;J`7IM(c\S\NkKom_Es^H[)Fq4g/im,jpir
Y\,;s*`ar7!&->3!LQDWdc)brStr%m6CSdI<WB=%7g>GMnXXgJ,AVPp,i6Ms.*>\?>),2>M/
?AHJnOup[tYu9Y%OfrhXq[#:jU#q0elRci$f_#63c&*X]ABNq=jge\!<@G$`e^5R+M@e?IqYU
U6beH/@<ag`?4]A/&%5Sm%-WKDs.8KTP;fb-Pjs6`/N33;5H%$/O;jj[rltGioA6X[lIHoIqm
S[nrERo6,r>W&~
]]></IM>
<ElementCaseMobileAttrProvider horizontal="1" vertical="0" zoom="true" refresh="false" isUseHTML="false" isMobileCanvasSize="false" appearRefresh="false" allowFullScreen="false"/>
</InnerWidget>
<BoundsAttr x="0" y="0" width="484" height="542"/>
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
<![CDATA[723900,723900,723900,723900,723900,723900,723900,723900,723900,723900,723900]]></RowHeight>
<ColumnWidth defaultValue="2743200">
<![CDATA[2743200,2743200,2743200,2743200,2743200,2743200,2743200,2743200,2743200,2743200,2743200]]></ColumnWidth>
<CellElementList>
<C c="0" r="0" cs="5" s="0">
<O>
<![CDATA[标准收益综述]]></O>
<PrivilegeControl/>
<CellGUIAttr/>
<CellPageAttr/>
<Expand/>
</C>
<C c="0" r="1" s="1">
<O>
<![CDATA[ABC公司（单位 千$）]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="1" r="1" s="2">
<O>
<![CDATA[Q2/04]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="2" r="1" s="2">
<O>
<![CDATA[Q2/05]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="3" r="1" cs="2" s="3">
<O>
<![CDATA[变化率]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="0" r="2" s="4">
<O t="DSColumn">
<Attributes dsName="ds1" columnName="type"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<NameJavaScriptGroup>
<NameJavaScript name="JavaScript1">
<JavaScript class="com.fr.js.JavaScriptImpl">
<Parameters>
<Parameter>
<Attributes name="type"/>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=A3]]></Attributes>
</O>
</Parameter>
</Parameters>
<JSImport>
<![CDATA[null]]></JSImport>
<Content>
<![CDATA[var pa=parent.FR.SessionMgr.getContentPane();
pa.getWidgetByName("iframeEditor1").setValue("ReportServer?reportlet=demo/analytics/get_1.cpt&__showtoolbar__=false&type="+FR.cjkEncode(type)+"");]]></Content>
</JavaScript>
</NameJavaScript>
</NameJavaScriptGroup>
<CellGUIAttr/>
<CellPageAttr/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[条件属性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[$type = A3]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.BackgroundHighlightAction">
<Scope val="1"/>
<Background name="ColorBackground" color="-4144960"/>
</HighlightAction>
</Highlight>
</HighlightList>
<Expand dir="0"/>
</C>
<C c="1" r="2" s="4">
<O t="DSColumn">
<Attributes dsName="ds1" columnName="sum"/>
<Condition class="com.fr.data.condition.ListCondition">
<JoinCondition join="0">
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[2]]></CNUMBER>
<CNAME>
<![CDATA[type]]></CNAME>
<Compare op="0">
<ColumnRow column="0" row="2"/>
</Compare>
</Condition>
</JoinCondition>
<JoinCondition join="0">
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[1]]></CNUMBER>
<CNAME>
<![CDATA[year1]]></CNAME>
<Compare op="0">
<O>
<![CDATA[2004]]></O>
</Compare>
</Condition>
</JoinCondition>
<JoinCondition join="0">
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[4]]></CNUMBER>
<CNAME>
<![CDATA[season]]></CNAME>
<Compare op="0">
<O>
<![CDATA[Q2]]></O>
</Compare>
</Condition>
</JoinCondition>
<JoinCondition join="0">
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[5]]></CNUMBER>
<CNAME>
<![CDATA[cate]]></CNAME>
<Compare op="0">
<O>
<![CDATA[现实]]></O>
</Compare>
</Condition>
</JoinCondition>
<JoinCondition join="0">
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[3]]></CNUMBER>
<CNAME>
<![CDATA[country]]></CNAME>
<Compare op="0">
<O>
<![CDATA[China]]></O>
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
<NameJavaScriptGroup>
<NameJavaScript name="JavaScript1">
<JavaScript class="com.fr.js.JavaScriptImpl">
<Parameters>
<Parameter>
<Attributes name="type"/>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=A3]]></Attributes>
</O>
</Parameter>
</Parameters>
<Content>
<![CDATA[var pa=parent.FR.SessionMgr.getContentPane();
pa.getWidgetByName("iframeEditor1").setValue("ReportServer?reportlet=demo/analytics/get_1.cpt&__showtoolbar__=false&type="+FR.cjkEncode(type)+"");]]></Content>
</JavaScript>
</NameJavaScript>
</NameJavaScriptGroup>
<CellGUIAttr/>
<CellPageAttr/>
<Expand dir="0"/>
</C>
<C c="2" r="2" s="4">
<O t="DSColumn">
<Attributes dsName="ds1" columnName="sum"/>
<Condition class="com.fr.data.condition.ListCondition">
<JoinCondition join="0">
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[2]]></CNUMBER>
<CNAME>
<![CDATA[type]]></CNAME>
<Compare op="0">
<ColumnRow column="0" row="2"/>
</Compare>
</Condition>
</JoinCondition>
<JoinCondition join="0">
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[1]]></CNUMBER>
<CNAME>
<![CDATA[year1]]></CNAME>
<Compare op="0">
<O>
<![CDATA[2005]]></O>
</Compare>
</Condition>
</JoinCondition>
<JoinCondition join="0">
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[5]]></CNUMBER>
<CNAME>
<![CDATA[cate]]></CNAME>
<Compare op="0">
<O>
<![CDATA[现实]]></O>
</Compare>
</Condition>
</JoinCondition>
<JoinCondition join="0">
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[4]]></CNUMBER>
<CNAME>
<![CDATA[season]]></CNAME>
<Compare op="0">
<O>
<![CDATA[Q2]]></O>
</Compare>
</Condition>
</JoinCondition>
<JoinCondition join="0">
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[3]]></CNUMBER>
<CNAME>
<![CDATA[country]]></CNAME>
<Compare op="0">
<O>
<![CDATA[China]]></O>
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
<NameJavaScriptGroup>
<NameJavaScript name="JavaScript1">
<JavaScript class="com.fr.js.JavaScriptImpl">
<Parameters>
<Parameter>
<Attributes name="type"/>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=A3]]></Attributes>
</O>
</Parameter>
</Parameters>
<Content>
<![CDATA[var pa=parent.FR.SessionMgr.getContentPane();
pa.getWidgetByName("iframeEditor1").setValue("ReportServer?reportlet=demo/analytics/get_1.cpt&__showtoolbar__=false&type="+FR.cjkEncode(type)+"");]]></Content>
</JavaScript>
</NameJavaScript>
</NameJavaScriptGroup>
<CellGUIAttr/>
<CellPageAttr/>
<Expand dir="0" leftParentDefault="false" left="A3"/>
</C>
<C c="3" r="2" s="4">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=(C3 - B3) / B3]]></Attributes>
</O>
<PrivilegeControl/>
<NameJavaScriptGroup>
<NameJavaScript name="JavaScript1">
<JavaScript class="com.fr.js.JavaScriptImpl">
<Parameters>
<Parameter>
<Attributes name="type"/>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=A3]]></Attributes>
</O>
</Parameter>
</Parameters>
<Content>
<![CDATA[var pa=parent.FR.SessionMgr.getContentPane();
pa.getWidgetByName("iframeEditor1").setValue("ReportServer?reportlet=demo/analytics/get_1.cpt&__showtoolbar__=false&type="+FR.cjkEncode(type)+"");]]></Content>
</JavaScript>
</NameJavaScript>
</NameJavaScriptGroup>
<CellGUIAttr/>
<CellPageAttr/>
<Expand leftParentDefault="false" left="A3"/>
</C>
<C c="4" r="2" s="5">
<PrivilegeControl/>
<NameJavaScriptGroup>
<NameJavaScript name="当前表单对象2">
<JavaScript class="com.fr.form.main.FormHyperlink">
<JavaScript class="com.fr.form.main.FormHyperlink">
<Parameters>
<Parameter>
<Attributes name="type"/>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=A3]]></Attributes>
</O>
</Parameter>
</Parameters>
<TargetFrame>
<![CDATA[_blank]]></TargetFrame>
<Features/>
<realateName realateValue="chart0" animateType="none"/>
<linkType type="0"/>
</JavaScript>
</JavaScript>
</NameJavaScript>
<NameJavaScript name="当前表单对象3">
<JavaScript class="com.fr.form.main.FormHyperlink">
<JavaScript class="com.fr.form.main.FormHyperlink">
<Parameters>
<Parameter>
<Attributes name="type"/>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=A3]]></Attributes>
</O>
</Parameter>
</Parameters>
<TargetFrame>
<![CDATA[_blank]]></TargetFrame>
<Features/>
<realateName realateValue="chart1" animateType="none"/>
<linkType type="0"/>
</JavaScript>
</JavaScript>
</NameJavaScript>
</NameJavaScriptGroup>
<CellGUIAttr/>
<CellPageAttr/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[条件属性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[D3 >= 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.BackgroundHighlightAction">
<Background name="ImageBackground" layout="1">
<FineImage fm="png">
<IM>
<![CDATA[!T4,'qMA$D7h#eD$31&+%7s)Y;?-[s('"=7('k*E!!'sECc_Us"fFp[5u`*!Fd7/M;g/qrms
>A0<8#IG(;tp:(")#S$P#S*i';+\#E"BML0K`h"LXmFJceirWi2k(77e1J8/Y;qXiCGW'1D@
EUE-)LC2Nb>pOWi`:]AL4N]A\MDXTA84G?UBfqQft-GP\OMTl/CMGFQ[d!e`on.$h@"2E5^r%T
@$fAQ:83,%m;#t4W=3n5W_8;p2ol^)p\S5Y@q!@'Kt5:(%mu:n9PqBW_B.mRWDH*3D9"Q(b!
s6O5jTIlCodRniRJJm=M9gM28o'$h9Qr,I6r?";VD2\B5k,[te$8*sBZf1`d27FoNt05e1UZ
X8SH%Nm3)iZ40jkYX$bI#NW]A-V_M"D*X:TmX1h]A:mXZf7Xfto9K0;.VPm=LJp,lWGnufK]Al>
YV>f$b%ma4=\':(gu8@ojp>kHX81K)A2Q@Xf\?D<2=8-\Z'=.Ae-SNcc.mgc/5t@TRQaONKH
D"E=Uq[oMpA?g^#B&O-C49:5MgLX9cW9C<()#cWt0[rDS[f=E-(dRYGnc@d0u1*4kc,>:>l*
`ep1V"b1;^8+/f:Xl>T_J[k+s&D(NTQ!6dj'm8"Lu;FS@<rO%]A@[DN9o%,nCLcRIVCiIQ?Yh
rr<lAKK$',T-Ej4EV"`o\A@uXscl93`W&X-NT.rO-=@hpNps"0#bffWM[3B3WRN6W$oeG[m?
Bq#+pnf9Yj@+5K+LVp&q_Q]Adt.#,Y7/7WoFYclqc]A%`[BE7B)Wc32K,6FSod*&9MGg;>u/b@
1"'iHgV/e1nL/f-(Ya2cZIt+OkLuo<=(8_"1BHCf3Y(OBRuq`$ND='Ze45%]A5'cP6Ab<oUZ8
$8&lVaesq<Q2A+.G=\TMp'#T>4'4F?G]A:#W3:=>u:9:DtL\q0thi[>kB=:V&B_C,4dgVo-/?
YJ1YJA(m9:hGLohW4mf"qG*##&t=^qO5=O9QQ0Lf"6d'9cdJp+.LXZ!k3mh-R>c,'#b]ASr\5
r_RR?tRaWOVaT1/3^#7Qn/KIE5</L?L;!uJo@Ao_idZ%A1p<(dSc(p2;S-$ZX]AQH1`B^oqF,
QBNA,CPV[OV%R#UV]AXa0#k'd'jqpm5htR5BU+EZNqV84#HANIqO`g!1&si*ZM?L:^h\'!>=m
R/K&?GJ:0mCLaKO,K1dBAsU]AUYV]AZA$QUS%o99IjKLJ!^WXF5@PDoN%eU^O*jB`P;WDNQ]AKE
:orD3p^p@Vqeh+Y$K@)G4hf&TOnFe80GEn`EoIOMC`<<ek/2:Y('B[IS"B#,)$JWdO_s?^@)
sK:KZBg,"OqGO5hpBg*?k=,TT/"9<*$JC^&NZNVSMN_>p1n!B1[9Db!u`Y&#["J_h]A,O^&Ob
So2q^BaYSApB_i@B0D]A\.$puT^X`/UPF%`bl%'#O?kZTYt1N564]AjHu1%*CQ@Z79&*Cm$;t`
ZZ<6:VN;"?+^lm6T"p.p`,Y"'fEEc5(1Z=F)6hpHAoVR@j`H>)Hk^.EYP(]A/&>+MT1VQX@8^
#pbUjdKYeB]Ae066kq>WH,)3IFo5s+si>V#K8fZ@$s]Am8eU%j==1@1(7/h]A$qdaZhu61a2K-D
0[%,WpA[dT^r)JFn/u35/=))1nmc*k&@>YY`^GoX3[r`;Uh'HXI>!1#Q'$PO(%c:Zbc='P(2
8$5"0K3E&qKqtI2CWUNA$&d+%j'>!X]AEmocI^"us-=."hI%=p4#LVVQ:%uS[Pd4/=hprN$F:
(V)><F.5C@O,_/$Xj>\/PWa"A>ZQYd3i&S`i^DN^m-RdN'4dTIQ6d?F9*XJ=:N23_@YhTd]Aa
KZlU4=Z%t;kMr8`<\6Z`D-Matkkj!i`*(X2f.gh'c?4;=$"4O\=[l>A-Zp(%"#L9'')8bmn,
NFg!(fUS7'8jaJc~
]]></IM>
</FineImage>
</Background>
</HighlightAction>
</Highlight>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[条件属性2]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[D3 < 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.BackgroundHighlightAction">
<Background name="ImageBackground" layout="1">
<FineImage fm="png">
<IM>
<![CDATA[!FH&(q2%pC7h#eD$31&+%7s)Y;?-[s('"=7('k*E!!'sECc_Us"suo05u`*!Fd!,.P=H>-(C
5eL_ZQ/s0jJH)<!_c>Js%<%ZrI@NH3$@K$Unp_.b'K9JO)`0:.L)%U*?F7JZ),Q:TU:bS18c
6&."@#0F8mGI/e(Te_6F?1V_U]Ap?hkAmG!$l!7B1I<t\5M/OB1WU:l&Ki(b0+XYPCVl+FCk]A
kOm;`'d2kngK?07FV]AFI/Mt&*Qa69;?]AF7dLHi]AR0(gI5)F@f"@Q+W:ZR4TA5K:k.u9q&SnP
.(#qDP3i3aQN/M)rhU&Aau,\k*ON5gebLsjc"T!SOXY[Fh6pP(6sX.&e;P1OBmSh]AY,g@VpX
gT)Mj.[<r"QOTbbrkj`)ia]AT<qf:&l.05mdH%8`dM=X&I$hC"F\dk:F:(VbHKJY0UP\0:/Q(
ItHXEsbu-n:i$mIPWJ]A2P#<JNjP8m\[en3$;-"AoBGleEpXeDpso]A",pV8R*7Bp>:^INCP^f
e5W!8"7<_5@(r_3dojVLW;kg:k+KD^PRtU]A)1lS-Yq)0)B&dr<h'$=*+lQX,\UuR2J^a)D7s
-%,49-!f'plK_<ULbVSU@9gS]AK_`q/h]A=]A`O1t!>?;heG?'7'CcF_!O<^,05+#n;JS"gGKFd
RqDD7(C?lEeD8Rd3@hI(/=9lpqWJ[T7QR\S!\"g-0&[jk,f&>H>/,4-cL0,?QMT\e3!RX#kq
g]AboL8uOO"B/FS6(_")h*B92j"HM!P.0t-O3lD=^D?R.+*V%^uX0jbLLb6I'a4&4u/^]Aeb'/
Xs$!!1YYAm4Hh[fka9!`OFAUR90U!+q*#NTo"r%Y=[2e4jK4J\)*B\rK.!@aZ0h'adkmESXG
bbL#Ul!iF@>4JKlO_PLKsnO^AP*m@#u&(:pf?UHN]A#';]A=4"^n-HUBpY3oc3,?nkM!3rG^k'
H=g?&;WJlMs3PX*5n>@PPe&^5s,A8Yr,jBd!3pc9erB>18<+?&:)dqE"WDZgr>7Dn)j)7q,Y
MVVAW#R)gs?iiB\p7eP#-Shm<a8/:p>)()g=FBVMjD@H"&j&[KUeY'R[PC=MGWU/$N.jO.GI
0eJ*;0pnq0)"=4hoH_fK1)ia(U(d=k8_:,a)qqNUPU7.R9r96K)4R@hAVrWmY*dDO>mItO19
bXjrE1ptm%fg[k%o,LA#%<&KYC/>a?o#SA7P[/:<lA7/:Jm5es>M.SVL7Xd1ER<5\t"_8i@X
#WT0_6%k_oNL^CEdLLYOFm0:P=/_H/D(lhWa"8&Cb%#Xna?%r.&6bSanTIMOEVRfBlI;fbOb
`!^AHgXaNWhCT=cOR`.5Q='E3LRSQh;g$+U>d@Q1W\p!d6;q+3^"g_^S*s^UC9u`^]A<s\F&g
UJ[#_LYqoBB5[^Ut;_ur*/p*^4U5Z)>k!mqbt%95kc]AXhupKmY?dg"SgTjG8h)erU%=J<<G/
769Z<Z0'/<8=Z6t1"li[Z&TAUfR``7mY9$-;6S)YQa\?s&UDY.,6.22Ffh7,\3VdCg<($kZo
)DI:6=*:KfgslN*?2M<G5U*d5>tLUf8gb)2FgR/uUZe_ikC3S>G58n--q!a%m8pIIRrHe5R>
,F/@!HK/tKKd-c0DK81N:.Hks:5aAlUDscqG+taeiDU.J9R0*0m+*;NCd-NS)&#*)ii'"KL4
?M<Wc.O9j/h&)0=0<.g^&qk5I""eZM_em%2Gd/@$>%j+:]Aq"i3QDZq_["PTZ5(Mbe"@-.6P1
4>(!d89oG*TD?]AK!Kc7cK`<cXe&3_:4srqK"]Ak7o2qT1Qu%'02etoBs"]A(_<IT)mnRFToP"`
C=sg'IQ\LIKd#Ya\e+fj,(\j6+^Z4G9+)OYeXLc$QS6ZBB6=9$ReuE#`#8Gp@NrqjRJf$QEQ
W(cWGQ+I#C;!t:b>r]Ap$+N8'3F5mqDDrHO2^Lj0P#16/\AYX;i1`mCr*3@jEQ(-s+h?>&kV4
Od^!LE&KNsopgQ-GZ&\-q^1Nm6>D91ra%^pX%\]AA->Mc/IKh$Q:X,_qY[6HW8PR,ada^0J3c
bt;8A':64"s4emz8OZBBY!QNJ~
]]></IM>
</FineImage>
</Background>
</HighlightAction>
</Highlight>
</HighlightList>
<Expand/>
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
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="微软雅黑" style="1" size="152" foreground="-4492536"/>
<Background name="ColorBackground" color="-398635"/>
<Border>
<Top style="1" color="-398635"/>
<Left style="1" color="-398635"/>
<Right style="1" color="-398635"/>
</Border>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="SimSun" style="1" size="72" foreground="-4492536"/>
<Background name="ColorBackground" color="-398635"/>
<Border>
<Left style="1" color="-398635"/>
</Border>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="SimSun" style="1" size="72" foreground="-4492536"/>
<Background name="ColorBackground" color="-398635"/>
<Border/>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="SimSun" style="1" size="72" foreground="-4492536"/>
<Background name="ColorBackground" color="-398635"/>
<Border>
<Right style="1" color="-398635"/>
</Border>
</Style>
<Style horizontal_alignment="2" imageLayout="1">
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[$#,##0;($#,##0)]]></Format>
<FRFont name="SimSun" style="0" size="72" foreground="-4492536"/>
<Background name="ColorBackground" color="-1"/>
<Border/>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="SimSun" style="0" size="72" foreground="-16776961" underline="1"/>
<Background name="ColorBackground" color="-398635"/>
<Border>
<Right style="1" color="-398635"/>
</Border>
</Style>
</StyleList>
<heightRestrict heightrestrict="false"/>
<heightPercent heightpercent="0.75"/>
<IM>
<![CDATA[m94d?;ch\MV&`c=_:epV,5Itt3$SHYC/ks7)llAAeQN,d=KI<mb9fWmR"`pG:b*kA,N+0L/Z
mUH;MYl.,h/R,']AkW1UbRse"G/sr&@.F8DQo%R_tULpVuALC&,4q%caiLiT6GS;pZ0,EFlCf
HcC*t[ju.&crlpF?DXM0s\#9(oq[<=4In`>FS(j)pCYjGKe"1#C=&;M2iis`aT/M(=?pPS%?
bC]Ao"Wi#_O8V@%[&oe$n&D`tAj*Q)iEr]A?XA.B&'>KcOqtn^C,iY;:c;ZD\Fo-,n,o]A1tl=N
Tb$@Uh-f$SPb?D(37TEHXrTuJ>D*)@iGeiIQsE?.X'=]Ah-W:,dGP\om@9nFTKBoO@[?OhU>&
&?0tp`MnGokK>3E(#JbeEpq9]A[^:M1gYLr''=4&fg74Mb7J'UmGq0&)W[SaaMFS8%4"o-"\N
Fa!pi=Yu,]A1NT:#[igQC'8p)BE)1<<-9%jg`a.*c,$n]Atu3lClG)g`[AI>/N=GiLX<bV1UeJ
[ZEC1@O).AD96Fb^P3_sf)j1L?[87L@g<XRjRItifG:9HT+1$$PC^6@ic<Q3.k@\N`hRL.c`
pea0\g(*F@P#DP=O^unmEq&kKXUWg\>9[i!&kPS0HC%RQR]AGRT9o)[l`\e\\Y4JL10)kk&@J
m<+]A:glo[Q=7XNXYGb3(d$/KrC7Xg@iOL"J25Z@:YsD%!W-%ZC#2bkqOgB1U/bD1Hg^41S?J
c-OhBFK6\W(%,Z=irko`['<NCcAcKK3gO!9PjPP9#%a'GL#k]A4RoA84Clsi\Q#<J(lr<p8A9
@rGf#Kl'2APOJ.I5S7hLDB-SJG@F*[2OuF;\.:n/X4iO`pp4lR/0[iVtu`)`33uUt:L:k`Le
4?5.bJ0CX6>dYd:K^e,J$6eMoT^A(X.p/'hkei(t."H>od%H4s'GU4OHf$_uaZMaY&Jn4fN)
"dZdl".Jnh;F.B$Ym&,DX%kZ`H5"DC2R)lmn5&QP/`m_LB??b\Rrn[`7+-T`d&/6/X/Y2r<-
[]ASYCU1?@@dWk0gM`ZcdRSnujul'[#bUoTp:C:=*'1l6tBOr2]A>1p/'a;olYH-Oj,]AdUXNj8
B_4-_`8=;-,LpKP:_MAqAk`<.A:"Z@5R&(Y(;0BHk@O/5s1A6p/@b=aCTc+B4=gF%I\#'HVe
i^YjJd^`@op3d6-Vnp6+pjVpF#18M0VC8@grJ&b.*hh;Q<Q;9g!gH[$u7,2"jlkg<m7`nR5b
NcHiLMSLM&Bh=q0q=cVn'KL?f1f0I?N"C9X7cbK)+%.>)(GsPl`\FfXH;tcR7]A]AsnD/ffS!K
j`sr<LN<%4qiD8<"Jp)jB/=Ae"@fpnF5]A`>OX(7ormi<"KstTS+8-FK9-Mc/RYT#=/=NH>U6
l+ion]ArgIj#4F2G%*7XH@[_17^7e]A)\Z3I%3pa_-`[^ARBFkrrEYep?kcj0sB4*fu'e4bnjY
l]AkI>Rr[jQUU<MKE3S`]Aq3MPJP&Q,K9g3Sh:>EW5T=?a]A#S`7oREOO>/@/Ypma1AtKD&qa9;
[Y_[),1Y<mZLU(pn`caEN"Yhp!M%[YDg4f;YI8N_2(&$/U,W;-4S<bs/r:J!M[>2oo1;ZsAX
FSj!j9_0;8$,acbN;3n`X8uJ'&fo/rnd\^Yo_%.,O$B]AImS\Rl&9P&>(dPZ-+?lJrK[\BP0<
?&ugVYMR?W72E"q3WZ`T(IX*nA6%K8S&Gl%2F8[*g2>B=W#.>Ud"!*PW;+t!Z3Ng9cf#9r5D
3`]A;@reTuC#iDo2!dBY4/ZU(EJRTZ3:G*(NHg)-uA%`"mX^3B'\%[T(*rK6;@Y^j"I.Ab)rJ
Xrt]AYJrZJq.#,a)bba(sQ+c^LjVrIL]A?@gK)WNnaYBP(kL>N*mZe.?hJ3T]Ag2sQTdeoU2_/i
']A?J]AeGE]AHREjbmsMa\-QiAR31jj2?s(2g_?c`(YaZXCY:<u)(hT;7adbF'Xqo7T%TEloo@E
hfNBo3<]AU:#"43#cK3Xm7F1N%rN_-;$qJEk&5R70k&2ZHUT46TV50`Nkh<GNVgg<?Vqsmu[i
iX):BVQaJH(Ig0MYH4Z,0A(^p(*)S,?-,A]AX.T`f9jD70[4]AMOfMCq`o8N2.T66$WM53.6>e
1^<gSj*o69dH5q(9t:.U_8kk![.!U*\R7^EN.AhKqr1P]A(SQlfG&OeC]ABd!g%c1g0Q^_p&O'
Hhm^prBen9p&\=Ma:(IPM`B4\r(t<MIkPQhJGG@\f\"g'FKHc_fC.R#E[HC*l4?"@0C&Hdf"
@&#(RV44'XO#3's<TlZIPI+jJ$]Ah4m/9c-c@INq4=c$.p-@,c8@3L9Qt2_3:[n2J]Agdbrkpg
!?WrtZRKdcN67logVH-#39&IeF=q$k`iD&r0;jFJpC53a<oSZpNL+84E;12IS-#(>5bPKh)3
=2\o(QVH)0iahlm!s'*^&LcYhU$_[CAZ?Hob,6EFa@=5"\$O9:J\"WfD._ofdg3Kj7WclFKP
QsHcKrRHE&5)+VAauLbbi+$o:A>6Qs(IZXk0J9^P#:WA3Fbog^R&(1#_?qjFn)rFX+L.QBt(
Qd\Eh#:B4^=KZBs6=OZ?=Q4e/]ALa:UFS+>S&I:sfHUg*_P8fL6BA=EO5sjX+P,W7(e`"oCh,
VO^&0:HKa/l%o?$qV_`JlQDd[7&0;iXbhMhS^<iCZ0Tb0:L%M="Nf:&Dod:,cSY@%OT]A3mAL
l-9@##Y[!<r*I8=7W]AKn*PC,;E3f7[*22@C?A\&A#[n__'3>mXM:.qu$]A$AR$f"X'-V28pE?
n9R`0\'[.+0s0kgr'#_F/oi/8dJ.(-B([gJ/rJsBqMGpe0VD8N8iVTI@D4R?5#\7FoU0W%3s
^!*CtiOF40eCeu/"\H`k)b-`!DGA*E?o>ouEqQTO)<S`TEsJ7]A\bmEMC3Y?IBVG(]A=[J&<`&
[6D:0=3=M4PmiS1"jMqNUDSkER4A.rXk%C3Ash*Y;d>i@)!MmFA7o6ZCSZqe6>+[c_ceUco4
1,sP_moWKB1]Ar`FW3%hckM7UI#1tn%Gg(m%5>i1tG2/d^3RC#+`0_?;inEO=2-XeEe[1Z7Ye
,ICJL\(<7CGOlk_3:^p>\\8#6!CIG^:a_C78f*KK=%i=k@i0_@jV\rYCAq%,2;X;Df>8X;Hl
LS4D!,-<(/m[rW,cDlnZdE4UOiB.GPO8<j`SO'oB-A??OWhI=d+'nXr6^d4S!<2U292`Ol<.
UDE)@fB,Eg?`cj$D:SE%uR\3d=oqPtP:ZTGNsOJRk-'Et4&8:-S^$Nr5P"2s/Q@NlY/Gl(=K
ITr(d=-[cOq>d]A_bgO1$DoXKfY\mEJ=k$#I@ZIn$<-i@P0Ae2Fm%H_TFMmq@G#qE!,-*LhER
i?GhODjc=<8O[=4K6(46\b)0.s_\_itG.dG1_-e;I7/k&#-(-,r>P'utXr5.dJ^JlO4n-O(U
JfQELZ,+5McjK`hL)j\gC8)^^B=6JHHK,f3QTFcUN,_+[46*0:MSKGkHC0h^($W5Sn#&TT(B
26ms`e)3:-kaOpK!Sa5+<>$n8jC2=>s&h69G:Yn'O7Q@%@8T7/FLLgYsaY*WLfYY]A;:!a5*X
/(2Mr.ula+<uNb3H<ZLij4Cl2`/CQL0ECp]AG=\'<7\bV*L^k'g=UrM!3CeDY;0@>R1Md<JS&
\,;mU]AS*uD(*cXkItC<#:\u#2IkS5UA1nBW;a#/WSj]A=9iJ_'o7g>4@%LG*qITV,TV`3>U\h
E.`AA\VHLs&^IjA'9@r-Y]AQW#>+Ap39-h9sP[neNqnKE2Qlh@uFj1YcC1GSnq06_8to&]Ags%
anW_1V7"2THg8,I)o5kK6g@tu4^#b=K]A3O!aI$&b^Uc2i%PKEc*.a.h.fR.R\+1[7#'H:)lF
qj&=qr>s/cWk32.jTPtfKj^+/pGAe#Pni&fbEtcnYfZ(V.2%b&uBJ/k8LDTh>&RfE^O9MAiU
T"O0)qM#]AVd>9(_j]A9/%A$,ZSJs*M[Thd*mC0?oRO:BqN''G/G.KN-<tgk+/]Ad0+aT^qNdH#
3dGK#m.`]A[N``DUj=k/<.$etB480aA4,[:CPCp4KD'S6@!lm;cUX*\IrN./bC`latU/1[2ni
f<02Z<9Kd'O,m8lj"Ss,9m\.Lp(9Y;bLZIg">0DuLRmhf&,"0A_sopChFTbd8B6+lBq^kZ9\
tgHQ1?A2"U,(4EIl?S_5(7=^4`C=.-V6jHo@10#NR'0-]A0>%Mj$q_!edkKcD8"XdisrQiM%T
lO2fK<$+979Bt#"!RKg77a>o^kLO:qrJc0(F,B"U7t))?J"+O'%B$:-ZF+HSr((,#`+&Nj`V
dm^$4Z8?k'uCn:2T!@S`4.:(T\@L@&ZjN>)JJnmuX==+dmjel[aYB>u241beS&]AN!Ms!1a,@
Hfqm1Nl5GSd".&EOc6f4bidqm)$lUtlTN-a[Pns%@oa`+[p%Yq&8c)2T!daJN^#kR]Apkgb:d
jc"on<WOFdsT_[!u9WKu^73(4Kh"D!R4^%HASN?WP)*$j?;M<q$"eLE$eD74l3<0JTGUnF/q
@)+gdb,p3nMWtS<o8Pir-k/2$8J^+"!ln:6"mLe[h%-_\5F6\P@f]AAM_H`$cK%t4dgG#ln-$
k39-5*(Sq1k+4_IsC@eTaMr%h!DT$!IA#F&-,Tm_<oY/2G'?f$R1u.]AEF=i.5#%lN&`/(o$n
Gi-:NPjd'l`oT0/i)2i4hu;WAZ7MM!BCD]A[5R8"e4d7hqaG&U/1E5+njN]And/ZVZFf$@dt34
F8:b/PTUAK4"E:?MMOG)M<t\-d_b6g#,CESjr;Worc%!mOLFqZNFIDS;G`UFjV@d/87<l`A.
(YUa)5oOJD)2*4#R72_*"Ea:*U[<UOoacD*0:-!&/j*+fY:KVZQufXS^+T#.V*_nk%kP%*#3
61DmG:KB<9E)Q[,;Tbb=tOD"Vuo:UFM@&iKWVO1Xcc@>/C]ALZQ0\aeK7fUi6C@-Qt?7he\6^
@YV[o%DX_#$KYVg*8CjYdbr-/mT#o+W@_(_6XUQ`c\f`jBHbQ1.#FPeT!G."`T(b+Q,V1%"Q
3&oUh7,j=Fri7LR:dA@Baj(&k.pPsA5!$G-%Xkshj]A)Al#Vm.\aah[/QmZi/732dqd!MWrOi
%,(ao>LpT(#k1.Vcda[=8EaG0<L+C/>5[<P+kJfJ+3*L=]AF<-l.LN@e0i^_/H*Eq]AUf]A";XK
`&j'ApIK2sn*)=tqXX/O8gc1\27lif[q-i2V>[JBGuYknfqsC5rgT)F5kc&quR+Y8':+&Zk&
rg^_U<?#^0`9#>KNUW"#sY1E48r.)hVg4)3Eh*:'T)o<NZ*Z=>GMp"a]A$).NriXG<980or1'
%H>eYR-\s?U.>oF1CM:kGpR6J<$1h_n<4ZQ3A2kAuZQUa_q:I*:?G^06BJ;r@e'S)4K&A`j6
.<n^.U9;)q]ANR"Wa]AqPQqHU]Ae=2i,[mO0]A]AR@31[-@PI-&oX##p`hgla5s+NUg$Dn/"P:eXl
JYQ]As;g&'%ZiRRY^'0H@bWRD9[Gc0C_WQ]A&np:@XL(CsWo<Hkn!TQDqN/rDIcs7R.V+*[)^&
o-P<l9b(-or#TJ]AE+T!dRU!EI!GD':5:"3oc#^JK*m<8F/.p4NIMF-UJ_2Fd#X3!=mDB=E)8
"\?9%1P:<,sq)_a\77^a'YBR\tK]AZDS:#'UKkauf325_U03<fp5"NU,PV^?E`M?PlkQjjm?T
hC]A7nJL1u)I,Ug0Ih`):fHDrrOuT6,42Rr1gOKPP$#g.QObI3.bbKO"uXj/+(4.YHVeEM<A9
6(0K]Aj+-J=9mm3ndFY;\.9b4K$YW3IV4!(<[L943oU@=[s]AOfZY)#Fd(^qp7HkG'5g77B=4@
@b0+%aH[Fgd_\S%772Db,c*)b0NFO)i;.=6T+g5]A`*r+S=F[5@]AYP))IE'8u']ApqsbP=7q-P
?h?S<515(;V'80D(&%pSObd^<YU,1."l#$+L=bi>*Q>FuGr0Up924V<L.>B66C@?R]A7W"''a
ac=+">!uW8]A!coBNUC(87AqoEI8p`5LdZ_I0/,uOR\/Y^Dd1*2)+GJC,QPBG7Ng=&q(i9s-@
d]An@h3St4M[#cQs#5,kYM;8MQ,Xa/)3Y9eL:G2H#7Z!*4%f2oI_QV`qj$Uq>m0?L62B,,A=u
Yr*Dc9Lqb$n9X9`fus448TpLXSHg]A%3Q~
]]></IM>
<ElementCaseMobileAttrProvider horizontal="1" vertical="0" zoom="true" refresh="false" isUseHTML="false" isMobileCanvasSize="false" appearRefresh="false" allowFullScreen="false"/>
</body>
</InnerWidget>
<BoundsAttr x="0" y="0" width="484" height="542"/>
</Widget>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.ui.container.WTitleLayout">
<WidgetName name="chart0"/>
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
<InnerWidget class="com.fr.form.ui.ChartEditor">
<WidgetName name="chart0"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<Margin top="0" left="0" bottom="0" right="0"/>
<Border>
<border style="1" color="-723724" borderRadius="0" type="1" borderStyle="0"/>
<WidgetTitle>
<O>
<![CDATA[=if(len($type)=0,\"  純收入\",\"  \"+$type)+\"的收益和損失\"]]></O>
<FRFont name=".SF NS Text" style="0" size="80" foreground="-12303292"/>
<Position pos="2"/>
<Background name="ColorBackground" color="-1"/>
</WidgetTitle>
<Background name="ColorBackground" color="-1"/>
<Alpha alpha="1.0"/>
</Border>
<Background name="ColorBackground" color="-1"/>
<LayoutAttr selectedIndex="0"/>
<ChangeAttr enable="false" changeType="button" timeInterval="5" buttonColor="-8421505" carouselColor="-8421505" showArrow="true">
<TextAttr>
<Attr alignText="0"/>
</TextAttr>
</ChangeAttr>
<Chart name="默认" chartClass="com.fr.plugin.chart.vanchart.VanChart">
<Chart class="com.fr.plugin.chart.vanchart.VanChart">
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-1118482"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<ChartAttr isJSDraw="true" isStyleGlobal="false"/>
<Title4VanChart>
<Title>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-6908266"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<O>
<![CDATA[新建图表标题]]></O>
<TextAttr>
<Attr alignText="0">
<FRFont name="SimSun" style="0" size="128" foreground="-13421773"/>
</Attr>
</TextAttr>
<TitleVisible value="false" position="0"/>
</Title>
<Attr4VanChart useHtml="false" floating="false" x="0.0" y="0.0" limitSize="false" maxHeight="15.0"/>
</Title4VanChart>
<Plot class="com.fr.plugin.chart.custom.VanChartCustomPlot">
<VanChartPlotVersion version="20170715"/>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<Attr isNullValueBreak="true" autoRefreshPerSecond="0" seriesDragEnable="false" plotStyle="0" combinedSize="50.0"/>
<newHotTooltipStyle>
<AttrContents>
<Attr showLine="false" position="1" isWhiteBackground="true" isShowMutiSeries="false" seriesLabel="${VALUE}"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##]]></Format>
<PercentFormat>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#0.##%]]></Format>
</PercentFormat>
</AttrContents>
</newHotTooltipStyle>
<ConditionCollection>
<DefaultAttr class="com.fr.chart.chartglyph.ConditionAttr">
<ConditionAttr name=""/>
</DefaultAttr>
</ConditionCollection>
<Legend4VanChart>
<Legend>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-3355444"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<Attr position="4" visible="true"/>
<FRFont name="Microsoft YaHei UI" style="0" size="80" foreground="-10066330"/>
</Legend>
<Attr4VanChart floating="false" x="0.0" y="0.0" limitSize="false" maxHeight="15.0" isHighlight="true"/>
</Legend4VanChart>
<DataSheet>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="1" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-16777216"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<Attr isVisible="false"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##]]></Format>
</DataSheet>
<DataProcessor class="com.fr.base.chart.chartdata.model.NormalDataModel"/>
<newPlotFillStyle>
<AttrFillStyle>
<AFStyle colorStyle="1"/>
<FillStyleName fillStyleName=""/>
<isCustomFillStyle isCustomFillStyle="true"/>
<ColorList>
<OColor colvalue="-11284046"/>
<OColor colvalue="-861324"/>
<OColor colvalue="-4363512"/>
<OColor colvalue="-16750485"/>
<OColor colvalue="-3658447"/>
<OColor colvalue="-10331231"/>
<OColor colvalue="-7763575"/>
<OColor colvalue="-6514688"/>
<OColor colvalue="-16744620"/>
<OColor colvalue="-6187579"/>
<OColor colvalue="-15714713"/>
<OColor colvalue="-945550"/>
<OColor colvalue="-4092928"/>
<OColor colvalue="-13224394"/>
<OColor colvalue="-12423245"/>
<OColor colvalue="-10043521"/>
<OColor colvalue="-406154"/>
<OColor colvalue="-13031292"/>
<OColor colvalue="-16732559"/>
<OColor colvalue="-7099690"/>
<OColor colvalue="-11991199"/>
<OColor colvalue="-331445"/>
<OColor colvalue="-6991099"/>
<OColor colvalue="-16686527"/>
<OColor colvalue="-9205567"/>
<OColor colvalue="-7397856"/>
<OColor colvalue="-406154"/>
<OColor colvalue="-2712831"/>
<OColor colvalue="-4737097"/>
<OColor colvalue="-11460720"/>
<OColor colvalue="-6696775"/>
<OColor colvalue="-3685632"/>
</ColorList>
</AttrFillStyle>
</newPlotFillStyle>
<VanChartPlotAttr isAxisRotation="false" categoryNum="1"/>
<VanChartRectanglePlotAttr vanChartPlotType="normal" isDefaultIntervalBackground="true"/>
<XAxisList>
<VanChartAxis class="com.fr.plugin.chart.attr.axis.VanChartAxis">
<Title>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-16777216"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<O>
<![CDATA[]]></O>
<TextAttr>
<Attr alignText="0">
<FRFont name="Verdana" style="0" size="88" foreground="-10066330"/>
</Attr>
</TextAttr>
<TitleVisible value="true" position="0"/>
</Title>
<newAxisAttr isShowAxisLabel="true"/>
<AxisLineStyle AxisStyle="1" MainGridStyle="1"/>
<newLineColor lineColor="-2236963"/>
<AxisPosition value="3"/>
<TickLine201106 type="2" secType="0"/>
<ArrowShow arrowShow="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="Microsoft YaHei UI" style="0" size="80" foreground="-10066330"/>
</Attr>
</TextAttr>
<AxisLabelCount value="=0"/>
<AxisRange/>
<AxisUnit201106 isCustomMainUnit="false" isCustomSecUnit="false" mainUnit="=0" secUnit="=0"/>
<ZoomAxisAttr isZoom="false"/>
<axisReversed axisReversed="false"/>
<VanChartAxisAttr mainTickLine="2" secTickLine="0" axisName="X軸" titleUseHtml="false" autoLabelGap="true" limitSize="false" maxHeight="15.0" commonValueFormat="true" isRotation="false"/>
<HtmlLabel customText="function(){ return this; }" useHtml="false" isCustomWidth="false" isCustomHeight="false" width="50" height="50"/>
<alertList/>
<customBackgroundList/>
</VanChartAxis>
</XAxisList>
<YAxisList>
<VanChartAxis class="com.fr.plugin.chart.attr.axis.VanChartValueAxis">
<Title>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-16777216"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<O>
<![CDATA[]]></O>
<TextAttr>
<Attr rotation="-90" alignText="0">
<FRFont name="Verdana" style="0" size="88" foreground="-10066330"/>
</Attr>
</TextAttr>
<TitleVisible value="true" position="0"/>
</Title>
<newAxisAttr isShowAxisLabel="true"/>
<AxisLineStyle AxisStyle="0" MainGridStyle="1"/>
<newLineColor mainGridColor="-1052689" lineColor="-5197648"/>
<AxisPosition value="2"/>
<TickLine201106 type="2" secType="0"/>
<ArrowShow arrowShow="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="Microsoft YaHei UI" style="0" size="80" foreground="-10066330"/>
</Attr>
</TextAttr>
<AxisLabelCount value="=0"/>
<AxisRange/>
<AxisUnit201106 isCustomMainUnit="false" isCustomSecUnit="false" mainUnit="=0" secUnit="=0"/>
<ZoomAxisAttr isZoom="false"/>
<axisReversed axisReversed="false"/>
<VanChartAxisAttr mainTickLine="0" secTickLine="0" axisName="Y軸" titleUseHtml="false" autoLabelGap="true" limitSize="false" maxHeight="15.0" commonValueFormat="true" isRotation="false"/>
<HtmlLabel customText="function(){ return this; }" useHtml="false" isCustomWidth="false" isCustomHeight="false" width="50" height="50"/>
<alertList/>
<customBackgroundList/>
<VanChartValueAxisAttr isLog="false" valueStyle="false" baseLog="=10"/>
<ds>
<RadarYAxisTableDefinition>
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<attr/>
</RadarYAxisTableDefinition>
</ds>
</VanChartAxis>
<VanChartAxis class="com.fr.plugin.chart.attr.axis.VanChartValueAxis">
<Title>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-16777216"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<O>
<![CDATA[]]></O>
<TextAttr>
<Attr rotation="-90" alignText="0">
<FRFont name="Verdana" style="0" size="88" foreground="-10066330"/>
</Attr>
</TextAttr>
<TitleVisible value="true" position="0"/>
</Title>
<newAxisAttr isShowAxisLabel="true"/>
<AxisLineStyle AxisStyle="0" MainGridStyle="1"/>
<newLineColor lineColor="-5197648"/>
<AxisPosition value="4"/>
<TickLine201106 type="2" secType="0"/>
<ArrowShow arrowShow="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="Microsoft YaHei UI" style="0" size="80" foreground="-10066330"/>
</Attr>
</TextAttr>
<AxisLabelCount value="=0"/>
<AxisRange/>
<AxisUnit201106 isCustomMainUnit="false" isCustomSecUnit="false" mainUnit="=0" secUnit="=0"/>
<ZoomAxisAttr isZoom="false"/>
<axisReversed axisReversed="false"/>
<VanChartAxisAttr mainTickLine="0" secTickLine="0" axisName="Y軸2" titleUseHtml="false" autoLabelGap="true" limitSize="false" maxHeight="15.0" commonValueFormat="true" isRotation="false"/>
<HtmlLabel customText="function(){ return this; }" useHtml="false" isCustomWidth="false" isCustomHeight="false" width="50" height="50"/>
<alertList/>
<customBackgroundList/>
<VanChartValueAxisAttr isLog="false" valueStyle="false" baseLog="=10"/>
<ds>
<RadarYAxisTableDefinition>
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<attr/>
</RadarYAxisTableDefinition>
</ds>
</VanChartAxis>
</YAxisList>
<stackAndAxisCondition>
<ConditionCollection>
<DefaultAttr class="com.fr.chart.chartglyph.ConditionAttr">
<ConditionAttr name=""/>
</DefaultAttr>
</ConditionCollection>
</stackAndAxisCondition>
<VanChartCustomPlotAttr customStyle="column_line"/>
<CustomPlotList>
<VanChartPlot class="com.fr.plugin.chart.column.VanChartColumnPlot">
<VanChartPlotVersion version="20170715"/>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<Attr isNullValueBreak="true" autoRefreshPerSecond="0" seriesDragEnable="false" plotStyle="4" combinedSize="50.0"/>
<newHotTooltipStyle>
<AttrContents>
<Attr showLine="false" position="1" isWhiteBackground="true" isShowMutiSeries="false" seriesLabel="${VALUE}"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##]]></Format>
<PercentFormat>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#0.##%]]></Format>
</PercentFormat>
</AttrContents>
</newHotTooltipStyle>
<ConditionCollection>
<DefaultAttr class="com.fr.chart.chartglyph.ConditionAttr">
<ConditionAttr name="">
<AttrList>
<Attr class="com.fr.plugin.chart.base.AttrTooltip">
<AttrTooltip>
<Attr enable="true" duration="4" followMouse="false" showMutiSeries="true" isCustom="false"/>
<TextAttr>
<Attr alignText="0"/>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="true"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipValueFormat">
<AttrTooltipValueFormat>
<Attr enable="true"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##]]></Format>
</AttrTooltipValueFormat>
</value>
<percent class="com.fr.plugin.chart.base.format.AttrTooltipPercentFormat">
<AttrTooltipPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##%]]></Format>
</AttrTooltipPercentFormat>
</percent>
<category class="com.fr.plugin.chart.base.format.AttrTooltipCategoryFormat">
<AttrToolTipCategoryFormat>
<Attr enable="true"/>
</AttrToolTipCategoryFormat>
</category>
<series class="com.fr.plugin.chart.base.format.AttrTooltipSeriesFormat">
<AttrTooltipSeriesFormat>
<Attr enable="true"/>
</AttrTooltipSeriesFormat>
</series>
<changedPercent class="com.fr.plugin.chart.base.format.AttrTooltipChangedPercentFormat">
<AttrTooltipChangedPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##%]]></Format>
</AttrTooltipChangedPercentFormat>
</changedPercent>
<changedValue class="com.fr.plugin.chart.base.format.AttrTooltipChangedValueFormat">
<AttrTooltipChangedValueFormat>
<Attr enable="false"/>
</AttrTooltipChangedValueFormat>
</changedValue>
<HtmlLabel customText="" useHtml="false" isCustomWidth="false" isCustomHeight="false" width="50" height="50"/>
</AttrToolTipContent>
<GI>
<AttrBackground>
<Background name="ColorBackground" color="-16777216"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="2"/>
<newColor borderColor="-16777216"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="0.5"/>
</AttrAlpha>
</GI>
</AttrTooltip>
</Attr>
<Attr class="com.fr.chart.base.AttrBorder">
<AttrBorder>
<Attr lineStyle="1" isRoundBorder="false" roundRadius="5"/>
<newColor borderColor="-1"/>
</AttrBorder>
</Attr>
<Attr class="com.fr.chart.base.AttrAlpha">
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</Attr>
<Attr class="com.fr.plugin.chart.base.VanChartAttrTrendLine">
<TrendLine>
<Attr trendLineName="" trendLineType="linear" prePeriod="0" afterPeriod="0"/>
<LineStyleInfo>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
<AttrColor>
<Attr/>
</AttrColor>
<AttrLineStyle>
<newAttr lineStyle="0"/>
</AttrLineStyle>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-16777216"/>
</AttrBorder>
</LineStyleInfo>
</TrendLine>
</Attr>
</AttrList>
</ConditionAttr>
</DefaultAttr>
</ConditionCollection>
<Legend4VanChart>
<Legend>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-3355444"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<Attr position="4" visible="true"/>
<FRFont name="Microsoft YaHei" style="0" size="88" foreground="-10066330"/>
</Legend>
<Attr4VanChart floating="false" x="0.0" y="0.0" limitSize="false" maxHeight="15.0" isHighlight="true"/>
</Legend4VanChart>
<DataSheet>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="1" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-16777216"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<Attr isVisible="false"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##]]></Format>
</DataSheet>
<DataProcessor class="com.fr.base.chart.chartdata.model.NormalDataModel"/>
<newPlotFillStyle>
<AttrFillStyle>
<AFStyle colorStyle="1"/>
<FillStyleName fillStyleName="新特性"/>
<isCustomFillStyle isCustomFillStyle="false"/>
<ColorList>
<OColor colvalue="-10243346"/>
<OColor colvalue="-8988015"/>
<OColor colvalue="-472193"/>
<OColor colvalue="-486008"/>
<OColor colvalue="-8595761"/>
<OColor colvalue="-7236949"/>
<OColor colvalue="-8873759"/>
<OColor colvalue="-1071514"/>
<OColor colvalue="-1188474"/>
<OColor colvalue="-6715442"/>
<OColor colvalue="-10243346"/>
<OColor colvalue="-8988015"/>
<OColor colvalue="-472193"/>
<OColor colvalue="-486008"/>
<OColor colvalue="-8595761"/>
<OColor colvalue="-7236949"/>
<OColor colvalue="-8873759"/>
<OColor colvalue="-1071514"/>
<OColor colvalue="-1188474"/>
<OColor colvalue="-6715442"/>
<OColor colvalue="-10243346"/>
<OColor colvalue="-8988015"/>
<OColor colvalue="-472193"/>
<OColor colvalue="-486008"/>
<OColor colvalue="-8595761"/>
<OColor colvalue="-7236949"/>
<OColor colvalue="-8873759"/>
<OColor colvalue="-1071514"/>
<OColor colvalue="-1188474"/>
<OColor colvalue="-6715442"/>
<OColor colvalue="-10243346"/>
<OColor colvalue="-8988015"/>
</ColorList>
</AttrFillStyle>
</newPlotFillStyle>
<VanChartPlotAttr isAxisRotation="false" categoryNum="1"/>
<VanChartRectanglePlotAttr vanChartPlotType="custom" isDefaultIntervalBackground="true"/>
<XAxisList>
<VanChartAxis class="com.fr.plugin.chart.attr.axis.VanChartAxis">
<Title>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-16777216"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<O>
<![CDATA[]]></O>
<TextAttr>
<Attr alignText="0">
<FRFont name="Verdana" style="0" size="88" foreground="-10066330"/>
</Attr>
</TextAttr>
<TitleVisible value="true" position="0"/>
</Title>
<newAxisAttr isShowAxisLabel="true"/>
<AxisLineStyle AxisStyle="1" MainGridStyle="1"/>
<newLineColor lineColor="-2236963"/>
<AxisPosition value="3"/>
<TickLine201106 type="2" secType="0"/>
<ArrowShow arrowShow="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="Microsoft YaHei UI" style="0" size="80" foreground="-10066330"/>
</Attr>
</TextAttr>
<AxisLabelCount value="=0"/>
<AxisRange/>
<AxisUnit201106 isCustomMainUnit="false" isCustomSecUnit="false" mainUnit="=0" secUnit="=0"/>
<ZoomAxisAttr isZoom="false"/>
<axisReversed axisReversed="false"/>
<VanChartAxisAttr mainTickLine="2" secTickLine="0" axisName="X軸" titleUseHtml="false" autoLabelGap="true" limitSize="false" maxHeight="15.0" commonValueFormat="true" isRotation="false"/>
<HtmlLabel customText="function(){ return this; }" useHtml="false" isCustomWidth="false" isCustomHeight="false" width="50" height="50"/>
<alertList/>
<customBackgroundList/>
</VanChartAxis>
</XAxisList>
<YAxisList>
<VanChartAxis class="com.fr.plugin.chart.attr.axis.VanChartValueAxis">
<Title>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-16777216"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<O>
<![CDATA[]]></O>
<TextAttr>
<Attr rotation="-90" alignText="0">
<FRFont name="Verdana" style="0" size="88" foreground="-10066330"/>
</Attr>
</TextAttr>
<TitleVisible value="true" position="0"/>
</Title>
<newAxisAttr isShowAxisLabel="true"/>
<AxisLineStyle AxisStyle="0" MainGridStyle="1"/>
<newLineColor mainGridColor="-1052689" lineColor="-5197648"/>
<AxisPosition value="2"/>
<TickLine201106 type="2" secType="0"/>
<ArrowShow arrowShow="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="Microsoft YaHei UI" style="0" size="80" foreground="-10066330"/>
</Attr>
</TextAttr>
<AxisLabelCount value="=0"/>
<AxisRange/>
<AxisUnit201106 isCustomMainUnit="false" isCustomSecUnit="false" mainUnit="=0" secUnit="=0"/>
<ZoomAxisAttr isZoom="false"/>
<axisReversed axisReversed="false"/>
<VanChartAxisAttr mainTickLine="0" secTickLine="0" axisName="Y軸" titleUseHtml="false" autoLabelGap="true" limitSize="false" maxHeight="15.0" commonValueFormat="true" isRotation="false"/>
<HtmlLabel customText="function(){ return this; }" useHtml="false" isCustomWidth="false" isCustomHeight="false" width="50" height="50"/>
<alertList/>
<customBackgroundList/>
<VanChartValueAxisAttr isLog="false" valueStyle="false" baseLog="=10"/>
<ds>
<RadarYAxisTableDefinition>
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<attr/>
</RadarYAxisTableDefinition>
</ds>
</VanChartAxis>
<VanChartAxis class="com.fr.plugin.chart.attr.axis.VanChartValueAxis">
<Title>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-16777216"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<O>
<![CDATA[]]></O>
<TextAttr>
<Attr rotation="-90" alignText="0">
<FRFont name="Verdana" style="0" size="88" foreground="-10066330"/>
</Attr>
</TextAttr>
<TitleVisible value="true" position="0"/>
</Title>
<newAxisAttr isShowAxisLabel="true"/>
<AxisLineStyle AxisStyle="0" MainGridStyle="1"/>
<newLineColor lineColor="-5197648"/>
<AxisPosition value="4"/>
<TickLine201106 type="2" secType="0"/>
<ArrowShow arrowShow="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="Microsoft YaHei UI" style="0" size="80" foreground="-10066330"/>
</Attr>
</TextAttr>
<AxisLabelCount value="=0"/>
<AxisRange/>
<AxisUnit201106 isCustomMainUnit="false" isCustomSecUnit="false" mainUnit="=0" secUnit="=0"/>
<ZoomAxisAttr isZoom="false"/>
<axisReversed axisReversed="false"/>
<VanChartAxisAttr mainTickLine="0" secTickLine="0" axisName="Y軸2" titleUseHtml="false" autoLabelGap="true" limitSize="false" maxHeight="15.0" commonValueFormat="true" isRotation="false"/>
<HtmlLabel customText="function(){ return this; }" useHtml="false" isCustomWidth="false" isCustomHeight="false" width="50" height="50"/>
<alertList/>
<customBackgroundList/>
<VanChartValueAxisAttr isLog="false" valueStyle="false" baseLog="=10"/>
<ds>
<RadarYAxisTableDefinition>
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<attr/>
</RadarYAxisTableDefinition>
</ds>
</VanChartAxis>
</YAxisList>
<stackAndAxisCondition>
<ConditionCollection>
<DefaultAttr class="com.fr.chart.chartglyph.ConditionAttr">
<ConditionAttr name=""/>
</DefaultAttr>
<ConditionAttrList>
<List index="0">
<ConditionAttr name="堆积和坐标轴1">
<AttrList>
<Attr class="com.fr.plugin.chart.base.AttrSeriesStackAndAxis">
<AttrSeriesStackAndAxis>
<Attr xAxisIndex="0" yAxisIndex="0" stacked="false" percentStacked="false" stackID="堆积和坐标轴1"/>
</AttrSeriesStackAndAxis>
</Attr>
</AttrList>
<Condition class="com.fr.data.condition.ListCondition"/>
</ConditionAttr>
</List>
</ConditionAttrList>
</ConditionCollection>
</stackAndAxisCondition>
<VanChartColumnPlotAttr seriesOverlapPercent="20.0" categoryIntervalPercent="20.0" fixedWidth="true" columnWidth="40" filledWithImage="false" isBar="false"/>
</VanChartPlot>
<VanChartPlot class="com.fr.plugin.chart.line.VanChartLinePlot">
<VanChartPlotVersion version="20170715"/>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<Attr isNullValueBreak="true" autoRefreshPerSecond="0" seriesDragEnable="false" plotStyle="4" combinedSize="50.0"/>
<newHotTooltipStyle>
<AttrContents>
<Attr showLine="false" position="1" isWhiteBackground="true" isShowMutiSeries="false" seriesLabel="${VALUE}"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##]]></Format>
<PercentFormat>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#0.##%]]></Format>
</PercentFormat>
</AttrContents>
</newHotTooltipStyle>
<ConditionCollection>
<DefaultAttr class="com.fr.chart.chartglyph.ConditionAttr">
<ConditionAttr name="">
<AttrList>
<Attr class="com.fr.plugin.chart.base.AttrTooltip">
<AttrTooltip>
<Attr enable="true" duration="4" followMouse="false" showMutiSeries="true" isCustom="false"/>
<TextAttr>
<Attr alignText="0"/>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="true"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipValueFormat">
<AttrTooltipValueFormat>
<Attr enable="true"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##]]></Format>
</AttrTooltipValueFormat>
</value>
<percent class="com.fr.plugin.chart.base.format.AttrTooltipPercentFormat">
<AttrTooltipPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##%]]></Format>
</AttrTooltipPercentFormat>
</percent>
<category class="com.fr.plugin.chart.base.format.AttrTooltipCategoryFormat">
<AttrToolTipCategoryFormat>
<Attr enable="true"/>
</AttrToolTipCategoryFormat>
</category>
<series class="com.fr.plugin.chart.base.format.AttrTooltipSeriesFormat">
<AttrTooltipSeriesFormat>
<Attr enable="true"/>
</AttrTooltipSeriesFormat>
</series>
<changedPercent class="com.fr.plugin.chart.base.format.AttrTooltipChangedPercentFormat">
<AttrTooltipChangedPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##%]]></Format>
</AttrTooltipChangedPercentFormat>
</changedPercent>
<changedValue class="com.fr.plugin.chart.base.format.AttrTooltipChangedValueFormat">
<AttrTooltipChangedValueFormat>
<Attr enable="false"/>
</AttrTooltipChangedValueFormat>
</changedValue>
<HtmlLabel customText="" useHtml="false" isCustomWidth="false" isCustomHeight="false" width="50" height="50"/>
</AttrToolTipContent>
<GI>
<AttrBackground>
<Background name="ColorBackground" color="-16777216"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="2"/>
<newColor borderColor="-16777216"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="0.5"/>
</AttrAlpha>
</GI>
</AttrTooltip>
</Attr>
<Attr class="com.fr.plugin.chart.base.VanChartAttrTrendLine">
<TrendLine>
<Attr trendLineName="" trendLineType="linear" prePeriod="0" afterPeriod="0"/>
<LineStyleInfo>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
<AttrColor>
<Attr/>
</AttrColor>
<AttrLineStyle>
<newAttr lineStyle="0"/>
</AttrLineStyle>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-16777216"/>
</AttrBorder>
</LineStyleInfo>
</TrendLine>
</Attr>
<Attr class="com.fr.plugin.chart.base.VanChartAttrLine">
<VanAttrLine>
<Attr lineWidth="2" lineStyle="0" nullValueBreak="true"/>
</VanAttrLine>
</Attr>
<Attr class="com.fr.plugin.chart.base.VanChartAttrMarker">
<VanAttrMarker>
<Attr isCommon="true" markerType="RoundFilledMarker" radius="4.5" width="30.0" height="30.0"/>
<Background name="NullBackground"/>
</VanAttrMarker>
</Attr>
</AttrList>
</ConditionAttr>
</DefaultAttr>
</ConditionCollection>
<Legend4VanChart>
<Legend>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-3355444"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<Attr position="4" visible="true"/>
<FRFont name="Microsoft YaHei" style="0" size="88" foreground="-10066330"/>
</Legend>
<Attr4VanChart floating="false" x="0.0" y="0.0" limitSize="false" maxHeight="15.0" isHighlight="true"/>
</Legend4VanChart>
<DataSheet>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="1" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-16777216"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<Attr isVisible="false"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##]]></Format>
</DataSheet>
<DataProcessor class="com.fr.base.chart.chartdata.model.NormalDataModel"/>
<newPlotFillStyle>
<AttrFillStyle>
<AFStyle colorStyle="1"/>
<FillStyleName fillStyleName="新特性"/>
<isCustomFillStyle isCustomFillStyle="false"/>
<ColorList>
<OColor colvalue="-10243346"/>
<OColor colvalue="-8988015"/>
<OColor colvalue="-472193"/>
<OColor colvalue="-486008"/>
<OColor colvalue="-8595761"/>
<OColor colvalue="-7236949"/>
<OColor colvalue="-8873759"/>
<OColor colvalue="-1071514"/>
<OColor colvalue="-1188474"/>
<OColor colvalue="-6715442"/>
<OColor colvalue="-10243346"/>
<OColor colvalue="-8988015"/>
<OColor colvalue="-472193"/>
<OColor colvalue="-486008"/>
<OColor colvalue="-8595761"/>
<OColor colvalue="-7236949"/>
<OColor colvalue="-8873759"/>
<OColor colvalue="-1071514"/>
<OColor colvalue="-1188474"/>
<OColor colvalue="-6715442"/>
<OColor colvalue="-10243346"/>
<OColor colvalue="-8988015"/>
<OColor colvalue="-472193"/>
<OColor colvalue="-486008"/>
<OColor colvalue="-8595761"/>
<OColor colvalue="-7236949"/>
<OColor colvalue="-8873759"/>
<OColor colvalue="-1071514"/>
<OColor colvalue="-1188474"/>
<OColor colvalue="-6715442"/>
<OColor colvalue="-10243346"/>
<OColor colvalue="-8988015"/>
</ColorList>
</AttrFillStyle>
</newPlotFillStyle>
<VanChartPlotAttr isAxisRotation="false" categoryNum="1"/>
<VanChartRectanglePlotAttr vanChartPlotType="custom" isDefaultIntervalBackground="true"/>
<XAxisList>
<VanChartAxis class="com.fr.plugin.chart.attr.axis.VanChartAxis">
<Title>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-16777216"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<O>
<![CDATA[]]></O>
<TextAttr>
<Attr alignText="0">
<FRFont name="Verdana" style="0" size="88" foreground="-10066330"/>
</Attr>
</TextAttr>
<TitleVisible value="true" position="0"/>
</Title>
<newAxisAttr isShowAxisLabel="true"/>
<AxisLineStyle AxisStyle="1" MainGridStyle="1"/>
<newLineColor lineColor="-2236963"/>
<AxisPosition value="3"/>
<TickLine201106 type="2" secType="0"/>
<ArrowShow arrowShow="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="Microsoft YaHei UI" style="0" size="80" foreground="-10066330"/>
</Attr>
</TextAttr>
<AxisLabelCount value="=0"/>
<AxisRange/>
<AxisUnit201106 isCustomMainUnit="false" isCustomSecUnit="false" mainUnit="=0" secUnit="=0"/>
<ZoomAxisAttr isZoom="false"/>
<axisReversed axisReversed="false"/>
<VanChartAxisAttr mainTickLine="2" secTickLine="0" axisName="X軸" titleUseHtml="false" autoLabelGap="true" limitSize="false" maxHeight="15.0" commonValueFormat="true" isRotation="false"/>
<HtmlLabel customText="function(){ return this; }" useHtml="false" isCustomWidth="false" isCustomHeight="false" width="50" height="50"/>
<alertList/>
<customBackgroundList/>
</VanChartAxis>
</XAxisList>
<YAxisList>
<VanChartAxis class="com.fr.plugin.chart.attr.axis.VanChartValueAxis">
<Title>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-16777216"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<O>
<![CDATA[]]></O>
<TextAttr>
<Attr rotation="-90" alignText="0">
<FRFont name="Verdana" style="0" size="88" foreground="-10066330"/>
</Attr>
</TextAttr>
<TitleVisible value="true" position="0"/>
</Title>
<newAxisAttr isShowAxisLabel="true"/>
<AxisLineStyle AxisStyle="0" MainGridStyle="1"/>
<newLineColor mainGridColor="-1052689" lineColor="-5197648"/>
<AxisPosition value="2"/>
<TickLine201106 type="2" secType="0"/>
<ArrowShow arrowShow="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="Microsoft YaHei UI" style="0" size="80" foreground="-10066330"/>
</Attr>
</TextAttr>
<AxisLabelCount value="=0"/>
<AxisRange/>
<AxisUnit201106 isCustomMainUnit="false" isCustomSecUnit="false" mainUnit="=0" secUnit="=0"/>
<ZoomAxisAttr isZoom="false"/>
<axisReversed axisReversed="false"/>
<VanChartAxisAttr mainTickLine="0" secTickLine="0" axisName="Y軸" titleUseHtml="false" autoLabelGap="true" limitSize="false" maxHeight="15.0" commonValueFormat="true" isRotation="false"/>
<HtmlLabel customText="function(){ return this; }" useHtml="false" isCustomWidth="false" isCustomHeight="false" width="50" height="50"/>
<alertList/>
<customBackgroundList/>
<VanChartValueAxisAttr isLog="false" valueStyle="false" baseLog="=10"/>
<ds>
<RadarYAxisTableDefinition>
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<attr/>
</RadarYAxisTableDefinition>
</ds>
</VanChartAxis>
<VanChartAxis class="com.fr.plugin.chart.attr.axis.VanChartValueAxis">
<Title>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-16777216"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<O>
<![CDATA[]]></O>
<TextAttr>
<Attr rotation="-90" alignText="0">
<FRFont name="Verdana" style="0" size="88" foreground="-10066330"/>
</Attr>
</TextAttr>
<TitleVisible value="true" position="0"/>
</Title>
<newAxisAttr isShowAxisLabel="true"/>
<AxisLineStyle AxisStyle="0" MainGridStyle="1"/>
<newLineColor lineColor="-5197648"/>
<AxisPosition value="4"/>
<TickLine201106 type="2" secType="0"/>
<ArrowShow arrowShow="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="Microsoft YaHei UI" style="0" size="80" foreground="-10066330"/>
</Attr>
</TextAttr>
<AxisLabelCount value="=0"/>
<AxisRange/>
<AxisUnit201106 isCustomMainUnit="false" isCustomSecUnit="false" mainUnit="=0" secUnit="=0"/>
<ZoomAxisAttr isZoom="false"/>
<axisReversed axisReversed="false"/>
<VanChartAxisAttr mainTickLine="0" secTickLine="0" axisName="Y軸2" titleUseHtml="false" autoLabelGap="true" limitSize="false" maxHeight="15.0" commonValueFormat="true" isRotation="false"/>
<HtmlLabel customText="function(){ return this; }" useHtml="false" isCustomWidth="false" isCustomHeight="false" width="50" height="50"/>
<alertList/>
<customBackgroundList/>
<VanChartValueAxisAttr isLog="false" valueStyle="false" baseLog="=10"/>
<ds>
<RadarYAxisTableDefinition>
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<attr/>
</RadarYAxisTableDefinition>
</ds>
</VanChartAxis>
</YAxisList>
<stackAndAxisCondition>
<ConditionCollection>
<DefaultAttr class="com.fr.chart.chartglyph.ConditionAttr">
<ConditionAttr name=""/>
</DefaultAttr>
<ConditionAttrList>
<List index="0">
<ConditionAttr name="堆积和坐标轴1">
<AttrList>
<Attr class="com.fr.plugin.chart.base.AttrSeriesStackAndAxis">
<AttrSeriesStackAndAxis>
<Attr xAxisIndex="0" yAxisIndex="1" stacked="false" percentStacked="false" stackID="堆积和坐标轴1"/>
</AttrSeriesStackAndAxis>
</Attr>
</AttrList>
<Condition class="com.fr.data.condition.ListCondition"/>
</ConditionAttr>
</List>
</ConditionAttrList>
</ConditionCollection>
</stackAndAxisCondition>
</VanChartPlot>
</CustomPlotList>
</Plot>
<ChartDefinition>
<CustomDefinition>
<DefinitionMapList>
<DefinitionMap key="column">
<OneValueCDDefinition seriesName="cate" valueName="sum" function="com.fr.data.util.function.SumFunction">
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<TableData class="com.fr.data.impl.NameTableData">
<Name>
<![CDATA[ds3]]></Name>
</TableData>
<CategoryName value="season"/>
</OneValueCDDefinition>
</DefinitionMap>
<DefinitionMap key="line">
<OneValueCDDefinition seriesName="cate" valueName="sum" function="com.fr.data.util.function.SumFunction">
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<TableData class="com.fr.data.impl.NameTableData">
<Name>
<![CDATA[ds4]]></Name>
</TableData>
<CategoryName value="season"/>
</OneValueCDDefinition>
</DefinitionMap>
</DefinitionMapList>
</CustomDefinition>
</ChartDefinition>
</Chart>
<tools hidden="true" sort="false" export="false" fullScreen="false"/>
<VanChartZoom>
<zoomAttr zoomVisible="false" zoomGesture="true" zoomResize="true" zoomType="xy"/>
<from>
<![CDATA[]]></from>
<to>
<![CDATA[]]></to>
</VanChartZoom>
<refreshMoreLabel>
<attr moreLabel="true" autoTooltip="true"/>
<AttrTooltip>
<Attr enable="true" duration="4" followMouse="false" showMutiSeries="false" isCustom="false"/>
<TextAttr>
<Attr alignText="0"/>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="true"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipValueFormat">
<AttrTooltipValueFormat>
<Attr enable="false"/>
</AttrTooltipValueFormat>
</value>
<percent class="com.fr.plugin.chart.base.format.AttrTooltipPercentFormat">
<AttrTooltipPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##%]]></Format>
</AttrTooltipPercentFormat>
</percent>
<category class="com.fr.plugin.chart.base.format.AttrTooltipCategoryFormat">
<AttrToolTipCategoryFormat>
<Attr enable="false"/>
</AttrToolTipCategoryFormat>
</category>
<series class="com.fr.plugin.chart.base.format.AttrTooltipSeriesFormat">
<AttrTooltipSeriesFormat>
<Attr enable="false"/>
</AttrTooltipSeriesFormat>
</series>
<changedPercent class="com.fr.plugin.chart.base.format.AttrTooltipChangedPercentFormat">
<AttrTooltipChangedPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##%]]></Format>
</AttrTooltipChangedPercentFormat>
</changedPercent>
<changedValue class="com.fr.plugin.chart.base.format.AttrTooltipChangedValueFormat">
<AttrTooltipChangedValueFormat>
<Attr enable="true"/>
</AttrTooltipChangedValueFormat>
</changedValue>
<HtmlLabel customText="" useHtml="false" isCustomWidth="false" isCustomHeight="false" width="50" height="50"/>
</AttrToolTipContent>
<GI>
<AttrBackground>
<Background name="ColorBackground" color="-1"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="1" isRoundBorder="false" roundRadius="4"/>
<newColor borderColor="-15395563"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="0.8"/>
</AttrAlpha>
</GI>
</AttrTooltip>
</refreshMoreLabel>
</Chart>
<ChartMobileAttrProvider zoomOut="0" zoomIn="2" allowFullScreen="true"/>
</InnerWidget>
<BoundsAttr x="484" y="36" width="479" height="199"/>
</Widget>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.ui.Label">
<WidgetName name="Title_chart0"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<widgetValue>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=if(len($type)=0,"  純收入","  "+$type)+"的收益和損失"]]></Attributes>
</O>
</widgetValue>
<LabelAttr verticalcenter="true" textalign="2" autoline="true"/>
<FRFont name=".SF NS Text" style="0" size="80" foreground="-12303292"/>
<Background name="ColorBackground" color="-1"/>
<border style="1" color="-723724"/>
</InnerWidget>
<BoundsAttr x="0" y="0" width="479" height="36"/>
</Widget>
<title class="com.fr.form.ui.Label">
<WidgetName name="Title_chart0"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<widgetValue>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=if(len($type)=0,"  纯收入",$type)+"的收益和损失"]]></Attributes>
</O>
</widgetValue>
<LabelAttr verticalcenter="true" textalign="2" autoline="true"/>
<FRFont name="微软雅黑" style="0" size="80" foreground="-12303292"/>
<Background name="ColorBackground" color="-1"/>
<border style="1" color="-723724"/>
</title>
<body class="com.fr.form.ui.ChartEditor">
<WidgetName name="chart0"/>
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
<LayoutAttr selectedIndex="0"/>
<ChangeAttr enable="false" changeType="button" timeInterval="5" buttonColor="-8421505" carouselColor="-8421505" showArrow="true">
<TextAttr>
<Attr alignText="0"/>
</TextAttr>
</ChangeAttr>
<Chart name="默认" chartClass="com.fr.chart.chartattr.Chart">
<Chart class="com.fr.chart.chartattr.Chart">
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-6908266"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<ChartAttr isJSDraw="true" isStyleGlobal="false"/>
<Title>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-6908266"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<O>
<![CDATA[新建图表标题]]></O>
<TextAttr>
<Attr alignText="0">
<FRFont name="Microsoft YaHei" style="0" size="88"/>
</Attr>
</TextAttr>
<TitleVisible value="true" position="0"/>
</Title>
<Plot class="com.fr.chart.chartattr.PiePlot">
<Plot>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<Attr isNullValueBreak="true" autoRefreshPerSecond="0" seriesDragEnable="true" plotStyle="0" combinedSize="50.0"/>
<newHotTooltipStyle>
<AttrContents>
<Attr showLine="false" position="1" isWhiteBackground="true" isShowMutiSeries="false" seriesLabel="${VALUE}${PERCENT}"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##]]></Format>
<PercentFormat>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##%]]></Format>
</PercentFormat>
</AttrContents>
</newHotTooltipStyle>
<ConditionCollection>
<DefaultAttr class="com.fr.chart.chartglyph.ConditionAttr">
<ConditionAttr name="">
<AttrList>
<Attr class="com.fr.chart.base.AttrBorder">
<AttrBorder>
<Attr lineStyle="1" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-1"/>
</AttrBorder>
</Attr>
</AttrList>
</ConditionAttr>
</DefaultAttr>
</ConditionCollection>
<Legend>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-6908266"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<Attr position="4" visible="true"/>
<FRFont name="Microsoft YaHei" style="0" size="72"/>
</Legend>
<DataSheet>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="1" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-16777216"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<Attr isVisible="false"/>
</DataSheet>
<DataProcessor class="com.fr.base.chart.chartdata.model.NormalDataModel"/>
<newPlotFillStyle>
<AttrFillStyle>
<AFStyle colorStyle="0"/>
<FillStyleName fillStyleName=""/>
<isCustomFillStyle isCustomFillStyle="false"/>
</AttrFillStyle>
</newPlotFillStyle>
<PieAttr subType="1" smallPercent="0.05"/>
</Plot>
</Plot>
<ChartDefinition>
<OneValueCDDefinition seriesName="country" valueName="sum" function="com.fr.data.util.function.SumFunction">
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<TableData class="com.fr.data.impl.NameTableData">
<Name>
<![CDATA[ds2]]></Name>
</TableData>
<CategoryName value=""/>
</OneValueCDDefinition>
</ChartDefinition>
</Chart>
</Chart>
<ChartMobileAttrProvider zoomOut="0" zoomIn="2" allowFullScreen="true"/>
</body>
</InnerWidget>
<BoundsAttr x="484" y="0" width="479" height="271"/>
</Widget>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.ui.container.WTitleLayout">
<WidgetName name="chart1"/>
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
<InnerWidget class="com.fr.form.ui.ChartEditor">
<WidgetName name="chart1"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<Margin top="0" left="0" bottom="0" right="0"/>
<Border>
<border style="1" color="-723724" borderRadius="0" type="1" borderStyle="0"/>
<WidgetTitle>
<O>
<![CDATA[=if(len($type)=0,\"  純收入\",\"  \"+$type)+\"的百分比\"]]></O>
<FRFont name=".SF NS Text" style="0" size="80" foreground="-12303292"/>
<Position pos="2"/>
<Background name="ColorBackground" color="-1"/>
</WidgetTitle>
<Background name="ColorBackground" color="-1"/>
<Alpha alpha="1.0"/>
</Border>
<Background name="ColorBackground" color="-1"/>
<LayoutAttr selectedIndex="0"/>
<ChangeAttr enable="false" changeType="button" timeInterval="5" buttonColor="-8421505" carouselColor="-8421505" showArrow="true">
<TextAttr>
<Attr alignText="0"/>
</TextAttr>
</ChangeAttr>
<Chart name="默认" chartClass="com.fr.plugin.chart.vanchart.VanChart">
<Chart class="com.fr.plugin.chart.vanchart.VanChart">
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-1118482"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<ChartAttr isJSDraw="true" isStyleGlobal="false"/>
<Title4VanChart>
<Title>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-6908266"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=if(len($type)=0,"纯收入",$type)+"的百分比"]]></Attributes>
</O>
<TextAttr>
<Attr alignText="0">
<FRFont name="微软雅黑" style="0" size="80" foreground="-12303292"/>
</Attr>
</TextAttr>
<TitleVisible value="false" position="2"/>
</Title>
<Attr4VanChart useHtml="false" floating="false" x="0.0" y="0.0" limitSize="false" maxHeight="15.0"/>
</Title4VanChart>
<Plot class="com.fr.plugin.chart.gauge.VanChartGaugePlot">
<VanChartPlotVersion version="20170715"/>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<Attr isNullValueBreak="true" autoRefreshPerSecond="0" seriesDragEnable="false" plotStyle="0" combinedSize="50.0"/>
<newHotTooltipStyle>
<AttrContents>
<Attr showLine="false" position="1" isWhiteBackground="true" isShowMutiSeries="false" seriesLabel="${VALUE}"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##]]></Format>
<PercentFormat>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#0.##%]]></Format>
</PercentFormat>
</AttrContents>
</newHotTooltipStyle>
<ConditionCollection>
<DefaultAttr class="com.fr.chart.chartglyph.ConditionAttr">
<ConditionAttr name="">
<AttrList>
<Attr class="com.fr.plugin.chart.base.AttrTooltip">
<AttrTooltip>
<Attr enable="false" duration="4" followMouse="false" showMutiSeries="true" isCustom="false"/>
<TextAttr>
<Attr alignText="0"/>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="true"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipValueFormat">
<AttrTooltipValueFormat>
<Attr enable="true"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##]]></Format>
</AttrTooltipValueFormat>
</value>
<percent class="com.fr.plugin.chart.base.format.AttrTooltipPercentFormat">
<AttrTooltipPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##%]]></Format>
</AttrTooltipPercentFormat>
</percent>
<category class="com.fr.plugin.chart.base.format.AttrTooltipCategoryFormat">
<AttrToolTipCategoryFormat>
<Attr enable="true"/>
</AttrToolTipCategoryFormat>
</category>
<series class="com.fr.plugin.chart.base.format.AttrTooltipSeriesFormat">
<AttrTooltipSeriesFormat>
<Attr enable="false"/>
</AttrTooltipSeriesFormat>
</series>
<changedPercent class="com.fr.plugin.chart.base.format.AttrTooltipChangedPercentFormat">
<AttrTooltipChangedPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##%]]></Format>
</AttrTooltipChangedPercentFormat>
</changedPercent>
<changedValue class="com.fr.plugin.chart.base.format.AttrTooltipChangedValueFormat">
<AttrTooltipChangedValueFormat>
<Attr enable="false"/>
</AttrTooltipChangedValueFormat>
</changedValue>
<HtmlLabel customText="" useHtml="false" isCustomWidth="false" isCustomHeight="false" width="50" height="50"/>
</AttrToolTipContent>
<GI>
<AttrBackground>
<Background name="ColorBackground" color="-16777216"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="2"/>
<newColor borderColor="-16777216"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="0.5"/>
</AttrAlpha>
</GI>
</AttrTooltip>
</Attr>
<Attr class="com.fr.plugin.chart.base.AttrLabel">
<AttrLabel>
<labelAttr enable="true"/>
<labelDetail class="com.fr.plugin.chart.base.AttrLabelDetail">
<Attr showLine="false" autoAdjust="false" position="5" isCustom="true"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="Microsoft YaHei" style="1" size="144" foreground="-342221"/>
</Attr>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="true"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipValueFormat">
<AttrTooltipValueFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##]]></Format>
</AttrTooltipValueFormat>
</value>
<percent class="com.fr.plugin.chart.base.format.AttrTooltipPercentFormat">
<AttrTooltipPercentFormat>
<Attr enable="true"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##%]]></Format>
</AttrTooltipPercentFormat>
</percent>
<category class="com.fr.plugin.chart.base.format.AttrTooltipCategoryFormat">
<AttrToolTipCategoryFormat>
<Attr enable="false"/>
</AttrToolTipCategoryFormat>
</category>
<series class="com.fr.plugin.chart.base.format.AttrTooltipSeriesFormat">
<AttrTooltipSeriesFormat>
<Attr enable="false"/>
</AttrTooltipSeriesFormat>
</series>
<changedPercent class="com.fr.plugin.chart.base.format.AttrTooltipChangedPercentFormat">
<AttrTooltipChangedPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##%]]></Format>
</AttrTooltipChangedPercentFormat>
</changedPercent>
<changedValue class="com.fr.plugin.chart.base.format.AttrTooltipChangedValueFormat">
<AttrTooltipChangedValueFormat>
<Attr enable="false"/>
</AttrTooltipChangedValueFormat>
</changedValue>
<HtmlLabel customText="function(){ return this.percentage;}" useHtml="false" isCustomWidth="false" isCustomHeight="false" width="50" height="50"/>
</AttrToolTipContent>
</labelDetail>
<gaugeValueLabel class="com.fr.plugin.chart.base.AttrLabelDetail">
<Attr showLine="false" autoAdjust="false" position="5" isCustom="true"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="Microsoft YaHei" style="0" size="80" foreground="-4210753"/>
</Attr>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="true"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipValueFormat">
<AttrTooltipValueFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##]]></Format>
</AttrTooltipValueFormat>
</value>
<percent class="com.fr.plugin.chart.base.format.AttrTooltipPercentFormat">
<AttrTooltipPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##%]]></Format>
</AttrTooltipPercentFormat>
</percent>
<category class="com.fr.plugin.chart.base.format.AttrTooltipCategoryFormat">
<AttrToolTipCategoryFormat>
<Attr enable="true"/>
</AttrToolTipCategoryFormat>
</category>
<series class="com.fr.plugin.chart.base.format.AttrTooltipSeriesFormat">
<AttrTooltipSeriesFormat>
<Attr enable="false"/>
</AttrTooltipSeriesFormat>
</series>
<changedPercent class="com.fr.plugin.chart.base.format.AttrTooltipChangedPercentFormat">
<AttrTooltipChangedPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##%]]></Format>
</AttrTooltipChangedPercentFormat>
</changedPercent>
<changedValue class="com.fr.plugin.chart.base.format.AttrTooltipChangedValueFormat">
<AttrTooltipChangedValueFormat>
<Attr enable="false"/>
</AttrTooltipChangedValueFormat>
</changedValue>
<HtmlLabel customText="" useHtml="false" isCustomWidth="false" isCustomHeight="false" width="50" height="50"/>
</AttrToolTipContent>
</gaugeValueLabel>
</AttrLabel>
</Attr>
</AttrList>
</ConditionAttr>
</DefaultAttr>
</ConditionCollection>
<DataSheet>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="1" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-16777216"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<Attr isVisible="false"/>
</DataSheet>
<DataProcessor class="com.fr.base.chart.chartdata.model.NormalDataModel"/>
<newPlotFillStyle>
<AttrFillStyle>
<AFStyle colorStyle="1"/>
<FillStyleName fillStyleName=""/>
<isCustomFillStyle isCustomFillStyle="true"/>
<ColorList>
<OColor colvalue="-342221"/>
<OColor colvalue="-11184811"/>
<OColor colvalue="-342221"/>
<OColor colvalue="-16750485"/>
<OColor colvalue="-3658447"/>
<OColor colvalue="-10331231"/>
<OColor colvalue="-7763575"/>
<OColor colvalue="-6514688"/>
<OColor colvalue="-16744620"/>
<OColor colvalue="-6187579"/>
<OColor colvalue="-15714713"/>
<OColor colvalue="-945550"/>
<OColor colvalue="-4092928"/>
<OColor colvalue="-13224394"/>
<OColor colvalue="-12423245"/>
<OColor colvalue="-10043521"/>
<OColor colvalue="-406154"/>
<OColor colvalue="-13031292"/>
<OColor colvalue="-16732559"/>
<OColor colvalue="-7099690"/>
<OColor colvalue="-11991199"/>
<OColor colvalue="-331445"/>
<OColor colvalue="-6991099"/>
<OColor colvalue="-16686527"/>
<OColor colvalue="-9205567"/>
<OColor colvalue="-7397856"/>
<OColor colvalue="-406154"/>
<OColor colvalue="-2712831"/>
<OColor colvalue="-4737097"/>
<OColor colvalue="-11460720"/>
<OColor colvalue="-6696775"/>
<OColor colvalue="-3685632"/>
</ColorList>
</AttrFillStyle>
</newPlotFillStyle>
<VanChartPlotAttr isAxisRotation="false" categoryNum="1"/>
<VanChartGaugePlotAttr gaugeStyle="slot"/>
<GaugeDetailStyle>
<GaugeDetailStyleAttr horizontalLayout="true" needleColor="-1" slotBackgroundColor="-1118482" antiClockWise="true"/>
<MapHotAreaColor>
<MC_Attr minValue="0.0" maxValue="100.0" useType="0" areaNumber="5" mainColor="-14374913"/>
<ColorList>
<AreaColor>
<AC_Attr minValue="=80.0" maxValue="=100.0" color="-14374913"/>
</AreaColor>
<AreaColor>
<AC_Attr minValue="=60.0" maxValue="=80.0" color="-11486721"/>
</AreaColor>
<AreaColor>
<AC_Attr minValue="=40.0" maxValue="=60.0" color="-8598785"/>
</AreaColor>
<AreaColor>
<AC_Attr minValue="=20.0" maxValue="=40.0" color="-5776129"/>
</AreaColor>
<AreaColor>
<AC_Attr minValue="=0.0" maxValue="=20.0" color="-2888193"/>
</AreaColor>
</ColorList>
</MapHotAreaColor>
</GaugeDetailStyle>
<gaugeAxis>
<Title>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-16777216"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<O>
<![CDATA[]]></O>
<TextAttr>
<Attr rotation="-90" alignText="0">
<FRFont name="verdana" style="0" size="88" foreground="-10066330"/>
</Attr>
</TextAttr>
<TitleVisible value="true" position="0"/>
</Title>
<newAxisAttr isShowAxisLabel="true"/>
<AxisLineStyle AxisStyle="1" MainGridStyle="1"/>
<newLineColor lineColor="-5197648"/>
<AxisPosition value="3"/>
<TickLine201106 type="2" secType="0"/>
<ArrowShow arrowShow="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="Verdana" style="0" size="64" foreground="-10066330"/>
</Attr>
</TextAttr>
<AxisLabelCount value="=0"/>
<AxisRange/>
<AxisUnit201106 isCustomMainUnit="false" isCustomSecUnit="false" mainUnit="=0" secUnit="=0"/>
<ZoomAxisAttr isZoom="false"/>
<axisReversed axisReversed="false"/>
<VanChartAxisAttr mainTickLine="2" secTickLine="0" axisName="X軸" titleUseHtml="false" autoLabelGap="true" limitSize="false" maxHeight="15.0" commonValueFormat="true" isRotation="false"/>
<HtmlLabel customText="function(){ return this; }" useHtml="false" isCustomWidth="false" isCustomHeight="false" width="50" height="50"/>
<alertList/>
<customBackgroundList/>
<VanChartValueAxisAttr isLog="false" valueStyle="false" baseLog="=10"/>
<ds>
<RadarYAxisTableDefinition>
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<attr/>
</RadarYAxisTableDefinition>
</ds>
<VanChartGaugeAxisAttr mainTickColor="-4539718" secTickColor="-1907998"/>
</gaugeAxis>
<VanChartRadius radiusType="auto" radius="100"/>
</Plot>
<ChartDefinition>
<MeterTableDefinition>
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<TableData class="com.fr.data.impl.NameTableData">
<Name>
<![CDATA[ds2]]></Name>
</TableData>
<MeterTable201109 meterType="1" name="type" value="百分比"/>
</MeterTableDefinition>
</ChartDefinition>
</Chart>
<tools hidden="true" sort="false" export="false" fullScreen="false"/>
<VanChartZoom>
<zoomAttr zoomVisible="false" zoomGesture="true" zoomResize="true" zoomType="xy"/>
<from>
<![CDATA[]]></from>
<to>
<![CDATA[]]></to>
</VanChartZoom>
<refreshMoreLabel>
<attr moreLabel="true" autoTooltip="true"/>
<AttrTooltip>
<Attr enable="true" duration="4" followMouse="false" showMutiSeries="false" isCustom="false"/>
<TextAttr>
<Attr alignText="0"/>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="true"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipValueFormat">
<AttrTooltipValueFormat>
<Attr enable="false"/>
</AttrTooltipValueFormat>
</value>
<percent class="com.fr.plugin.chart.base.format.AttrTooltipPercentFormat">
<AttrTooltipPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##%]]></Format>
</AttrTooltipPercentFormat>
</percent>
<category class="com.fr.plugin.chart.base.format.AttrTooltipCategoryFormat">
<AttrToolTipCategoryFormat>
<Attr enable="false"/>
</AttrToolTipCategoryFormat>
</category>
<series class="com.fr.plugin.chart.base.format.AttrTooltipSeriesFormat">
<AttrTooltipSeriesFormat>
<Attr enable="false"/>
</AttrTooltipSeriesFormat>
</series>
<changedPercent class="com.fr.plugin.chart.base.format.AttrTooltipChangedPercentFormat">
<AttrTooltipChangedPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##%]]></Format>
</AttrTooltipChangedPercentFormat>
</changedPercent>
<changedValue class="com.fr.plugin.chart.base.format.AttrTooltipChangedValueFormat">
<AttrTooltipChangedValueFormat>
<Attr enable="true"/>
</AttrTooltipChangedValueFormat>
</changedValue>
<HtmlLabel customText="" useHtml="false" isCustomWidth="false" isCustomHeight="false" width="50" height="50"/>
</AttrToolTipContent>
<GI>
<AttrBackground>
<Background name="ColorBackground" color="-1"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="1" isRoundBorder="false" roundRadius="4"/>
<newColor borderColor="-15395563"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="0.8"/>
</AttrAlpha>
</GI>
</AttrTooltip>
</refreshMoreLabel>
</Chart>
<ChartMobileAttrProvider zoomOut="0" zoomIn="2" allowFullScreen="true"/>
</InnerWidget>
<BoundsAttr x="484" y="36" width="479" height="199"/>
</Widget>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.ui.Label">
<WidgetName name="Title_chart1"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<widgetValue>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=if(len($type)=0,"  純收入","  "+$type)+"的百分比"]]></Attributes>
</O>
</widgetValue>
<LabelAttr verticalcenter="true" textalign="2" autoline="true"/>
<FRFont name=".SF NS Text" style="0" size="80" foreground="-12303292"/>
<Background name="ColorBackground" color="-1"/>
<border style="1" color="-723724"/>
</InnerWidget>
<BoundsAttr x="0" y="0" width="479" height="36"/>
</Widget>
<title class="com.fr.form.ui.Label">
<WidgetName name="Title_chart1"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<widgetValue>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=if(len($type)=0,"  纯收入",$type)+"的百分比"]]></Attributes>
</O>
</widgetValue>
<LabelAttr verticalcenter="true" textalign="2" autoline="true"/>
<FRFont name="微软雅黑" style="0" size="80" foreground="-12303292"/>
<Background name="ColorBackground" color="-1"/>
<border style="1" color="-723724"/>
</title>
<body class="com.fr.form.ui.ChartEditor">
<WidgetName name="chart1"/>
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
<LayoutAttr selectedIndex="0"/>
<ChangeAttr enable="false" changeType="button" timeInterval="5" buttonColor="-8421505" carouselColor="-8421505" showArrow="true">
<TextAttr>
<Attr alignText="0"/>
</TextAttr>
</ChangeAttr>
<Chart name="默认" chartClass="com.fr.chart.chartattr.Chart">
<Chart class="com.fr.chart.chartattr.Chart">
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-6908266"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<ChartAttr isJSDraw="true" isStyleGlobal="false"/>
<Title>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-6908266"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<O>
<![CDATA[新建图表标题]]></O>
<TextAttr>
<Attr alignText="0">
<FRFont name="Microsoft YaHei" style="0" size="88"/>
</Attr>
</TextAttr>
<TitleVisible value="true" position="0"/>
</Title>
<Plot class="com.fr.chart.chartattr.Bar2DPlot">
<CategoryPlot>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<Attr isNullValueBreak="true" autoRefreshPerSecond="0" seriesDragEnable="true" plotStyle="0" combinedSize="50.0"/>
<newHotTooltipStyle>
<AttrContents>
<Attr showLine="false" position="1" isWhiteBackground="true" isShowMutiSeries="false" seriesLabel="${VALUE}"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#.##]]></Format>
<PercentFormat>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#0.##%]]></Format>
</PercentFormat>
</AttrContents>
</newHotTooltipStyle>
<ConditionCollection>
<DefaultAttr class="com.fr.chart.chartglyph.ConditionAttr">
<ConditionAttr name=""/>
</DefaultAttr>
</ConditionCollection>
<Legend>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-6908266"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<Attr position="4" visible="true"/>
<FRFont name="Microsoft YaHei" style="0" size="72"/>
</Legend>
<DataSheet>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="1" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-16777216"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<Attr isVisible="false"/>
</DataSheet>
<DataProcessor class="com.fr.base.chart.chartdata.model.NormalDataModel"/>
<newPlotFillStyle>
<AttrFillStyle>
<AFStyle colorStyle="0"/>
<FillStyleName fillStyleName=""/>
<isCustomFillStyle isCustomFillStyle="false"/>
</AttrFillStyle>
</newPlotFillStyle>
<RectanglePlotAttr interactiveAxisTooltip="false"/>
<xAxis>
<CategoryAxis class="com.fr.chart.chartattr.CategoryAxis">
<newAxisAttr isShowAxisLabel="true"/>
<AxisLineStyle AxisStyle="1" MainGridStyle="0"/>
<newLineColor mainGridColor="-4144960" lineColor="-5197648"/>
<AxisPosition value="3"/>
<TickLine201106 type="2" secType="0"/>
<ArrowShow arrowShow="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="Microsoft YaHei" style="0" size="72"/>
</Attr>
</TextAttr>
<AxisLabelCount value="=0"/>
<AxisRange/>
<AxisUnit201106 isCustomMainUnit="false" isCustomSecUnit="false" mainUnit="=0" secUnit="=0"/>
<ZoomAxisAttr isZoom="false"/>
<axisReversed axisReversed="false"/>
</CategoryAxis>
</xAxis>
<yAxis>
<ValueAxis class="com.fr.chart.chartattr.ValueAxis">
<ValueAxisAttr201108 alignZeroValue="false"/>
<newAxisAttr isShowAxisLabel="true"/>
<AxisLineStyle AxisStyle="1" MainGridStyle="1"/>
<newLineColor mainGridColor="-4144960" lineColor="-5197648"/>
<AxisPosition value="2"/>
<TickLine201106 type="2" secType="0"/>
<ArrowShow arrowShow="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="Century Gothic" style="0" size="72"/>
</Attr>
</TextAttr>
<AxisLabelCount value="=0"/>
<AxisRange/>
<AxisUnit201106 isCustomMainUnit="false" isCustomSecUnit="false" mainUnit="=0" secUnit="=0"/>
<ZoomAxisAttr isZoom="false"/>
<axisReversed axisReversed="false"/>
</ValueAxis>
</yAxis>
<secondAxis>
<ValueAxis class="com.fr.chart.chartattr.ValueAxis">
<ValueAxisAttr201108 alignZeroValue="false"/>
<newAxisAttr isShowAxisLabel="true"/>
<AxisLineStyle AxisStyle="1" MainGridStyle="1"/>
<newLineColor mainGridColor="-4144960" lineColor="-5197648"/>
<AxisPosition value="4"/>
<TickLine201106 type="2" secType="0"/>
<ArrowShow arrowShow="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="Century Gothic" style="0" size="72"/>
</Attr>
</TextAttr>
<AxisLabelCount value="=0"/>
<AxisRange/>
<AxisUnit201106 isCustomMainUnit="false" isCustomSecUnit="false" mainUnit="=0" secUnit="=0"/>
<ZoomAxisAttr isZoom="false"/>
<axisReversed axisReversed="false"/>
</ValueAxis>
</secondAxis>
<CateAttr isStacked="false"/>
<BarAttr isHorizontal="false" overlap="-0.25" interval="1.0"/>
<Bar2DAttr isSimulation3D="false"/>
</CategoryPlot>
</Plot>
</Chart>
</Chart>
<ChartMobileAttrProvider zoomOut="0" zoomIn="2" allowFullScreen="true"/>
</body>
</InnerWidget>
<BoundsAttr x="484" y="271" width="479" height="271"/>
</Widget>
<Sorted sorted="false"/>
<MobileWidgetList>
<Widget widgetName="report0"/>
<Widget widgetName="chart0"/>
<Widget widgetName="chart1"/>
</MobileWidgetList>
<WidgetZoomAttr compState="0"/>
<AppRelayout appRelayout="true"/>
<Size width="963" height="542"/>
<ResolutionScalingAttr percent="1.0"/>
<BodyLayoutType type="0"/>
</Center>
</Layout>
<DesignerVersion DesignerVersion="KAA"/>
<PreviewType PreviewType="0"/>
<TemplateIdAttMark class="com.fr.base.iofile.attr.TemplateIdAttrMark">
<TemplateIdAttMark TemplateId="8c94cc27-9b32-4070-ba1d-f81e3faab992"/>
</TemplateIdAttMark>
</Form>
