<?xml version="1.0" encoding="UTF-8"?>
<Form xmlVersion="20170720" releaseVersion="10.0.0">
<TableDataMap>
<TableData name="ds3" class="com.fr.data.impl.DBTableData">
<Parameters>
<Parameter>
<Attributes name="province"/>
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
<![CDATA[SELECT * FROM 地圖1 where 1=1 ${if(len(province) = 0||province=='中國'," order by 銷售額 desc","and pid='"+province+"'")} ]]></Query>
<PageQuery>
<![CDATA[]]></PageQuery>
</TableData>
<TableData name="ds4" class="com.fr.data.impl.DBTableData">
<Parameters/>
<Attributes maxMemRowCount="-1"/>
<Connection class="com.fr.data.impl.NameDatabaseConnection">
<DatabaseName>
<![CDATA[FRDemoTW]]></DatabaseName>
</Connection>
<Query>
<![CDATA[SELECT * FROM 地圖1]]></Query>
<PageQuery>
<![CDATA[]]></PageQuery>
</TableData>
</TableDataMap>
<FormMobileAttr>
<FormMobileAttr refresh="false" isUseHTML="false" isMobileOnly="false" isAdaptivePropertyAutoMatch="false" appearRefresh="false" promptWhenLeaveWithoutSubmit="false" allowDoubleClickOrZoom="true"/>
</FormMobileAttr>
<Parameters/>
<Layout class="com.fr.form.ui.container.WBorderLayout">
<WidgetName name="form"/>
<WidgetAttr aspectRatioLocked="false" aspectRatioBackup="0.0" description="">
<MobileBookMark useBookMark="false" bookMarkName="" frozen="false"/>
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
<ShowBookmarks showBookmarks="false"/>
<Center class="com.fr.form.ui.container.WFitLayout">
<WidgetName name="body"/>
<WidgetAttr aspectRatioLocked="false" aspectRatioBackup="0.0" description="">
<MobileBookMark useBookMark="false" bookMarkName="" frozen="false"/>
<PrivilegeControl/>
</WidgetAttr>
<Margin top="5" left="8" bottom="1" right="8"/>
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
<LCAttr vgap="0" hgap="0" compInterval="5"/>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.ui.container.WTitleLayout">
<WidgetName name="report0"/>
<WidgetAttr aspectRatioLocked="false" aspectRatioBackup="0.0" description="">
<MobileBookMark useBookMark="false" bookMarkName="report0" frozen="false"/>
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
<WidgetAttr aspectRatioLocked="false" aspectRatioBackup="0.0" description="">
<MobileBookMark useBookMark="false" bookMarkName="" frozen="false"/>
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
<![CDATA[0,1409700,1028700,936000,533400,723900,723900,1790700,723900,723900,914400,1066800,723900,190500,1408320,1104900,892800,838200,838200,723900]]></RowHeight>
<ColumnWidth defaultValue="2743200">
<![CDATA[2743200,2743200,2743200,2743200,2743200,0,2743200,2743200,2743200,2743200]]></ColumnWidth>
<CellElementList>
<C c="0" r="0">
<PrivilegeControl/>
<Expand/>
</C>
<C c="0" r="1" cs="5" s="0">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[="  " + if(len($province) = 0 || $province = "中國", "全國資料", $province + "資料")]]></Attributes>
</O>
<PrivilegeControl/>
<CellGUIAttr adjustmode="0"/>
<CellPageAttr/>
<Expand/>
</C>
<C c="0" r="2" s="1">
<O>
<![CDATA[地名]]></O>
<PrivilegeControl/>
<CellGUIAttr adjustmode="0"/>
<CellPageAttr/>
<Expand/>
</C>
<C c="1" r="2" s="2">
<O>
<![CDATA[銷售額]]></O>
<PrivilegeControl/>
<CellGUIAttr adjustmode="0"/>
<CellPageAttr/>
<Expand/>
</C>
<C c="2" r="2" s="2">
<O>
<![CDATA[利潤額]]></O>
<PrivilegeControl/>
<CellGUIAttr adjustmode="0"/>
<CellPageAttr/>
<Expand/>
</C>
<C c="3" r="2" s="2">
<O>
<![CDATA[運營費用]]></O>
<PrivilegeControl/>
<CellGUIAttr adjustmode="0"/>
<CellPageAttr/>
<Expand/>
</C>
<C c="4" r="2" s="3">
<O>
<![CDATA[稅費]]></O>
<PrivilegeControl/>
<CellGUIAttr adjustmode="0"/>
<CellPageAttr/>
<Expand/>
</C>
<C c="0" r="3" s="4">
<O t="DSColumn">
<Attributes dsName="ds4" columnName="省份"/>
<Condition class="com.fr.data.condition.CommonCondition">
<CNAME>
<![CDATA[省份]]></CNAME>
<Compare op="0">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=if(len($province) = 0 || $province = "中國", nofilter, $province)]]></Attributes>
</O>
</Compare>
</Condition>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Result>
<![CDATA[$$$]]></Result>
<Parameters/>
</O>
<PrivilegeControl/>
<CellGUIAttr adjustmode="0"/>
<CellPageAttr/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[条件属性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($province) = 0 || $province = "中國"]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.ValueHighlightAction">
<O>
<![CDATA[全國]]></O>
</HighlightAction>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="1" r="3" s="5">
<O t="DSColumn">
<Attributes dsName="ds4" columnName="銷售額"/>
<Condition class="com.fr.data.condition.CommonCondition">
<CNAME>
<![CDATA[省份]]></CNAME>
<Compare op="0">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=if(len($province) = 0 || $province = "中國", nofilter, $province)]]></Attributes>
</O>
</Compare>
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
<CellGUIAttr adjustmode="0"/>
<CellPageAttr/>
<Expand/>
</C>
<C c="2" r="3" s="5">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=B4 - D4 - E4]]></Attributes>
</O>
<PrivilegeControl/>
<CellGUIAttr adjustmode="0"/>
<CellPageAttr/>
<Expand leftParentDefault="false" left="B4"/>
</C>
<C c="3" r="3" s="5">
<O t="DSColumn">
<Attributes dsName="ds4" columnName="運營費用"/>
<Condition class="com.fr.data.condition.ListCondition"/>
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
<CellGUIAttr adjustmode="0"/>
<CellPageAttr/>
<Expand leftParentDefault="false" left="B4"/>
</C>
<C c="4" r="3" s="6">
<O t="DSColumn">
<Attributes dsName="ds4" columnName="稅費"/>
<Condition class="com.fr.data.condition.ListCondition"/>
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
<CellGUIAttr adjustmode="0"/>
<CellPageAttr/>
<Expand leftParentDefault="false" left="B4"/>
</C>
<C c="0" r="4" cs="5" s="7">
<PrivilegeControl/>
<Expand/>
</C>
<C c="0" r="5" cs="5" rs="8" s="8">
<O t="CC">
<LayoutAttr selectedIndex="0"/>
<ChangeAttr enable="true" changeType="carousel" timeInterval="5" buttonColor="-8421505" carouselColor="-8421505" showArrow="true">
<TextAttr>
<Attr alignText="0" predefinedStyle="false">
<FRFont name="SimSun" style="0" size="72"/>
</Attr>
</TextAttr>
</ChangeAttr>
<Chart name="默认" chartClass="com.fr.plugin.chart.vanchart.VanChart">
<Chart class="com.fr.plugin.chart.vanchart.VanChart">
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr gradientType="normal" gradientStartColor="-12146441" gradientEndColor="-9378161" shadow="false" autoBackground="false" predefinedStyle="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-1118482" autoColor="false" predefinedStyle="false"/>
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
<Attr gradientType="normal" gradientStartColor="-12146441" gradientEndColor="-9378161" shadow="false" autoBackground="false" predefinedStyle="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-6908266" autoColor="false" predefinedStyle="false"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<O>
<![CDATA[新建图表标题]]></O>
<TextAttr>
<Attr alignText="0" predefinedStyle="false">
<FRFont name="SimSun" style="0" size="128" foreground="-13421773"/>
</Attr>
</TextAttr>
<TitleVisible value="false" position="0"/>
</Title>
<Attr4VanChart useHtml="false" floating="false" x="0.0" y="0.0" limitSize="false" maxHeight="15.0"/>
</Title4VanChart>
<Plot class="com.fr.plugin.chart.column.VanChartColumnPlot">
<VanChartPlotVersion version="20170715"/>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr gradientType="normal" gradientStartColor="-12146441" gradientEndColor="-9378161" shadow="false" autoBackground="false" predefinedStyle="false"/>
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
<Format class="com.fr.base.CoreDecimalFormat" roundingMode="6">
<![CDATA[#.##]]></Format>
<PercentFormat>
<Format class="com.fr.base.CoreDecimalFormat" roundingMode="6">
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
<Attr enable="true" duration="4" followMouse="false" showMutiSeries="false" isCustom="false"/>
<TextAttr>
<Attr alignText="0" predefinedStyle="false">
<FRFont name="Microsoft JhengHei" style="0" size="72"/>
</Attr>
</TextAttr>
<AttrToolTipContent>
<TextAttr>
<Attr alignText="0" predefinedStyle="false">
<FRFont name="Microsoft JhengHei" style="0" size="72"/>
</Attr>
</TextAttr>
<richText class="com.fr.plugin.chart.base.AttrTooltipRichText">
<AttrTooltipRichText>
<Attr content="" isAuto="true" initParamsContent=""/>
<params>
<![CDATA[{}]]></params>
</AttrTooltipRichText>
</richText>
<richTextValue class="com.fr.plugin.chart.base.format.AttrTooltipValueFormat">
<AttrTooltipValueFormat>
<Attr enable="true"/>
</AttrTooltipValueFormat>
</richTextValue>
<richTextPercent class="com.fr.plugin.chart.base.format.AttrTooltipPercentFormat">
<AttrTooltipPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat" roundingMode="6">
<![CDATA[#.##%]]></Format>
</AttrTooltipPercentFormat>
</richTextPercent>
<richTextCategory class="com.fr.plugin.chart.base.format.AttrTooltipCategoryFormat">
<AttrToolTipCategoryFormat>
<Attr enable="true"/>
</AttrToolTipCategoryFormat>
</richTextCategory>
<richTextSeries class="com.fr.plugin.chart.base.format.AttrTooltipSeriesFormat">
<AttrTooltipSeriesFormat>
<Attr enable="true"/>
</AttrTooltipSeriesFormat>
</richTextSeries>
<richTextChangedPercent class="com.fr.plugin.chart.base.format.AttrTooltipChangedPercentFormat">
<AttrTooltipChangedPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat" roundingMode="6">
<![CDATA[#.##%]]></Format>
</AttrTooltipChangedPercentFormat>
</richTextChangedPercent>
<richTextChangedValue class="com.fr.plugin.chart.base.format.AttrTooltipChangedValueFormat">
<AttrTooltipChangedValueFormat>
<Attr enable="false"/>
</AttrTooltipChangedValueFormat>
</richTextChangedValue>
<TableFieldCollection/>
<Attr isCommon="true" isCustom="false" isRichText="false" richTextAlign="left" showAllSeries="false"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipValueFormat">
<AttrTooltipValueFormat>
<Attr enable="true"/>
</AttrTooltipValueFormat>
</value>
<percent class="com.fr.plugin.chart.base.format.AttrTooltipPercentFormat">
<AttrTooltipPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat" roundingMode="6">
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
<Format class="com.fr.base.CoreDecimalFormat" roundingMode="6">
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
<Attr gradientType="normal" gradientStartColor="-12146441" gradientEndColor="-9378161" shadow="true" autoBackground="false" predefinedStyle="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="2"/>
<newColor borderColor="-16777216" autoColor="false" predefinedStyle="false"/>
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
<newColor borderColor="-1" autoColor="false" predefinedStyle="false"/>
</AttrBorder>
</Attr>
<Attr class="com.fr.chart.base.AttrAlpha">
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
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
<Attr gradientType="normal" gradientStartColor="-12146441" gradientEndColor="-9378161" shadow="false" autoBackground="false" predefinedStyle="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-3355444" autoColor="false" predefinedStyle="false"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<Attr position="4" visible="true" predefinedStyle="false"/>
<FRFont name="Microsoft YaHei UI" style="0" size="64" foreground="-10066330"/>
</Legend>
<Attr4VanChart floating="false" x="0.0" y="0.0" layout="aligned" customSize="true" maxHeight="100.0" isHighlight="true"/>
</Legend4VanChart>
<DataSheet>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr gradientType="normal" gradientStartColor="-12146441" gradientEndColor="-9378161" shadow="false" autoBackground="false" predefinedStyle="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="1" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-16777216" autoColor="false" predefinedStyle="false"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<Attr isVisible="false" predefinedStyle="false"/>
<FRFont name="Microsoft JhengHei" style="0" size="72"/>
<Format class="com.fr.base.CoreDecimalFormat" roundingMode="6">
<![CDATA[#.##]]></Format>
</DataSheet>
<DataProcessor class="com.fr.base.chart.chartdata.model.NormalDataModel"/>
<newPlotFillStyle>
<AttrFillStyle>
<AFStyle colorStyle="1"/>
<FillStyleName fillStyleName=""/>
<isCustomFillStyle isCustomFillStyle="true"/>
<PredefinedStyle predefinedStyle="false"/>
<ColorList>
<OColor colvalue="-12276512"/>
<OColor colvalue="-12203043"/>
<OColor colvalue="-10760542"/>
<OColor colvalue="-1059000"/>
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
<GradientStyle>
<Attr gradientType="normal" startColor="-12146441" endColor="-9378161"/>
</GradientStyle>
<VanChartRectanglePlotAttr vanChartPlotType="normal" isDefaultIntervalBackground="true"/>
<XAxisList>
<VanChartAxis class="com.fr.plugin.chart.attr.axis.VanChartAxis">
<Title>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr gradientType="normal" gradientStartColor="-12146441" gradientEndColor="-9378161" shadow="false" autoBackground="false" predefinedStyle="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-16777216" autoColor="false" predefinedStyle="false"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<O>
<![CDATA[]]></O>
<TextAttr>
<Attr alignText="0" predefinedStyle="false">
<FRFont name="Verdana" style="0" size="88" foreground="-10066330"/>
</Attr>
</TextAttr>
<TitleVisible value="true" position="0"/>
</Title>
<newAxisAttr isShowAxisLabel="true"/>
<AxisLineStyle AxisStyle="1" MainGridStyle="1"/>
<newLineColor mainGridPredefinedStyle="false" lineColor="-5197648" predefinedStyle="false"/>
<AxisPosition value="3"/>
<TickLine201106 type="2" secType="0"/>
<ArrowShow arrowShow="false"/>
<TextAttr>
<Attr alignText="0" predefinedStyle="false">
<FRFont name="Microsoft YaHei UI" style="0" size="64" foreground="-10066330"/>
</Attr>
</TextAttr>
<AxisLabelCount value="=1"/>
<AxisRange/>
<AxisUnit201106 isCustomMainUnit="false" isCustomSecUnit="false" mainUnit="=0" secUnit="=0"/>
<ZoomAxisAttr isZoom="false"/>
<axisReversed axisReversed="false"/>
<VanChartAxisAttr mainTickLine="0" secTickLine="0" axisName="X軸" titleUseHtml="false" labelDisplay="interval" autoLabelGap="true" limitSize="false" maxHeight="15.0" commonValueFormat="true" isRotation="false" isShowAxisTitle="true" gridLineType="solid"/>
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
<Attr gradientType="normal" gradientStartColor="-12146441" gradientEndColor="-9378161" shadow="false" autoBackground="false" predefinedStyle="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-16777216" autoColor="false" predefinedStyle="false"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<O>
<![CDATA[]]></O>
<TextAttr>
<Attr rotation="-90" alignText="0" predefinedStyle="false">
<FRFont name="Verdana" style="0" size="88" foreground="-10066330"/>
</Attr>
</TextAttr>
<TitleVisible value="true" position="0"/>
</Title>
<newAxisAttr isShowAxisLabel="true"/>
<AxisLineStyle AxisStyle="0" MainGridStyle="1"/>
<newLineColor mainGridColor="-1118482" mainGridPredefinedStyle="false" lineColor="-5197648" predefinedStyle="false"/>
<AxisPosition value="2"/>
<TickLine201106 type="2" secType="0"/>
<ArrowShow arrowShow="false"/>
<TextAttr>
<Attr alignText="0" predefinedStyle="false">
<FRFont name="Verdana" style="0" size="64" foreground="-10066330"/>
</Attr>
</TextAttr>
<AxisLabelCount value="=1"/>
<AxisRange/>
<AxisUnit201106 isCustomMainUnit="false" isCustomSecUnit="false" mainUnit="=0" secUnit="=0"/>
<ZoomAxisAttr isZoom="false"/>
<axisReversed axisReversed="false"/>
<VanChartAxisAttr mainTickLine="0" secTickLine="0" axisName="Y軸" titleUseHtml="false" labelDisplay="interval" autoLabelGap="true" limitSize="false" maxHeight="15.0" commonValueFormat="true" isRotation="false" isShowAxisTitle="true" gridLineType="solid"/>
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
<VanChartColumnPlotAttr seriesOverlapPercent="20.0" categoryIntervalPercent="20.0" fixedWidth="true" columnWidth="25" filledWithImage="false" isBar="false"/>
</Plot>
<ChartDefinition>
<NormalReportDataDefinition>
<Series>
<SeriesDefinition>
<SeriesName>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=[B3:E3]A]]></Attributes>
</O>
</SeriesName>
<SeriesValue>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=[B4:E4]A]]></Attributes>
</O>
</SeriesValue>
</SeriesDefinition>
</Series>
<Category>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=A4]]></Attributes>
</O>
</Category>
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
</NormalReportDataDefinition>
</ChartDefinition>
</Chart>
<UUID uuid="4f25bff3-a2ee-412d-ab56-0904309752f9"/>
<tools hidden="true" sort="true" export="true" fullScreen="true"/>
<VanChartZoom>
<zoomAttr zoomVisible="false" zoomGesture="true" zoomResize="true" zoomType="xy" controlType="zoom" categoryNum="8" scaling="0.3"/>
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
<Attr alignText="0" predefinedStyle="false">
<FRFont name="Microsoft JhengHei" style="0" size="72"/>
</Attr>
</TextAttr>
<AttrToolTipContent>
<TextAttr>
<Attr alignText="0" predefinedStyle="false">
<FRFont name="Microsoft JhengHei" style="0" size="72"/>
</Attr>
</TextAttr>
<richText class="com.fr.plugin.chart.base.AttrTooltipRichText">
<AttrTooltipRichText>
<Attr content="" isAuto="true" initParamsContent=""/>
<params>
<![CDATA[{}]]></params>
</AttrTooltipRichText>
</richText>
<richTextValue class="com.fr.plugin.chart.base.format.AttrTooltipValueFormat">
<AttrTooltipValueFormat>
<Attr enable="true"/>
</AttrTooltipValueFormat>
</richTextValue>
<richTextPercent class="com.fr.plugin.chart.base.format.AttrTooltipPercentFormat">
<AttrTooltipPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat" roundingMode="6">
<![CDATA[#.##%]]></Format>
</AttrTooltipPercentFormat>
</richTextPercent>
<richTextCategory class="com.fr.plugin.chart.base.format.AttrTooltipCategoryFormat">
<AttrToolTipCategoryFormat>
<Attr enable="false"/>
</AttrToolTipCategoryFormat>
</richTextCategory>
<richTextSeries class="com.fr.plugin.chart.base.format.AttrTooltipSeriesFormat">
<AttrTooltipSeriesFormat>
<Attr enable="false"/>
</AttrTooltipSeriesFormat>
</richTextSeries>
<richTextChangedPercent class="com.fr.plugin.chart.base.format.AttrTooltipChangedPercentFormat">
<AttrTooltipChangedPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat" roundingMode="6">
<![CDATA[#.##%]]></Format>
</AttrTooltipChangedPercentFormat>
</richTextChangedPercent>
<richTextChangedValue class="com.fr.plugin.chart.base.format.AttrTooltipChangedValueFormat">
<AttrTooltipChangedValueFormat>
<Attr enable="false"/>
</AttrTooltipChangedValueFormat>
</richTextChangedValue>
<TableFieldCollection/>
<Attr isCommon="true" isCustom="false" isRichText="false" richTextAlign="left" showAllSeries="false"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipValueFormat">
<AttrTooltipValueFormat>
<Attr enable="false"/>
</AttrTooltipValueFormat>
</value>
<percent class="com.fr.plugin.chart.base.format.AttrTooltipPercentFormat">
<AttrTooltipPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat" roundingMode="6">
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
<Format class="com.fr.base.CoreDecimalFormat" roundingMode="6">
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
<Attr gradientType="normal" gradientStartColor="-12146441" gradientEndColor="-9378161" shadow="false" autoBackground="false" predefinedStyle="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="1" isRoundBorder="false" roundRadius="4"/>
<newColor borderColor="-15395563" autoColor="false" predefinedStyle="false"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="0.8"/>
</AttrAlpha>
</GI>
</AttrTooltip>
</refreshMoreLabel>
<ThemeAttr>
<Attr darkTheme="false" predefinedStyle="false"/>
</ThemeAttr>
</Chart>
<Chart name="图表2" chartClass="com.fr.plugin.chart.vanchart.VanChart">
<Chart class="com.fr.plugin.chart.vanchart.VanChart">
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr gradientType="normal" gradientStartColor="-12146441" gradientEndColor="-9378161" shadow="false" autoBackground="false" predefinedStyle="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-1118482" autoColor="false" predefinedStyle="false"/>
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
<Attr gradientType="normal" gradientStartColor="-12146441" gradientEndColor="-9378161" shadow="false" autoBackground="false" predefinedStyle="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-6908266" autoColor="false" predefinedStyle="false"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<O>
<![CDATA[新建图表标题]]></O>
<TextAttr>
<Attr alignText="0" predefinedStyle="false">
<FRFont name="SimSun" style="0" size="128" foreground="-13421773"/>
</Attr>
</TextAttr>
<TitleVisible value="false" position="0"/>
</Title>
<Attr4VanChart useHtml="false" floating="false" x="0.0" y="0.0" limitSize="false" maxHeight="15.0"/>
</Title4VanChart>
<Plot class="com.fr.plugin.chart.PiePlot4VanChart">
<VanChartPlotVersion version="20170715"/>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr gradientType="normal" gradientStartColor="-12146441" gradientEndColor="-9378161" shadow="false" autoBackground="false" predefinedStyle="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-1118482" autoColor="false" predefinedStyle="false"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<Attr isNullValueBreak="true" autoRefreshPerSecond="0" seriesDragEnable="false" plotStyle="0" combinedSize="50.0"/>
<newHotTooltipStyle>
<AttrContents>
<Attr showLine="false" position="1" isWhiteBackground="true" isShowMutiSeries="false" seriesLabel="${VALUE}"/>
<Format class="com.fr.base.CoreDecimalFormat" roundingMode="6">
<![CDATA[#.##]]></Format>
<PercentFormat>
<Format class="com.fr.base.CoreDecimalFormat" roundingMode="6">
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
<Attr enable="true" duration="4" followMouse="false" showMutiSeries="false" isCustom="false"/>
<TextAttr>
<Attr alignText="0" predefinedStyle="false">
<FRFont name="Microsoft JhengHei" style="0" size="72"/>
</Attr>
</TextAttr>
<AttrToolTipContent>
<TextAttr>
<Attr alignText="0" predefinedStyle="false">
<FRFont name="Microsoft JhengHei" style="0" size="72"/>
</Attr>
</TextAttr>
<richText class="com.fr.plugin.chart.base.AttrTooltipRichText">
<AttrTooltipRichText>
<Attr content="" isAuto="true" initParamsContent=""/>
<params>
<![CDATA[{}]]></params>
</AttrTooltipRichText>
</richText>
<richTextValue class="com.fr.plugin.chart.base.format.AttrTooltipValueFormat">
<AttrTooltipValueFormat>
<Attr enable="true"/>
</AttrTooltipValueFormat>
</richTextValue>
<richTextPercent class="com.fr.plugin.chart.base.format.AttrTooltipPercentFormat">
<AttrTooltipPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat" roundingMode="6">
<![CDATA[#.##%]]></Format>
</AttrTooltipPercentFormat>
</richTextPercent>
<richTextCategory class="com.fr.plugin.chart.base.format.AttrTooltipCategoryFormat">
<AttrToolTipCategoryFormat>
<Attr enable="false"/>
</AttrToolTipCategoryFormat>
</richTextCategory>
<richTextSeries class="com.fr.plugin.chart.base.format.AttrTooltipSeriesFormat">
<AttrTooltipSeriesFormat>
<Attr enable="true"/>
</AttrTooltipSeriesFormat>
</richTextSeries>
<richTextChangedPercent class="com.fr.plugin.chart.base.format.AttrTooltipChangedPercentFormat">
<AttrTooltipChangedPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat" roundingMode="6">
<![CDATA[#.##%]]></Format>
</AttrTooltipChangedPercentFormat>
</richTextChangedPercent>
<richTextChangedValue class="com.fr.plugin.chart.base.format.AttrTooltipChangedValueFormat">
<AttrTooltipChangedValueFormat>
<Attr enable="false"/>
</AttrTooltipChangedValueFormat>
</richTextChangedValue>
<TableFieldCollection/>
<Attr isCommon="true" isCustom="false" isRichText="false" richTextAlign="left" showAllSeries="false"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipValueFormat">
<AttrTooltipValueFormat>
<Attr enable="true"/>
</AttrTooltipValueFormat>
</value>
<percent class="com.fr.plugin.chart.base.format.AttrTooltipPercentFormat">
<AttrTooltipPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat" roundingMode="6">
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
<Attr enable="true"/>
</AttrTooltipSeriesFormat>
</series>
<changedPercent class="com.fr.plugin.chart.base.format.AttrTooltipChangedPercentFormat">
<AttrTooltipChangedPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat" roundingMode="6">
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
<Attr gradientType="normal" gradientStartColor="-12146441" gradientEndColor="-9378161" shadow="true" autoBackground="false" predefinedStyle="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="2"/>
<newColor borderColor="-16777216" autoColor="false" predefinedStyle="false"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="0.5"/>
</AttrAlpha>
</GI>
</AttrTooltip>
</Attr>
<Attr class="com.fr.chart.base.AttrBorder">
<AttrBorder>
<Attr lineStyle="1" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-1" autoColor="false" predefinedStyle="false"/>
</AttrBorder>
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
<Attr gradientType="normal" gradientStartColor="-12146441" gradientEndColor="-9378161" shadow="false" autoBackground="false" predefinedStyle="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-3355444" autoColor="false" predefinedStyle="false"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<Attr position="4" visible="true" predefinedStyle="false"/>
<FRFont name="Microsoft YaHei UI" style="0" size="64" foreground="-10066330"/>
</Legend>
<Attr4VanChart floating="false" x="0.0" y="0.0" layout="aligned" customSize="true" maxHeight="100.0" isHighlight="true"/>
</Legend4VanChart>
<DataSheet>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr gradientType="normal" gradientStartColor="-12146441" gradientEndColor="-9378161" shadow="false" autoBackground="false" predefinedStyle="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="1" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-16777216" autoColor="false" predefinedStyle="false"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<Attr isVisible="false" predefinedStyle="false"/>
<FRFont name="Microsoft JhengHei" style="0" size="72"/>
</DataSheet>
<DataProcessor class="com.fr.base.chart.chartdata.model.NormalDataModel"/>
<newPlotFillStyle>
<AttrFillStyle>
<AFStyle colorStyle="1"/>
<FillStyleName fillStyleName=""/>
<isCustomFillStyle isCustomFillStyle="true"/>
<PredefinedStyle predefinedStyle="false"/>
<ColorList>
<OColor colvalue="-12276512"/>
<OColor colvalue="-12203043"/>
<OColor colvalue="-10760542"/>
<OColor colvalue="-1059000"/>
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
<GradientStyle>
<Attr gradientType="normal" startColor="-12146441" endColor="-9378161"/>
</GradientStyle>
<PieAttr4VanChart roseType="normal" startAngle="0.0" endAngle="360.0" innerRadius="0.0" supportRotation="false"/>
<VanChartRadius radiusType="auto" radius="100"/>
</Plot>
<ChartDefinition>
<NormalReportDataDefinition>
<Series>
<SeriesDefinition>
<SeriesName>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=B3:E3]]></Attributes>
</O>
</SeriesName>
<SeriesValue>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=B4:E4]]></Attributes>
</O>
</SeriesValue>
</SeriesDefinition>
</Series>
<Category>
<O>
<![CDATA[]]></O>
</Category>
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
</NormalReportDataDefinition>
</ChartDefinition>
</Chart>
<UUID uuid="99bfe80a-dbf6-43d3-bfd0-51fb9edd45ab"/>
<tools hidden="true" sort="true" export="true" fullScreen="true"/>
<VanChartZoom>
<zoomAttr zoomVisible="false" zoomGesture="true" zoomResize="true" zoomType="xy" controlType="zoom" categoryNum="8" scaling="0.3"/>
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
<Attr alignText="0" predefinedStyle="false">
<FRFont name="Microsoft JhengHei" style="0" size="72"/>
</Attr>
</TextAttr>
<AttrToolTipContent>
<TextAttr>
<Attr alignText="0" predefinedStyle="false">
<FRFont name="Microsoft JhengHei" style="0" size="72"/>
</Attr>
</TextAttr>
<richText class="com.fr.plugin.chart.base.AttrTooltipRichText">
<AttrTooltipRichText>
<Attr content="" isAuto="true" initParamsContent=""/>
<params>
<![CDATA[{}]]></params>
</AttrTooltipRichText>
</richText>
<richTextValue class="com.fr.plugin.chart.base.format.AttrTooltipValueFormat">
<AttrTooltipValueFormat>
<Attr enable="true"/>
</AttrTooltipValueFormat>
</richTextValue>
<richTextPercent class="com.fr.plugin.chart.base.format.AttrTooltipPercentFormat">
<AttrTooltipPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat" roundingMode="6">
<![CDATA[#.##%]]></Format>
</AttrTooltipPercentFormat>
</richTextPercent>
<richTextCategory class="com.fr.plugin.chart.base.format.AttrTooltipCategoryFormat">
<AttrToolTipCategoryFormat>
<Attr enable="false"/>
</AttrToolTipCategoryFormat>
</richTextCategory>
<richTextSeries class="com.fr.plugin.chart.base.format.AttrTooltipSeriesFormat">
<AttrTooltipSeriesFormat>
<Attr enable="false"/>
</AttrTooltipSeriesFormat>
</richTextSeries>
<richTextChangedPercent class="com.fr.plugin.chart.base.format.AttrTooltipChangedPercentFormat">
<AttrTooltipChangedPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat" roundingMode="6">
<![CDATA[#.##%]]></Format>
</AttrTooltipChangedPercentFormat>
</richTextChangedPercent>
<richTextChangedValue class="com.fr.plugin.chart.base.format.AttrTooltipChangedValueFormat">
<AttrTooltipChangedValueFormat>
<Attr enable="false"/>
</AttrTooltipChangedValueFormat>
</richTextChangedValue>
<TableFieldCollection/>
<Attr isCommon="true" isCustom="false" isRichText="false" richTextAlign="left" showAllSeries="false"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipValueFormat">
<AttrTooltipValueFormat>
<Attr enable="false"/>
</AttrTooltipValueFormat>
</value>
<percent class="com.fr.plugin.chart.base.format.AttrTooltipPercentFormat">
<AttrTooltipPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat" roundingMode="6">
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
<Format class="com.fr.base.CoreDecimalFormat" roundingMode="6">
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
<Attr gradientType="normal" gradientStartColor="-12146441" gradientEndColor="-9378161" shadow="false" autoBackground="false" predefinedStyle="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="1" isRoundBorder="false" roundRadius="4"/>
<newColor borderColor="-15395563" autoColor="false" predefinedStyle="false"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="0.8"/>
</AttrAlpha>
</GI>
</AttrTooltip>
</refreshMoreLabel>
<ThemeAttr>
<Attr darkTheme="false" predefinedStyle="false"/>
</ThemeAttr>
</Chart>
</O>
<PrivilegeControl/>
<CellGUIAttr/>
<CellPageAttr/>
<Expand/>
</C>
<C c="0" r="14" cs="5" s="0">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[="  " + if(len($province) = 0 || $province = "中國", "全國下屬地區資料", $province + "下屬地區資料")]]></Attributes>
</O>
<PrivilegeControl/>
<CellGUIAttr adjustmode="0"/>
<CellPageAttr/>
<Expand/>
</C>
<C c="0" r="15" s="1">
<O>
<![CDATA[地名]]></O>
<PrivilegeControl/>
<CellGUIAttr adjustmode="0"/>
<CellPageAttr/>
<Expand/>
</C>
<C c="1" r="15" s="2">
<O>
<![CDATA[銷售額]]></O>
<PrivilegeControl/>
<CellGUIAttr adjustmode="0"/>
<CellPageAttr/>
<Expand/>
</C>
<C c="2" r="15" s="2">
<O>
<![CDATA[利潤額]]></O>
<PrivilegeControl/>
<CellGUIAttr adjustmode="0"/>
<CellPageAttr/>
<Expand/>
</C>
<C c="3" r="15" s="2">
<O>
<![CDATA[運營費用]]></O>
<PrivilegeControl/>
<CellGUIAttr adjustmode="0"/>
<CellPageAttr/>
<Expand/>
</C>
<C c="4" r="15" s="3">
<O>
<![CDATA[稅費]]></O>
<PrivilegeControl/>
<CellGUIAttr adjustmode="0"/>
<CellPageAttr/>
<Expand/>
</C>
<C c="0" r="16" s="9">
<O t="DSColumn">
<Attributes dsName="ds3" columnName="省份"/>
<Condition class="com.fr.data.condition.CommonCondition">
<CNAME>
<![CDATA[pid]]></CNAME>
<Compare op="0">
<Parameter>
<Attributes name="province"/>
<O>
<![CDATA[]]></O>
</Parameter>
</Compare>
</Condition>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Result>
<![CDATA[$$$]]></Result>
<Parameters/>
</O>
<PrivilegeControl/>
<CellGUIAttr adjustmode="0"/>
<CellPageAttr/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.ListCondition">
<JoinCondition join="0">
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len(province) = 0 || $province = "中國"]]></Formula>
</Condition>
</JoinCondition>
<JoinCondition join="1">
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($$$) = 0]]></Formula>
</Condition>
</JoinCondition>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand dir="0"/>
</C>
<C c="1" r="16" s="10">
<O t="DSColumn">
<Attributes dsName="ds3" columnName="銷售額"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.SummaryGrouper">
<FN>
<![CDATA[com.fr.data.util.function.SumFunction]]></FN>
</RG>
<Parameters/>
</O>
<PrivilegeControl/>
<CellGUIAttr adjustmode="0"/>
<CellPageAttr/>
<Expand/>
</C>
<C c="2" r="16" s="10">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=B17 - D17 - E17]]></Attributes>
</O>
<PrivilegeControl/>
<CellGUIAttr adjustmode="0"/>
<CellPageAttr/>
<Expand leftParentDefault="false" left="B17"/>
</C>
<C c="3" r="16" s="10">
<O t="DSColumn">
<Attributes dsName="ds3" columnName="運營費用"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.SummaryGrouper">
<FN>
<![CDATA[com.fr.data.util.function.SumFunction]]></FN>
</RG>
<Parameters/>
</O>
<PrivilegeControl/>
<CellGUIAttr adjustmode="0"/>
<CellPageAttr/>
<Expand/>
</C>
<C c="4" r="16" s="11">
<O t="DSColumn">
<Attributes dsName="ds3" columnName="稅費"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.SummaryGrouper">
<FN>
<![CDATA[com.fr.data.util.function.SumFunction]]></FN>
</RG>
<Parameters/>
</O>
<PrivilegeControl/>
<CellGUIAttr adjustmode="0"/>
<CellPageAttr/>
<Expand/>
</C>
<C c="5" r="16" s="12">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=len(INDEXOFARRAY(A19, 1))]]></Attributes>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="0" r="17" s="9">
<O t="DSColumn">
<Attributes dsName="ds3" columnName="pid"/>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len(pid) != 0]]></Formula>
</Condition>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Result>
<![CDATA[$$$]]></Result>
<Parameters/>
</O>
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len(province) != 0 && $province != "中國"]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand dir="0"/>
</C>
<C c="1" r="17" s="10">
<O t="DSColumn">
<Attributes dsName="ds3" columnName="銷售額"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.SummaryGrouper">
<FN>
<![CDATA[com.fr.data.util.function.SumFunction]]></FN>
</RG>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="2" r="17" s="10">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=B18 - D18 - E18]]></Attributes>
</O>
<PrivilegeControl/>
<CellGUIAttr adjustmode="0"/>
<CellPageAttr/>
<Expand/>
</C>
<C c="3" r="17" s="10">
<O t="DSColumn">
<Attributes dsName="ds3" columnName="運營費用"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.SummaryGrouper">
<FN>
<![CDATA[com.fr.data.util.function.SumFunction]]></FN>
</RG>
<Parameters/>
</O>
<PrivilegeControl/>
<CellGUIAttr adjustmode="0"/>
<CellPageAttr/>
<Expand/>
</C>
<C c="4" r="17" s="11">
<O t="DSColumn">
<Attributes dsName="ds3" columnName="稅費"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.SummaryGrouper">
<FN>
<![CDATA[com.fr.data.util.function.SumFunction]]></FN>
</RG>
<Parameters/>
</O>
<PrivilegeControl/>
<CellGUIAttr adjustmode="0"/>
<CellPageAttr/>
<Expand/>
</C>
<C c="5" r="17" s="12">
<PrivilegeControl/>
<Expand/>
</C>
<C c="0" r="18" s="13">
<O t="DSColumn">
<Attributes dsName="ds4" columnName="省份"/>
<Condition class="com.fr.data.condition.ListCondition">
<JoinCondition join="0">
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[0]]></CNUMBER>
<CNAME>
<![CDATA[省份]]></CNAME>
<Compare op="0">
<Parameter>
<Attributes name="province"/>
<O>
<![CDATA[]]></O>
</Parameter>
</Compare>
</Condition>
</JoinCondition>
<JoinCondition join="0">
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len(pid) != 0]]></Formula>
</Condition>
</JoinCondition>
</Condition>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<SelectCount count="5"/>
<Result>
<![CDATA[$$$]]></Result>
<Parameters/>
</O>
<PrivilegeControl/>
<CellGUIAttr adjustmode="0"/>
<CellPageAttr/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($$$) = 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand dir="0" multiNumber="5"/>
</C>
<C c="1" r="18" s="14">
<O t="DSColumn">
<Attributes dsName="ds4" columnName="銷售額"/>
<Condition class="com.fr.data.condition.ListCondition"/>
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
<CellGUIAttr adjustmode="0"/>
<CellPageAttr/>
<Expand/>
</C>
<C c="2" r="18" s="14">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=B19 - D19 - E19]]></Attributes>
</O>
<PrivilegeControl/>
<CellGUIAttr adjustmode="0"/>
<CellPageAttr/>
<Expand/>
</C>
<C c="3" r="18" s="14">
<O t="DSColumn">
<Attributes dsName="ds4" columnName="運營費用"/>
<Condition class="com.fr.data.condition.ListCondition"/>
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
<CellGUIAttr adjustmode="0"/>
<CellPageAttr/>
<Expand/>
</C>
<C c="4" r="18" s="15">
<O t="DSColumn">
<Attributes dsName="ds4" columnName="稅費"/>
<Condition class="com.fr.data.condition.ListCondition"/>
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
<CellGUIAttr adjustmode="0"/>
<CellPageAttr/>
<Expand/>
</C>
<C c="5" r="18" s="16">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=len(INDEXOFARRAY(A17, 1))]]></Attributes>
</O>
<PrivilegeControl/>
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
<Style imageLayout="1">
<FRFont name="Microsoft YaHei" style="0" size="96" foreground="-16749643"/>
<Background name="ColorBackground" color="-2953990"/>
<Border>
<Top style="1" color="-1446671"/>
<Bottom style="1" color="-1446671"/>
<Left style="1" color="-1446671"/>
<Right style="1" color="-1446671"/>
</Border>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="微软雅黑" style="0" size="80" foreground="-14145496"/>
<Background name="NullBackground"/>
<Border>
<Top style="1" color="-1446671"/>
<Bottom style="1" color="-1446671"/>
<Left style="1" color="-1446671"/>
</Border>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="微软雅黑" style="0" size="80" foreground="-14145496"/>
<Background name="NullBackground"/>
<Border>
<Top style="1" color="-1446671"/>
<Bottom style="1" color="-1446671"/>
</Border>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="微软雅黑" style="0" size="80" foreground="-14145496"/>
<Background name="NullBackground"/>
<Border>
<Top style="1" color="-1446671"/>
<Bottom style="1" color="-1446671"/>
<Right style="1" color="-1446671"/>
</Border>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="微软雅黑" style="0" size="64" foreground="-11579569"/>
<Background name="NullBackground"/>
<Border>
<Top style="1" color="-1446671"/>
<Left style="1" color="-1446671"/>
</Border>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="微软雅黑" style="0" size="64" foreground="-11579569"/>
<Background name="NullBackground"/>
<Border>
<Top style="1" color="-1446671"/>
</Border>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="微软雅黑" style="0" size="64" foreground="-11579569"/>
<Background name="NullBackground"/>
<Border>
<Top style="1" color="-1446671"/>
<Right style="1" color="-1446671"/>
</Border>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="SimSun" style="1" size="72"/>
<Background name="NullBackground"/>
<Border>
<Left style="1" color="-1446671"/>
<Right style="1" color="-1446671"/>
</Border>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="SimSun" style="0" size="72"/>
<Background name="NullBackground"/>
<Border>
<Bottom style="1" color="-1446671"/>
<Left style="1" color="-1446671"/>
<Right style="1" color="-1446671"/>
</Border>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="微软雅黑" style="0" size="64" foreground="-11579569"/>
<Background name="ColorBackground" color="-1"/>
<Border>
<Top style="1" color="-1446671"/>
<Bottom style="1" color="-1446671"/>
<Left style="1" color="-1446671"/>
</Border>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<Format class="com.fr.base.CoreDecimalFormat" roundingMode="6">
<![CDATA[#0]]></Format>
<FRFont name="微软雅黑" style="0" size="64" foreground="-11579569"/>
<Background name="ColorBackground" color="-1"/>
<Border>
<Top style="1" color="-1446671"/>
<Bottom style="1" color="-1446671"/>
</Border>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<Format class="com.fr.base.CoreDecimalFormat" roundingMode="6">
<![CDATA[#0]]></Format>
<FRFont name="微软雅黑" style="0" size="64" foreground="-11579569"/>
<Background name="ColorBackground" color="-1"/>
<Border>
<Top style="1" color="-1446671"/>
<Bottom style="1" color="-1446671"/>
<Right style="1" color="-1446671"/>
</Border>
</Style>
<Style imageLayout="1">
<FRFont name="SimSun" style="0" size="72"/>
<Background name="ColorBackground" color="-1"/>
<Border/>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="微软雅黑" style="0" size="64" foreground="-11579569"/>
<Background name="NullBackground"/>
<Border>
<Top style="1" color="-1446671"/>
<Bottom style="1" color="-1446671"/>
<Left style="1" color="-1446671"/>
</Border>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<Format class="com.fr.base.CoreDecimalFormat" roundingMode="6">
<![CDATA[#0]]></Format>
<FRFont name="微软雅黑" style="0" size="64" foreground="-11579569"/>
<Background name="NullBackground"/>
<Border>
<Top style="1" color="-1446671"/>
<Bottom style="1" color="-1446671"/>
</Border>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<Format class="com.fr.base.CoreDecimalFormat" roundingMode="6">
<![CDATA[#0]]></Format>
<FRFont name="微软雅黑" style="0" size="64" foreground="-11579569"/>
<Background name="NullBackground"/>
<Border>
<Top style="1" color="-1446671"/>
<Bottom style="1" color="-1446671"/>
<Right style="1" color="-1446671"/>
</Border>
</Style>
<Style imageLayout="1">
<FRFont name="SimSun" style="0" size="72"/>
<Background name="ColorBackground" color="-103"/>
<Border/>
</Style>
</StyleList>
<heightRestrict heightrestrict="false"/>
<heightPercent heightpercent="0.75"/>
<IM>
<![CDATA[m(@OA;d9,V$A]AlA:f*7V'Tkb$,$hJ#6)9:91a*Rt21YWJ;P]A%"d\MOkkXCU\9krmS!sBd#cp
AiuiGK@QH/IKrhmhQ&m_/X*(kY%2fk[^&XZ>Q#T=&icfNfNJdjJ6n:f'uY<`cnUO+QAi(^7k
jMrVj..p3/V.11sArp$t1)#0r19[c>SNR[C"f3J<u4\WM(KT.^ebNcHuPfSiR%07]A-ilQ,B%
S^#Loq.%fp$O>_oP;]A)n'=a#5PU_mp"#ALd9C8'Dqq2'I5h#t'riYC]AcQ6'=?`dL;ZU>V]Ac`
`U]Ac!&@%.UO9P-O=[crWA67+.a(fM`=NT`W5"nMV;[8\T(Fl6B*Pic&.]Ao&/6@(2=1%2t.(I
$)Na-1bGd=#X1[sJrT?l_'Ou6m++??3sfr+m<i$=[O&JA5\fs3SftN)]A3.Zqbgo@ANpd-gGT
b$scbi)<D<LW6V*$tG]A1>;GdbejRUP^_31joqb?,JeX3Ll0!]A:1`2;__0!aU,@Z;;U'$_L:_
fJY>VX.hX(JAcD(X<1g.,PJZV-\-b$RHhQ8ipu[*]AAQc4677p97Dp7`uK)):DX.-fcXU7"td
djh$qfRS+o/=Kp^=rG\Q8KjZEoY35HfUSI'KN=XGiUOeg#HOBQ45W32PekU_$Dt8quaC]A;?s
"B45$<@@aKs.EH8G%MX7ImD6pH>-^I6'7o`!k-CIaIf%f_Vn/gn<$b46\*!9+-9cp<#s%Vc9
XY;%!P9;[@$Fs)+/eQNq=[q7IkogY-?)^c>7_:=_biA4_=7Q2f>2QsdaIB%pIF>gO&lPO<5E
j`+rAq/6_HcJu(2(_JjRVY8iB<;k_*/Ke?RrNY8??gXZkH?#is%J!d#[+(#:&uYC68=!nB7B
NkJBRec)"oH,P`IqO1946Z!C7;r!M,C`0o+hMkl)Vmqhu493d)'L?e2G4RrPogadV_`l486Z
<Z_%>;oaK4I'Ghd#$$`lg5YFm5@+[<,QrW/=`700TY;5Mf_FbRI%Y<8+6iWkH\YCijJ:qI\o
^tX(mfsn4f\p[>AZ(YB7[kN(l*g%V:!s@cU[.M%"'W,Ii(a_1.+*b;Vn,_3'n>[ltX#%87lS
]AtEpa^(?tpA_j+dko*L/g;t^LS2:dbP2"Mpl`KP;1CCTc_HKRt@,0KhG]A16#@Mpmt_dpO7V5
pVk:VWNZR.KrU!KZWA<$O_KeXs(>4U2Y$]A8uE1BoD.-]AUc*1^6H!f6G`F;]AfLdS\ft*W[/NL
S'$eggb4:YjM,?>NQg,F]AfY(I,nJJq'#[>XpHKl8f'B:fr"o%P^W#:PL,ILIe=,UJ%+n8V,b
VJTr,ZC?dZ%A17BaYf]AJ'<Qh4au)G<-%dtMkXt&W,(5W$MTUlN-]ARs0783tCuCt.XW&`F$Vb
L*98pMrLE[/@]ADG!0Bin*+0`7aUG/$6l!PX/)$M,e>V[K7L10>6F:%41^OGjo4S+LUHp.OJ5
78L:%=H;JmeS_jjgL[BlR5`C$]A,*ZWVKQ:O/6js6h]AjfAP<":$Y_c"W[gl!1G/bH.EE5g+jt
d*]Ac#`PA8(G0Tj+5o`0*9IiEC2%5+1hZc8mM6<5>a$YXgGns.FWA1_@U":qh%1tH4A2U30K4
BVR=?)C?`(0P-ZuZi_;(,=2AeA[8AkXr8qB=(g\LY6OR*aRrK^N&j+dQ7ab(D"S>4LJGT3BF
?II1DPJf!Z)dlJ8]A28A):CS"b=UndY8):aC`998#r[8WAa2=_3!map.b0FT,!$1!:4oV]AoCe
$!F4E<O(iq:bB8:7l9psad(/ET?qiDtW3R'X1=tHT*_;@n3gqsEQi3);p,_JrhM/_7[<XdsV
5;`MJ-TIL,Fr]A!C)(0pf'875t?7p[dhPULtOg4K0(DLs[R-M4KS`%j]AR5r[4-ILASC+>*''h
"CR:t`cIT5%S3)&_c.Dd^G=NRr/&R]AGH/ngW(k>86dkETB]AmWBRJKfDa0s.rcHqL6ZZ1[**b
)C#3ZaUtFaiCmgacZ#iE:Pcruu+Uo#TS*O\a2a_9iU:<r^\p`/I1$@Mb]A.HY>Y%uEGT`VHp+
sX"iKZUZ$'iSjSiZCq,%S^jp_AdZ+irskQY*a)I\U_!N':#>S`Q_7hC#=\ObE([k3#mS[G\m
Ls2AP'[JLd<_^!`VUY_;@>iZ>Do-n!9X:rEU99G1mGppg]AF=^,[.N/RUUUfa,bXZ`0H"u-Wa
oW>LVkM^c_"kW]A-2N"Hs]A[Y+E8Y&8l=Q+#(I72"79ch70lf)0>HLr2iq,VQifBS!IVP+ualW
'uW'.8sa`"ukI;)^dn?!H<WT^&*Ucr]An(f8/27GRW4;*3:h8&2`N9>Y<&_fO)9,S.nN/[5;]A
o"X8:(qVFXmZR5OkIJ2<*$L1F$:Cr%\MiUh3Uf52URk`QS.&>W(I-D<hpQaVtZ,/;XTmb.(<
7#b9fY'AcV/O"iC'icJeW(*k*&?gIasp1J-4=dtHD?']APW82$%Qo<40c=r!reDRESZ@Sfm#%
=f;dEoO!l(fHVR[eSamo*pU^B(a5shNt\@\=:'1H9sU--,ge6A15m"&rYZ(*Y`fHU?E!OB6J
;)=Bga4KV2+M#<biVh'F3Hhe[\Z`"PRmI$;::==-Qf=^1;X^.3fR@g^knnNh?`i!@J_*3n1t
+nKRoatuf[Y7X84h^K\aC4>Oho@*%A39m-E3c:QI="=<6AlJ#0U=uaq*c=49H+KHhE0db2da
9oZ$V"nm%KUF*-JuXj+JI0=:tdRI*'g[=R7rDWh%W3nqp.\1r&_37mFVWJb]A9#kWhQYH#-oL
PJB%k/'+$LL>XG4En>Sf$o4SP.>)-!/V1oWRj1ZJQOhGIIBb&5m^!Cf#5FV:?#(K8jN7&d.(
VDQDgKS4XN1ONAaP((H=4,[;rU%Nm%"5YJjKSMN8nK<CcKK0$,,AeX/24SX#C*D*,<`aLDt_
g[&%YiVs5aWBN8ubt;^0GZ.u=_arA'JbHU69>$l&F4'u2UA64t's7lM@oK-Pc(`Lh&M"Q\<o
>7,rlKcFZB,cuB-nQ6G5S-3HJc3438rJt$opFFX7OO)djO$cNuA3kb)F[6O8AISq6h=q".&a
q51B=H%%7n/G!;Z&Z1B(`M-B"$Wbf>p)jBS(bhcpS#QUKOr\2[Mh@*,)_7p7)Ni^.6Sgj7,c
BF<U:8u.:m0>NFd5L8C-n<0\=FYN^dIPd`a1D.P'&F^pOm<kT$,r3_"Q,jdknT_$4,4\t]AsL
R14+Gm:2)O\;V%IZ"2ril$J7_.(cMhMC3^C-NgP:^imattEFW8;$ZiB!=1M[\ro._Q/SAqc*
j=TH\24"-qSAG)OYee&_'G\2\@H?R<j>/!Y3W'_fg\FZpBo=DLbF(_d!IH%4]AB.eWAh<D^Hc
>Z'\Qn\gbR'>D`F.8KqP+2L?K0!5M/0SilkEooa+c-3<g-gTNC-SNF9k:6.]A\!9aOt;K4\9-
"ofC<?HHM,Z8hOaUY@RN>8=9Y'X+eft^WC)TC`Fb-1>rd'Ob^S]A;pub*A'rG)mC9*fTK4ZWX
2s_3XG4K2?0PHtP\D35E:lb%I+a9VGjd8?RpfI&,h`J+Ze*4!i&B%`Hl\]A5A_d\>(7Bq)oAY
a+=mlN^ilaUslD0se@ESn3HH_aYX]A8*5/LkN"p)9poT<g.4QaHK1]AoTt5\i9M`G53=MW-j)7
`WAh^!1-B+?<Zm@5Z\so'Zatl?U^Rg^?2q`35Dd?c]A">+.\&&*79WDUSQXd27p_/pP,$cKnf
5k8YTmtdp]A_]AS:Joq#:)>/qlf\s[Hf4R9I=Ba:R\B__:qPi;']AbRsHNEE-^#7gP\34Z*+F"\
GYafeLXB8qSl$"+=hkHG71YhWaXfcCeP5:Q4<C8`=AcQ!%Q"*c7[s`[<oc,l'!XitgJW;OfE
`S;#jRqUaH=)B,,2HLb0Rhk_(cT/XLVS@U/RlK.iT;2jpZU(`Oo6_SI760B.WLB"`&2ti'90
2Yp0Dl30WRjil`qCERl7k&Gl_GpE;*@4iSDi3AjSo1&`oA^AQR5LrFRg!2L34MC0`+FhhHZ4
&p'UY?VRNYLqC0RJ-/<@[d6^LEV9s<l;Tpq`7I2#S!^b#laK.)VSX;\B'kbn:DLnV%.de1$E
\cO?T#_Ki0J3(cEV#a<tB[!eudS-Z<;2;13%I.+.D;'2s>V(R+CbTA`"K;1P/u,+/(?"F/(@
h5WB]AHbq5+Tpb=+67M=4Rrf$p1Y)"`:'<#pI?9O\^,4Br?.@&]AU;'XG(=+Hb[Q.BCu%&,)Im
&sgY1uS?**%i_?E'f@fQn%:_ibZ#gCQaYV0&eP$VttQfDj4]Aip(E;sf!>1L:;+>YK2*MYp>'
"(&@^,EYmKM#CDcLD':r!^$>".`3Gcs_H[JIg*?'0Ao/DEJH:)Ll0@((i,h=G;fGNJEl9Ql=
KEX;A1cO19\L/eK]AAq>u9"-QA+&jb%NQ><aG<\bWO'^9:h;KV[kI8c;L*acE?S#i%B'U"Y[<
&3%b4.,kcA[3q-e=!=YdX*Kj`5f1?pf4l*u@c20Q,Uf*-e\+FV@ai?p7<!;D0;?J!."#\PO%
Mc\3'mQZ@+'IlEqFNSoA7&5*5+`SO,QXK2$V!5-8?Rm9Tal7"`+b&)S]AD>0c)>o4]A^M/q5Xh
]A>M)X7N-bOVf7@df%pD)UJ$_%,"g$A)sCAjgLNL5;RP.AF#7\3g0F5M^:tj"[o7c.R5QT6UB
kk4@JKq?#%Ymc_+#ak=>q_Mf?;4Gkm):>uf2PQLPh0]AlBA(rQ`b]AcX:U-fu&a]A6Ohi_L*<-;
Y!qA0]A'p9?rO`;o+HEeZAB.FKSuJ)RM6oh2H1=I%Y,&.[;50US[9YYT6<\4YMD>gU:F'Y\ZA
0&F<>[=)EZ%p.`>k#b\B*E_mZtJW?c$icjNDa=8U75^#FoOoGa-/#Eu8&('*>bYBSA0SZaA:
Y2f@8J]A:InG+0RsONnt/\EkS:nHD.qVg2=7PdqKQa:nP-$7^LnA8]A4$IZ=t\%%chn4a;5/"-
]AoS/YM.M5]A/u+f+ICP+bsi]AKeZif64!'.qSUF`oD<MX]A$(G.OUn11ZrQLiIqKfRoY?+03PAB
a>3"L5bV0)4=L#QM/0XQErN<<dPU[db]A@I>9"TF7N7jYQME6<k\cMI5@iBh3MMI%`lt0ORA@
&'\d&APE"7i'kbcgP&oaX[&nYCD?a\Te%:J\/R+/kN&Xd6cuu@$(W#5Sp[1gfc)bZAO;7?jB
G'+m^5\i7<Tq``hlgdCc,mL/2&Sl"@=dW2VW?*jq^0dP^CnVMdf_+Bs.:MDQI(_h48B\2[5=
#<4erL*;aN`G4_dRj'sFTeHKk!I[/e4n/$g69mZ)4nrjihm0beeF^Fe5k*AdoP5(fD9Hk+;b
-i,Koph4HK3l9-BHCi%_Hj+B4AcEj[<)m@Vk=:YT0b"^UTp@XH93#jj1=HkYNTk9lVI.'%VB
Oc1h2V&CZ^_R4-UTuGY;e>;u!ri%EGp#_CO</Z-Gkr3:h]A^-5IGeMtFh"@IpW<.XM#kbto0;
rP#I>F?jIr_?WDR/[ADU\+8hbOZ$=?^p8*,MQ=8smM9G\XkN]AWXmjl:W=pgC=Y)s-+%AUr,=
s.qD)0F2==g@a)q4LY=K9^>"U5pmF1!;(n,0`9leB(u$un@>)CjJ)Tp[:)P;Fi5eJr1$,4(@
Bnd:22!hTo`bgOm(-,$bZfJ/"InR;\dWqK3^Vm.Br$cc0.h?Pu;a#?-_Iu$<belP&te>QIH!
RIVsiZ%$ZAoQE#]AO1B,o+JG\8mQXW6V2,d&&`1E0Jg(s-_%QfZbpm4dSo\DaUR%n05i5'#?8
V<>0BQlU#ig19Z25/W,V6\Kh^BhLoXN_/\NBcIq[f#*H@!rOr"LM`q%-M[c``2<n3%JF+?Q@
Bi2Z&-+2>eo6-D52P'-aaPF^]Ahs,5^O)a@r!fZ!T2]A4I(/G,fO8B)Webd<lA*!:I-(W-&t@F
cd*GE0bqWlJGsj''/'Got"4UO;-XWC^Ql4Gh6\)X\0,auJ0.dL$A1::SKT4El7^s3T<WhJ,o
=]AVifPT>3O9^N<^STA(9om3TU;3Do@o#76nP]AmJ+T_ab?_pB#l*:5iM)mh#W<Qb<.us$i:&^
GbCg*'2Se'@e&=N7uCDn40U+K0h\9?HVto8p2Ps-#(X:b/BR&IPeK8?lQ"H@9F,3)rO[(#hm
F"-94+2MCmIs9nIO)&t_MYAWSD).`3dQ1OaBW+X<bWI=I*0"H.H^4N:.>9O4H><'"8(LgL<=
V!9Aqc?fdE]AUKBX/EN/83-K7pls3X#etH4>*,BhIUgj]Am>re^UL`>b0DCnFTpT!h_na?;%M^
.;$2"c/b+X2]AN#I7&TqNUaKlqeb'QRAe-NO(V54gjZ(T`B:Im2ft",e$-;8+D5#fB52ZMjrP
:OS_shDA0qH%Mfi/[n)M:E_NoELA@OLBPF<)*%6O(_-bni&+W+;Pj=$FaOOR_V).'GD;O"qc
.C8dldOlakcR+o=`mUOom^rB*8u4brYP1F4GMn0l&%mB8Y=*#jatA)b@;P)ba*^a01eQZ8G<
<#\K>(GDX#lQI#X[lFMeOXQ_<7\DKS!ZqkRoC>,o>H>QO-XC:ulP@^DMl/;17X0cWb^UQ\*6
lU:KsQW;aR=MI,0AIAQZD'j+d&Vs,J8et"q;e<Xo6[e(`DG@aAFl<9uG%7BC7DE9ABe=<!?%
fb$ml;$AF_V,+eU*pAD_>]AM68Mm[B3S^mUNuUgZcNhHddV]A0XsA\]ArIe!CVE^Yl'RHS'eKN1
a<5Wc1E2+"3go`SfJ\4WNM-ADG;3E'l<B>]ASZ'pH:]Ad)18=6;:fOI*P@6RF1k1huSfMdDmDo
'@`P;?ooC$*S5koZ3UZ+a]A4'-2)dR#!*rDpGTVSQEW8IaG5$E*0dCs"goSS7@TI#B<U7CDhI
29cr9Cs>HdG>[#&S5#hd-TmmAShd;o>&fl]AJ^K<K6<BI.]AQE[sE[p7VPofikXn9Tggk!Pie@
V,uAr793<M+6'BOW"Eo9M5TM`S"3im[5:(aQR[t;4dRHL-^oC(C":N$S-d'h,"h=qJ*:s=eh
Pk`892p*<1m$eFU$:#I\c]A^OWFVR'fjd<0/k;#WG,>QSME-r%J;.<p`_P2GC5m:e''2-K`'s
s1$VNIcf99=SL!5RUYPI>>j)8p2lpM,e'R[p1sr3#I`ijYp>^5jm]A7IbFFR92ekS]A2B;GH?N
E^.0Ok.lk?i=T/Hq12`4%k=aKer!.T$OB1,9>MC22^8(qhHD$_#rhpn8Ztt&sI5,KEC16`Nu
jR1'i?Q1/CaD!a:n?37Jk+Q<5T:d>+[ojV8Ih'pFp^C"VbsRY2s#7t&@HOIW<j7>jQFC7b?J
l/moU?P(]A[KsrigSnD)cn$.Rn:*lZ)E-!M!VieY%ps,tsk'1><R9X<%4'1m1L0J+.L*[^(4M
lR6)Gsm.eirWu*A&<FkE(/<;l><<Yq:uWm1I(r=_tS!k#kV>`sW)/F1]A6dq_OA?#g2Yd&gpa
`rjbJ]AS83<p[=cju:&.5W705i7\n7]AUmmbcDc0cn-gaD&uosY)j$su[m,Z<Oa]AADS.)1,L1r
q*nikA<8^$G3ZX0dN,J;-rUg!LH%BHgd\G-7I#KeJmV4fMt#dMR_1M@!NWl\2teeMSnmM-Yo
g8s(S73*Nk5I[\t:=llaPLkm+i^:S1Wu+5fRMR5,GTq>,b_6^_OtJ*o@_:+bXp>WaA5f8>(.
$h`EDQ-g=n)=fIK,Z9Kgc%SEQ'LD2Sls=pI-2B6,e>IbH#UM3-?S9D+*s+MaTtXrFX3tZVZV
"q&=&6op!``%OllXZ<GDXsK%s9]A\\*\L!Wl<V$UsGZ%.;c/$NRSuVB7i!+Ru7*LU6Gp<cX?I
ugo-p==5KrX\NXW9#H&D"AZ"pR1tSGd_5a,LW#at_V2]Agj-.rstZJtN9K6kXVjeL2XFB%1*3
>GWBa>)C>]A3l4Ze)"5?FKGI;HD3EmK2e>l.NIdjlS`q5Z7(!)m$HX=]AoLUnd%'51L:`tBAB\
^#p]AI-_=_?Gee>oeN\<<%&PZFO`<iifV+_e?RklmWXAgm*lGZuWL^&Zs)b<`^)M5kQf997q/
!"sm('hE:h#r,$%F)a/m7Bn/ao*tQi%"7&e@id2[^-=@`Y]AgMl#mgo4@-lWCm\/KN=J"!A<.
W&"Iur2J]AIc3_7XsPK9;u[(0<;b39'h<'oq"%XhbmE:J&ZK)-#TTWpZnh-gcKPd3"^XHmRW<
.`u*ub1$^d4N2q-[a8V@Y*F9k(qq6b3/X?t'802-;ps$AW5)&dZ=%ndVl^FO-D*`&\lR8k7l
Y!VtK:3fj..h.gY$aJ?_#\Ud"`FqmA?nCbWAH3cr)`rB,(u:<G@I3TYp<=doHYNs"EI!#M(s
\l5B:U`WTOO2nQ%J*&;PjN;!Rn&3i'DO[TMi60V\>!_f7<t@D,7fc3^i(,Su9WX$baj;e]A8$
ceCW)<Z8?uGg.H.6EO',rm&Wu:hhDX&piD\HY)!=N(fR*4RQR:B:\5s=W5MX=">-qfYPI2dL
/(^=\LJReG'2:jc?r'%["aO1*B2+\.)qD7DY:a2dc5D)kVuH]Ak=dRNC$dB$'cmVLAY_*0D.(
d=nX6!Kf0+8UIA*8W""@TX?G^;Wp'@g^rE*3LTcBa/^<_6bt6BCeAE!qG)iTCL@8*#of[$HR
M_`3\^;/@TKMMaal@-0]A7N\*GFmeI$(cXAC2"q)E2e=s&"a]A-?XE/_Y$f0cEJHOl[R7O,GOh
WTL/Y#pA").6oYRPp)oP&]AIkS_4j8haF>)(.28K?mgUV^IJ*1=rU7JQ#%&AGDS/`g;@0gj=L
\K/Z8J/JkUN^8T?^fTb4\gjXDSbd,$>3e"s_pV&^nghqVk#H%CaWBmH>c0RhI7clQRGXOBm:
cN_[Fn'K^4'9u8YK/+Jr5GOMh+n\['nss,()4RfoX2=T30^/>5."'`*1i^ku6L%(#L]A,0gg`
mNI%kV]AeJ:(Tk1lsQu6o.lUFU*CfAJoT7O'u:CI'-7piGOb)7^4[YBSg;:.4=Pt4&-n!M.Wm
S8`hLXp*m.XJe=)/:LYR.*a<7pOgBN]A-a*`jbHcUL*p/QCtYf'O=8*QC#eVSOT/*dN+?U;U)
W89gB%Z[uZ@7/3=2eH/OrO_j,!*r!Z8%AbCrr<P2&%/0NUgcK*31RG2oUl6j!j>rEFiHeY1_
HHFVkAX9PW=cJst&77Nn>>`N<gR>&HqATF>"Uh,3<$^qVm>n^,CUt\Vms70FA[C)^i)R-f3c
@2lH3GfGQ'_4&Kh"3W4(_.)'j`?86\29q;).b4T3oeJ$''&#X7O$9(gkASGX2SB2;L'h<fl1
k]A5&,G?f=5UEM6,nVm3I1Na]Aq(?$iu)T58=&n_MJM"_W?aOIC381&"7U,C,K)!ArO\Y4Q1#E
Q"IB#W=4ReV/A)9L%;KYhmBidIfT^ctZ2MMZBfEpomt#Ar3/CH6H9GJ>t;K%sml>dbjKaYsR
!uU_iL@@8'D[*IZ;UdJZ'5;8&0q2#b`S^$o#"0doDtHE$kA=#7hbU(Kk,!rq)jGZjVq7ercK
>oKI[l%;C7!a!Og^<?AO]ANs(Fe.#[aq2)]Ae/gl"i93$]A]A[H_te$0(Ma'5^%&l_5DHA<4+XME
s_3*;Y0`G2lkLTm_1$HY4hq[f5dH'N@58a%a9TZCE55qQV8ZY<a`Cf^ZRY-'(BQ*?OnE;)*L
.qo8Z6G/"8YQ`mudql8P[(.F(%Fj&X?qJ+BP:s5s'(Oe2cW1gjO`?:3_"^h;__I79u7]A")C%
^jGCDW4$Rj4]A9+#+/.H5CD[-'#O<,4+rEh[UL&ZDL#mJ(]A\&Cn67CUJs2c-f#8u,9FgYC2<#
\:o)&9.$+2]AkWS]AdQ2WMQ>[^^qW#E80D;eZ+e\H1K_4GJlm$!gesqCFemeTTfZkf[T<nFgOf
EA(cTD.<MgIhEAl<Os2+JX=u@cllYjX2k*9I@rbq5/j:K"*KJ%>7\D,;k>)rBJma?%F"r=i$
n[EZl"KmKto8)[kltAJW:MZ]AChh73``58n2<A27_fZ(6Vk6e<%dEt/0ojkee!":^.8O$I6=(
>HIWsjX?!=AUtg7.SDR(*^F*%4o,=J(#BT!Qq?pb>+XG.OB"tYBN"U02plncbne!I>-JRqki
I*G.#css-=-&s[FBHOX)L=m)C@W2)\d?+jEKg\Q=ld60g#aZZ/pd4Ab1m9]A\o3<d'40F?[Iq
Z#p`2\fSfZQUnY$_u++"T_H?!l)$c\MW`%To/3lH4oL-c@"?2DWb8=Ve4-4r]A>HU#0?epc>b
A.1Xd&N2@Z+6rlLS&UY>hmHtiC'6tZFYO\jEeg"O]A=VYu_:b3]ALBI#5'8R]AsQ%:L:W*s5Ce4
g+e#SUM]A#7eM;<i!YfUCfQ$d)Kn@cG/RV[b]ABJ)<h!5\<S'BG(>'Y(n>=B/2usW4mc,cW7&'
]Aar[o:FKAQ7a$(4Rf.G`*mY14Zfbnh0T"_e.$ngCb?W495p7-(RD]Ak6LhMKpp^,UO^$h#j50
&\9hm+f(B2Q+%<[#G+%28;>7m[;V<'?Mm((H\2B5V(]Arj.Q7b1$U6EGBo9hLlf)k<mE=t+Hm
,b4MLR^EjN7_qqgDXWiE(XV:fOSFRM%0TE5]AJ2.iA9@Zsr[p2$gGJe1?`R2Wt(K1q1RL)iHA
UFe2S2@e-`djnYA+fn!=,<#ib77gACKfMDQJm#scC01!/G5H9(CI]A.B^I.@ePY!Ljdu6LRTC
l&p&hGXI5F=6r2hA')P]A2n;n[MtnSt*dIc/j,-NEJ>K@@&Y3l@Vl^QPJj:#!$-)/>WgQA7GQ
t/6gHs]Ag-#_L+c)/:Zo8-(tK1:H&,W%D&$qdA"o(ROLC,;E%?DnpAA5beHuFD/TVSj,!<<9b
>^M;J;.L!Yr4,WC"2[O28)=$(a3ne>!]Af?M\dbUYa?]A1X-a:!gXK&O8TVehB0kW<(\P3i[A"
"BM\\/AL[Un9BuQ[4F7%t(i=b[@1'K)`cgW,taHe-;/nqn`4j)0]A54.O.(q]AELqMg?4e?k+G
eG1ec78?>rq^)a/4oI!9rlf8oFT5<[-$AS1btFNo,qsTYB#aLu:7ADp[$f7>4J"U/06^9spM
meT$I7j6Hmt=9]AWunr8ZX"2;5'8>+uMCbe'CEuE*huEk:]A690a`?,/<cH_i+gW.Q=7(u)i%c
qg=2+sIbD*i!W4#85pUlKOnBi^IM:#QC:pP93HUcqkl+.*RA=?>nnAa\pl0.3Zo:<RY8;PsB
<+e@%O15I^,$SUSF>L7&XNb@"&[UZeh^JX^Z0)a&-,j_hCC6406qPpAKr@!bIEmKC9Ld\+9R
f*]ARnoq?)4&M2.Xni(aea^,UfKnU[a`3;nh4`jnucZ]ACprISn(8hnES>4BCM/Z+Dd&`LP&J5
X'tInQ5f\2=tKEMOR'`g9B/*?,C@8Y*8S<gJZ>Rs]AGjTfoCZl6_NG@o*-`.Rch:1l]AZ9!*lc
DT505'Cno&'[M@*2`ICnGV+!gPtoD/2g)l@VR8<4J#4P'6`8UmW09C's'KYd\R[K`)`\2jCV
+CCp&.RPc;AVD)M<d#]AtWV*B%M,dlj7I9ek8R*/`U7)p:9UH?*5F`=p+Y:2kub>:c4QhY78B
eo&p@9ago>YOld7lI#^dgcb7\[iYh2\r1FbZ#bC:nME'Q(&n292WtKP0N1127ZF?:m\O2HYX
rp5Ze)ROIk*s,(oRG']A8lI>"&44<YlaE[##kuiWqB&b70lP3jfQ))_Ym+<8?h@mTVehMsPr8
'tiT".QTd+L7^p/5\`a7VbDD+mj4jT-1[,i8+gt+QtcF)"[:UVCu-1:dCq!WiF1-/WkBNm9'
a7,4JbstC=a(j)8:e@m9MqZ"eq"9%2s&R^/rhtVi#%b5PHJeJ\7.1fDTrD%[0V89,SLXjC%;
2!ac./XTkQ\7JaX11-.:.A3HY">3Yp.<faFrmW-q'T$2<)Z=i495Zguc_m>$f:9'uh6bI?8<
7+8fKYsXpIT]A7m'@`,r(DO5J'=PT]A6#Om^7^?qJQaZLN`niAm@]Aa$3Yo6D7CnF<fqcH\FA_H
l\[&0MFU>e#T>Y0kN[f35\B!4Ri/8j+i4-L)jHYE?E1&mcsd_sC((R0Z<jO/.Li*c*./p0(i
F2FAWKnO)j_5kSK-b)[,O8ZscjUGXcbqtseY[]AX\dJqnV]A5Wl==3Di;cKMo8V:KJS;.BB>b+
]A[g/a"FhMM#%*e0B=28+n'h')4fCp#;+>A<'+PPd`;,OuMLq+jUj,MTVuqiY1Gk,(gJ<:+]A8
J,6jX^nmFBP.i!oT/Gt8/n"l-,_WJe.d1!hu[Mk]AnqhGm<%\Hf2FH*8Y,G^OAm5>]AmPcKLp(
)8[W#g`LukF'i*Y#1I0[oJeS8TDIlAg5\t%jq."0^=/F'5.kWaE@*Z+7*C@-A+Rg8Pr\0eh6
n!_I>MdM<\a^:B_TH?20qu#Pk!Yp32_t+hU`;r,oig7BskLWM76PY(1GYNXXgB"0miK3Ce/b
+pk=O<migcmY&_HqV#t3H``oe.$bct!uCPjUEKBRap]Ab8NgMps+,t24`i$/'9RWuV0g05Ag7
@#$kg$^5Y6ZH!eC#<l&qKJ7.U+Btp'IemfQ8'L)>Q(oST&4R:TNKse(7#9Vsh;g9K]AF4n'4(
bgUKEDaKOTf_i@X\1\9TbpF>[E6*!,SnCh9,qV\$l+i7#UfS:fe`".SG;`MLjdEaR1+^\q.i
lbUKqhKA]AK0L>eQF]AtFYgkZ:qH2ee%;jS749VZVD^&0N3PUsf%igpQBMMpN9L-lbEX=#:'"T
bVrJ*TZ0kt=E88Uucb?\gpF#+UF^=YO=%U7cTfjlCl_?=_9<g>DpbXt;677qPS,KJcg+U<Sf
=f[IV;!;,(?0j;CB2@a/-?X2")Da?G"K)"1U"p)KWRr!L$CBb2.8/dc0+K')g,dYl4+X`>j%
[K>8ucEJ"^J'&OI#'mOCRbbI!J3uOg+MWb,&.D\;@G[;rGNB9DH"g9\.&Jo),[iIp0*OJJ)e
YA>S<_<dBpHpR+oceH:T[`Kc#P@:d3El(pdb\I"MIIk#^ag,;M^2&IeA;DZ@t@-^2e7&4u"P
i#;W'R_Zbo>Wkg"1qY1@[]A)2dIHJ+e&a61CtKdK/]A6Njb6m@m9=]A`_'GY\&8Wt#X6H]Ase/S7
tq!iuLg2FQs<q2bllW$SNVqFCicF0(Y922&+@8njc8?iM.\%F0S()u\G!&XBku0Qjmc?VcO+
MGHDuDscQnahF0+"3Qr>IcjX1fbA)$&*;`T.)Ir]AIg[mja/sj,c5UhlA2O,7$hal"M@Do>O2
`dmK,,FU(?Dc#:+)HT*'TN"C)3iKpUE["0Z`>_ZqZeE<P-Q?95]AVk?Z$AH0L8^NCuuu`qUe5
_FM^GK-8t2>&&f0)^A;^]AdM;H<Dh'6-MC(-H^D]AbW93L]A0_,%C7k)>NDf0i<L;\80=H&*mJh
kQ7Hd_bn'H'["77glV-)(;=&]A/of!196T%d]AJ8T&o:E1*>ICe_tG;_qOc.j=q2[QHe+lc:%h
LAO)$,XX&VX+]AA*%F-%[""+FCj)\R&#CHY+[0XJI9I68obJET#[!'Ze!iW:e-T'Z(JF#$LVM
CsrfIf:dBu6R_.//uYnnqp;OZ^UKDn*jC%G%ULNjLpVF>K6O]At34icu,R@6>1ftYH2$PSt<m
MjSO[??"mL1DpUP$JY]Ab6"fSj+I`Sp'BV^!eMF[n_"c)4\D`p=:i&a>>4K9$tA-/nlpRWVa]A
k+2u7Yp>t\$JrkD$6"Qn/[+CC_0lL<eSJ;9?kRI%N4]A&[g7JlhiK.!;g=mRc;rq*ZBCVn]Ah'
GN7qT2caR78Wc_,85s<B"n[-C's#d5HD>Ik=^7E[8=;2s!lr?.@St><e4EgCVmi$2QBT_s6V
Fb-p.a@eL;n%%ZeLpRJotd(4,7:cU0.lRXtSg)`tY8-fW_5/&U)PAqIh(W*<l(U[U<f==`*s
YoXo,Fqtf,$nR%KiSfju"\tk5^OG>$Dc\R!p=W;>,k:e5>1SKGF6bpSec',,cB[WpNb7e9U*
Ac:"TL36)leZi8uAuipYUDnkaFNQe9'<lgDcKP`p43eXW-AFijfDUl.dDj5,TZtn;6/a\">E
(fi"',T._ZF%(XM!60:=SJqH-@Vh&.r[5@cTY--%OAqsSph5I=Oc]A3P.(@CJTLh:]AIOkn4(:
-@2un)'TgL#&K(7WellFa&$[HVF.`H)&\_A@J:3ZFG@hM(C;L',Mao?/E;7G/H`3C0N/SQX7
-&eManN'EGEgd60qg,k=bm:BauQ.4ut)$+M*&/VfK16]AD48mSS@?q:X=.?p*=?rZAu']Ak(aG
IXlSY\>7NMff@C;eSduIa.0o.N3\XKeGn?GBH6p0q5eS,rc>h9jXmUWS=OtgRi;p2V/)hjA5
=,37W3`n#FoV'F)s&".Lq@F\J:M/BA;Ro:1JDIJMp<i4D'Wn.cA3BG;e>%$uY@Nc86fAE4\W
$rbhb)Zf@Ea>u$fN_hT4[S(KY1Ng94hX3U[4JP`iWp1XJXE(aF;PYfarZa^_EHba!IAj0san
#d<<+AoncTAXV?UA[5"&&TiNI\2qS^(mNnb4th.rThKPmBs>H4N^OI<AIk?j5[tbYH]AU#Tjt
(9LepI(DB'k^"_I,_QCgKB8^GNA.]ATj,`@r.k+']AXo-S&c2ma#Hl8g2:j*YEZF.t4j[ZWKIh
ODX5H5B9!<eBeci%6tj):l=0=Y2_pA47SiD]AKPG$Y,,nLJBj)25ItDugUY<%-B%>VOFVkr5s
+M^9acmDimAmfL-TVC?69/X>qRaR(U$HmIp\\tM5'.D5_ru!/J-i9HdcibWMukR0.8HeWq,u
9X&jI_eE.j(di2sM)B/<oWc:;cQM7el"?p#QEa$)j\OXQLI8/>R*Fbp2DC2ugU]AeHApI/e+l
#-pNLq0q,@nY7*l*^GR=Eo'M:"t<+0F@H/42dsua3b)U"XOO^1`@2(@2^lBVBLSR=V.V'EcS
mlr@.ho6hTO/@C>r8:IpHuG1k*WrGd@\`8"j?WoJ8tbcUe"S>!',9t,/'ohrsKc-P7:+,=.j
2Y1u(=16?2T5]AiN@nerR$UZ;f;I7(Ma[6L`\,=rc;n3V]A(5FkERB-7$0<O6X=_mF/BpI$kqH
jL@\j['.oDa<T\R?Ve\XYi(ir%0&^fZmFF]AI.,e7r09c$)nQ2``B9m4Y"9$E_RfO']AgoS6l3
mSB$9H4ir0R>`bAW*Z:>=+3[Z(es\l&]A.^k,7s]Aha:Nff4N@kR-J=S"Sor,BSWJ<)\r\;F5F
CKEqNQ_`de^iHI#L!(4\b:-ns)WkVFspfA$1B+!95i;WiXun`Q.AH>-h]A@rMYJ'6ptE\o">g
#R\/6gW^&.K?RC_$F;3@?;4!L#:pUqFe\=g0M06K2Zg!St20@-prdiJJ!`lH'6:/8tL9)F5L
dXF"DMk8'!0Gn'`#C3!92_^U)<Z:7qO/X+O)B'Mt,pjlcg!GZ1P`:*<-j=XM5gLbZV>V@VN!
g'L/\L4Km?Bi7FR6Wj0*=g`q?#j]A?srEY.pgWO,/OtH"U.s0rjrQYA'fp`L%)+sUGY.ccL2,
K-V%8NXnCo6a[RRrhHQ]A=20U7)*,a;\8fc<R'q4Q,pdHl8J,4dKVWp3V>4%cUd:(6GP>>l,*
+,ZAFCqmCJo,2<f7?.2o!m>LruT56@XjQR59s\cZb<e]Ar92Hsra`c,=(%$?%W?\J<4)XW=t(
:\Q`5h1!4/0"J$E!E3'7D1XCpV/5Ugr/i#O%N?`7F(*s6:uQkhc%KF5q]AH^JsM&=hu^B[#_2
'QhJ%;j$]APJM?Wj5RXcoZdoQ(H?5dp`.C<2CA<'GEMlt(ARTSK6S*ZCck%_fpCCE1N?<a>G=
SIjP[=k5oo0US=V-QQcgVcQOO'!,DIK>q53MqmIG#S\$@]AueI+j(+*PWs9'l2<YmE`QfO!=#
GK`#]As5ZRYb"S<;m8F]Ai\'mc_Q+$fZp9@`WrEJp*efXjRU-%bd*i=P)X2aU7;Slj]AoXJ2c+o
=dnDBB9A&6MUZ[l[AkMeVmCT7r?9<&!3qk;qfRG#"6f^jM%p3[ZeI,*2\U8!58g?@h;.5XBi
XQGAM0^lSj86a=C1R?t[hlA`W?gN"4[4K`-D@p?jG2:BW;eail+*Q*<hl?YYi?It6aSJ[CY`
f<"E&NRNb2A\263l\rdjqu7_RQ1ku^UF]AI7HQs_F:PtsQVSm%5V]Ag7aqjk)\`s(nbAGi$sEs
A<>);uu79JqP'&(V4$;uhj:F(0BQs,Wj0>GD<?.\U)nk\m=1ZsrSrSQ6U-QrL2??\$$EqYqK
N_^^`>r:A6!*<cFU%#g2%"9\jN'-WZCc7L!'RarB?CRpHUE5,-Wh,XD45C08S11q]ArF9()=!
j'7&%(AChM:K/IGC[W$p$<B%FO[4(,8B''eA#^2WhdK<kXB%&>_V"ATD;JQd9PSMkc.&F&ak
r+j[2W9Bh6QRCRj_q"rUOM^:_+[%2dKN?uqF3OeJIAci;W"2)H[.8,7R1OZ@'mST)1F^bB@9
(V:T<RlG%!F*$^N'529;-A<H)geVg)SDC]A%V,A%)P,g.Q5>>XkI)59Y)Y6GMiOG8(>$g3CKh
Z"5Xo^WS35WSF_9-==H^QJ)TNLH#J/Oi8CCa;=T9lVh!ERCIIl8q,+s\A\e/^ea0?&fW%WBN
Jh;$]AcN$VAXrk1KQe8kT&jX??".e!;5(fXq>ac[lU;IA^2[tu2BCes*dWKu&\NE&\uU4WF2W
N.=>*/EKlS101L2J*/=6M+o\VT,oegK,pfV+%>4:?4C"ACPV(,F15e4WGLAZ\<uM7Q-98q8t
-6)VY/cYhKb6ZBR4pr>54K\rQd+[EH@hI6(@="[_p?oZU31LhMXB@GX1<;pbE`]A(>+2$`45S
k8]AU\KK';nZ!!Kaml^_]AjQTEqM`Z%s&9YG-T0HO\[UUXIO$Nm#oI&:]A#_*DU<p]A(]A,*i_AkX
WL\hK0YJPNT&6.[aWlJK*#*"s0(%_qr0.p,=,3ppBJ#UG8NA6j4><?n*B2J[itR_V9+r?E$)
7aRtTo(Cu8al5M3<BqrJ3@134ZEAN=C('$n0X(iIIlS#g-VBSds5)_pg.qL>dLlk^:=.K!3:
Sd/sN\D.hXmN`_n#cbu#!F@RZ__5OSR(7XTPh-H#9^6p_buBrJ1YhI@UaibrPNH\&P`p2+fY
/YfmSpE(@f=jna5g'IS0KQlln0&`E=E:?*t%@;!A"(0h9sghE;B_qY"D8o&k5chD*_N%tiQq
ri]A`+\p3B/9tIra!F1Wd+-,32,]A:4GDGPQ_s,5Pn(QX1&f4fKS:O8g"]Af29]Afi%&rC3)4Ph(
P]A5P*E*dR"!rX1-;&W]A_TaCSR)0^R55=12)#jg$1cf^"\q72m;ot^5r+E%<jJHQ0rfl`d(ho
fI?O3bOi!+),b#'VD8<gF>:t<HWie5hnNNoa!L%RdcrsNCgMFH8]A5&3q!R'8J6u*)a`<td=7
L[sG,gsDC?+e)R#'qaR0i9dDf;?h^Z_ZG/YZ4'QcZHuunERHcC+Qu*;>]AQXhii.nd/\#54kV
F-)t1ti9T\`%dT?%\St)-!FMU/e!-o[<W4<R&:.^;B/J1H]A)iU%mH':A>Xh:hBiYgue#+f=:
7a><l.51EL<8\/sAW<'K6mFqqObJsC67hCY>TA[uc+X[Ifk1+VP:YlDm=R3ub$7BocB:MdJI
b:`mGmfA5op,X[pCYd#9oadEHpZ;J&W@A<,E_=3WDcnlD70N<db4gMTu*^Y]Arl;C.72V;VGc
ds,fSbMN6i-%jt4RI/,Q;dZ.5igFR,oRQgX*4]A?tTkDO[oD@r'.Q`L]A-%QY:<(02@k(_iMBl
Kn&[V=e11;*G60\ZnZY8sH[o.^OaSa56m<pA(B^]A?/1:W>UZ0`J-XmCBfkuC%bCu-i)lu%=r
\-_f(g<@Opm+^R2!9%G".H'hdjcY,W1=n<OJf\m+R8&CTE,qL$%A]Ah&Q-HVkB;?kXfWcrnZ7
a*7-@U#F'#^u-rbgkjc9ptI>DU8%O"+Yq4XiU6*Hhnn_GjB<nWP6M:iHQ$:5HGhc(2-##'l]A
4gdjr'r/n<Zc1!ctJrTbS4FP!^XZbIe-;L<eM)!9!t$qu^(QGD-@>*5b%mn3">+^V?7C=BHt
-c6\RnP]AWQs'aek`?@XtJe\3bu*NYH*hY&\&LZf;`a</JN4Fe%Y!E*NC"RZ:/]Antu[?Csk*^
'\p!CS'C3KA$5!nFGsC;bP<2CBp)b0K(hTl)ao_aBc'E?K"?$!p.h1k-;ML<AI`ITlQ+CEXV
>rk416\CF>@("5IDm]AB/>6LVVO7N]A-/FO,/8$J#no+'l$khY?2Ju'_+fO3sU3q_Z0f`'L@m$
OP9SC+Z7[lfFMu9c*acff4hejf0N27MnAP)<&+lX=*fD=E</k]Ab\;@)"M]A/I_e5H;6Uq5%R!
kGc8;*+VTcq?/+u(^14Z<m\S^LaQa=T9-c8k3%bj!NKj9a/1QOgbT:_%P9oa?S3E%\%(n#Kk
-ZIjCg8oYoTpEp#MUBb1qJrfc[M,WTEbPFG%3"M>2/M8ZI!>u`EoC*X(fk1@/=L\pJ;i1O^^
_^4^[U(j]AGBCD)TdS[rF'39#5'Fj[Fju\`c)pGPgBDDspqM>)4h;F$`fgKV&$X\#QjO:b^8O
D)'9Z_kb50G<Uk[a?IG:Jt[6qDYfCVsa"1l.<_!.`-HC#IGDQof3h7Eo#PM=A:WG2M[UZ-O0
a$ShN)1OX%=DM?M?QdP.]A7\.oDA;:,<f-sidN<Ie>F[!jY%N2%l8gq]A?6)c/$Xib%a?6gdFg
N)@n(,eaP1R$YMN=X_<uIZqWk8-hL[/RGF1_HTQMt7@%3UisWG3;7^a9`\T;h>_aP,m/gF"6
FHWFP&=/GM<mO*G?Z_2U$mVccT>Rd!.-(3>,,DM!:pJV%'l^@WeLrg6RqrRE]AV;-UUBjB,b^
%Kl_/klGEBU\,sigG7()=DhJG+/[f#6u6^U^>P)4+IojR5OJqb=;<B"QXnI-r\DWC,DJT`pE
-mf*k?T^luK:o3mh4d?_pf.[`d,Yo(0F2=LSSdaK-p$b.(UI%iRPc;D3J^CUUe`&OZ?rRoIf
d4JPbM#>Lg<\#UMUJoPCQaK<-KrC$Npk4=A^Y9f/r$<b)C^LgdJ+\]A%9!kfIaqHs>$,=7D1T
:^g>l:p'C%q_ui@t@F@56^r'Beq!&V-X:;<.<toP@Eu'>_,rbs%@!\,fR"jp-S;>[s1G_[T?
<2_lo7IY`ip9ch)c!)72MgOZtOV-sA$DZeIP-qk<dOO_c*[Tj9H"(J'k8-L]A1%aUoq!$"^oF
'ns^lED?SSmS?J_Ke_^%A_I;F#3d1Fsn,?iJuMj[LAp:\l!hSWXbF'e8PD/XRZU2el]Aa;q!<
.Dga8nFCLqnb'N"o;ML/2QN(V954MP&h3b<C((LCt3Xm8Mr3);Z?1B_B8Sj6(6W&FY9s6s.)
,,MuESt>K7^cGsD?H+'qGHg3a0erF3^&M6maTegi?iFenKXmp*\Tk"MNadY#j<i2+bo5;9bI
P<9UU`eYpJ,)>^NCB\3^=bkM)Cd`gja;^a@92sfQOAe+]AC)6`X%$Y_n?:9OELGQZ@RR^Q%Q/
o<bXWW4.cJn*DS+klVI*@Jnb+S/p5/+6cbtUX8M=+pa^l9D0<+jZWejI;]AqtsiMR@,4j/>i\
`7&o(^jn\6M+>OB9RtH(_3I2RJ#_ZM]A&Y#FqVP;Q9b86?)Bi-H,RhR^Jc,6!u#Qn^M/D4s4k
CT(RnFjnF:&%"ie1HpD8:re+0(Bq4@=N`r=a(IsS?.s6m(IT<e`R*W>_?b#b01@Dk;U)[JXo
GHG)GGH#l&ZU@\p7-\FP0gI&<s//T4GQ4"I0j,PmSGC)&&R3J\s!n#?.m8WDHfqh%DuZHFqu
8VRJ%o]A#>-XQbGH1as;oR!VQSBKEnh5mEWVejqUnd5F;eU4#erD`[#GJU+@r3mtL,;^@E^\[
pKXq,anM0j/QCr?<f>TmUY!q<Or#c6.)6+*2k/_3DkH5=mS;1VO^#rsA@F6KBmKA;^KP#H>+
P7:'XsNiZYR(8mLu`(KdL3pML1a+SQ$655MNGs1?h2^C?&!=12sGq'>"25^":UEWhFa"1hOF
ptc.`gXO8M2TAioLp<UI<(<G?13aiUhp6RrtWo4L.,eO_9L9\/:V9NIUc0aJYrL%;"&[l9QV
-J`,b1<p'EM7E!$"5!#"&u\PAZ?$U42Q#PPFF(H/o+*GUM5qUmoC(g8#V`]AX0&qeS!U>p$jV
jRu$'`1b$Db"?';;J?XAL!Z6b(8cbDZfCe/Z7's'4NC87PWAEhect`OAc1k=#n`OA<dpeQLp
0:2:=8jZZ1QDt!PKeIDKR9g!>Ta"=hAU<`r':bLBRh)"!3\I!`9M"D's0=)-H:=]A^&Sjn<I4
o^s8Ca7o\#lkrP3/sRn5XEd+e8C-oh7'ZobUQQXC(CYR%1S:5lFQ2'"U3(Wn/1>n[Kg@FgDH
eK5b%"FKnj07_84N20"/mbXYi.]A)'2I&mld"\*qa@]Ab,VUG)',1$H\5Gu<Y]A0%?%1L:/r(!?
!?XUSrnPeEpQeF0ecTStJ!)[Oa[r5Y.Gs"+<@5i9b\Zin45YE'Y.T#@_jfB:al?hZ9;!`*)d
*^`i/h*ZgLfBTP".?SIMc`C@Eb$ud:]AXPXba!!:8MQq%]AhuJ/ff$q.P\NjW2+a<I2>[u[oBB
'!Y2QXdup%`(5)`?.n4W`XfW%P-YktBnm^E'44_6j=B'abN[q4\1-[B75q2ejq='Jd33\"=A
5.uPo5BP3=qq.K'j==M$FWn8a_+u4%31F2>`OlH8a%J62s6DSf0=^Tep@I<'`(e.NJtPJ\%%
QWG//c7?3.&BK9'):&4eLXTthF%\jBXH-o:u0p$04UO`?51R\WJ,4u';[86DT@h?Qfq9\KmP
fTABjQ?f6sI1mg[>uU+he@>\KH1^91?DQ#t"8q`Ukg4KR-AE6K/GS#3?Vl'1C=^1UNGHK?.'
8[rYL.\+`N!(#IG4mtoUi^HD3%VDMo1k]AepCK4RW[VG<lMrS/5(c^K2n\I8\iC*XasqfZ;Cq
%@XR8kU_j+\`R$iI\it=^/&/ZZ-$'s",BlL[?Cp8\iJGRgNs:fb[WQe+J^hPH#hec^IW^R\%
&d:cN(OpU4?mc_67"FgV^%OWM_MQZCP=0tAqH&%N(c,XFf6-A4R?MAS3a+R\6U:hP(`n#0eR
IG@$j%0ic-(>(kZt60#B-@Gfbqb7.lCK51nA,gdEkFDjRUsRI>f2^5LZ^6UEHsS&\E'(OB$$
labX+dDd+*l3E([HjZHKqF72h9GMDF2F,ul@\F$'T=oN$,p>Dh@*nR7(M57ZfR^';i]AEkg6X
Ga5^4fFLCU$MtRF0FD#A@Eb3[jW"2buY7kN[Z!iZeP,)O,>:(?Rjg31L4Sj%R;4l9Io$iC<e
=F14IV^!.WUK$,&NK&3"nQ[L@NYPT+,B!V&sh&Eb<UKepfN/6sX>b.-E6mpVP:TmI2bUGk7c
"fANLFJJe=p!r+5\It4V,++]AVP?\j/WZBK%<7N=fjr9b=QC]A8jogseo:0KR)q<4g',YFp8ku
s6B&FgtB4[4?rZXHpFDt(f?@)",>WdFXJp,mgYUjOQ,EYe3rJFgW3K!<.2!@&lH(guQJDOi7
J+WMh4`JF[J&sn#pJ+$e:"#&S]AF24g4"Ro1hgW8^p&/A02a`e-r\q"L.oC]A%q>FDY$RP(0eK
cGpd`qgRHU]AV\JT40X;3]A]A$+(g)5TgsD=?LQ;sV,T<Mg""npe/[Ha3DkjML4a3s\SQ/Bi_.D
?[9SuhXF#`?-9A%K\U8k@9e=A"LAB,!NtF\&fAGJUQLsc++7Ng5p*1<U8M@WUhK#LDer;LC^
UD2m:q55/@J0(F>trIf1>=^sbnQuF31aq+Ac2KY+kGq(`>gh,pnZ<.OJ^`]A^u".Rc/C"4Pqf
T<_/$US@`N'@8HbXhs!1#a&h-%/Q/U[BEq/lSjgr>AC`u6&mg-1?k$d+QO`)>rIr/j'dLPgC
!5`k;lT"_W.3L'\4[TbigMb6!"g-+o]AJe$2X5DIY?(P-2-^[+N=m*\"egq2`(KaCKjA*Me+-
,^.o.AiC"fhN,CUK4ZYa-77(oKQBOkaR`q:;8$=KRg+8_rXB4;W]AU6kT`K'&5q7Dbc$Ml'fK
oR40UN$pQCi[+.&V]AR"),D<"WQ)(%&(kFo*r^$^?qHOJ@=:!g#gfJ?e%;EGGUR>L>2C@=<\R
V]AI@;*[FcK"Qst&JYnS,9S+jfDq0`dQ<'/HZ((#-q^np9*D%Lkp049TEL&^MNEK>#bcrC+G:
;hS.OPbf@o-7qqHIf1!]AU&IPSu-TB@hJcKgp?hXa$Z`67%T[D0S-TrY6U2$Qs4'gM]ADG%RY>
<.JXI^BfB&7:nDtL4#oQP.a'8Em8uWd4Hna#hL"eHX/3dD;"_:/BQ'2-[sdWdG?`(ih6kIHf
1g9S5Cfn+nJ5dFn=FL,>uH5O3M[fc+qIl$TTYPE.$gFB*,HUkfVS\^4GE1`>KRck>:>Sh^nD
2UM4m[d#;9":X\d\)N[]ASW&E?^O7qCf1_h[,7#<!E\3)ANIFtHlABbK`cH<)c.3ClNV9>rM.
XT@HC'9G':Fg2q#p1YC)caZhR$0`a-*9[*XepW/jC!2SenXI6>G<cR$bOKQ;dQWR+#\NV\pH
m3%I!6fq!WF0Y'ncZ\TB`0`SanlGKJ*ha<`%&fQfQ:a,hZ4R;R"B7(#'MO,-$B^1DJ.,/s8A
>E:7dh`j,=24nmo;K7mnq7qt"q]AE^N#]AK3WdH:paUjkUuhPZ,**Qco-bUX;t+`i%6l7%kumf
omq/N[bt+.b(o*,lWZ8t:2@pk(>2>VTXP@"%&&98Pdi4)VlMJ*(I(nBmA?R^F]A=r"[.Qj-[3
Mp0t@urAO>-"P7?fO,LcS/uY;QhmS5$KGp,GL^q==c'uJ"LMG!-1qe8U,J2_/bVK>/Ug^lm,
dqERoCBHl<n`0G"1A2i`CJ6]AHAK!XHrJ)Cc6,bcc$3_(I^kT'&[FXoVG$TIOulkY*H8F,dp$
@IJqerLV`q+!lGJ,W6dKDr1Uq0c>A;9<G5potn`'#?)(rD%L(6,2j3A@7JO#L,Y62bLS/\B_
r%]AEh%c;i<o-2t<L0NFo4M=7l#j27,.YoujFIlo]AcNf>?Z>^,8l5H(lp[SB5O;_[4<u+DPs(
f5+ZFZht5+8_WAjl$FQT+(R0"s==cTVZ/*>6G@i)X6*8*hfEHca:)9PVfURj!i'<M.6p\It?
HK;-3H^8>*(e,jEq5/SmJdD5UJ":C=6kQqPbIGpM]A9pRQZdF&&XWDd^r[,8RH%=JB.9_WYu=
W'f6:8\RX>R?/@)eJt0%h:bc\`H'Gb5^KlTj)O'r""e%0No"CABVQ-=CJs.pG))G$N'H[3F,
:hZ_)1,f#n:_%Mr0NT<R%iosc]Aql/)F#1W%J\e;d"^`n!)lhnt76QpjB#X/ZiL%S`Kg\LfN!
Fp;iKP+!KG]A(p(ZE>*1eQ+GI[R8WWj\3lO^mSZd&!WZNf%I5.HQ!/nPM@W<DDKDG`B1`ThVH
[jB3NU!f'Z"oI6K&md<0J.ki<Vt#Eck!_AVNfZV2?Q2@!d.pE2Qk1TlAIR-dS?n-m'q5)0FY
28&`c`Ghf'pl$hc^rdMKE'T<j,@9j$?oR^$n-'3GGrD)f:!mDY9-E3(Q:s.#H$A(Yuj0qAYW
,k8fe<mGJp2k+j9m8HbPp+g5(JK<7L]ApQlLr=@q:RPKMqNh$2/34KLL+?S*#X.'*hb_")Pg5
QIa]ARq@UfCoTmi+bPAe48qqJ-/NP\$aKDo.$bD)?S>V72e)Z+=f1ba)8V\R0c(BO[t.`CIQ>
jU!e%Nj<A='7mJ\X;D]A$4Md@"<(GisNNef5k79@\[fG&.Fb2NkZnQD2=$I4m@.BmB):$:&>#
S;q[sb.'d)7#8W6Qakn+,)I8tB$7C4<U^J%CG.He`+e=A%5lI'pL;`lG2"%8kUm!-?6r>0SG
VIS9^[dDTOd>ts]AJhUR>2Z63(q/s;LK?)&6Pp/Gmea\FJN.pCF6V%:YjbB!m^^^sn*70c(f>
D-(']APh3]A?fR(Q4K1G\e65Doi0Go'4k$IJP8HF[856!?-'U@%NE9+)\qSqum.$LU-QD,sC%P
b:d1H[nmB/S'W;8it,=7RU75N'BmOK,>,t>5#\V@1%V)lAd([TZP<r*+6q2ZMI*DpeTo2<5Z
FrNk#,g&jA":.=cf6)gOQW5DmZ/OlFD2_LD^+Q>;2l*e(0QHlWo9m&g1&Unu9iI+2X6@!`/@
nPX,Df\Df?Tbm)/8-;Z-tS$dcS"Ll:X$QGK&!sMi0.`']AEX-_oZYtNS_b:E(kY>BGZQ[\Ii$
q6:a*V57l\OfH6o6,G`<U<$>Qqm8NVs!9u,fUX?E=QO*3m;pL6p/2,6IMJje#K(GE5`"!/%A
&3=>DWgfdE$ALR(]A-p,p3E]A8q>Ot`;G%;Hc4=\G);47eZ2+6;NGk=\Na\9?`aXcl1JPW81cQ
3'?-K>nKfO?HH8G6E45\+",IjZtCs,=[[Uu?`hL:'g'+cnU0hDFuRqIB6\Ei?(1hZ@sBo\()
/#Uf^a5laDW\_>Q]A78-oDTXUEJK<mU.hpYl`1\PNY8ePmEQDp8/(VA4pjB$N@F`ELW%lrU[r
%DX")>+2kp9hRA-W-95Y+_RdQ;&=JF@?>2uQI7RY(]A4_:W/j3]AO#@j*`^e'YbgE]Ag8]AY?i_8
O^\sRD>J6(jlU19=,2mpQ/`nMZ/I/\#Zu`V'VXHP/BlFK>4^km5Xq\;K]AfpeK>P%F(C+Z#d:
1f]A]AP+(qkX"DI;P[fLUVa?%#oQY)9SoZF#+(67p\/o_3J[M@KP^1T0ola$`3L\5+aF&Oc#o:
Bd^MqHpi.(`oA^A'kcdNSa=5N*Y`44N%p'QZnW:YE<q2LW=M/"%9?i;ige+7\b\:o,t5@&rT
NPmc"/X>FnVjLrsqWo);Zg2K(U#7H%`-C9^\BgmYlIMj-Udth,C4uUNkVi6)X"X[OMk:L5`_
XmHU(r/Re5]AV2JX`cEBr#N_fG]A:u\.$B40"6lE@5sl\O)d;SY?O:l$8m;<]A)i"bFdkr(KRS8
:9(**n&sJ>i=F`=(ftWDL-FgqiT"gfE5$kj;&pZJ#/!3/k8PrRN1H+[j=mG)3`i'R*3KrXEk
c;+T2C6cA2PD@kAES1<_tGT=N3CT=$=>phqaL]AeeUL[4"qA1V<P?LT_lhGaD8-3#;2/<I&V<
DF@-TdTc0_8`)"0D;R7o'K17(K#V)8Muh/!NT@HjL;a+-YYQALGJ_s,HYYB*d*2tJSHD24#%
^cH]A!BkG$K4u.q;dYlu<R7RRa;n.S_iT$S&/kXS/MEL+cU5ie@^8e</%2G3Y*T66E:!-%OJq
Te7o$s?dEtV8_4\Ld,osM(hZ:Xtkl;C8X1!n)TIu>tj>D4?^;]A5#k+%4E>q9/?j#OspGhtbO
_h,W]AEA,!m#>R;HY5E'#S_1mnI+eXq--X,0E<<qfA9tEG9cAt6jPa>&lO%OS/SQf;IEZO]Ak!
&&4NW':30gh5d^r.CIsUq3Lj*^1Oa#jCB00^JEBqF!N?dTT$`j'4*7=Jr?b>JZ&kf^Z;<0fZ
?3HYTBmQ!q/4c"Of?[f-=V:X5D#-,ZL%W2uBl"E!VS-n8(e4(9hMJF/Mb-&CpYQ.&^ggNA^H
>$<b&$.Cf\QkbfE)==dQL9B0cf',g@11'kDrJcihm^S$'4+dd,Zde*9<9=hJ1"KVL-<h<ggD
HUm<9_T:0(;>,a<+D:+4IN%/cP(U%56lg;e=eFeBHL:/na-d?1bqW/GSIY^ePeZnpk/<U]ArF
nHY$G@;L;%^m/pc)m@>5b9Ps_g>q1dW;ej9V,GSrBHF7Ne]A(AmM#$*'h<gqI4X\(ACL(toP7
8c1>CJYs(WR$#E1/BB!8<?<7S!QIA?!,8KrBb^k_Rllkp@^B9!\s1+J[CXrSl21MC/itU64P
Dc2D5X]AiC6sbb;jDu_QD`-4dnJ^d)EKu=*WUk*g_6K@QF8%qj`ucTAGrWOt2rI1S*"Rdr1=!
2^,%>(gU[S-me3knHJ<63!=]A"(H*cs68m(?=rOf**]As@$CU;?&gtV%$;:jO0>!1]AsWpi5Iam
7Jp?iT[$q@=I#r'G59`U&<Yo[ZUfOW%8h.%jf=PSrAiP\VO.I55iqR+3($'K;8mpe=N_;q@D
b8tO#Ll]A")g,lhb?IgJE>d1Y88q(6?mVD!(\m%[gRelc%+R]Ad1@$]AL>fItXu<BT^3&`:hjl!
5=4+(?pB,;iTV8pTH=dnEIWhZ_B<?Xu10gZ^mGi=B@n'fnkqX@3%Gp09-))hfrg^WH3ZEV9F
bHTn]Aj#4<pV?CVhgENkAb?+e\'sbK$$(BQ3'GKXh<1E%O%j\l_GI"F!h@Di;,AR)S;.$UK,Y
"LfL0T-f?'8%YqG5B#2DdSB$>h2"`-SQ!E;f0c#roujkI8d9"`ZW$%sPJ5@$pG#.J)+QcEV9
*b-*-)l,SH5@[1?EGe3[]A/d^3'3I@W+M.?Lm+*V7>TT&HO`A[&Et"RP*_-pPSWB),*S/o!OA
qhe_qt`NJ)+)T,C`U3#_'%_`Yg]A"1f@;5mB&0`=cPCg!FHoJoIt94K+g^*+,p63kKWN.XMsH
!lBn/uCjr^Cd8+<UQ%UQOPm#M?\<\quRauVW@@G^g10-POY3^-b\8Pb@+,sj(oo4&Ui_=fB;
*A\L;>uhY':k%`9CgW>Ltgh?d8iTPTT>-cCThJ>o_Q7VtmFY2i=uO%[lQ>j@j;^,!;fV3.Aq
Y>/f4dZ.`VC`P@mrH!J894g75>$JMCg:ZBYCJ%m:*Npe*YE-62m\4&&+oV+U6CCchiaO<!@Z
buT679)L%Qu*8bAdL9]AMGfQ@XBDV@&bEe+&f^`dnUIjQfgT@$]A%7(M74faH_%8<U2eI]A37dk
DbjiPkb6EBf(.GKb'A'o&F@hd<hUR[F$iltZcK[@2(A_HPRLI%NCA*PZDQ?!Li@+N$-+qEL)
KbYl]AB.LBd;doUdAA9Y7]ANED8p.G#)n<)sjs+O]AI1P8B&f`Pfr^N\/P!dK0fDkV$W[>.dp;h
CQ!8[m;na'H#4p>$S2V+K0:F,JD9*73p[QTXqB^4EcF4A&&b&*ok:8;A.qUbZqg"$7*J^$It
$5kO3.=a+R>K)V!MK6KA="`&855<QX(1D+HQ3-Ee/`+jtqZb(&>UtM1Ah]A$F+c#bV%!/smqr
3T;+Y5UQpmKK-m_&OP1DNo5$^\Vlbu]Aqsa([KcS+bU)*5#8G=Q[U/[oFS6\.8!W[BNu"l^SY
_8se#0m:Gf)0op%LMI%f/X0gUP4K:LO:Y:.u\fT%JF70p7\Y!65Xn.ESrtnU2-r'VoV2^I>;
g;P9fEnj0jA8>g^RO@)KLm<rF$eWd7h.iS9b.%Bf$UDl6\1pA&@eI8Qd^jB_tH0,O1@c[C6R
8*CR&l+0otKP<Fn[3`qb,[P:!,WZZTG/V3V/c("pWcL042Y1D'soL-V4o(;>$;1Ie=!o$#3.
:4KCC9<_]ARbKHFj:[]ABt\EEgN:^oe]A"6hb`P7g4Dnq3%sABeHG)=`FDT`f4]AbM:McNtJ**$5
4f9j/@"lEONp>^RjMR,5<i5c7uMh[`crtSn@%T@]A,2)65$,@cM^..E]ANeB:Km\IY^>J8nc;]A
e+Z$8_Afo7TDK`Gpifj[l=s"=r"4q[58,%_:\l%%d<Jb;71/aHaAV)pjq&Pr5WCmpFE,pa-\
nBJ<)\Zt_.JEC(=1`&k(:chL(e\>3UM\1V+i;F@ct.'C$e*=kT467.?69$5_';j5KbbjqRuN
#1PDrfCm-A53D_8A4-VLiQ?9?JUn5?p5YtFW"3tjigoa<:MjNm+ZT!0RXQ&:O>)CqDd1TrpA
(DkNkmbHODrc8Uf.DJ;,C4Ks/L0WA:^lM.e<_02k@#fZ[R*H8IpkM8::M#s$D30n'XtT4ni$
oXeJnuHM;I98<ST=/&FDWN'oLZYBLU=f'4qV<H?nJ!?s!i;uCI)*IP[27*R?SIR&'u=;308\
+T>Il_9fE?oHe;<AenDadJnnONcYJm>W(20UoiE#;.XS1D_NElMd7kNu(Vg<&aT"73&D;XF8
DG0h9^,Fc+7+T`5iUk*(i?:B(gb=+-^ornf!!8:&mkcV7,2"A$F-8#kX!D3<9CES4Tnh%l3o
]AA\0lt0s0WE]ADs[)/,/37MgZibdrN"+A%5l_#8!Lcp_]AasZSG]A_5*F<F9aNe#^De7j<DeXae
Fp!E+;Va^)aKQ,X!alp26`49cGucl4:OIR:%do"n[E5(oO9UeGb+IK2FWgrf3.@fB?lL_P5#
(GjP7AYKYiE6u0F[SVDtaTBWU&m3Cqhg7$6hlIOo@fuT/O>!EDA$g2!WC#1#!Abe$RY%q/7.
dAtDJF%^ORiP%-='KQ$g:<'sU'J*'E!TN;A4I-l"0K5G_+;`90;MS9':"V+aoLJ3K`FHOs2N
E8J1-?LGMM):q4*<Zp>l02)2SW<mbLi6?*rGA3b$+^Vn\jCkr(k$07(q=CLEs:Gjfm&BM6$c
H?TALmg%q6kK!%gAuH2Xmo?M32.JDm?SWYI/FT.uB<]A8\@R1fdgn4XiJ]Ad5gqcCiju+`B_I9
!MjbW4E@/5d4W745Zu,n9Wel%l^m\I+t>\8O(Q[YZf0XX8Z_mA<ZdE@fh'4.2cZ&q<L*u"9o
'm6c2pRH^hERLL-r=p`9H-6=p8S&%8D,&d+Pu'nF[rL3bLCWre.&)eq63('D@Q5D(D@u/*a#
.gfkGaYGIER+mme02MA.j8q[&bM%Y$fYk?H86%oWtekDf#U6KZ'^_;6l//4q(b!LJNP;A0o5
SU^1h%5[7Glu#u@I)eq@CE%T&hg[WgcO[nLmVkNs!X]A)d.c?7j;9;#H38>>nH*'o3s["AkbM
CYPHrb*ecYKOXacM.,&XMon[h.tca++2"D=V#5[HN!"@WDX3h&%#:X5q&s7>P9AF#/$A`8lD
)>Zn=$Emr`4oB-oWIRfqSNQ`@9jXr]AROFQsC'R_FrXo$TNKqnYD:Es@0qTR0H,oQ$1#c.:.F
);JY-MAO*_Ym_O'[GF2]AEo[mu\&tDXfCWo0(UfEA<`$\^[22GBmG_41CS/OP^LfUl1U@)l3T
*GtG]AIm[!4;0oo::bp8_Je\'&.>iZhR6-u1))6!j/K>)-'[20q>GuQqk6\"2Wki.T)Tio=>2
&)R"I)]ACg+dCQfoBaC_E.BjhoaHc>3D+7&nstZm&dLV^egLQ:3P;0m%<O=<"9p21HD@F4H-2
o1FZnCOCU3%,a,cFNEm\_eFY0Og/-qb;g)p2;!5D>!6PB']A;)E9/Tmrtj(UPk^+j*)L]AqKN3
i/21?F`Q,HUd4+8Vot#Z#Psr?kj\1b1$UNTX868B`Y-PKBI_$\\_P,6^"gb)%)A?/XW=bDdE
Cg1QMPV28"c7\K\O(6frE4a;`[c@5!KM(Fahk`[tUS>U_?^r(UC.PTEU;sD\l.J1cQ.>8G$%
=^)j]Ai`S"l)6c!e@4I,ij`\pbb0:?Dt#2^]An..c,?ShTMg/G,`VY#-i;3\0O$D(Ur(3B`T!G
6ak3&D-p8V4?B!boD.bf8]A/K[qE=-]Aeqh!CS,f(::`d_Z4L;Ca%POZHSc4j^Jl`=TRX]A42BR
:qE[J@@^E72^\$YjC7Z@8H.f1>e=]A61Ii+O\]A70OmB`:Pd:Wqr)!)63hD*p.BMC:H@O.9(7H
V7Dn,JqJ:TS%mc*FR,h.oA)9g98=1lD:>@-V`Ckr4eWif_1@^?9o\bF*N(rf?Vdf=gd8&bXs
H^S(CuHQL4H^]A`?W#bHJt&]Aj2Is6[jCVSCipNPVs0[&%.K_0(IG]A=.#.A/X"TbE4E[]A/#]AZ'
"<@9p2fQW+i9Q-MAbkM!V:plNCOZ!e9GQkJV?=-CMM4ue`ICe=ks*eE.`05CDAO<-GCFn9al
AlR21=/;n6D:_)>R"V<QHQ1&$5GJg!aLW&lIJ=D-<L6=<BN-2!e]A3u,C.0@N06M5>rnbr1/'
1/X+I=]AJOA_TKF]AP.f9=mPo_*,aAGut(QGtXuU,bUtH:jc=^d@3uTVa*oZ]AGI[lTFJhK(AaK
r(sP=9FP10)e&C&n4BsWUlNlL"KLt!arn4u`:]AGXU6eD@#KjX*Q]AnIdBjO)5RUnnbmrIV[D3
a;Km[-KF`Wl\7^7(krltT\;@IF:Q(H5AHs)]A^mFbS$=Kh$ph)?$Sh7o(6!\F?'RTp6&\!Cmq
Rml8"5kesETY+cHO!eB%CW;q9Dl1sGj9:VE82lL%07hoY'B>S#;5;R.i8lmbo%-qYW:dKKlP
`j5*^,bliSiXYcYK2K&:NZ)f8F6\<"mT'4,8mp:pXQA1&4K\9mIsb+7dSk-0\WBD`rNdj&]A6
YVf9/,u"Ht]A&6Q&qZ!uIWU1SCXU1%0Z(mXPg0G5k"@?s@Cb$aj/\BIiOXM'"k#7NDj'>^,-'
nc%Wb&RW7IPLJ3_9#1`IFPi:cFD?=K3P(V=`T3QOK*nqgcdq.]A4?-X#)$,ZFF*d3E(#K%jNB
.QG$6BF,G*h>@=Go\AMqR,QWC)H.f&$]A6g8#RL":%lZ?:,hYpA>')5+rq/]At;\C4%\-5m>E8
N!3t0@)Hb-Yf0$]A=MDLIY%:Nn'O^cUV.j/b[`H.9-SA4u>,BQi2A_I$d1-]APkNWJZ8l3[1[d
uc.rIK5gNMqqH6a2E`]A`ZY@C9lZ`:+WSl.lF^YXc"PcX5BXs"GLo_VNmQJdYP$tL<M.m"cjf
3LmN)9)&E@[QKKf@@$_,j)d"Fl`>.01(:rb(P<j@iJ87"N2JX6,FN:9%sUb)M(6[qccr`U"%
oI^rN\BR6S4P@!bo8aXTmQ[Monm(/5j)7r#h.\%;UF4k>Y,PNM3=JLXj[]AnEI-^0tDad#eLf
%<)[-/f]ASaO;>Nnj;L[p"S.Ro@LnjU&YnL!9b(*3\J0C`0!*8(\be?$n<RODhe]A<o%W95NV/
OP=;=j*:ZZHeT<0m`c]AiDTo9CpgW@/TP/\6_$#TaC4A(PuTBN!Slf?u=.pYN&j[7Hd+q8Zh3
<oJ14#^oima;rNa[?oLRmQlCJoZ(fk>ruLC;6$'VG.c2X%]A!WP-q!>^7R`5,edct[_DJlhnD
SDf;!@';:\?uCMg>E6g6`E[&&#->T=tII2m"^1XS`HZ9i50^tQNU>U4l(I[igu>oCY\b1>]AL
B*jd"\.tCH"jjQ'FC;R&nOA$/dHhl%7Gk2N/KO.qh0u;R3/pT`6*(@2HE,"bhi1p`:CHfD.A
Gc_h7cWh*:DKdYST*rZU2S1EuH:+fL.`mdQ3<7kW?q&fpUtB"2Q<.WiO)d*.=%nI#8Tl@-Vb
j9:*nk%ncW:=6A%)R0R*12>;WVT3fl>:akcr/8n(hPah[ISV]A3#4PU6`kKO0(Q4]An%M_)kc(
F579>maV0)RCona?@Bh@/FRjMQX'@(!>Q&0DMVH40[rjfqg)3f&!&Rr?-1:46$OPGPuBBcr3
ZF.2lIV45bY771hl;DEFZ>\"rs>cOt.c^?d#2M;-2eL?jsF_CmaZR0MsO#Y8$>A&49#klTqb
+!66l)gO+@NdVM`KKPK..g4B\KA,SN=-8@'.UjraQu8_!nV!reUX)FTFrQ,b-$lb/r^Npe#&
(RXjYBkbWJ?c5d$f.eoWB=c=P:,-Q-;"*aRaVK+?5S]AO)!!Do9e0k@fqWVj*`]A3SWDkR^YeZ
nX1r_C[/D;_d0RDUC/nh/LF\SW^%R6RW=AjLCXh.KOhRl1M'll<b&Vo$)"(lo\[.n4bNu-t&
nUZ3?4DPZQEX7?*s?d).f$dqWaSY+iP5o:_O<D`AplY\,C_S=8)V!`q_u9lji0a:5>*YB?i:
KdI`28T73iP^]A0SX+P*K-(ArXPh0EHP5kZIs&_5_]A]A\_UNs@R>5]AWT`1'L)@?'EHW+CE%Th=
*G4-F:"_2;&lLFT^D(^J7tJ@T["&Y>NDq!;ZKKP%Q5IE^2`XD"GSKoI_HtHRc`tr=q3auOf"
?fo?gQ$P^(5-Z\#:k2k'sY%q`S-c[p5_[Vk8J.pWJTY+.L8Z=YKM^O2IF+$5G[L:aTOXR*?o
ZDm#qe1:Cum:##Cj6GR\8m6'r1+t8`_eT8o.8cd'ukZ18V6pC!0oI4P(DS(tM;;:^+S,c(ea
Yh\b\%NC'LHauus$A#R0h-sY*!-0O(IP_kW@$^oa>h(JMNEu/=ob6\p)m[`ZSICV+!;*7kN3
T(rs$,(>r@_6e!U<NN[-&u5`u3qMk*XVNI/Fj3)>!SDDd3*WX&IA<_Sme&u!NL/t1fkT12]AX
qQM`+mjt?`<u4LQFDH)""OmF^.<(G2Pc`p_?1:S%=4Y*6X$+q*ro#eYb(e=sG#%b7b#38N(?
o<iLPXC6J:8DJ@k\Y%]Aq@E]AQA9(h(lKLq8-ugE!MF0_]Aj.FMWI>WQG,Gj[A<T)5,u<L9Va@+
nDi,r#kWu6"k*@'uZVQRb0O2O-ghei@E.pNJ\unJ&LkrK@%UL&:YeG?;__,KJ?k0s(WX+hsi
d>D84'[6ql:MU.d>JC^bn$4_-iZZ)eE<G1XF;i1Qu0og<KE0Babp!c_*Pl.N>?24EJAm0+93
+d(asEF6nopAQXq2n2NJ=RgR@8An5uPtVr\o#.[:mb-\(dq%n]APWFd943eti;XaRS]A=l1KXa
JUX>LUf%,Og\C;i>Mk]A'We"&"%R-0AhFl[%2cnnH;fr:[RO2H5nI<&-MTo6Mp(\-h)q35paM
,_.%65b\.&9A0(-?`3?eoQtP57_-^[t+9l@Y(e0>tTV6Ie$a4'`N0naM6aGe'Nrpj#+--@!D
qN=km7NV5,uSX-RCJPpc%(]A<f1hE-4D.Pe+-e/qQs_YQ!J(Zm"B<Ou^EZ.-R%jI4/qP<B;\c
*9-F$(0rAm7Vr9I&3*"NOg=KnEKA2K)gi/Ea&hmIZn=?@<*W>\ES0VY\,&K&k"U,0VF*G%.j
R6WOMZDPgXYGnV#Vh\U7>+@=4":N*pmCrIA23TZTY0PKH1dkSraXftLDiri(ErR,5#?k7if#
-bXjrc1ljT\_TXsBM-Fm!PM1AK_B(7P$ah'Uq-O[2*e87)s7q6fTCCROfb';,66gajnK#X/H
Z!J*,X=Aq"b37il_fM)H^b\aZ7K2Dn=?oRcCmSk@0M`e("8Pq/s#fTmXIcFMHL>eS*'noq,$
)l+sg"B.LjM6'<OMeX$Dn.3MDCD4!YRGsMbjRI"X#H&Mm7#%'+D\)`\0?a<N(q3'Tb7H"k\/
asiho19/KdZ5KWE>r8RGuYfg?eY6i`:W4!;Rd"ESic&o!O3Y3<.pV2BbR+,DL(69NHF(/h:7
4.'oNR0:oCg-Pb=$YKWWp,`Z7=2=[_Z'a@)+%OLER!**M5;C"=%Up\p.\`#4Al4am!.RJo7`
[aAr:6@-NKRQ6Eq-'Qo!1c1r'5"LNe_d5)acmh$.k;NS,%9#2hD<_cD7=V1cU9dXtVd12P*=
_(H^e%QH&n-!@Y3lAZr:pa:]A'be55*)d-QpBsHEm+7Zn5a<[g<hI;6<]A,tRTKDI106j*$Zgm
^dm*q+3LIR&K>?o?%=8rfecOa^gC`M=oJCq+Fj=qKK'QOK?Ce0rWmo(1URFdZ7e4f_3I.j?1
tQE<RfCS_L"P`e40?SIBDf8DeZ0BXJ7%l\,F4&^;NT02/"9`Z?emuE\nVg@C<0-<Z\6VZi1'
0(^&-'qHcaZ<XbUX_+>4Ji2/\sNauS<5o+2ueDNo,dI[;RY&DsNW6Z:&5`ALY<H^.8*o%qs=
_q;p,9(VQ/]ATi3]AStSq6g?!m4]AQ9uU'7kFJ"LWajR!:'iX?-_18a%9QE[+YZ/J^M(<N\&:?s
t('6aWg2%V]ArJ7m@UO?>!g6V"7Lfg$%0M;2&?8<fr.h'G;IP04"9`gqS_KgrmQPYr,LD7jMn
CjN8\hBq=YRC1.bPZoNfY[(Lq!#ZtLq*,',&/,G-6C03XmqhN6E5<mS`KgQ%nl'^r2's1k_9
'FrsS>!>'F0a%&bPQ0moo8A4F7^@9OQ;jKMGBj2:QkSoDlea;:ZA5sc$VT`70E(l!LE+&aho
/MD`D&BKqNaDCHFG`:!.0FUH"2+49K$)^D9021GMNlS1a4<^*9-/m6FS3@"&mI'G7&tT,BJi
B.M$;VK6@DZrInQS.>Gl\i$+:WRe21/dbE:0!nk:T5)J]AN6Zc(%PU'PW!d?)&r:iE55uhV=\
%5cGVOU)1$9]A?4j7hG<Kl4OWW:7ob^FS[fZ*4>\hoS_gn6d.$[pf$e,MHoX&H?)a,H`!UeW,
tPrD^_>=TGmRuBV==*LRt1g8g4q0iqm%U*&,ncV+mP2@onhJ\gP/]A(%UPAf1n']AjSY[6lE>Q
eHSsjsg\h[@W[a4o;47)a^?F?SuoSR@ourXB/]AfF><`3TJ-;S`Nupqr<-_')PIOaRj.KEnuH
I?Fo!=jGK-8<d%rP$D1Yt.Ub9IWbrf7L]A[#!*2Zb0fQ\/2MV&u*[=V30OMk7"_;]A=9%#*&=J
%I#?OA^s!.>HlF8[V*YbA#$[e"0[A6lqqeWC#8CXE5!DW;2Y)V+pbr6)4MJf]AZN\CSGb`64`
pGd*9R[@]AAhWBr:*3SG-ee4`HCj9DM-ZZ%WN;+<gllL%#\u"0+kTQc/'fF_,T#a%^`2?rT4T
7gkJ=RMmnR;^?8UJLYafY[[WkCYUOR>I!K3Zq.`mK02]AjhYaJI*5e]Alu&j_[RmnR%']AH]A1.@
7Z=@q!D[jm[L=[l;=>+QOj(UYk&Q0F%ncRYLf?IjA&:\h)@UJ9.M_t5Q,@`%o2nuhj9m.g-P
?)WJTpU[J/4XF<,O,iP98":jE4n:(d',(`3n*Yb/=.bO9D<1;2ESJ-D)&Co`L#"d(_2fSgHW
R%3D3Z$e=oJF$Zf_VI2^7G:tB.K"kn;p3_V`A#$CUh#&[CpEW-re5HSJP^1uX/-Ctrf#PEj&
d^'8-`Q;(VEf=1p?*S3Qj9EggYb$BjSlFQ>s!ffaitgL?&(!DAA1_7:[jBlkH#J$'`=CB]A]Ac
/S3FPYM9f<T?f$AZ[jUgS0$h5bBYu9%)*M8A%,nC_J0Ej9\j!Y</DQPr[s_ktnYZ!n^M&b&n
no?@0$j?E/Fpno,hk>A\!s+qL;l,T/$E6bW'4Q7B6<Z/s#t@M2osZ!T#O`7BeOogGV-CCi-L
d'h,]Ap42+\hVe70FCdHRe?/C2-%2ndtX&J9moEd"Te2H/267;U2Cg[;]A+ODF=E,Y[Q_lSYc8
76T>=:R(3YHHe-JH*OLZ#E%_Z?D>_^S&A3&LP(kX(]A,Z[kR6Kh>M6t<ajNEhXdYVd/J\cnq%
"<''R@B[j+(,1H)/QLWG9;;PT0<H3F$#7LX0>ap%3$jSPf$HOm(n*_5##*)WhO"[D(BYP5h^
^oTWjFj`>Q;/eTa$03q%QEbO)qN*Ymjpq8UjNu0CcZ,#+(B,n8+:n!$90.KEpq#P$T!FD,\2
C:Ac5,(bG3i,UDm>5SFOS]A*cC2b&T=11+PKPut+Hd`0WPNS/!@pCbuZQ4`Nbkc@+c70).<%#
G$_Y,5^5Ve;pWX\L=ce>aYS*j!.qlfuYGl3/P'EK&VntYhR,]AaJ:Sir`m=l*cj*O(!jP2%;6
dXF3k'#p>bPL;.rQUnCDbe,Z,r(Ors"oG?,>jqR#l@8stUdt<'c5qfLEqI0r(K,=u1H+(6,V
jN!@_3'DJ#++tODB%RCdu(@2glScjq6JY.l;bs;.rMt@ll$lD(A"DmoA)O#rqK(MD.JSrsHg
.Kqb56+A$.8du*QAf-$2.k2/&Ome7(_+mC<S%[M9:V'`3%EtiLGLHHCW_^Kaq6t_rJ-p]A$DW
8NYh@6Gu'e*!!YW$:\`rorlXclht':lU7'j3_]Aqnm3!tq_8>ZBcS?OG/%JH=P!"[k5_d7*Ef
!=@Lon4o$gB^B;IT]A)?cR<T0Lilj0h2$]AsE5^5]A'Jf>n:\cb%FDY9'kpFO$_jPqM@Zo!K.&c
qpL18D+*4Zj[e7icfDDrq/!Z^l+MFf]Abbf@O6b&"l:g>XK0bFg`Fh?g)MIfL_k_U\s,r:>\\
=UjlJ!(jQ12dC[bT(2Y0iYBUiD/V=iWNrpMF*mNtgPl1oQ7PFDm<R3UHh6d]A&<M&%_UA^_b,
ckb1GGKTCR50&h7o_\ej=gKlCEb&nJJB/*>o,ZnUFkVpjKeXA3ojR]Ad>Rd.RiBm(:u32]AG?9
B]Ag-'_V8q#YU#m;q,C^-q"%^[ioFX.rp!A[**isg"lte8:0(>\_HE'_(@ofp8#?LPl3l)_W_
#SR=)QY+?EN6fR[s+!"_^g9(S7hp"T;]AGWlU7N<c*8[*oTC6KBZU`8A/cRdc,/N;ueTs7C8m
/jn%;mis1qOj;XeLY(;:Q:B&CkE3&jD(G9>r@"JV1I-^\^R#C7?lg[)NBB\J)?p(sAbIMkDl
Y.ug3O)a+h"Ci<[eOI4Ql)6kS,";(sbtf?S'Kic8EJmDkipf%2tV'hns'Z*W)5Fh+Y,,,CQ_
kjcJU!?0"Dq,"fMUEcn,A[;:^3^Z-/fn!#`b$'[6]A']AEF7mC_?.b"1LdFlZ.>]AaPnjXUYmkA
QqA#2(HG#W3k*d/736^"A&4aLh>=d)-rC7!7M[FD`ZPaCcrdooArCjR1q(p\h;qPiJ[L2Kpd
H%#elSIQ_%>o5]Af&ZW=@]AIXr&blLT%UWPF`)S2!<Eh6r;=OF]ABb6CSC@QSiM)&9SHJJL#hFN
W2:dSFoR)h\Gc_'l(R;f$^5B-i!:G"g2%j@o@"lYp>TRl?Bji*M6j[_5-bO(9AFWm$j-7V;G
6s<`rJU^SPN@&%M"<EV/DG?]Ani'*s.5n5qu-AU86hC&MI&_=/P6TZM(raC&N4jcM2f8>!34\
MobLlAT.sGq$T8pY]A%/C[FaPD2cc6-HX#3TY]A6<[nUa_6)Jm[X1#qp#tq=NSAZr8QFjmbI#O
!pJILPY4a2-K8dMfEXX]A5V)lek[t0l&6m"&o"pcYDf^:=uuP7/odZ/HG]A&j2&'sC7`"FeXoF
$B<3Sgeee+9K5<@<;Lu58a6f:=Ld)[6ahoJ*npTa%FZGF%;mDMbHBZe'cq_;+l6g=N:`H11H
Ae[Pk9.eZD2MMS*'lLR-ECQ/]A*-Vn>11;7r]AAsN?To-6f6M&ArTt:PBF6?Tn"7bf1=qZ+igU
2EkpWP'TLqUX<("JJ:W%XY.9S><V]A4@5X$_+95s4$dPBLcgHP0N+riD%VY$ADJehu/`hdk5l
>^KH'1/oj_MpQ\d,1TEpa]A/F3DG1b8=<KpmQ#I*t.o9c?<?K<&HVX3q4jHG(jV5i#q>8g,sS
7'*)`u_nc'*W.S<JK&X:NbOLIi6RpDH_GLS?,Sfe-BmhIK!UR"nTf2]AifTpHB<D%r934]AG&T
j(CFqmKO<."nM$t?jgs_:n@Wn+.!Y2&=-N0<D"Kk(2e+W^_%J_*s+O?"G<=l-F7X)KubL4^C
fR+:+_L]Ar_!>Taebdlr'Kb%r,JE6CI1>JiH,N4@Y/Bc>s(gn`8AAS%=X/j&8m[\$?(cU=U*U
YJXE]AUSA3la&FFUDk>\rp>0<gurK8!<.1]A&tlSOH"_aAMr+ne"JN.s/)N%3^!YXBkCci$lV@
UV6Y@O:]ABM*eloB)?f7E\]AouhB.mu@D$<+ji?peFU-9TXh[*0@lF1NO3.#htEHW/tIf_Or6J
TGN@dgA<YVf`OV@4$L7Cg4D7le]AZtqc?r*Mo?4:C),C(OL*>>`?&.YOmV(><`FK8">!lP&#I
W^^sbH)aY\HXAK#P,k4nI$I"Y<Y3HtV7kJ;Zg"!8=kZD7io;+nH02;*nu#E%^<NKfFHH&L7R
Uh'Bdabo_kb-GJTKcD@9\Z?HM`Vlf9"l_/B?.-M3X_)th4d?d3p^3<-/[8QpZ#*,pNT-1BGK
^PF5DKP)ISM]AXcQrk*`.W3G\n-3"qOa9E"rpg[H7:l.0$1a^e9Vl*`;Zd[ITLNbUF&9K-'5S
A-TUZ2,XjY@pOCNsnB;833C+I/TRO6!0o-Kq>F#\1'!=8UNdal6A7Hm%Y;:+n@UP/+TUht%"
>QZ)b1,rqLn.Q0jJ*-<r3DF#eas/^Mo^"u`2[sQ]AYQe``X_>=G)Qf9<!g0T9"DY$rn-cZ5LZ
XNfRS#uHK<@5FhW_tmKlrnp:5h&ZPV>_kF[kp,[fc7>N/Qka#FT3r0J*bl,Kp7Ys@E*F6kMV
fX"c0n>B1h6aTRR?bF+loR!Y.$nN_Mn78.T@f3XuM\^E(l@E+1k69#(6k+UEZF3[A!Y0C/aL
c3+g=B.2pYic>$gjC$UZ,"HE<.djE;@Sp'.Y<8m1Eg'!j\uI"\r.3OSc'1GhUi.A__"T$3uG
$?$Sh)UhW%?dXlsuI0G?q^l&#FT(hDs#!eLQWl8D)8'u`>4uBIb2BZ"3l>-\N5c9SGX$-aV:
_Au-n[8q$77L(Uq$\cdIf".ML/Lrn6'#t#AE9B[Z)l[qF-sL6T3u*1.mn+<T_U.jC&Zb!GG`
,413Mrc'YbaVZ/74&/T?&H&L\A)IVO_Qcu!QQP"ZDb.[h^dJYdI&<eCY7?8=NhLX<`05Ap&M
C:2kr%ltK8qk9KHS?0TN<49SPYcqc>V/l/U(G5?PAQ8.D"&skJ#:$:DWZMCsNZ0,>;:>ZIA)
GP,%p$Q.T5-Si[9h%-=*ed+]A=G@+g'ZQ7i9\#r`RU@>qJDZ9a>)gYG9;+f=.`huhU?:ZVh.l
$(#=T9-F]A]A#+5-:3)Y?nqQW!313RZ4hZQe+l/D,92@j#%U/([+HoOq#f138sT#Gge7nu]A#F'
d:>t]ADm\9n,8Qoh$'=/VAJ!d==ACJmKRS-gO2!Urt.&"*RkF>(Y[,b1rK>Mdd8:n*(Q<%n%L
@/&tU[ughr89`d5?O.fqO$4g-o%2t=O@$kV#bfs+Dm<`uJa&$hqJP=.VWLtR^dN8:g.T:G<E
WV`@gmA8=ib=?KG%#7+:ItXuLo\eknrfnh[>@1/idG_iu\h`mgr8f6sb;LdPkhMXq--hWu)`
B'.]A]AAiK2udLX`h5=sH59[m';POBW:tK:R9e%504'7&@O-'n`?6@CdTcQ:"iiCn]AUgQV;e)N
;igK:6?Y_!=2bX$.>&GP8?V7_>&S&Z-;Oc)pDb7k%XXs]APaIPi_4R7JdO!Y*Ik6-W$\k)kTI
1Go?.TE"IK.iX.ZfGH4OPIN3Gn\La#CKZhOHX"aEi?'6f_kPI_S<B1D?Ye+_)K?Fp",8'[!!
6>STMV*CPdfIdP(U^"'5:T3_E@T>HbUEI2MoC[<.C.dhKfJfY*11V!ms`UJ1;mYV5qeC;NIe
F!0FN$>!ij!ERS]Af8XDDpquikrYkk;o(=VcT@<_Q!-h'UDkP7co*KH)9?"u[4(A./1+e%hl(
'K,f>a(bmcurA.hI*;,S%6?/_Z^o$b_%4rfoQ7#C80+noZG(/"b"..G1-]AmlLUieoHe/*?F_
;n7^%GbnP_j+2,?iS(:i8JPu1G5H#f+=Z+D2AEQ"KB6k1&M%g90o\;Ap^q_"?$aa;K[X-kZL
O]A1-`u5!K*#qik\@k^lI6JSa^f5g<i;ujL1^ZKR=Wb^aFO&4Er2<tm!n5RbM=81tngX!7U(d
a<Y`%i0rd<j>0Kk_Mps%*TWQs`-4`$1n4+>tiGNV$1g+;YWOqG2<9me1+oil.p6`o\Get:,N
]ArkOpJ/o+]A-1^AE-B/pfX)1;ha`hRF7r<1)i3(/6GEu/BgJdb[d7fhVZE&o]A+(VrDm(2N-h<
E%eT2J[pc0BYMNS2SD`',+.^K.6iJ!6+b2Q(;WY=TV7P0A=Dc99)aD!KK'2MWWK`)*&!-'=\
=fliqr_4jl2l=nOM?%btQS6UBf[Obt>6-EsAF%T8G,FZ5gHWr!`L%;eiETbRMX`T_?ma3=or
:'Q&\<rj\,>ZcL_]AE9>.u6D!;hLUcVCjQ"H`-rFUs$)F.(k9dS5P#^\n*c;`O2f3"b"L(mR8
cWI1u6uQPeI6l<<A?VH528)YNo,-&/b7qsD+K<M8nObgj-dl"GW5'5)"*&S+8CUJF6AS^=p:
@)t&0m37PEFR_$AkJS@m%[\k\LXuchI.:!4RsFGkHem4oasl?['2Za8MLdYs73f3X[6^Oc(6
=d;Dge@T+p*-G,9=m\.'1<q^K,VZmSS/@+Dfp#H!V=$q:CG&G`2i)Fr$dWIApZa'__Z)hl4B
lUNP"9PC5*/i:TaIPB`o!iqA<og$"cJ,tN9%b-MlY#_&P1YIlUjOq5+]A%D9o1Q['X$&U-&\^
Ydt.1)58;;KbY72#%[?5!;%Shd9RaS,s/<g#iB8AN=AF(;(qQ^ET<7;:/8,K35q8R!m@U<)9
@hl4rjF0snpeV?W>ja$9O$F+t*co.g>`2`hm(Pb8Rd*?;WKr&f#E<FGbI2S9^aG,?k$;\Gt'
bJZ$6Wt(?e5mU3(j`&5H9nN+K/)U5.A`58pq=\,'\-"n0]AKOeXQ^cslW"N"h(Fk]A[R-:V(g,
@QkGXL9VOt:S<k7^=V;5sZP\XtGB9,dm%S.g#>->EdTGJUsp<o6:E/"o%?I>mb/X;%Q?6$?1
b[Xf^"i6*5&c'V&sNT&F,fI0i]AV+m$NW?PhC47OSp,=(n:_d^'/LcegS"[.)f7jV$;n.90=N
Bj+<d)iI[Pp!u"1tMudLl9$LN*_6e0/G5TUZ^2U<i6qC5,!2\d?2h1YRc,Ao+Tm."`lD+Rt"
&-;=0'qRj,oTD^T;[Y>N*hqV)@*B8jT*q'X_%D:?'\ZXb:>akm<96?rMJN;(HkQ<mlG%E##i
p%Cau\(Fj2UP^:%%Nd$HX=B3W[/Zri6`lEAXUS/hY4%^cDuc#PXUpNUk.Hg',f_#6He#c3KB
gu&i=EEGbQ&clL?@[ncC$frBeG24:A`AZp"Aa$qS,m\_H+N[Eah#IIja0RAHfQ@<U?N1'Bn^
-4,56Apfk_g3?T@Th$iq1SUnUZGR"3t,D5_0QmghH:"(d*XiqB2L84[7FW`"uTL/dKAnJBd&
jeYG[r0-k/E<]Al\>Y4q*cKic;D8'R1)(+HmSeU_o#d=!r93#RaI(9Z5t()Ae$#Tr)-?tK1B7
Ig^"L2'3p)SNI:QMY,-Q$lF"Bc^1CG9J7\m0D]A%H![A<=[[<n'uk\b[/N\$61LH"Y@@=0Kr9
>#AE)""YOA,#!D,oD8tD`4n>=S72nHGU91?Wte]Ah133l'">\XQ9inmRD<2;JgOZ7E2Z>eeGs
n*bMmSBaXi,'O3r0+ihX>pS:2_IgIQ(l)M28YBrBX82*k=A`g$tZ@I(3VVKnYf+N2Z2XoTeu
rNTjssr[dGG>f!+t19E;g5TWDPIkM]AU,ij2LVe*r62B$NBG6)3)HD\.fUJLn&[?f]A/lFdAKU
\a'?`d*u91t*,_:?V<D2lJUNO/r[uhiuXI`CEDni;9:gmoppj&7rI16&iF_apNb>,=EX;_-n
r[^t^t#M!8tJj.#N#\oLCl'Ku/0''<u=e#50b0Vee#+r]ATcNtL=/ibBZ?p9K2I2>84?R1S[g
kZ"a2`\;gEG1-=OFX-R_s#0]A2'+JC#;SIdi"Y.<>HR"TR0>a7\'f@r0="BK*[5i)h]AH9AE8C
rP5@aqXE;rhD3[cA(lo_E\Z)%M>jcU#N)c]Ag3mAuANV:04k;rZhHids]A-KlX05o=g2AGd+lk
!PRk4W.iAA+OAYmB;5NS>I]AE'b39RJ4fC5=_9.CmDh+7abH^m`+#l[66DM!=e9)5,LLJ?T03
&7`6]A\/5pH$/VOg?rcE??kbc4pq/t;W)9Y?]AY>#HP#*7OFnseETIdCZ@_3,TI+s`bdk:2_-H
[+BdZ^[A"'G8V#*>P7E\2;+,n]A':\_VD\+*2rE%WSm)JjIQ4jrr%IG@8(EQ]A&:;TV-Z%hXt_
OU8@LFZAQN>QhHbI,dA,:8'*JOs'TF7gII=".rrOSMY?`2rZo_ZER'-.[B3d!F$>c8_tEhAk
aDGnG'"]A@T:k*<B@CIY/1uV$J)$N2jE5tN&io[lK:?ApI3%?@<$eI&t&:Sim3k%OA'CnKe9K
4#m[#n<+[Uc7kFtX?.8*M0[0Z'5)o#)66LBbnesA:g&hf:;rm.P&9du]Aec1am.+RgcX.IaS@
-SUs0[7\]A87GOZ0^&E"N+`!!?LD,dU\jV/(7]AcXQ`8Go;($<Xnsk%$'GfJ?N6e-WQ=pqXgAX
J4aRjEg06YsJl\&#4\\?*GFTn[J>q11^8UPPP<l38?k[.c]A;$@>q0;i?P9PFZZHS'gGU-=8I
s$(sQ6t'6>l0+sn<9NW,>q76+?Rb,HLKC24h4sXq.Y52Q1*]A\3r]AnA\@"*<U[7J03cu/5B!l
]AkTS/f0X]A5?-C7Cekl^7cKUc<bNBYl*ir9:*B\gNtpa/odk)Cj<aqGY_tHJ36(<P%'V6-$c7
gn63dqEs`XZ/k*CE:JLl5$f&j3U;+5`'V]A6QeN]A6*m'Z(9p-K$@%*(WLNg7ZA7oSptqIa(t+
6/M]A/>R0W1E5)n<kHO9P8okE^I%H#<,:h)JCbV;c7c+"09*sb([5FS55TV9`sD4HFCd_A`;c
??\BVBg,iqnCS)"8d"e1P\3a%FV@a+S8Q2H&UQ7Z_6YJ%pYIp]A6fo?c7Xi:6Pq>IH<?]AbV$+
hm$a>fDKOfrtb*B!WNr)DZTkRn8A@-(@_?`J/njna'"^YGDt79#A<rofREb;P2)VB-`D;TCY
T/O^$!JVZG_&0A4^djgO#q0#O<Q5*r>?!ruV%*U&W#,*f6pa-7UJb5Bm.=UMY7Vk(_pVrs&
~
]]></IM>
<ElementCaseMobileAttrProvider horizontal="1" vertical="0" zoom="true" refresh="false" isUseHTML="false" isMobileCanvasSize="false" appearRefresh="false" allowFullScreen="false" allowDoubleClickOrZoom="true" functionalWhenUnactivated="false"/>
<MobileFormCollapsedStyle class="com.fr.form.ui.mobile.MobileFormCollapsedStyle">
<collapseButton showButton="true" color="-6710887" foldedHint="" unfoldedHint="" defaultState="0"/>
<collapsedWork value="false"/>
<lineAttr number="1"/>
</MobileFormCollapsedStyle>
</InnerWidget>
<BoundsAttr x="598" y="0" width="364" height="541"/>
</Widget>
<ShowBookmarks showBookmarks="false"/>
<body class="com.fr.form.ui.ElementCaseEditor">
<WidgetName name="report0"/>
<WidgetAttr aspectRatioLocked="false" aspectRatioBackup="0.0" description="">
<MobileBookMark useBookMark="false" bookMarkName="" frozen="false"/>
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
<CellElementList/>
<ReportAttrSet>
<ReportSettings headerHeight="0" footerHeight="0">
<PaperSetting/>
<Background name="ColorBackground" color="-1"/>
</ReportSettings>
</ReportAttrSet>
</FormElementCase>
<StyleList/>
<heightRestrict heightrestrict="false"/>
<heightPercent heightpercent="0.75"/>
<ElementCaseMobileAttrProvider horizontal="1" vertical="0" zoom="true" refresh="false" isUseHTML="false" isMobileCanvasSize="false" appearRefresh="false" allowFullScreen="false" allowDoubleClickOrZoom="true" functionalWhenUnactivated="false"/>
<MobileFormCollapsedStyle class="com.fr.form.ui.mobile.MobileFormCollapsedStyle">
<collapseButton showButton="true" color="-6710887" foldedHint="" unfoldedHint="" defaultState="0"/>
<collapsedWork value="false"/>
<lineAttr number="1"/>
</MobileFormCollapsedStyle>
</body>
</InnerWidget>
<BoundsAttr x="598" y="0" width="364" height="541"/>
</Widget>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.ui.container.WTitleLayout">
<WidgetName name="chart1"/>
<WidgetAttr aspectRatioLocked="false" aspectRatioBackup="0.0" description="">
<MobileBookMark useBookMark="false" bookMarkName="chart1" frozen="false"/>
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
<WidgetAttr aspectRatioLocked="false" aspectRatioBackup="0.0" description="">
<MobileBookMark useBookMark="false" bookMarkName="" frozen="false"/>
<PrivilegeControl/>
</WidgetAttr>
<Margin top="0" left="0" bottom="0" right="0"/>
<Border>
<border style="1" color="-723724" borderRadius="0" type="1" borderStyle="0"/>
<WidgetTitle>
<O>
<![CDATA[=\"  \"+\"地區資料(多層鑽取聯動)\"]]></O>
<FRFont name="微软雅黑" style="0" size="96" foreground="-16749643"/>
<Position pos="2"/>
<Background name="ColorBackground" color="-2953990"/>
<BackgroundOpacity opacity="1.0"/>
</WidgetTitle>
<Alpha alpha="1.0"/>
</Border>
<LayoutAttr selectedIndex="0"/>
<ChangeAttr enable="false" changeType="button" timeInterval="5" buttonColor="-6710887" carouselColor="-8421505" showArrow="true">
<TextAttr>
<Attr alignText="0" predefinedStyle="false">
<FRFont name="PingFangSC-Regular" style="0" size="96" foreground="-1"/>
</Attr>
</TextAttr>
</ChangeAttr>
<Chart name="默认" chartClass="com.fr.plugin.chart.vanchart.VanChart">
<Chart class="com.fr.plugin.chart.vanchart.VanChart">
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr gradientType="normal" gradientStartColor="-12146441" gradientEndColor="-9378161" shadow="false" autoBackground="false" predefinedStyle="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="1" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-3355444" autoColor="false" predefinedStyle="false"/>
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
<Background name="ColorBackground" color="-1"/>
<Attr gradientType="normal" gradientStartColor="-12146441" gradientEndColor="-9378161" shadow="false" autoBackground="false" predefinedStyle="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-6908266" autoColor="false" predefinedStyle="false"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="0.75"/>
</AttrAlpha>
</GI>
<O>
<![CDATA[]]></O>
<TextAttr>
<Attr alignText="0" predefinedStyle="false">
<FRFont name="Microsoft YaHei" style="0" size="128" foreground="-13421773"/>
</Attr>
</TextAttr>
<TitleVisible value="false" position="0"/>
</Title>
<Attr4VanChart useHtml="false" floating="false" x="0.0" y="0.0" limitSize="false" maxHeight="15.0"/>
</Title4VanChart>
<Plot class="com.fr.plugin.chart.drillmap.VanChartDrillMapPlot">
<VanChartPlotVersion version="20170715"/>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr gradientType="normal" gradientStartColor="-12146441" gradientEndColor="-9378161" shadow="false" autoBackground="false" predefinedStyle="false"/>
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
<Format class="com.fr.base.CoreDecimalFormat" roundingMode="6">
<![CDATA[#.##]]></Format>
<PercentFormat>
<Format class="com.fr.base.CoreDecimalFormat" roundingMode="6">
<![CDATA[#0.##%]]></Format>
</PercentFormat>
</AttrContents>
</newHotTooltipStyle>
<ConditionCollection>
<DefaultAttr class="com.fr.chart.chartglyph.ConditionAttr">
<ConditionAttr name="">
<AttrList>
<Attr class="com.fr.plugin.chart.base.AttrBorderWithAlpha">
<AttrBorder>
<Attr lineStyle="1" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-1" autoColor="false" predefinedStyle="false"/>
</AttrBorder>
<AlphaAttr alpha="1.0"/>
</Attr>
<Attr class="com.fr.chart.base.AttrAlpha">
<AttrAlpha>
<Attr alpha="0.75"/>
</AttrAlpha>
</Attr>
<Attr class="com.fr.plugin.chart.map.attr.AttrMapTooltip">
<AttrMapTooltip>
<areaTooltip class="com.fr.plugin.chart.base.AttrTooltip">
<AttrTooltip>
<Attr enable="true" duration="4" followMouse="false" showMutiSeries="true" isCustom="false"/>
<TextAttr>
<Attr alignText="0" predefinedStyle="false">
<FRFont name="Microsoft JhengHei" style="0" size="72"/>
</Attr>
</TextAttr>
<AttrToolTipContent>
<TextAttr>
<Attr alignText="0" predefinedStyle="false">
<FRFont name="Microsoft JhengHei" style="0" size="72"/>
</Attr>
</TextAttr>
<richText class="com.fr.plugin.chart.base.AttrTooltipRichText">
<AttrTooltipRichText>
<Attr content="" isAuto="true" initParamsContent=""/>
<params>
<![CDATA[{}]]></params>
</AttrTooltipRichText>
</richText>
<richTextValue class="com.fr.plugin.chart.base.format.AttrTooltipMapValueFormat">
<AttrTooltipValueFormat>
<Attr enable="true"/>
</AttrTooltipValueFormat>
</richTextValue>
<richTextPercent class="com.fr.plugin.chart.base.format.AttrTooltipPercentFormat">
<AttrTooltipPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat" roundingMode="6">
<![CDATA[#.##%]]></Format>
</AttrTooltipPercentFormat>
</richTextPercent>
<richTextCategory class="com.fr.plugin.chart.base.format.AttrTooltipAreaNameFormat">
<AttrToolTipCategoryFormat>
<Attr enable="true"/>
</AttrToolTipCategoryFormat>
</richTextCategory>
<richTextSeries class="com.fr.plugin.chart.base.format.AttrTooltipSeriesFormat">
<AttrTooltipSeriesFormat>
<Attr enable="true"/>
</AttrTooltipSeriesFormat>
</richTextSeries>
<richTextChangedPercent class="com.fr.plugin.chart.base.format.AttrTooltipChangedPercentFormat">
<AttrTooltipChangedPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat" roundingMode="6">
<![CDATA[#.##%]]></Format>
</AttrTooltipChangedPercentFormat>
</richTextChangedPercent>
<richTextChangedValue class="com.fr.plugin.chart.base.format.AttrTooltipChangedValueFormat">
<AttrTooltipChangedValueFormat>
<Attr enable="false"/>
</AttrTooltipChangedValueFormat>
</richTextChangedValue>
<TableFieldCollection/>
<Attr isCommon="true" isCustom="false" isRichText="false" richTextAlign="left" showAllSeries="false"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipMapValueFormat">
<AttrTooltipValueFormat>
<Attr enable="true"/>
<Format class="com.fr.base.CoreDecimalFormat" roundingMode="6">
<![CDATA[#.##]]></Format>
</AttrTooltipValueFormat>
</value>
<percent class="com.fr.plugin.chart.base.format.AttrTooltipPercentFormat">
<AttrTooltipPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat" roundingMode="6">
<![CDATA[#.##%]]></Format>
</AttrTooltipPercentFormat>
</percent>
<category class="com.fr.plugin.chart.base.format.AttrTooltipAreaNameFormat">
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
<Format class="com.fr.base.CoreDecimalFormat" roundingMode="6">
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
<Attr gradientType="normal" gradientStartColor="-12146441" gradientEndColor="-9378161" shadow="true" autoBackground="false" predefinedStyle="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="2"/>
<newColor borderColor="-16777216" autoColor="false" predefinedStyle="false"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="0.5"/>
</AttrAlpha>
</GI>
</AttrTooltip>
</areaTooltip>
<pointTooltip class="com.fr.plugin.chart.base.AttrTooltip">
<AttrTooltip>
<Attr enable="true" duration="4" followMouse="false" showMutiSeries="true" isCustom="false"/>
<TextAttr>
<Attr alignText="0" predefinedStyle="false">
<FRFont name="Microsoft JhengHei" style="0" size="72"/>
</Attr>
</TextAttr>
<AttrToolTipContent>
<TextAttr>
<Attr alignText="0" predefinedStyle="false">
<FRFont name="Microsoft JhengHei" style="0" size="72"/>
</Attr>
</TextAttr>
<richText class="com.fr.plugin.chart.base.AttrTooltipRichText">
<AttrTooltipRichText>
<Attr content="" isAuto="true" initParamsContent=""/>
<params>
<![CDATA[{}]]></params>
</AttrTooltipRichText>
</richText>
<richTextValue class="com.fr.plugin.chart.base.format.AttrTooltipMapValueFormat">
<AttrTooltipValueFormat>
<Attr enable="true"/>
</AttrTooltipValueFormat>
</richTextValue>
<richTextPercent class="com.fr.plugin.chart.base.format.AttrTooltipPercentFormat">
<AttrTooltipPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat" roundingMode="6">
<![CDATA[#.##%]]></Format>
</AttrTooltipPercentFormat>
</richTextPercent>
<richTextCategory class="com.fr.plugin.chart.base.format.AttrTooltipAreaNameFormat">
<AttrToolTipCategoryFormat>
<Attr enable="true"/>
</AttrToolTipCategoryFormat>
</richTextCategory>
<richTextSeries class="com.fr.plugin.chart.base.format.AttrTooltipSeriesFormat">
<AttrTooltipSeriesFormat>
<Attr enable="true"/>
</AttrTooltipSeriesFormat>
</richTextSeries>
<richTextChangedPercent class="com.fr.plugin.chart.base.format.AttrTooltipChangedPercentFormat">
<AttrTooltipChangedPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat" roundingMode="6">
<![CDATA[#.##%]]></Format>
</AttrTooltipChangedPercentFormat>
</richTextChangedPercent>
<richTextChangedValue class="com.fr.plugin.chart.base.format.AttrTooltipChangedValueFormat">
<AttrTooltipChangedValueFormat>
<Attr enable="false"/>
</AttrTooltipChangedValueFormat>
</richTextChangedValue>
<TableFieldCollection/>
<Attr isCommon="true" isCustom="false" isRichText="false" richTextAlign="left" showAllSeries="false"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipMapValueFormat">
<AttrTooltipValueFormat>
<Attr enable="true"/>
<Format class="com.fr.base.CoreDecimalFormat" roundingMode="6">
<![CDATA[#.##]]></Format>
</AttrTooltipValueFormat>
</value>
<percent class="com.fr.plugin.chart.base.format.AttrTooltipPercentFormat">
<AttrTooltipPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat" roundingMode="6">
<![CDATA[#.##%]]></Format>
</AttrTooltipPercentFormat>
</percent>
<category class="com.fr.plugin.chart.base.format.AttrTooltipAreaNameFormat">
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
<Format class="com.fr.base.CoreDecimalFormat" roundingMode="6">
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
<Attr gradientType="normal" gradientStartColor="-12146441" gradientEndColor="-9378161" shadow="true" autoBackground="false" predefinedStyle="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="2"/>
<newColor borderColor="-16777216" autoColor="false" predefinedStyle="false"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="0.5"/>
</AttrAlpha>
</GI>
</AttrTooltip>
</pointTooltip>
<lineTooltip class="com.fr.plugin.chart.base.AttrTooltip">
<AttrTooltip>
<Attr enable="true" duration="4" followMouse="false" showMutiSeries="true" isCustom="false"/>
<TextAttr>
<Attr alignText="0" predefinedStyle="false">
<FRFont name="Microsoft JhengHei" style="0" size="72"/>
</Attr>
</TextAttr>
<AttrToolTipContent>
<TextAttr>
<Attr alignText="0" predefinedStyle="false">
<FRFont name="Microsoft JhengHei" style="0" size="72"/>
</Attr>
</TextAttr>
<richText class="com.fr.plugin.chart.base.AttrTooltipRichText">
<AttrTooltipRichText>
<Attr content="" isAuto="true" initParamsContent=""/>
<params>
<![CDATA[{}]]></params>
</AttrTooltipRichText>
</richText>
<richTextValue class="com.fr.plugin.chart.base.format.AttrTooltipValueFormat">
<AttrTooltipValueFormat>
<Attr enable="true"/>
</AttrTooltipValueFormat>
</richTextValue>
<richTextPercent class="com.fr.plugin.chart.base.format.AttrTooltipPercentFormat">
<AttrTooltipPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat" roundingMode="6">
<![CDATA[#.##%]]></Format>
</AttrTooltipPercentFormat>
</richTextPercent>
<richTextCategory class="com.fr.plugin.chart.base.format.AttrTooltipStartAndEndNameFormat">
<AttrToolTipCategoryFormat>
<Attr enable="true"/>
</AttrToolTipCategoryFormat>
</richTextCategory>
<richTextSeries class="com.fr.plugin.chart.base.format.AttrTooltipSeriesFormat">
<AttrTooltipSeriesFormat>
<Attr enable="true"/>
</AttrTooltipSeriesFormat>
</richTextSeries>
<richTextChangedPercent class="com.fr.plugin.chart.base.format.AttrTooltipChangedPercentFormat">
<AttrTooltipChangedPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat" roundingMode="6">
<![CDATA[#.##%]]></Format>
</AttrTooltipChangedPercentFormat>
</richTextChangedPercent>
<richTextChangedValue class="com.fr.plugin.chart.base.format.AttrTooltipChangedValueFormat">
<AttrTooltipChangedValueFormat>
<Attr enable="false"/>
</AttrTooltipChangedValueFormat>
</richTextChangedValue>
<TableFieldCollection/>
<Attr isCommon="true" isCustom="false" isRichText="false" richTextAlign="left" showAllSeries="false"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipValueFormat">
<AttrTooltipValueFormat>
<Attr enable="true"/>
</AttrTooltipValueFormat>
</value>
<percent class="com.fr.plugin.chart.base.format.AttrTooltipPercentFormat">
<AttrTooltipPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat" roundingMode="6">
<![CDATA[#.##%]]></Format>
</AttrTooltipPercentFormat>
</percent>
<category class="com.fr.plugin.chart.base.format.AttrTooltipStartAndEndNameFormat">
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
<Format class="com.fr.base.CoreDecimalFormat" roundingMode="6">
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
<Attr gradientType="normal" gradientStartColor="-12146441" gradientEndColor="-9378161" shadow="true" autoBackground="false" predefinedStyle="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="2"/>
<newColor borderColor="-16777216" autoColor="false" predefinedStyle="false"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="0.5"/>
</AttrAlpha>
</GI>
</AttrTooltip>
</lineTooltip>
</AttrMapTooltip>
</Attr>
<Attr class="com.fr.plugin.chart.map.attr.AttrMapLabel">
<AttrMapLabel>
<areaLabel class="com.fr.plugin.chart.base.AttrLabel">
<AttrLabel>
<labelAttr enable="false"/>
<labelDetail class="com.fr.plugin.chart.base.AttrLabelDetail">
<AttrBorderWithShape>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="2"/>
<newColor borderColor="-16777216" autoColor="true" predefinedStyle="false"/>
<shapeAttr isAutoColor="true" shapeType="RectangularMarker"/>
</AttrBorderWithShape>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr gradientType="normal" gradientStartColor="-12146441" gradientEndColor="-9378161" shadow="false" autoBackground="false" predefinedStyle="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-16777216" autoColor="false" predefinedStyle="false"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="0.8"/>
</AttrAlpha>
</GI>
<Attr showLine="false" isHorizontal="true" autoAdjust="false" position="5" align="9" isCustom="true"/>
<TextAttr>
<Attr alignText="0" predefinedStyle="false">
<FRFont name="Microsoft YaHei UI" style="0" size="72" foreground="-1"/>
</Attr>
</TextAttr>
<AttrToolTipContent>
<TextAttr>
<Attr alignText="0" predefinedStyle="false">
<FRFont name="Microsoft YaHei UI" style="0" size="72" foreground="-1"/>
</Attr>
</TextAttr>
<richText class="com.fr.plugin.chart.base.AttrTooltipRichText">
<AttrTooltipRichText>
<Attr content="" isAuto="true" initParamsContent=""/>
<params>
<![CDATA[{}]]></params>
</AttrTooltipRichText>
</richText>
<richTextValue class="com.fr.plugin.chart.base.format.AttrTooltipMapValueFormat">
<AttrTooltipValueFormat>
<Attr enable="false"/>
</AttrTooltipValueFormat>
</richTextValue>
<richTextPercent class="com.fr.plugin.chart.base.format.AttrTooltipPercentFormat">
<AttrTooltipPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat" roundingMode="6">
<![CDATA[#.##%]]></Format>
</AttrTooltipPercentFormat>
</richTextPercent>
<richTextCategory class="com.fr.plugin.chart.base.format.AttrTooltipAreaNameFormat">
<AttrToolTipCategoryFormat>
<Attr enable="true"/>
</AttrToolTipCategoryFormat>
</richTextCategory>
<richTextSeries class="com.fr.plugin.chart.base.format.AttrTooltipSeriesFormat">
<AttrTooltipSeriesFormat>
<Attr enable="false"/>
</AttrTooltipSeriesFormat>
</richTextSeries>
<richTextChangedPercent class="com.fr.plugin.chart.base.format.AttrTooltipChangedPercentFormat">
<AttrTooltipChangedPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat" roundingMode="6">
<![CDATA[#.##%]]></Format>
</AttrTooltipChangedPercentFormat>
</richTextChangedPercent>
<richTextChangedValue class="com.fr.plugin.chart.base.format.AttrTooltipChangedValueFormat">
<AttrTooltipChangedValueFormat>
<Attr enable="false"/>
</AttrTooltipChangedValueFormat>
</richTextChangedValue>
<TableFieldCollection/>
<Attr isCommon="true" isCustom="true" isRichText="false" richTextAlign="center" showAllSeries="false"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipMapValueFormat">
<AttrTooltipValueFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat" roundingMode="6">
<![CDATA[#.##]]></Format>
</AttrTooltipValueFormat>
</value>
<percent class="com.fr.plugin.chart.base.format.AttrTooltipPercentFormat">
<AttrTooltipPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat" roundingMode="6">
<![CDATA[#.##%]]></Format>
</AttrTooltipPercentFormat>
</percent>
<category class="com.fr.plugin.chart.base.format.AttrTooltipAreaNameFormat">
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
<Format class="com.fr.base.CoreDecimalFormat" roundingMode="6">
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
</labelDetail>
</AttrLabel>
</areaLabel>
<pointLabel class="com.fr.plugin.chart.base.AttrLabel">
<AttrLabel>
<labelAttr enable="false"/>
<labelDetail class="com.fr.plugin.chart.base.AttrLabelDetail">
<AttrBorderWithShape>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="2"/>
<newColor borderColor="-16777216" autoColor="true" predefinedStyle="false"/>
<shapeAttr isAutoColor="true" shapeType="RectangularMarker"/>
</AttrBorderWithShape>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr gradientType="normal" gradientStartColor="-12146441" gradientEndColor="-9378161" shadow="false" autoBackground="false" predefinedStyle="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-16777216" autoColor="false" predefinedStyle="false"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="0.8"/>
</AttrAlpha>
</GI>
<Attr showLine="false" isHorizontal="true" autoAdjust="false" position="5" align="9" isCustom="false"/>
<TextAttr>
<Attr alignText="0" predefinedStyle="false"/>
</TextAttr>
<AttrToolTipContent>
<TextAttr>
<Attr alignText="0" predefinedStyle="false"/>
</TextAttr>
<richText class="com.fr.plugin.chart.base.AttrTooltipRichText">
<AttrTooltipRichText>
<Attr content="" isAuto="true" initParamsContent=""/>
<params>
<![CDATA[{}]]></params>
</AttrTooltipRichText>
</richText>
<richTextValue class="com.fr.plugin.chart.base.format.AttrTooltipMapValueFormat">
<AttrTooltipValueFormat>
<Attr enable="false"/>
</AttrTooltipValueFormat>
</richTextValue>
<richTextPercent class="com.fr.plugin.chart.base.format.AttrTooltipPercentFormat">
<AttrTooltipPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat" roundingMode="6">
<![CDATA[#.##%]]></Format>
</AttrTooltipPercentFormat>
</richTextPercent>
<richTextCategory class="com.fr.plugin.chart.base.format.AttrTooltipAreaNameFormat">
<AttrToolTipCategoryFormat>
<Attr enable="true"/>
</AttrToolTipCategoryFormat>
</richTextCategory>
<richTextSeries class="com.fr.plugin.chart.base.format.AttrTooltipSeriesFormat">
<AttrTooltipSeriesFormat>
<Attr enable="false"/>
</AttrTooltipSeriesFormat>
</richTextSeries>
<richTextChangedPercent class="com.fr.plugin.chart.base.format.AttrTooltipChangedPercentFormat">
<AttrTooltipChangedPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat" roundingMode="6">
<![CDATA[#.##%]]></Format>
</AttrTooltipChangedPercentFormat>
</richTextChangedPercent>
<richTextChangedValue class="com.fr.plugin.chart.base.format.AttrTooltipChangedValueFormat">
<AttrTooltipChangedValueFormat>
<Attr enable="false"/>
</AttrTooltipChangedValueFormat>
</richTextChangedValue>
<TableFieldCollection/>
<Attr isCommon="true" isCustom="false" isRichText="false" richTextAlign="center" showAllSeries="false"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipMapValueFormat">
<AttrTooltipValueFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat" roundingMode="6">
<![CDATA[#.##]]></Format>
</AttrTooltipValueFormat>
</value>
<percent class="com.fr.plugin.chart.base.format.AttrTooltipPercentFormat">
<AttrTooltipPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat" roundingMode="6">
<![CDATA[#.##%]]></Format>
</AttrTooltipPercentFormat>
</percent>
<category class="com.fr.plugin.chart.base.format.AttrTooltipAreaNameFormat">
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
<Format class="com.fr.base.CoreDecimalFormat" roundingMode="6">
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
</labelDetail>
</AttrLabel>
</pointLabel>
</AttrMapLabel>
</Attr>
<Attr class="com.fr.plugin.chart.base.VanChartAttrMarker">
<VanAttrMarker>
<Attr isCommon="false" anchorSize="22.0" markerType="AutoMarker" radius="3.5" width="30.0" height="30.0"/>
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
<Background name="ColorBackground" color="-1"/>
<Attr gradientType="normal" gradientStartColor="-12146441" gradientEndColor="-9378161" shadow="true" autoBackground="false" predefinedStyle="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="2"/>
<newColor borderColor="-3355444" autoColor="false" predefinedStyle="false"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="0.75"/>
</AttrAlpha>
</GI>
<Attr position="4" visible="true" predefinedStyle="false"/>
<FRFont name="Microsoft YaHei UI" style="0" size="72" foreground="-10066330"/>
</Legend>
<Attr4VanChart floating="false" x="0.0" y="0.0" layout="aligned" customSize="true" maxHeight="100.0" isHighlight="false"/>
<Attr4VanChartScatter>
<Type rangeLegendType="1"/>
<GradualLegend>
<GradualIntervalConfig>
<IntervalConfigAttr subColor="-14374913" divStage="1.0"/>
<ValueRange IsCustomMin="false" IsCustomMax="false"/>
<ColorDistList>
<ColorDist color="-7874817" dist="0.0"/>
<ColorDist color="-13075251" dist="1.0"/>
</ColorDistList>
</GradualIntervalConfig>
<LegendLabelFormat>
<IsCommon commonValueFormat="true"/>
</LegendLabelFormat>
</GradualLegend>
</Attr4VanChartScatter>
</Legend4VanChart>
<DataSheet>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr gradientType="normal" gradientStartColor="-12146441" gradientEndColor="-9378161" shadow="false" autoBackground="false" predefinedStyle="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="1" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-16777216" autoColor="false" predefinedStyle="false"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<Attr isVisible="false" predefinedStyle="false"/>
<FRFont name="Microsoft JhengHei" style="0" size="72"/>
</DataSheet>
<NameJavaScriptGroup>
<NameJavaScript name="当前表单对象1">
<JavaScript class="com.fr.form.main.FormHyperlink">
<JavaScript class="com.fr.form.main.FormHyperlink">
<Parameters>
<Parameter>
<Attributes name="province"/>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=AREA_NAME]]></Attributes>
</O>
</Parameter>
</Parameters>
<TargetFrame>
<![CDATA[_blank]]></TargetFrame>
<Features/>
<realateName realateValue="report0" animateType="none"/>
<linkType type="1"/>
</JavaScript>
</JavaScript>
</NameJavaScript>
</NameJavaScriptGroup>
<DataProcessor class="com.fr.base.chart.chartdata.model.NormalDataModel"/>
<newPlotFillStyle>
<AttrFillStyle>
<AFStyle colorStyle="1"/>
<FillStyleName fillStyleName="新特性"/>
<isCustomFillStyle isCustomFillStyle="false"/>
<PredefinedStyle predefinedStyle="false"/>
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
<GradientStyle>
<Attr gradientType="gradual" startColor="-12146441" endColor="-9378161"/>
</GradientStyle>
<VanChartMapPlotAttr mapType="area" geourl="assets/map/geographic/world/中國.json" zoomlevel="4" mapmarkertype="0" markerTypeKey="default" autoNullValue="false" nullvaluecolor="-3355444"/>
<lineMapDataProcessor>
<DataProcessor class="com.fr.base.chart.chartdata.model.NormalDataModel"/>
</lineMapDataProcessor>
<GisLayer>
<Attr gislayer="predefined_layer" layerName="tw"/>
</GisLayer>
<ViewCenter auto="false" longitude="103.826447" latitude="36.059561"/>
<pointConditionCollection>
<ConditionCollection>
<DefaultAttr class="com.fr.chart.chartglyph.ConditionAttr">
<ConditionAttr name=""/>
</DefaultAttr>
</ConditionCollection>
</pointConditionCollection>
<lineConditionCollection>
<ConditionCollection>
<DefaultAttr class="com.fr.chart.chartglyph.ConditionAttr">
<ConditionAttr name=""/>
</DefaultAttr>
</ConditionCollection>
</lineConditionCollection>
<matchResult/>
<layerMapTypeList>
<single type="area"/>
<single type="area"/>
<single type="area"/>
<single type="area"/>
</layerMapTypeList>
<layerLevelList>
<single level="0"/>
<single level="6"/>
<single level="0"/>
<single level="0"/>
</layerLevelList>
<drillUpHyperLink>
<NameJavaScriptGroup>
<NameJavaScript name="当前表单对象1">
<JavaScript class="com.fr.form.main.FormHyperlink">
<JavaScript class="com.fr.form.main.FormHyperlink">
<Parameters>
<Parameter>
<Attributes name="province"/>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=AREA_NAME]]></Attributes>
</O>
</Parameter>
</Parameters>
<TargetFrame>
<![CDATA[_blank]]></TargetFrame>
<Features/>
<realateName realateValue="report0" animateType="none"/>
<linkType type="1"/>
</JavaScript>
</JavaScript>
</NameJavaScript>
</NameJavaScriptGroup>
</drillUpHyperLink>
<DrillMapTools>
<drillAttr enable="true"/>
<TextAttr>
<Attr alignText="0" predefinedStyle="false">
<FRFont name="Microsoft YaHei UI" style="0" size="96" foreground="-5066062"/>
</Attr>
</TextAttr>
<backgroundinfo>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr gradientType="normal" gradientStartColor="-12146441" gradientEndColor="-9378161" shadow="false" autoBackground="false" predefinedStyle="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-16777216" autoColor="false" predefinedStyle="false"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="0.8"/>
</AttrAlpha>
</GI>
</backgroundinfo>
<selectbackgroundinfo>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr gradientType="normal" gradientStartColor="-12146441" gradientEndColor="-9378161" shadow="false" autoBackground="false" predefinedStyle="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-16777216" autoColor="false" predefinedStyle="false"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
</selectbackgroundinfo>
</DrillMapTools>
<matchResultList>
<matchResult/>
<matchResult/>
<matchResult/>
<matchResult/>
</matchResultList>
</Plot>
<ChartDefinition>
<DillMapDefinition>
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<Attr fromBottomData="false"/>
<bottomDataDefinition class="com.fr.plugin.chart.map.data.VanMapMoreNameCDDefinition">
<MoreNameCDDefinition>
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<TableData class="com.fr.data.impl.NameTableData">
<Name>
<![CDATA[ds2]]></Name>
</TableData>
<CategoryName value="pid"/>
<ChartSummaryColumn name="销售额" function="com.fr.data.util.function.NoneFunction" customName="销售额"/>
</MoreNameCDDefinition>
<attr longitude="" latitude="" endLongitude="" endLatitude="" useAreaName="true" endAreaName=""/>
<matchResult/>
</bottomDataDefinition>
<eachLayerDataDefinitionList>
<SingleLayerDataDefinition class="com.fr.plugin.chart.map.data.VanMapMoreNameCDDefinition">
<MoreNameCDDefinition>
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<TableData class="com.fr.data.impl.NameTableData">
<Name>
<![CDATA[ds4]]></Name>
</TableData>
<CategoryName value="pid"/>
<ChartSummaryColumn name="銷售額" function="com.fr.data.util.function.NoneFunction" customName="銷售額"/>
</MoreNameCDDefinition>
<attr longitude="" latitude="" endLongitude="" endLatitude="" useAreaName="true" endAreaName=""/>
<matchResult/>
</SingleLayerDataDefinition>
<SingleLayerDataDefinition class="com.fr.plugin.chart.map.data.VanMapMoreNameCDDefinition">
<MoreNameCDDefinition>
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<TableData class="com.fr.data.impl.NameTableData">
<Name>
<![CDATA[ds4]]></Name>
</TableData>
<CategoryName value="省份"/>
<ChartSummaryColumn name="銷售額" function="com.fr.data.util.function.NoneFunction" customName="銷售額"/>
</MoreNameCDDefinition>
<attr longitude="" latitude="" endLongitude="" endLatitude="" useAreaName="true" endAreaName=""/>
<matchResult/>
</SingleLayerDataDefinition>
<SingleLayerDataDefinition class="com.fr.plugin.chart.map.data.VanMapMoreNameCDDefinition">
<MoreNameCDDefinition>
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
</MoreNameCDDefinition>
<attr longitude="" latitude="" endLongitude="" endLatitude="" useAreaName="true" endAreaName=""/>
<matchResult/>
</SingleLayerDataDefinition>
<SingleLayerDataDefinition class="com.fr.plugin.chart.map.data.VanMapMoreNameCDDefinition">
<MoreNameCDDefinition>
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
</MoreNameCDDefinition>
<attr longitude="" latitude="" endLongitude="" endLatitude="" useAreaName="true" endAreaName=""/>
<matchResult/>
</SingleLayerDataDefinition>
</eachLayerDataDefinitionList>
</DillMapDefinition>
</ChartDefinition>
</Chart>
<UUID uuid="03851f6a-8a6f-40d8-951c-f1d14cd77271"/>
<tools hidden="true" sort="false" export="false" fullScreen="false"/>
<VanChartZoom>
<zoomAttr zoomVisible="false" zoomGesture="true" zoomResize="true" zoomType="xy" controlType="zoom" categoryNum="8" scaling="0.3"/>
<from>
<![CDATA[]]></from>
<to>
<![CDATA[]]></to>
</VanChartZoom>
<refreshMoreLabel>
<attr moreLabel="true" autoTooltip="true"/>
<AttrTooltip>
<Attr enable="true" duration="4" followMouse="false" showMutiSeries="true" isCustom="false"/>
<TextAttr>
<Attr alignText="0" predefinedStyle="false">
<FRFont name="Microsoft JhengHei" style="0" size="72"/>
</Attr>
</TextAttr>
<AttrToolTipContent>
<TextAttr>
<Attr alignText="0" predefinedStyle="false">
<FRFont name="Microsoft JhengHei" style="0" size="72"/>
</Attr>
</TextAttr>
<richText class="com.fr.plugin.chart.base.AttrTooltipRichText">
<AttrTooltipRichText>
<Attr content="" isAuto="true" initParamsContent=""/>
<params>
<![CDATA[{}]]></params>
</AttrTooltipRichText>
</richText>
<richTextValue class="com.fr.plugin.chart.base.format.AttrTooltipValueFormat">
<AttrTooltipValueFormat>
<Attr enable="true"/>
</AttrTooltipValueFormat>
</richTextValue>
<richTextPercent class="com.fr.plugin.chart.base.format.AttrTooltipPercentFormat">
<AttrTooltipPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat" roundingMode="6">
<![CDATA[#.##%]]></Format>
</AttrTooltipPercentFormat>
</richTextPercent>
<richTextCategory class="com.fr.plugin.chart.base.format.AttrTooltipCategoryFormat">
<AttrToolTipCategoryFormat>
<Attr enable="false"/>
</AttrToolTipCategoryFormat>
</richTextCategory>
<richTextSeries class="com.fr.plugin.chart.base.format.AttrTooltipSeriesFormat">
<AttrTooltipSeriesFormat>
<Attr enable="false"/>
</AttrTooltipSeriesFormat>
</richTextSeries>
<richTextChangedPercent class="com.fr.plugin.chart.base.format.AttrTooltipChangedPercentFormat">
<AttrTooltipChangedPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat" roundingMode="6">
<![CDATA[#.##%]]></Format>
</AttrTooltipChangedPercentFormat>
</richTextChangedPercent>
<richTextChangedValue class="com.fr.plugin.chart.base.format.AttrTooltipChangedValueFormat">
<AttrTooltipChangedValueFormat>
<Attr enable="false"/>
</AttrTooltipChangedValueFormat>
</richTextChangedValue>
<TableFieldCollection/>
<Attr isCommon="true" isCustom="false" isRichText="false" richTextAlign="left" showAllSeries="false"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipValueFormat">
<AttrTooltipValueFormat>
<Attr enable="false"/>
</AttrTooltipValueFormat>
</value>
<percent class="com.fr.plugin.chart.base.format.AttrTooltipPercentFormat">
<AttrTooltipPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat" roundingMode="6">
<![CDATA[#.##%]]></Format>
</AttrTooltipPercentFormat>
</percent>
<category class="com.fr.plugin.chart.base.format.AttrTooltipAreaNameFormat">
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
<Format class="com.fr.base.CoreDecimalFormat" roundingMode="6">
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
<Attr gradientType="normal" gradientStartColor="-12146441" gradientEndColor="-9378161" shadow="false" autoBackground="false" predefinedStyle="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="1" isRoundBorder="false" roundRadius="4"/>
<newColor borderColor="-15395563" autoColor="false" predefinedStyle="false"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="0.8"/>
</AttrAlpha>
</GI>
</AttrTooltip>
</refreshMoreLabel>
<ThemeAttr>
<Attr darkTheme="false" predefinedStyle="false"/>
</ThemeAttr>
</Chart>
<ChartMobileAttrProvider zoomOut="0" zoomIn="2" allowFullScreen="true" functionalWhenUnactivated="false"/>
<MobileChartCollapsedStyle class="com.fr.form.ui.mobile.MobileChartCollapsedStyle">
<collapseButton showButton="true" color="-6710887" foldedHint="" unfoldedHint="" defaultState="0"/>
<collapsedWork value="false"/>
</MobileChartCollapsedStyle>
</InnerWidget>
<BoundsAttr x="0" y="36" width="598" height="505"/>
</Widget>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.ui.Label">
<WidgetName name="Title_chart1"/>
<WidgetAttr aspectRatioLocked="false" aspectRatioBackup="0.0" description="">
<MobileBookMark useBookMark="false" bookMarkName="" frozen="false"/>
<PrivilegeControl/>
</WidgetAttr>
<widgetValue>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[="  "+"地區資料(多層鑽取聯動)"]]></Attributes>
</O>
</widgetValue>
<LabelAttr verticalcenter="true" textalign="2" autoline="true"/>
<FRFont name="微软雅黑" style="0" size="96" foreground="-16749643"/>
<Background name="ColorBackground" color="-2953990"/>
<BackgroundOpacity opacity="1.0"/>
<border style="1" color="-723724"/>
</InnerWidget>
<BoundsAttr x="0" y="0" width="598" height="36"/>
</Widget>
<ShowBookmarks showBookmarks="false"/>
<title class="com.fr.form.ui.Label">
<WidgetName name="Title_chart1"/>
<WidgetAttr aspectRatioLocked="false" aspectRatioBackup="0.0" description="">
<MobileBookMark useBookMark="false" bookMarkName="" frozen="false"/>
<PrivilegeControl/>
</WidgetAttr>
<widgetValue>
<O>
<![CDATA[地区数据]]></O>
</widgetValue>
<LabelAttr verticalcenter="true" textalign="2" autoline="true"/>
<FRFont name="微软雅黑" style="0" size="96"/>
<Background name="ColorBackground" color="-6697729"/>
<BackgroundOpacity opacity="1.0"/>
<border style="1" color="-723724"/>
</title>
<body class="com.fr.form.ui.ChartEditor">
<WidgetName name="chart1"/>
<WidgetAttr aspectRatioLocked="false" aspectRatioBackup="0.0" description="">
<MobileBookMark useBookMark="false" bookMarkName="" frozen="false"/>
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
<Attr alignText="0" predefinedStyle="false"/>
</TextAttr>
</ChangeAttr>
<Chart name="默认" chartClass="com.fr.chart.chartattr.Chart">
<Chart class="com.fr.chart.chartattr.Chart">
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr gradientType="normal" gradientStartColor="-12146441" gradientEndColor="-9378161" shadow="false" autoBackground="false" predefinedStyle="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-6908266" autoColor="false" predefinedStyle="false"/>
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
<Attr gradientType="normal" gradientStartColor="-12146441" gradientEndColor="-9378161" shadow="false" autoBackground="false" predefinedStyle="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-6908266" autoColor="false" predefinedStyle="false"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<O>
<![CDATA[地区数据]]></O>
<TextAttr>
<Attr alignText="0" predefinedStyle="false">
<FRFont name="微软雅黑" style="0" size="88"/>
</Attr>
</TextAttr>
<TitleVisible value="true" position="0"/>
</Title>
<Plot class="com.fr.chart.chartattr.MapPlot">
<MapPlot>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr gradientType="normal" gradientStartColor="-12146441" gradientEndColor="-9378161" shadow="false" autoBackground="false" predefinedStyle="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<Attr isNullValueBreak="true" autoRefreshPerSecond="-1" seriesDragEnable="true" plotStyle="0" combinedSize="50.0"/>
<newHotTooltipStyle>
<AttrContents>
<Attr showLine="false" position="1" isWhiteBackground="true" isShowMutiSeries="false" seriesLabel="${SERIES}${BR}${CATEGORY}${BR}${VALUE}"/>
<Format class="com.fr.base.CoreDecimalFormat" roundingMode="6">
<![CDATA[#.##]]></Format>
<PercentFormat>
<Format class="com.fr.base.CoreDecimalFormat" roundingMode="6">
<![CDATA[#.##%]]></Format>
</PercentFormat>
</AttrContents>
</newHotTooltipStyle>
<ConditionCollection>
<DefaultAttr class="com.fr.chart.chartglyph.ConditionAttr">
<ConditionAttr name=""/>
</DefaultAttr>
<ConditionAttrList>
<List index="0">
<ConditionAttr name="条件属性1">
<AttrList>
<Attr class="com.fr.chart.base.AttrBackground">
<AttrBackground>
<Background name="ColorBackground" color="-6697984"/>
<Attr gradientType="normal" gradientStartColor="-12146441" gradientEndColor="-9378161" shadow="false" autoBackground="false" predefinedStyle="false"/>
</AttrBackground>
</Attr>
</AttrList>
<Condition class="com.fr.data.condition.ListCondition">
<JoinCondition join="0">
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[0]]></CNUMBER>
<CNAME>
<![CDATA[区域名]]></CNAME>
<Compare op="0">
<O>
<![CDATA[广东省]]></O>
</Compare>
</Condition>
</JoinCondition>
<JoinCondition join="0">
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[0]]></CNUMBER>
<CNAME>
<![CDATA[区域名]]></CNAME>
<Compare op="0">
<O>
<![CDATA[广州市]]></O>
</Compare>
</Condition>
</JoinCondition>
</Condition>
</ConditionAttr>
</List>
</ConditionAttrList>
</ConditionCollection>
<Legend>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr gradientType="normal" gradientStartColor="-12146441" gradientEndColor="-9378161" shadow="false" autoBackground="false" predefinedStyle="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-6908266" autoColor="false" predefinedStyle="false"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<Attr position="4" visible="true" predefinedStyle="false"/>
<FRFont name="Microsoft YaHei" style="0" size="72"/>
</Legend>
<DataSheet>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr gradientType="normal" gradientStartColor="-12146441" gradientEndColor="-9378161" shadow="false" autoBackground="false" predefinedStyle="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="1" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-16777216" autoColor="false" predefinedStyle="false"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<Attr isVisible="false" predefinedStyle="false"/>
<FRFont name="Microsoft JhengHei" style="0" size="72"/>
</DataSheet>
<NameJavaScriptGroup>
<NameJavaScript name="当前">
<JavaScript class="com.fr.form.main.FormHyperlink">
<JavaScript class="com.fr.form.main.FormHyperlink">
<Parameters>
<Parameter>
<Attributes name="province"/>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=AREA_NAME]]></Attributes>
</O>
</Parameter>
</Parameters>
<TargetFrame>
<![CDATA[_blank]]></TargetFrame>
<Features/>
<realateName realateValue="report0" animateType="none"/>
<linkType type="1"/>
</JavaScript>
</JavaScript>
</NameJavaScript>
</NameJavaScriptGroup>
<DataProcessor class="com.fr.base.chart.chartdata.model.NormalDataModel"/>
<newPlotFillStyle>
<AttrFillStyle>
<AFStyle colorStyle="0"/>
<FillStyleName fillStyleName=""/>
<isCustomFillStyle isCustomFillStyle="false"/>
<PredefinedStyle predefinedStyle="false"/>
</AttrFillStyle>
</newPlotFillStyle>
<newattr201212 mapName="中国" isSvgMap="true" mapType="Map_Normal" isHeatMap="true" heatIndex="0"/>
<MapHotAreaColor>
<MC_Attr minValue="100.0" maxValue="600.0" useType="0" areaNumber="5" mainColor="-14374913"/>
<ColorList>
<AreaColor>
<AC_Attr minValue="=500.0" maxValue="=600.0" color="-14374913"/>
</AreaColor>
<AreaColor>
<AC_Attr minValue="=400.0" maxValue="=500.0" color="-11486721"/>
</AreaColor>
<AreaColor>
<AC_Attr minValue="=300.0" maxValue="=400.0" color="-8598785"/>
</AreaColor>
<AreaColor>
<AC_Attr minValue="=200.0" maxValue="=300.0" color="-5776129"/>
</AreaColor>
<AreaColor>
<AC_Attr minValue="=100.0" maxValue="=200.0" color="-2888193"/>
</AreaColor>
</ColorList>
</MapHotAreaColor>
<BubblePlot>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr gradientType="normal" gradientStartColor="-12146441" gradientEndColor="-9378161" shadow="false" autoBackground="false" predefinedStyle="false"/>
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
<Format class="com.fr.base.CoreDecimalFormat" roundingMode="6">
<![CDATA[#.##]]></Format>
<PercentFormat>
<Format class="com.fr.base.CoreDecimalFormat" roundingMode="6">
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
<Attr gradientType="normal" gradientStartColor="-12146441" gradientEndColor="-9378161" shadow="false" autoBackground="false" predefinedStyle="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-6908266" autoColor="false" predefinedStyle="false"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<Attr position="4" visible="true" predefinedStyle="false"/>
<FRFont name="SimSun" style="0" size="72"/>
</Legend>
<DataSheet>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr gradientType="normal" gradientStartColor="-12146441" gradientEndColor="-9378161" shadow="false" autoBackground="false" predefinedStyle="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="1" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-16777216" autoColor="false" predefinedStyle="false"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<Attr isVisible="false" predefinedStyle="false"/>
<FRFont name="Microsoft JhengHei" style="0" size="72"/>
</DataSheet>
<DataProcessor class="com.fr.base.chart.chartdata.model.NormalDataModel"/>
<newPlotFillStyle>
<AttrFillStyle>
<AFStyle colorStyle="0"/>
<FillStyleName fillStyleName=""/>
<isCustomFillStyle isCustomFillStyle="false"/>
<PredefinedStyle predefinedStyle="false"/>
</AttrFillStyle>
</newPlotFillStyle>
<RectanglePlotAttr interactiveAxisTooltip="false"/>
<xAxis>
<ValueAxis class="com.fr.chart.chartattr.ValueAxis">
<ValueAxisAttr201108 alignZeroValue="false"/>
<newAxisAttr isShowAxisLabel="true"/>
<AxisLineStyle AxisStyle="1" MainGridStyle="1"/>
<newLineColor mainGridColor="-4144960" mainGridPredefinedStyle="false" lineColor="-5197648" predefinedStyle="false"/>
<AxisPosition value="3"/>
<TickLine201106 type="2" secType="0"/>
<ArrowShow arrowShow="false"/>
<TextAttr>
<Attr alignText="0" predefinedStyle="false"/>
</TextAttr>
<AxisLabelCount value="=0"/>
<AxisRange/>
<AxisUnit201106 isCustomMainUnit="false" isCustomSecUnit="false" mainUnit="=0" secUnit="=0"/>
<ZoomAxisAttr isZoom="false"/>
<axisReversed axisReversed="false"/>
</ValueAxis>
</xAxis>
<yAxis>
<ValueAxis class="com.fr.chart.chartattr.ValueAxis">
<ValueAxisAttr201108 alignZeroValue="false"/>
<newAxisAttr isShowAxisLabel="true"/>
<AxisLineStyle AxisStyle="1" MainGridStyle="1"/>
<newLineColor mainGridColor="-4144960" mainGridPredefinedStyle="false" lineColor="-5197648" predefinedStyle="false"/>
<AxisPosition value="2"/>
<TickLine201106 type="2" secType="0"/>
<ArrowShow arrowShow="false"/>
<TextAttr>
<Attr alignText="0" predefinedStyle="false"/>
</TextAttr>
<AxisLabelCount value="=0"/>
<AxisRange/>
<AxisUnit201106 isCustomMainUnit="false" isCustomSecUnit="false" mainUnit="=0" secUnit="=0"/>
<ZoomAxisAttr isZoom="false"/>
<axisReversed axisReversed="false"/>
</ValueAxis>
</yAxis>
<BubblePlotAttr bubbleSize="50.0" bubbleType="1" isNegative="true"/>
</BubblePlot>
<Plot>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr gradientType="normal" gradientStartColor="-12146441" gradientEndColor="-9378161" shadow="false" autoBackground="false" predefinedStyle="false"/>
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
<Format class="com.fr.base.CoreDecimalFormat" roundingMode="6">
<![CDATA[#.##]]></Format>
<PercentFormat>
<Format class="com.fr.base.CoreDecimalFormat" roundingMode="6">
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
<Attr gradientType="normal" gradientStartColor="-12146441" gradientEndColor="-9378161" shadow="false" autoBackground="false" predefinedStyle="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-6908266" autoColor="false" predefinedStyle="false"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<Attr position="4" visible="true" predefinedStyle="false"/>
<FRFont name="SimSun" style="0" size="72"/>
</Legend>
<DataSheet>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr gradientType="normal" gradientStartColor="-12146441" gradientEndColor="-9378161" shadow="false" autoBackground="false" predefinedStyle="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="1" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-16777216" autoColor="false" predefinedStyle="false"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<Attr isVisible="false" predefinedStyle="false"/>
<FRFont name="Microsoft JhengHei" style="0" size="72"/>
</DataSheet>
<DataProcessor class="com.fr.base.chart.chartdata.model.NormalDataModel"/>
<newPlotFillStyle>
<AttrFillStyle>
<AFStyle colorStyle="0"/>
<FillStyleName fillStyleName=""/>
<isCustomFillStyle isCustomFillStyle="false"/>
<PredefinedStyle predefinedStyle="false"/>
</AttrFillStyle>
</newPlotFillStyle>
<PieAttr subType="1" smallPercent="0.05"/>
</Plot>
<CategoryPlot>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr gradientType="normal" gradientStartColor="-12146441" gradientEndColor="-9378161" shadow="false" autoBackground="false" predefinedStyle="false"/>
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
<Format class="com.fr.base.CoreDecimalFormat" roundingMode="6">
<![CDATA[#.##]]></Format>
<PercentFormat>
<Format class="com.fr.base.CoreDecimalFormat" roundingMode="6">
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
<Attr gradientType="normal" gradientStartColor="-12146441" gradientEndColor="-9378161" shadow="false" autoBackground="false" predefinedStyle="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-6908266" autoColor="false" predefinedStyle="false"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<Attr position="4" visible="true" predefinedStyle="false"/>
<FRFont name="SimSun" style="0" size="72"/>
</Legend>
<DataSheet>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr gradientType="normal" gradientStartColor="-12146441" gradientEndColor="-9378161" shadow="false" autoBackground="false" predefinedStyle="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="1" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-16777216" autoColor="false" predefinedStyle="false"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<Attr isVisible="false" predefinedStyle="false"/>
<FRFont name="Microsoft JhengHei" style="0" size="72"/>
</DataSheet>
<DataProcessor class="com.fr.base.chart.chartdata.model.NormalDataModel"/>
<newPlotFillStyle>
<AttrFillStyle>
<AFStyle colorStyle="0"/>
<FillStyleName fillStyleName=""/>
<isCustomFillStyle isCustomFillStyle="false"/>
<PredefinedStyle predefinedStyle="false"/>
</AttrFillStyle>
</newPlotFillStyle>
<RectanglePlotAttr interactiveAxisTooltip="false"/>
<xAxis>
<CategoryAxis class="com.fr.chart.chartattr.CategoryAxis">
<newAxisAttr isShowAxisLabel="true"/>
<AxisLineStyle AxisStyle="1" MainGridStyle="0"/>
<newLineColor mainGridColor="-4144960" mainGridPredefinedStyle="false" lineColor="-5197648" predefinedStyle="false"/>
<AxisPosition value="3"/>
<TickLine201106 type="2" secType="0"/>
<ArrowShow arrowShow="false"/>
<TextAttr>
<Attr alignText="0" predefinedStyle="false"/>
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
<newLineColor mainGridColor="-4144960" mainGridPredefinedStyle="false" lineColor="-5197648" predefinedStyle="false"/>
<AxisPosition value="2"/>
<TickLine201106 type="2" secType="0"/>
<ArrowShow arrowShow="false"/>
<TextAttr>
<Attr alignText="0" predefinedStyle="false"/>
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
<newLineColor mainGridColor="-4144960" mainGridPredefinedStyle="false" lineColor="-5197648" predefinedStyle="false"/>
<AxisPosition value="4"/>
<TickLine201106 type="2" secType="0"/>
<ArrowShow arrowShow="false"/>
<TextAttr>
<Attr alignText="0" predefinedStyle="false"/>
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
</MapPlot>
</Plot>
<ChartDefinition>
<MapMoreLayerTableDefinition>
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<TableData class="com.fr.data.impl.NameTableData">
<Name>
<![CDATA[ds2]]></Name>
</TableData>
<MoreMapSingle>
<MapSingleLayerTableDefinition>
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<AreaName areaName="省份"/>
<DefinitionList>
<SeriesDefinition>
<SeriesName>
<O>
<![CDATA[销售额]]></O>
</SeriesName>
<SeriesValue>
<O>
<![CDATA[销售额]]></O>
</SeriesValue>
</SeriesDefinition>
</DefinitionList>
</MapSingleLayerTableDefinition>
</MoreMapSingle>
</MapMoreLayerTableDefinition>
</ChartDefinition>
</Chart>
</Chart>
<ChartMobileAttrProvider zoomOut="0" zoomIn="2" allowFullScreen="true" functionalWhenUnactivated="false"/>
<MobileChartCollapsedStyle class="com.fr.form.ui.mobile.MobileChartCollapsedStyle">
<collapseButton showButton="true" color="-6710887" foldedHint="" unfoldedHint="" defaultState="0"/>
<collapsedWork value="false"/>
</MobileChartCollapsedStyle>
</body>
</InnerWidget>
<BoundsAttr x="0" y="0" width="598" height="541"/>
</Widget>
<ShowBookmarks showBookmarks="true"/>
<Sorted sorted="false"/>
<MobileWidgetList>
<Widget widgetName="chart1"/>
<Widget widgetName="report0"/>
</MobileWidgetList>
<FrozenWidgets/>
<MobileBookMarkStyle class="com.fr.form.ui.mobile.impl.DefaultMobileBookMarkStyle"/>
<WidgetZoomAttr compState="0"/>
<AppRelayout appRelayout="true"/>
<Size width="962" height="541"/>
<ResolutionScalingAttr percent="1.2"/>
<BodyLayoutType type="0"/>
</Center>
</Layout>
<DesignerVersion DesignerVersion="KAA"/>
<PreviewType PreviewType="0"/>
<TemplateIdAttMark class="com.fr.base.iofile.attr.TemplateIdAttrMark">
<TemplateIdAttMark TemplateId="be2c7e25-d26f-4473-8e17-dbb231158bc9"/>
</TemplateIdAttMark>
</Form>
