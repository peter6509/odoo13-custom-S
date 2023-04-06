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
<![CDATA[SELECT 銷售員|| ${ int (RAND()*8)} as 銷售員,銷量 FROM 銷量]]></Query>
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
<LCAttr vgap="0" hgap="0" compInterval="0"/>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.ui.container.cardlayout.WCardMainBorderLayout">
<WidgetName name="tablayout0"/>
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
<NorthAttr size="36"/>
<North class="com.fr.form.ui.container.cardlayout.WCardTitleLayout">
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
<EastAttr size="25"/>
<East class="com.fr.form.ui.CardAddButton">
<WidgetName name="Add"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<AddTagAttr layoutName="tabpane0"/>
</East>
<Center class="com.fr.form.ui.container.cardlayout.WCardTagLayout">
<WidgetName name="tabpane0"/>
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
<LCAttr vgap="0" hgap="1" compInterval="0"/>
<Widget class="com.fr.form.ui.CardSwitchButton">
<WidgetName name="01db9b0e-e92d-4084-83e7-9b041c08d8d8"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<Text>
<![CDATA[TAB塊下整體復新]]></Text>
<SwitchTagAttr layoutName="cardlayout0"/>
</Widget>
<Widget class="com.fr.form.ui.CardSwitchButton">
<WidgetName name="bcb9ef42-dfd7-4720-a141-c9ca0558e582"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<Text>
<![CDATA[TAB塊下單個圖表塊復新]]></Text>
<SwitchTagAttr layoutName="cardlayout0" index="1"/>
</Widget>
<DisplayPosition type="0"/>
<FLAttr alignment="0"/>
<ColumnWidth defaultValue="80">
<![CDATA[200,80,80,80,80,80,80,80,80,80,80]]></ColumnWidth>
<FRFont name="SimSun" style="0" size="72"/>
<TextDirection type="0"/>
<TemplateStyle class="com.fr.general.cardtag.DefaultTemplateStyle"/>
<MobileTemplateStyle class="com.fr.general.cardtag.mobile.DefaultMobileTemplateStyle">
<initialColor color="-13072146"/>
<tabFontConfig selectFontColor="-16777216">
<FRFont name="Dialog.plain" style="0" size="72"/>
</tabFontConfig>
<custom custom="false"/>
</MobileTemplateStyle>
</Center>
<CardTitleLayout layoutName="cardlayout0"/>
</North>
<Center class="com.fr.form.ui.container.WCardLayout">
<WidgetName name="cardlayout0"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<Margin top="0" left="0" bottom="0" right="0"/>
<Border>
<border style="1" color="-723724" borderRadius="0" type="1" borderStyle="0"/>
<WidgetTitle>
<O>
<![CDATA[新建标题]]></O>
<FRFont name="SimSun" style="0" size="72"/>
<Position pos="0"/>
<Background name="ColorBackground" color="-13400848"/>
</WidgetTitle>
<Alpha alpha="1.0"/>
</Border>
<LCAttr vgap="0" hgap="0" compInterval="0"/>
<Widget class="com.fr.form.ui.container.cardlayout.WTabFitLayout">
<Listener event="click">
<JavaScript class="com.fr.js.JavaScriptImpl">
<Parameters/>
<Content>
<![CDATA[
var chartWrapper = FR.Chart.WebUtils.getChart("chart0");
chartWrapper.dataRefresh();


var chartWrapper1 = FR.Chart.WebUtils.getChart("A1");
chartWrapper1.dataRefresh();


var chartWrapper2 = FR.Chart.WebUtils.getChart("A18");
chartWrapper2.dataRefresh([1]A);]]></Content>
</JavaScript>
</Listener>
<WidgetName name="Tab0"/>
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
<![CDATA[復新]]></O>
<TextAttr>
<Attr alignText="0">
<FRFont name="微软雅黑" style="0" size="128" foreground="-13421773"/>
</Attr>
</TextAttr>
<TitleVisible value="true" position="0"/>
</Title>
<Attr4VanChart useHtml="false" floating="false" x="0.0" y="0.0" limitSize="false" maxHeight="15.0"/>
</Title4VanChart>
<Plot class="com.fr.plugin.chart.column.VanChartColumnPlot">
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
<Attr isNullValueBreak="true" autoRefreshPerSecond="6" seriesDragEnable="false" plotStyle="4" combinedSize="50.0"/>
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
<Attr enable="true" duration="4" followMouse="false" showMutiSeries="false" isCustom="false"/>
<TextAttr>
<Attr alignText="0"/>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="true"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipValueFormat">
<AttrTooltipValueFormat>
<Attr enable="true"/>
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
<Attr shadow="true"/>
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
<Attr lineStyle="1" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-1"/>
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
<FRFont name="verdana" style="0" size="88" foreground="-10066330"/>
</Attr>
</TextAttr>
<AxisLabelCount value="=1"/>
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
<FRFont name="verdana" style="0" size="88" foreground="-10066330"/>
</Attr>
</TextAttr>
<TitleVisible value="true" position="0"/>
</Title>
<newAxisAttr isShowAxisLabel="true"/>
<AxisLineStyle AxisStyle="0" MainGridStyle="1"/>
<newLineColor mainGridColor="-3881788" lineColor="-5197648"/>
<AxisPosition value="2"/>
<TickLine201106 type="2" secType="0"/>
<ArrowShow arrowShow="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="verdana" style="0" size="88" foreground="-10066330"/>
</Attr>
</TextAttr>
<AxisLabelCount value="=1"/>
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
</YAxisList>
<stackAndAxisCondition>
<ConditionCollection>
<DefaultAttr class="com.fr.chart.chartglyph.ConditionAttr">
<ConditionAttr name=""/>
</DefaultAttr>
</ConditionCollection>
</stackAndAxisCondition>
<VanChartColumnPlotAttr seriesOverlapPercent="20.0" categoryIntervalPercent="20.0" fixedWidth="false" columnWidth="0" filledWithImage="false" isBar="false"/>
</Plot>
<ChartDefinition>
<MoreNameCDDefinition>
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<TableData class="com.fr.data.impl.NameTableData">
<Name>
<![CDATA[ds1]]></Name>
</TableData>
<CategoryName value="銷售員"/>
<ChartSummaryColumn name="銷量" function="com.fr.data.util.function.NoneFunction" customName="銷量"/>
</MoreNameCDDefinition>
</ChartDefinition>
</Chart>
<tools hidden="true" sort="true" export="true" fullScreen="true"/>
<VanChartZoom>
<zoomAttr zoomVisible="false" zoomGesture="true" zoomResize="true" zoomType="xy"/>
<from>
<![CDATA[]]></from>
<to>
<![CDATA[]]></to>
</VanChartZoom>
<refreshMoreLabel>
<attr moreLabel="false" autoTooltip="true"/>
<AttrTooltip>
<Attr enable="true" duration="4" followMouse="false" showMutiSeries="false" isCustom="false"/>
<TextAttr>
<Attr alignText="0"/>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="true"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipValueFormat">
<AttrTooltipValueFormat>
<Attr enable="true"/>
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
<BoundsAttr x="479" y="0" width="479" height="502"/>
</Widget>
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
<![CDATA[刷新]]></O>
<TextAttr>
<Attr alignText="0">
<FRFont name="微软雅黑" style="0" size="128" foreground="-13421773"/>
</Attr>
</TextAttr>
<TitleVisible value="true" position="0"/>
</Title>
<Attr4VanChart useHtml="false" floating="false" x="0.0" y="0.0" limitSize="false" maxHeight="15.0"/>
</Title4VanChart>
<Plot class="com.fr.plugin.chart.column.VanChartColumnPlot">
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
<Attr isNullValueBreak="true" autoRefreshPerSecond="6" seriesDragEnable="false" plotStyle="4" combinedSize="50.0"/>
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
<Attr enable="true" duration="4" followMouse="false" showMutiSeries="false" isCustom="false"/>
<TextAttr>
<Attr alignText="0"/>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="true"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipValueFormat">
<AttrTooltipValueFormat>
<Attr enable="true"/>
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
<Attr shadow="true"/>
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
<Attr lineStyle="1" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-1"/>
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
<FRFont name="verdana" style="0" size="88" foreground="-10066330"/>
</Attr>
</TextAttr>
<AxisLabelCount value="=1"/>
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
<FRFont name="verdana" style="0" size="88" foreground="-10066330"/>
</Attr>
</TextAttr>
<TitleVisible value="true" position="0"/>
</Title>
<newAxisAttr isShowAxisLabel="true"/>
<AxisLineStyle AxisStyle="0" MainGridStyle="1"/>
<newLineColor mainGridColor="-3881788" lineColor="-5197648"/>
<AxisPosition value="2"/>
<TickLine201106 type="2" secType="0"/>
<ArrowShow arrowShow="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="verdana" style="0" size="88" foreground="-10066330"/>
</Attr>
</TextAttr>
<AxisLabelCount value="=1"/>
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
</YAxisList>
<stackAndAxisCondition>
<ConditionCollection>
<DefaultAttr class="com.fr.chart.chartglyph.ConditionAttr">
<ConditionAttr name=""/>
</DefaultAttr>
</ConditionCollection>
</stackAndAxisCondition>
<VanChartColumnPlotAttr seriesOverlapPercent="20.0" categoryIntervalPercent="20.0" fixedWidth="false" columnWidth="0" filledWithImage="false" isBar="false"/>
</Plot>
<ChartDefinition>
<MoreNameCDDefinition>
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<TableData class="com.fr.data.impl.NameTableData">
<Name>
<![CDATA[ds1]]></Name>
</TableData>
<CategoryName value="销售员"/>
<ChartSummaryColumn name="销量" function="com.fr.data.util.function.NoneFunction" customName="销量"/>
</MoreNameCDDefinition>
</ChartDefinition>
</Chart>
<tools hidden="true" sort="true" export="true" fullScreen="true"/>
<VanChartZoom>
<zoomAttr zoomVisible="false" zoomGesture="true" zoomResize="true" zoomType="xy"/>
<from>
<![CDATA[]]></from>
<to>
<![CDATA[]]></to>
</VanChartZoom>
<refreshMoreLabel>
<attr moreLabel="false" autoTooltip="true"/>
<AttrTooltip>
<Attr enable="true" duration="4" followMouse="false" showMutiSeries="false" isCustom="false"/>
<TextAttr>
<Attr alignText="0"/>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="true"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipValueFormat">
<AttrTooltipValueFormat>
<Attr enable="true"/>
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
</body>
</InnerWidget>
<BoundsAttr x="479" y="0" width="479" height="502"/>
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
<FileAttrErrorMarker class="com.fr.base.io.FileAttrErrorMarker" pluginID="com.fr.plugin.reportRefresh" oriClass="com.fr.plugin.reportRefresh.ReportExtraRefreshAttr">
<Refresh customClass="false" interval="0.0" state="0"/>
</FileAttrErrorMarker>
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
<C c="0" r="0" cs="7" rs="14">
<O t="CC">
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
<![CDATA[復新]]></O>
<TextAttr>
<Attr alignText="0">
<FRFont name="微软雅黑" style="0" size="128" foreground="-13421773"/>
</Attr>
</TextAttr>
<TitleVisible value="true" position="0"/>
</Title>
<Attr4VanChart useHtml="false" floating="false" x="0.0" y="0.0" limitSize="false" maxHeight="15.0"/>
</Title4VanChart>
<Plot class="com.fr.plugin.chart.column.VanChartColumnPlot">
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
<Attr isNullValueBreak="true" autoRefreshPerSecond="6" seriesDragEnable="false" plotStyle="4" combinedSize="50.0"/>
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
<Attr enable="true" duration="4" followMouse="false" showMutiSeries="false" isCustom="false"/>
<TextAttr>
<Attr alignText="0"/>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="true"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipValueFormat">
<AttrTooltipValueFormat>
<Attr enable="true"/>
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
<Attr shadow="true"/>
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
<Attr lineStyle="1" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-1"/>
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
<FRFont name="verdana" style="0" size="88" foreground="-10066330"/>
</Attr>
</TextAttr>
<AxisLabelCount value="=1"/>
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
<FRFont name="verdana" style="0" size="88" foreground="-10066330"/>
</Attr>
</TextAttr>
<TitleVisible value="true" position="0"/>
</Title>
<newAxisAttr isShowAxisLabel="true"/>
<AxisLineStyle AxisStyle="0" MainGridStyle="1"/>
<newLineColor mainGridColor="-3881788" lineColor="-5197648"/>
<AxisPosition value="2"/>
<TickLine201106 type="2" secType="0"/>
<ArrowShow arrowShow="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="verdana" style="0" size="88" foreground="-10066330"/>
</Attr>
</TextAttr>
<AxisLabelCount value="=1"/>
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
</YAxisList>
<stackAndAxisCondition>
<ConditionCollection>
<DefaultAttr class="com.fr.chart.chartglyph.ConditionAttr">
<ConditionAttr name=""/>
</DefaultAttr>
</ConditionCollection>
</stackAndAxisCondition>
<VanChartColumnPlotAttr seriesOverlapPercent="20.0" categoryIntervalPercent="20.0" fixedWidth="false" columnWidth="0" filledWithImage="false" isBar="false"/>
</Plot>
<ChartDefinition>
<MoreNameCDDefinition>
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<TableData class="com.fr.data.impl.NameTableData">
<Name>
<![CDATA[ds1]]></Name>
</TableData>
<CategoryName value="銷售員"/>
<ChartSummaryColumn name="銷量" function="com.fr.data.util.function.NoneFunction" customName="銷量"/>
</MoreNameCDDefinition>
</ChartDefinition>
</Chart>
<tools hidden="true" sort="true" export="true" fullScreen="true"/>
<VanChartZoom>
<zoomAttr zoomVisible="false" zoomGesture="true" zoomResize="true" zoomType="xy"/>
<from>
<![CDATA[]]></from>
<to>
<![CDATA[]]></to>
</VanChartZoom>
<refreshMoreLabel>
<attr moreLabel="false" autoTooltip="true"/>
<AttrTooltip>
<Attr enable="true" duration="4" followMouse="false" showMutiSeries="false" isCustom="false"/>
<TextAttr>
<Attr alignText="0"/>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="true"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipValueFormat">
<AttrTooltipValueFormat>
<Attr enable="true"/>
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
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="0" r="17" cs="7" rs="14">
<O t="CC">
<LayoutAttr selectedIndex="0"/>
<ChangeAttr enable="true" changeType="button" timeInterval="5" buttonColor="-8421505" carouselColor="-8421505" showArrow="true">
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
<![CDATA[不復新]]></O>
<TextAttr>
<Attr alignText="0">
<FRFont name="微软雅黑" style="0" size="128" foreground="-13421773"/>
</Attr>
</TextAttr>
<TitleVisible value="true" position="0"/>
</Title>
<Attr4VanChart useHtml="false" floating="false" x="0.0" y="0.0" limitSize="false" maxHeight="15.0"/>
</Title4VanChart>
<Plot class="com.fr.plugin.chart.column.VanChartColumnPlot">
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
<Attr isNullValueBreak="true" autoRefreshPerSecond="6" seriesDragEnable="false" plotStyle="4" combinedSize="50.0"/>
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
<Attr enable="true" duration="4" followMouse="false" showMutiSeries="false" isCustom="false"/>
<TextAttr>
<Attr alignText="0"/>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="true"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipValueFormat">
<AttrTooltipValueFormat>
<Attr enable="true"/>
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
<Attr shadow="true"/>
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
<Attr lineStyle="1" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-1"/>
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
<FRFont name="verdana" style="0" size="88" foreground="-10066330"/>
</Attr>
</TextAttr>
<AxisLabelCount value="=1"/>
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
<FRFont name="verdana" style="0" size="88" foreground="-10066330"/>
</Attr>
</TextAttr>
<TitleVisible value="true" position="0"/>
</Title>
<newAxisAttr isShowAxisLabel="true"/>
<AxisLineStyle AxisStyle="0" MainGridStyle="1"/>
<newLineColor mainGridColor="-3881788" lineColor="-5197648"/>
<AxisPosition value="2"/>
<TickLine201106 type="2" secType="0"/>
<ArrowShow arrowShow="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="verdana" style="0" size="88" foreground="-10066330"/>
</Attr>
</TextAttr>
<AxisLabelCount value="=1"/>
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
</YAxisList>
<stackAndAxisCondition>
<ConditionCollection>
<DefaultAttr class="com.fr.chart.chartglyph.ConditionAttr">
<ConditionAttr name=""/>
</DefaultAttr>
</ConditionCollection>
</stackAndAxisCondition>
<VanChartColumnPlotAttr seriesOverlapPercent="20.0" categoryIntervalPercent="20.0" fixedWidth="false" columnWidth="0" filledWithImage="false" isBar="false"/>
</Plot>
<ChartDefinition>
<MoreNameCDDefinition>
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<TableData class="com.fr.data.impl.NameTableData">
<Name>
<![CDATA[ds1]]></Name>
</TableData>
<CategoryName value="銷售員"/>
<ChartSummaryColumn name="銷量" function="com.fr.data.util.function.NoneFunction" customName="銷量"/>
</MoreNameCDDefinition>
</ChartDefinition>
</Chart>
<tools hidden="true" sort="true" export="true" fullScreen="true"/>
<VanChartZoom>
<zoomAttr zoomVisible="false" zoomGesture="true" zoomResize="true" zoomType="xy"/>
<from>
<![CDATA[]]></from>
<to>
<![CDATA[]]></to>
</VanChartZoom>
<refreshMoreLabel>
<attr moreLabel="false" autoTooltip="true"/>
<AttrTooltip>
<Attr enable="true" duration="4" followMouse="false" showMutiSeries="false" isCustom="false"/>
<TextAttr>
<Attr alignText="0"/>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="true"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipValueFormat">
<AttrTooltipValueFormat>
<Attr enable="true"/>
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
<Chart name="图表2" chartClass="com.fr.plugin.chart.vanchart.VanChart">
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
<![CDATA[復新]]></O>
<TextAttr>
<Attr alignText="0">
<FRFont name="微软雅黑" style="0" size="128" foreground="-13421773"/>
</Attr>
</TextAttr>
<TitleVisible value="true" position="0"/>
</Title>
<Attr4VanChart useHtml="false" floating="false" x="0.0" y="0.0" limitSize="false" maxHeight="15.0"/>
</Title4VanChart>
<Plot class="com.fr.plugin.chart.column.VanChartColumnPlot">
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
<Attr isNullValueBreak="true" autoRefreshPerSecond="6" seriesDragEnable="false" plotStyle="4" combinedSize="50.0"/>
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
<Attr enable="true" duration="4" followMouse="false" showMutiSeries="false" isCustom="false"/>
<TextAttr>
<Attr alignText="0"/>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="true"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipValueFormat">
<AttrTooltipValueFormat>
<Attr enable="true"/>
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
<Attr shadow="true"/>
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
<Attr lineStyle="1" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-1"/>
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
<VanChartRectanglePlotAttr vanChartPlotType="normal" isDefaultIntervalBackground="true"/>
<XAxisList>
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
<Attr alignText="0">
<FRFont name="verdana" style="0" size="88" foreground="-10066330"/>
</Attr>
</TextAttr>
<TitleVisible value="true" position="0"/>
</Title>
<newAxisAttr isShowAxisLabel="true"/>
<AxisLineStyle AxisStyle="0" MainGridStyle="1"/>
<newLineColor mainGridColor="-3881788" lineColor="-5197648"/>
<AxisPosition value="3"/>
<TickLine201106 type="2" secType="0"/>
<ArrowShow arrowShow="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="verdana" style="0" size="88" foreground="-10066330"/>
</Attr>
</TextAttr>
<AxisLabelCount value="=1"/>
<AxisRange/>
<AxisUnit201106 isCustomMainUnit="false" isCustomSecUnit="false" mainUnit="=0" secUnit="=0"/>
<ZoomAxisAttr isZoom="false"/>
<axisReversed axisReversed="false"/>
<VanChartAxisAttr mainTickLine="0" secTickLine="0" axisName="X軸" titleUseHtml="false" autoLabelGap="true" limitSize="false" maxHeight="15.0" commonValueFormat="true" isRotation="false"/>
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
</XAxisList>
<YAxisList>
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
<Attr rotation="-90" alignText="0">
<FRFont name="verdana" style="0" size="88" foreground="-10066330"/>
</Attr>
</TextAttr>
<TitleVisible value="true" position="0"/>
</Title>
<newAxisAttr isShowAxisLabel="true"/>
<AxisLineStyle AxisStyle="1" MainGridStyle="1"/>
<newLineColor lineColor="-5197648"/>
<AxisPosition value="2"/>
<TickLine201106 type="2" secType="0"/>
<ArrowShow arrowShow="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="verdana" style="0" size="88" foreground="-10066330"/>
</Attr>
</TextAttr>
<AxisLabelCount value="=1"/>
<AxisRange/>
<AxisUnit201106 isCustomMainUnit="false" isCustomSecUnit="false" mainUnit="=0" secUnit="=0"/>
<ZoomAxisAttr isZoom="false"/>
<axisReversed axisReversed="false"/>
<VanChartAxisAttr mainTickLine="2" secTickLine="0" axisName="Y軸" titleUseHtml="false" autoLabelGap="true" limitSize="false" maxHeight="15.0" commonValueFormat="true" isRotation="false"/>
<HtmlLabel customText="function(){ return this; }" useHtml="false" isCustomWidth="false" isCustomHeight="false" width="50" height="50"/>
<alertList/>
<customBackgroundList/>
</VanChartAxis>
</YAxisList>
<stackAndAxisCondition>
<ConditionCollection>
<DefaultAttr class="com.fr.chart.chartglyph.ConditionAttr">
<ConditionAttr name=""/>
</DefaultAttr>
</ConditionCollection>
</stackAndAxisCondition>
<VanChartColumnPlotAttr seriesOverlapPercent="20.0" categoryIntervalPercent="20.0" fixedWidth="false" columnWidth="0" filledWithImage="false" isBar="true"/>
</Plot>
<ChartDefinition>
<MoreNameCDDefinition>
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<TableData class="com.fr.data.impl.NameTableData">
<Name>
<![CDATA[ds1]]></Name>
</TableData>
<CategoryName value="銷售員"/>
<ChartSummaryColumn name="銷量" function="com.fr.data.util.function.NoneFunction" customName="銷量"/>
</MoreNameCDDefinition>
</ChartDefinition>
</Chart>
<tools hidden="true" sort="true" export="true" fullScreen="true"/>
<VanChartZoom>
<zoomAttr zoomVisible="false" zoomGesture="true" zoomResize="true" zoomType="xy"/>
<from>
<![CDATA[]]></from>
<to>
<![CDATA[]]></to>
</VanChartZoom>
<refreshMoreLabel>
<attr moreLabel="false" autoTooltip="true"/>
<AttrTooltip>
<Attr enable="true" duration="4" followMouse="false" showMutiSeries="false" isCustom="false"/>
<TextAttr>
<Attr alignText="0"/>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="true"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipValueFormat">
<AttrTooltipValueFormat>
<Attr enable="true"/>
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
<StyleList/>
<heightRestrict heightrestrict="false"/>
<heightPercent heightpercent="0.75"/>
<IM>
<![CDATA[c+F?bbj59nr0`rg;A*/H)/CBfU8")BOq-c5,d!k/WZgae1NA4;#YCNA;%t>Dc&dgk&Lsn=Q*
`J+X]A)PhpLeNl\!cgcs0(>O4TFS)Qclq`h"UbmYHR]AdI=L[30)oWo-6op#$A'B<o3FGZ+:(D
j+Jd.2$1Q&KLXKQ9EpGI;Z0aeAHs_JBN-se#574+.g?U*^H4#'<C!#_N2_GLY%=P@!bjI@[_
m2L+lk3<""F`CQap_jd<c$A#414A^)rD<uDJk^nT65),d8Tdo7N*kGo%(O(26e`!.4=AJM=T
3AjR-W>e:qn"G*ZH-]A+S%MUXaI0_,E2"b7$I@mPFB\CjC-1lm)-tlkR/GGQ"9_?%X.H]AAka1
NG-Q-UgC_,m%9Dsc8lV/L5WX[iR&s5"\n>lJ)g4<iCAJ#-`Rr`rNubj8r5YlId<J"AZJ53@"
:^Xi47jhWIdtqK<PNGhKkZUI>njJGeD`#eZYtA-l5DVLTDQig_DeG%1c"`fK!0p?Pt5O8CPL
.Q8B;uXL?%S#"8JJH?]A!'flgj!\3ej,cR*WQ'>:ASN8kjQEqKnf^uClBiA;5e59Dhfh^=,en
r6C>\u!iW&W3tkCa`O)M"Q_`*';rVBE$!cs8;`(UohbjX;Li\5"m^gn&Ih3XMbnG/J.qQ?G6
)o7.BU5"16rqTV/mthWhffq>']A>Uof,+DQk$aYcDg%)E`eYXhI[Xd#.?N#9)e`\\FbB2q03/
>gDpIqV.BY8[h#-G<P7q[F,@Pp$!qi[oHq%L+.:'D0D$2lG-3-5$9MkAG2Pd8TN-!O+1n\RT
udshV%I"&!nRm(>TB<H$')>>;t#KEEIUdM:e91NEK\[a'0d!SR`eNBjACjF6+0-bf]A*L7++"
8J'IPLf[Vq,Tn+,\9LMg5j[l+ToZa=ggkDb(IV<W9Y0O#TeE8CD'/Z<m<paW:e"k+7Juf/ph
RJu\'oZ^UB<,t!?F60/]A#ERlbbi#2>8?rMZMPT9Z!k]A+HH5Ns]AY+4k1l[daeJ#!mr:.lU!cN
2ls(*a-_IMG4,/W2WMK,`#`,%Sn[otDE9pe;c3$Bi?Y\!5MrU_#b:Z$ksLb6%4@s>?B+/r9F
n"c2h,EI>U"O`'R;gHelb3'k+Ycp0:9;"juG]ANS=bg="EJS1-_9(t.9TD^\5BjMZ7QIO0)r+
"8(X=*ZNd*Xg/e1^s]An<B31IOihEc:rE/Eeh?MV\OCj>:*;&pJb=fjC@XH,UN'BOQQ^YSPB)
B4LsA%2a2A<S%l9l=aa49*4oAcNJMiMllD'g909`0"G-=o?K9DI3RAMD6X4"!>NN,P+GZsKm
gY+B:.[>M*:gijR@>f`-3khWf:XqVVeS$_l_X>pPp-*09F`<0d\TUK8.8PLe=8S,A&jV--1-
Fc'?+*L:+g^0'O=6ZdiCN1SMVhGSar^iBWh(r0.7I7>O"F!OZ1R^bp,fm![!=,9dnC703bl$
_^78+U8_i7k(!:E&E<\]A>eGYj$O6$;B-p;P*+!U1<M:chc*3l/8BOt+j``fmBJpGT1jk@fGe
fkie3#b%DY3t@6@]A5(H?qG[lP-W0nk)Ie2/-BM^1oI2.XsR;5H]Am(]A;Xp-Egiao?n*YtK,IZ
"]Aq/P65nmMrau*1s7G9pjO'IlAbuf,n<gi5Wk7C-5$lL-tV=Al[8dO35Jh`=0?Iis[2^rjUT
'=2ZE4SLWI\OM7e54lt`nB%ArZD>A4bfb=>rji&d@1oXIFF^$osf]A)XiZ4S=AEYbV(,eO>LM
p$Mi;&e7&-8!Du1PmmmY.Qq3>m?9>%_1eRWIO/P:o\Wks=6LZs*[j*[_;30hQ'1!$@Q\F/GW
N<D22;]A/\cFuEgs(C/nqJ.rb:'XM?L;G956n[UG9*#nmFqb@q,C-3l>kor\Ts*j>m<C8p$-P
Ui,;(*&QW/r*$GE#3Vhn]A70EoCY<CO)uFX$QaA"6*s=55!JkP&6rdLo._F_@\4c4$%2_i17Z
NQp^9s1e-q4S#Z\K:m*SZR;0"*_Y#GGAZD7AGYT5A30`l.rR`HuauckLC#m<#U%Gnm4:0PNE
o1uUX<uA8?/*fR^''?4PP[^*%np%aLuq=(*aZk^L=^S.;`SWLSH[)5:uq*I+k:%K9OBrrl@_
4*+uDG&_b]A8&&_s01D=TN+=c]AIj#["2_+gieS<LcpA*i"4Xc<:D$)LohrRu=WaBfS=;[YVSt
><$Z,U9Y6D=S?*)l;BN1;:_lB_d$Xr8NX4h?L9^O`=K(Hncm)LO_DW(<BbHj(X%Wc=Mh)3a%
InE3@qk79@%4'DcT7Dn4-[JMGqYD?L?15"tP"l_VGqtX`^H08oHkA*c'WYUD7YSSbD0Nk&p>
KXmn"\WVosIcaO-7.8S.!\7;Z$"*nuA#nPmFZLK6$%M$b3FlnoK>)r/W&ieI`STT*%_4uFZ$
_W,75EL@BVIf!@/&fHd/CQAr1Pn(m"+mr\QUp<)8?_9$J]ADY1D3PXH-2`ASMi#7e;A76@LpD
_N*;4),Eh>0@?$;rbg5ML;gdgOMk%YZb[9:!4XmmGiU7'n8iM@lR7oJLO%seSps(idX/0K+,
ElkUu?a0!eblF/Y)h;N"D^!=]AaP,)QWEn>JjUQbdXXou#$d$@n$0p\7\Hr(a+Q!`V_:Z/s;t
]AB8SrIYO$hqpQXfQqb=)&MIQI&9kQ]Ao&O.:=Y"\f7]A)<7N6`WGG=:oL;_Z/Y9AlQ@g(RmZN9
PlVD_0%]A[UTbJH',,7T*jgp]Ato(`.?B#-Z(BQMP0<;[XDT?f^2)d@Ob0h]Ac,1Zq<7gAmsp^`
0C"7G:DV8q=Uotobnc_c6PCN,^1aOief6%O_qiDI"0t$X`O,D7p:rg'M_=2.YMY?&LCCPbm-
sMV8$1]AEGG,Gf@g3B:tom_0n_$VH(g2If2i9JLpF$bIXnH_Bd*&OMW&hdH74FD%;/2--l>OK
lsj%(WG`t[m[b0>@PO(qL90ir;L'Wf=9q'!`n4Ci;fcLo.UL\d$Ep]A9,?22'l_1l0CsEHc+W
X#ZagP[H:+i&m9:+3Z$Ba--Z`n@lh>:P\W^e\<2C7JT=9p>!PIj9hAAGqIVu6R,D$ThEjumA
V0?M)[\[:Y^`rlF@+q,K-LaJY2E8\0]Ai/kbp-[6s1FSs=2]A-TD5',$#ibM'r.(QpPa$$-o@7
e(`T-6TLZ%T+uT['go]AiRr"DIDoC]A)$JZe(62CBJj-I0K9-.P;U/uAr/Wq8C"m;fP4"ZI]AR_
k^_tk.odJ*j]AK7<[McdN=F=U_9d9hW`l8#M1EB6!dABoi'8_<CmpXE:PcLD!F4BAF4sC11es
85DsTP;83T&kjt:Nk_sE\e_,SS@coP^jq@H@u5.)J!+?T4"n_B9kT1R]Ae8t%S>*J,m!NqiQ^
ncb4BX(qIrU?d5g]A(Z2;_3S`;/A8hB=p[d^4Z,OG;V#H.puYrr!;W'28SRH+T+;A]Am^i22M`
!CA>=g_2TU-;YZN?3o[[9%J^!"Qp!Sq'k]Ad*"\I1'd"IjlRkh?.gV<\l*`*5Q!XBhEps@oBo
ZkSMeo,F!Vg<B9rDL>GmNOubD8d<[gg\fe@fPb8B^QCQK96D'A8qBn:6+?.dI$K&o`f"R>jM
)iC5.f<S.F%);\&go`C6Ke"&\ZgqX6B#:u=@.h9neZ\[#WprELUa)F.IBVF!3#hDMb_S\u$\
4T\(/ar)X*Co`*!jFq[E'GR^<>tgJKCDN)]Akbtn\l2?+OpG;R"qm+_PJ9SiFDA*;]ABaCGd#l
4#\`YZn%Q9c;C$Ld9G(6R`LHA6d7egE)kC>^*h?0hX7U4f,6q_ce^F'Q]A[`i\o%dkW4i&Qsd
cgt8,;]A\LB#!kP.L"ABS+_!]AHXM,td_At6Hb$#tq4(=mL1C?cAJ7<ukbj/>=0/4%4c_CcNO:
`i]Aq0>(VG/;:u1'I/X_*P_ekQ:X/^c^/%@B2&1<8A/HO0*X,`C9A2QcH\l_.#FhS#"]A,+fSG
;1'kpFMdnGYAW%mffUmr7@U<1Z;blm6g]A/37),%Ph]A(?\+NrIDI8,^URKiX[.c<t?R'72Wm*
$t0k>)qF$@a.F1cH:-"&&4Y*BW#1FZAKt%QN2DH+cM"ts7$G2ql;tW6VPKX1-gKkH,Wf;R(b
.r5P$`H`3,rLA\R-$X"#_cL:.20(eA1.f4jt9sK/a&1cOs6-cQfC2/.IQtO*;&t5O.RcYA<2
>N!%J%-9ANn)Zo/s4KJZ\>_582k1DifA5A0:`5`h?gXk,l]An-a^Hi9cseZiLTiE/aW4r4+J\
$qZ+rQ%ZPE%GJTJ(>1V-5CP*7QO'M9DnY115_[PR90Yn[H[:N"i4]A,hous-AQQOo02utY^nn
qW2_>R.,3"OF\eLq<;U&E!2>9%AH!eLT1c.#lFB0^C[YZh@\;[XFJaSKH@2)unE-]A=%i\AT+
i1&9gL\E&[i3kK*q8^-4FKAZ&lmhBb9igj_cg)1@%6["o('1#%S<fUIjgOb8!Za>[G&%[m!Z
/1l-M>#dd9E#:WJIs_O$YQ^6ic]Ah_R94RPT&UR?\W$<IUM0a?SD_uLML-tj@s#@k'1OkEKE4
0erNVS0+!lVnP)=:F&'K8,<OgA]AFd@X_,rUGg7U!#q5[]A5r-bkWdjT!:L$#B5Tft2WGKtI0'
$NbmiEO#Z;N+q[9,Z;p+<k["Bt/_]Anol]AajmUtXb3ddSAXmDZCl.Qk-u/qf!'s;I[R&p'1s_
]A2&;QE*0fstr:DobS//sSpcMU-jq:V?ce_mG;l8pgV^UFoXkaGMZR-`KQ"R2+QQW(tXUn)-W
q)Y]A09>hW4HGmJf+FX6_\m'R#%5n[&>l(Ir9DhrpBn8AIhbF<.3%^Yh?AW^$6V%MgXIZ6;-!
cad/]Ac;bFm\ONT;U`uj,+Iprd&%a&igsS@Wnet9CT!2Dr8mY,HSa^;_c1'q4t<!#;Kod'M%S
/H&sU%UHiPp_Yce+6^2GEfRPaH*8#jI%chPPCS[PD&X[R-;\VB8]A25%hk,\;DBkFW+GWcAg,
1N=?W;]AF/:tZ=&lF?M?DcJ+thEuLCE'u3MIsf39KTRW)8J4!tNX,ULWnmgh^NJbI?PR*k4&5
VD@[CC->fmJ44VqVXf[VPa/[`0?Y]AgHi;ud<Fl0D-*`R2E>'Ip^m*.h7`X7nY1):=:t.5knl
5Sqea"O31ffQWZ1:HSj^6PfB'-Cg=5Q7IoVii%!^KkaT+$WG`Qqi?<R\jrYHE>#c:6*PLd62
\k/.JmIAJ8B?'kgc3h)`$3V04-S]ACd=9BOI7lV544pj7:U-PJ)r'oC0[\h2&.hp+3jH42O5V
7bpP$)PX3U8^4^X<K_%!I4Y\iN1Qtt,@&Ro,bo8HJdE^WmZ:*><H_V#!VV9`N9TR9p@$X2aj
D%9/E=B:nKJF#2NAb@f/AKrC?oR3^[6YADqG@?]AdRV;tjiR0anJW4VrGI\Eh@5M@:(2>&N<'
>AX7-0]AOe8,tcm=AboiEIrKnJja6?5s+Lgreb#_5G@$dr_6.M1&L5H?4pD.A[\"$-2;RW"d#
,cotqE%CV/-0(UV&\mb$8cs3s6G(@'3RDl%A*kE3Q/QNBf9a2KjA<5ho^&lFYua&C$5j/N$u
n.d<k9r,A6!T00<E6"M=o8Lim+sDMFn+EHsUCZ7`Eo<>T'GIC?SbU?7?O"Y:c&B2ki#*\n0<
s2`bpC*//5&O/^M&,&fCd#rW#!l<tD@a4RKe-n=iLB*mA,WMMU_Vt@a&;LV:Y=*)rYL8P8To
9S8_9%kqH*+c?u8k=/SBAR6<d-m75h]Ao>,;6\$!f6V6deag*-(Fbe3a;Ol)Z9OWg4RV>P^@7
T3Gk`USFBe[&cqp:.NRH)Ro!s*H$HFA<hC+2!A*3\lHp4K`FC"cM'IHJhodZ-Daa-ne0,%iR
jlNSdo<!]AtjAFV))"oP00-cV>cs3qd#`J5(crGoMn/bE-"2kXJV`'qKqr5ZRf;\FWE&G\&kn
$oW_b&8GPE&XdFdPnh]A=Y?Fcu%I%^1tj]Ap:?6[DiR/M6!_3l&+7ERR(7rR'UIY:6qQ@*)KBp
*er\0k8*&oc=M?0&d"#UE^lR<=6Y-$L7jehUSL5O8&r_KtBh^f6]AihZdK?tue`.$eG+k$_.:
4<@t;qWeIQ"?M=P'0CDNipo=4:-ojm=l/KC?l=rbJ/MNK'o-CDF,_?J'd6'3'P1H1:1^(bGn
7AK4O@:5T+<0't#&H1sX]A!G/'=9%!tQcN(fiKMA#d6,-n+T%W6[R4`B]AKCjI8ZWu'Nn4pG,6
rZsIB3g1?G+t/JH<_:YF+@=dG>g?1H9.4Q.P8a`keTdS6LM:M4HS0%52)'C&!"/YkW=^JUBi
clKfPJm*'lK-,qo^/kG9;>\#:]AVC,FceqW9e;cWHc[n\b:S%<bpesR)'Qo1,?&V`UMj?gYl@
0V.lp=Ts:E:+H7&JfljA7L!&Z/rN]Ak2;D$"Z"Zh\''<*C.=T'9gDB7da$b-KPankpU<MN@E5
lno"CJaSap*7!:_Jn(//7,#_Ja=o*=p13n$0pGa?VloueAh7<HC:QR9(>t6,)<Q`DY_LWE0H
1jD,,$$^MX3P#m5AJhGPN4c=7V1L8Y9+jgd\"jQEY>?-tSs!ViQP.['m#mcnA<m[M(A/;tka
<e=9Zq,*cicOJ<!+\R-N`WF<XD!1F/AQr5khKg$TW<@"&LE*)@X9q/e_upZmf'LtA/@'P'Sn
tDEJ?&ZG61OH%R?$jYH?[AqI,D[Tam.?)FGfOEb.`P5rs?R_."#4Ijb&-Dm/RGhG[,k$/HAB
h-FQ?\G,(]A+F6)-LEHs#S',&H0.=[^c3bJ4rlC5=Qs5]Ag]A/^jp9_"BRJ7??F=*Cs>!IhdCj<
4'F6/8o-d7pTk4<9O&s-$&=u3%:\ZEqdFE@Meb+)u\>L=e$`Oacg7?L8H8R9C+/GGSXCfa9Y
fS@D"*`HNq`39aK:\mVp$_LY18Og::CW0e2*GfiLG04c\H"_bonsL/oUW;b2dpYFfGBb]A"UV
%/m)KPhp9ZrU3`*)]AOhpaG+J8:JV64&TNr5@GqF2T+_m:?#,6q2G?J(O0q9G^oq+Q>D).QZi
7"LC)6Q?Sm-[R+X12b*7sNj3(2^Dqt;#n*XgTD).-_c5-Pf5BBSXNp,ntIc#oG*iW2,LGhl6
C.hC7)?5i@$o;5A"_l:/Z.el\-abN@@8F=JEl=jab=!1c?QP6Inq<L,*di)T*QurWLeC.pXM
&G8Im!2kWO$qctBu#+*ON5ERk:Z,N\,ab_RJ>eAW%Z19mFrE7/SESh:S]AljL"'.i0e.b$;04
VBL/:k$i_L$.6LQbf$\`(RjCAR<BAb)NE&!@!jfnj&q&.Z4Q]AJBNnb!\#pf4C",_>[-%*eOt
ZG)@-[e1X;96I(E!p?"ap0NtL8Fo=<HttO#i!8p4IAG_0?gT<e-"M;S.,drj5p)u;[d0=^(/
UoA>'LJV0#9QUT.6fCos.cdmWN)Q)*j+"Z#+Z)2='B]Ad6m07raHr"+7s0o9M<(fMZiBU8]AL:
[\]A,c-;a18Z>A>?Vb7p&IJY\(!\BP+b\=L9aOGqKYMjfA".;mB"pV)I]AO5\*Lh'/9#'4HBej
i"Ik1b:BH'^-6Z6"I3[`\/O>`;$bZmdm3E4:bj)@ol+qNhjo7"QNgZ*CC)IN$!u*HJ/2n/M8
\X0eGBk9lp7e9j$=Co@65mZN>)(VnEWVO;EER]A9UJ9VsD2T<s;C@TX%K-nJAj*AZ%4Mh=OH1
BA0"Im\$+"L7$CuB[HOY7D`;83%iF+JD;8,FMH%k;Uqc/bVDuN38*$*4[ZJZlJLUP[,RCG.$
#.V]A)W%OX&TAKbq14,RE`X`:Y9SpN,`blgM"[5EO&_lif.&E,KcMMU`ia)'3!D$2g#An)':p
_D)\Q\E0,@?^ueMOo@n?*"V"B>=S0h>)Y&;MZ+k%^*$C%6pkcB@cI;JjC?0*%2'l@k?X^$35
MG2<N8lk,ju8dN_$3+-8HM-bkkCG";*U15alL1+]A3&Tb.VmePKmD(+LQ9>Oc>S4neiF+,:Y)
:)nne[9VoSbpg/t;-Ye4e14IHnp"N7_j;eQh?f2uk4D5_2r<fcFlpGHfbq.1QsDG&=S$e8M8
/SVP*\$\F#1UffN:a=Cc2NGnn7jk?jn5`qK'WoV*DDe\t:91ih(3Ms6;>9PoPt``B49C7mA_
QWTK1DQ)hB)*9gpJAE7ld5EQ6Aaa9mD44@R8`_Xt\iJ+"-@\K!IjtOTX2SHad<&5hK;V-5n'
sHjA`X2!iL:r$oO-?kWJ1n.IZ.aXD,Bp[/A:nZ3a="F&lj^`Q%Pfs"+=]Au=s8>Yl!<6F!j\8
CQFYW)##'(-2BS.H.`8#:dNH,LI&XQP#gR1Z-_<Q#W9]AenF"_^/a3DE9%gX53f2n3GWU?4%t
WZoO:&m<ro//i,"3Z%T*49kZ.11A[nS`00hFt&am?E+j?>r++LRD%Z5W#XL[/]AP_Sg`$^$u:
/VA?qSK"=T`ZVa`C>nXtNL2;H+g1VUPsZDZ;S9*"d3Y^%=uNUjlbu;'oT&c]A6M@gg+p$r<18
PWg"=)d^SIEA!ZV@%&p07ejgCOnma^j9pATCtQ<Z0\bj+:&aqh%@!W.68@Zt_2_<kFS;7j$;
)7[CdV6i1J_D;T]A-q&Il;)`'[JA<`cS%KB(79-A/R'd@2J_5^!):QX/P59OkG4Ut;CR/2ZR9
T]A13F(cVj##%b^XL-g<Q8\_-HPJ]A$;_R?T_;(#<`:NR7a(7J/Dpp>T=mi+Z,g!U&[F(t;!Ot
>I\Eq-s,oKVD4%]A&P:(ZX[E]AEqL.uZ-/0LOl&KIrS[lDonOR-b>lXKOf(_YiE^=uQsYfQjXG
o-O8:Hk5j^8_;Bh`Gq[=43\@eUkRYR=MDK2CKO@^W2lD9e'b8r&m>7F%'BC$Jaq?iMI^D^qd
>]An)MJOsLSsp11.[&+@.I5^)m6SubeAek6a08:@QhPE4]A4"`]AJ;TLW*>EMAZn,CMt_n1k)l:
87AN^E/TS!s<E4^\\#V4#:9\Zc5]Acc/dF82n/gFK=[(Op!BtgHZ3,ki?A6;W^f(YhT\G"]AZd
B/?*:'f4ArWPrg7mro?6PI6MBO%nFmXS?`I^54pCh[2G-t#G-U`X]A!rp1le!9s3d^Ag4`c?+
uIGR<n8hD,T/[L"X@[is2W+BdK".<B/*US3fMNUDB>[>C/ZBkCQSHIL,LCK\i\F+19pY!YCT
JYX\FO/6T4qH;aXNQ.35_pe?iD?s.tG;[e&$iL%$`^6sOm%))0kKs,-eH=m:"D3L;"a`*GC]A
j;L'XF_)QEc!6*Q^4;'@hr<eqh.RC(ee?GB#s\8D7Z0I8q&MOpb9<,fP"h14J.>l1&-ZCbpq
"9i'6X>cEK0('qn</h7(&1i6lRL8"p9e`Heo'\=1e%6eUN(aHb"IN'aFMPMoWd35C2DN-7;h
7!M]ADKQ8P7@/[Ckg-C>JS^:o^4RcLA-uTPP4)$2;OqK+nml]A=5:gPiZe"g3Ck05,!.?pD\'L
1C8&S0nW@'fM&LNa1#Oa7s0`70Vr\nJgSP1IPPC%`aJ^G6)V#A-h!A,N@P(;sQ3X5,(E'Z\1
d*rYtkE49;l)6X5(omTfUtb;P*'-'[?(Khc(D>85>51OqHFbCEbEJJLV`-k'XukDS%paomWZ
-Q=m8tKKTkZ4*\3SqK+-oeMjo#&@%-.E<nqfSK9e)Z%;K.?a['D3bg0iuIor/%abU8i8co:S
bRd@p."'d2f!38\c%HmFka*I=USKq3:M-".BmI#NpC6ET@j7ctTEp<n)GOHLLi).Pa$Yeo;J
,!Ip,hpq>L?<W&XR_`S:21D\J<_qY!P89bM+*0+%@c^29>?=f?h#+Vj;tt1RQWXFAaTsGDNh
[GE,W,'S$7F^qNSDj`/t)*:2c:>N5=Ijllen=-$%BG'l&=r<DI;*-<^)?'uVd%7#4Mi:rH_d
Jp01O-?EjPr7Eiq`hnE(QAmAX2iL@sW(q%r(Ec[\,ag8up7^o+q7>g#HR`2qVgE2d[QcO*Wo
B&`#Fn`>nGk3g_PU_tK.nO"_VW'6C7-YAcn4QLZ6hi*h*j/7$!4<MaO/:.RGO1g"2B&4pYj/
!Q`B.e?P`j+Bc3NFSCSpE[i\pn^i0F`J>;_@d[9_'O@A?Dl2`HJE`F?X*`B4ieMG1Sk)t[Sj
udR[RY6CUJ)Ar6DX;`b;#M6,#AAjOH!W0lfT._4'i'(dOPC*Xo91S'LS_!;R^'(%_Y_4uiO9
eR8!pGK@U"##=[VTfnj"GoKg(u?0AUMlo)P#nb$(&S6_e\rhg.lbJ/!(g;,13AF)@#E!Y,r=
]A`cK^CjZ2hXnm7gg`(G-\^?d4/')bJ3:]A4;UpCcWBW<1kb#cZJh$ZNR_QG7%06ja5b#X@C)R
LT`->-5qNttL;M^&t)DZKkncZ1&kPg^e)14LImo:cr&RY06KJE<&nmBE-Mb@SSN1)iIHdWct
\GJHXVI5BSgVYtnOl_=8#Z5SEHY"OTic$(Y$9'N"7O8()jBY9')r8=u0LTW2_%b8Cri>Tb^P
J_[Z>ju;$:*(<#g&6o:S9(rqK^n8SDuZE;,Lc#dC%F9I:ZV+1B`,a;N`D(TKg1oQL+28.kh5
Y:8H#Ii:=UUlS9E(Q%c[aFcp8[e&3eriFph.Ln;`a8)ZR<kTK@1$m;khcq[b[^*t##$C;WeG
p<,1D77V>3&i<Ti@EaRl^g2smiqrfadQ::Q^W^C"D+dDUXY1Y=>g7#UfU[+14mq"TCftK2(T
LiSXRAZn2XG=BS4hnHTh^(Am@@[Z<[=ecW;IPK<:-<m#`o\Pe1+;,Mhl%-$B_hPP?B?IHZLq
OU?!'[+@)IiJ]AUC^#/^6Z!$I2O=<<50*&t:ec`hCt(!(bjk(gB,4ZZ"RGG9Xj!sER5bFC/9A
.`H`:B+d%,0BB`M)^`4O4M$u$Kns'WcZtYl4Y,'5Cj.F*6/h;W$Kd$7Kdcob+-P7=4CBK5tg
^U3h82\o5=A)qQCkb.5cJo5aaa&Z&te?KA[4D4GK7-;d-p&!qPs\H&%rO1S__W,*^1?UM!s@
cQPF&kttfh2(JJJ(#up5N&LlcSWfSa$d!(2]A+(FWh#$&ZBVdR1`Te8YSLdi&bd(jlfA>r69)
tVAM+kMB-qb3V01^MG`hTrNg#PBtF5Tl&(hoE?b2>b?HRU8fWf.XORFPAfALe8Z^Ld:(*u(O
@GJcSuaQ1(YSi,5O.4Ek:)T,EBd+E>7In.g.ekW^;aq3W9.L41^@$E$-C]AG-Nr]AqnqDNG2T<
=N)C`g98Xk@<G;\&q!$*aI#8Ir<_[%U&^sfc9mSiI_8c0(kkR1h`L0#Or5t<X=M\mLm]A-/Al
[SbWP>V_HoFHQ_[,fQXl?G$,A=3RDP6OoLF+WMJ]A&J\!it]A45_O)BdfZgPgn")Od3X4il9UW
WE0@cL=MT-mWUL+AQe#)G=^+dS[]Ae]AiDq]A^7VUWahC:V)9Yr]AhBrpO4=D[`[c[4F4TPO+/fq
%fISW4cpr?+qL(arVdH%u'0\rsR:<kglkN7gT"$)dK%%(A_"]AWC`d]ATj0_=Ra0sLZmGNqr!]A
RkOqjEh-pioP51KLA&nX_)]AnQqPH7cW;MZGXYns#@g+sd,94%N`F>JFtfF4]AV3XYC-9.6i5H
;FfIfinWdp^0a^$.=i9`7cmWX\K;.q)mM68U0dIDJ:gujBUG(B4el?FItt16ktYAs4V1>,F=
b)jEB]AH-hbXFWne\_o`p./dei-?JQ[EbXU:jPj3d>o;>nabrnVVb?d-48+H5/2B!5<%^>'uj
":I?s$f))<0AA^.ND>_SLOmkP7XYpP(JdiQI%S\6_hXn:!m?\(Z_E`;cTsAUSTs@53o;>Vgc
HKXGW"*"gR9Oqm*V'sI<Wh#Sc9JnJLr-e;bk:p=mrkP0_FDd/T.K3ga"Y?1eQGF&5=d?9%pi
\&RU8U-[&>f.p.ouDo3NURDQQF"Yqp)CI$oach<frRO=WfkC6X_kYZ`">MS0R)?m!W2Om(ZP
4$@t0+2'+]AaXe)oJ@9d)l*eX(KXmkNO?gQnMW1*FS5=JDK!?L>ANC'(Gff4=P!&tYT(X.*uI
7s*>jkpaV+i-h2`,.)+EbA&)MT^dhdMB&UMSQ`YR%c6Sts\YrbG@.VRUP7Ot\"R6;=?F1Qgr
?0@%#^MfN-`=;h=I?HHqIG_P@n1+7!R#u\`8U;*,_+a&u[sK7Og!]A<kr+^C,,&2:Un:(9N1c
]AC>3B2sU7o7>#)=B6S\.tU7:*_LDa.K'4L.i+RWq;-:e)ghU_<9Y:$QiLM[kEG2G(*s-T6l]A
t-%C<ac@jN+I3Ak<)1AMVQGBK4+,]AHggIn1lj*@2WV+\7NDRC*;^Ga[]AN@Y?\]A",G9OP3(E:
n1PRI?.pj:rEhO5[RkHHo`VadO9G^?)=]A$=Nk\'*pY(We@Q-]AikUSgNbW/Q<bt#_jIlNFiX5
Cb4!X!SFW&^Mm&f1&SX9!,X*'>lFjVUaUJ\8I_C@1#;)Oa4lTOXc7.IIig"QSlrLDfpP(*$=
#PO]Au<gGI^Ph@o/STDVKKMSDBOpbpQ%`WZE]Ac<SHp!'2g'B)nXMWrQqq)qj]A\UN122[ckh3Y
@E3[n*Z@'f+.blBJD/VJ-`tj4q>6>2::Wo_ces=cq7*6ljjjTXe'SEO9MC]A;15t)hi!hjA>l
n$_NL(ZlsT>@#7*t=<;i*WoVT%W,if44WF<@F6gn%J"<oNr,oON=c?IE?>^&F,?F=rJ^^GKW
d[CN/2hr&R:>g6"k$.>D3dWEMY2VcGY6N[s&.(t8g]A@::S.b&/AlJgH!\AhrsbkKm;Oa4S^g
s^b5POch\DdLL]A7(r;2%?(eZCQCl:-a7?]AF5]ACVgHX]A;b#e`#+]A*!QbuNRBA3:pNHer0VZa2
Kqea3Qj;#u[Wq8E.Ja[e_e6UOf*aXBg9;<8`seV7o8uc(+pXVhk&#Bl.`eVu\>S<i!A=tbf_
pN9K[X"%)FCGSrW9B.+h'Ff6l0e8T)"'2HIX1D<Q8s!pq=4?Q\J7Q#?B1PlZ1c6pFQ#JS,8P
`nYg":ePFh%QNW3YZ0^%es.2o\rH8%^L+W@GcbY"We#WeH3aM:OkY#EADWLh==#I]A`0TL(af
BiZi[u8$98]A>u.dE>uQK%&2das(K_Ui<(inEJA2GQ68jhCj`GeHrO0^!J"l`hl%mPD?L-#VF
@:S/E)&Jd]AUXAa#3$1L4Pek(lS#TBQ`[s!'I=-<]A:21i`)D;:Xg?;%Q>=rZh<)"XYP:')K)a
!79e$RkWs4;u)A&$>QXi'XdP[QaB:hU:V<:G7ReO9L39)"j#'%5Kj&g3Hnt3!?$bOq<]A(bn[
%'pN6o>i:Y-DgA-Wa?s.PT>=NU#.U?lfq:@ao`,Ng?%Ih=uNXYc&Yrls&6C3qQ/m1XStFut2
S]Aeo+Op$YSPKZ\K:T0;bsHdMMmjNYHBWd+_/,6!YHpf*;fp1Rf'C&0%Ed"C5%8;V/2,EACQ0
Z*fQ#"IZflI?r;rpN3oZ;`@Q<Yi0B:u]AeG+Q8T7CP5g`da&PbOPf3='uYSn6b(In0U?V?KIB
^4NRV=^U@eJ`=S]A.]Ar,r"#J\q?eUX"T^S,`(8:=?c]AhpW3s^>HLl=or>2qaka',Y?pQs(a#G
:!t?-rB;>-h:X,an,I*30.r>ICYcIe*4bIG6f:*E_uDG,r\qXmYJL0ECWosl,/5dI%NHV)h2
`@VDI"Lh6OfFUL*1`R!p=5:LA?Xb?;S]A>9'1l>dBIpVWlj?3/?hZ0p@%#XX<ZGp24]A;Rb.9l
]AmB]AkgWM4>?5.u`UO4(O&7;;PUE@6=p'8[Z?fMI*jIRogXb7qQGXZM'&UQJsCW?=_sb7)s$*
gNT+)'T"PG"MI0JL\d"a<L`,Z@?_"6VIK3l.:`MLAZR09a=(X/6LS<IjL=_]A&6@mmgi3m#_]A
lA4QUI5-@)O^YhI#B<4:Kp)sdFZJ$QjR<I8@\GX&l;;SP&G;u3nmb&*-\_N&ZD$+deDU_)t%
W4a(u_U7(f:/\"qV`'p6`T(k($kT]A(,ahe'Xr?h:lK@%`dDK]Af)eG'(qJ/0eq7ZW>C=qM-;E
]AKu*UF=^75GFi):$Uc"(/8!Cst_7>Bc=L5uj53m'EUK:3>)e/s/>\I7aG97eY1?R^2n:-hZJ
_fua&+VM=7(TJ'fai1%1)OA^PEBs$*:UqNV@Vjj=X'B":5>A`pU)NS%Y3%Y)<mi@0X?Lqn(<
+\VD[5S2QS)#7dGJZh3aBjdM(>?_MnA]AkR3GQ)P%4dWYV&T:[Po)0q0W'#^ah<LOWY_M/=tI
0`b`\BhD83'Uk]AnE[qq&WRE2Rj'G8U;q'Yae\`h&59kn+SPHi-'4F#2DhIMV_K$rd.3L??P-
f!"-3Vq=LTmLLV/V_5;)\G$3TB7K]A#nSFhuM4sgshQN%-I=[2u\DVM,L8A6l\X6X0Ehfjs"l
!@3pAQeD?&>9-\BVsd)B),[iMj9?-;('2VEibi^r5`Vpc'p88R3H+rTbKf_smoOZa4=85CZ7
J*'Pf!)j\Y?8QJ2*OJJ?&g3$`O'6t?4^+nZsXc:UZG"R\M;TDsb,<^FFNAr0?L+!.'eeK(;R
TKRFmXM.-b8R,k\P;1GGh:u?GP/H"dR)U&\ej.i;Rkr[9jcjH!EGQa,*U%NMG9=RcXK=>X:b
.GHeojB0O$Ce\2Tnqp[5C3VPlZNKFI0MKRG7^H]A@94=kh58ol%FsA?L@K[^`f`S(?GT9;tgR
VfYLW:8mRL`Prk&1_)Bt3t?%*+e27.Ldlg=aY%f842UN7Z5.G9@%jnMo%,2FQU+5m4MSYFYE
QaV2jXn)q"jVY:WT3<lE[9no?"n@m]AEb5hQ2iSI;1p#hI^e0KBl?-f#!5[@:NJ-3o<`ioDP7
:3ZTYH:!8V&@XbXu3@;4j[Y4jDPdt@06nmAs>E;,0:42b;OqN7@^N?qCnMWrRN+]A`JYf+FYa
<n9UolaEA,-?fMO^m2UN+/fXlO'^p2+%T#m=a7$DMJ:<9EKAgZ@n5<Nl0DgG9f,=Qu;B7)*8
sbg!cpG?^))`YDIJeW(`F4>(*`5C-D-2f6H<faAA#g4&c4qJojMKL3qPR!6j'F&M]A,g6W,o(
eePgIs$pW&7/%)q0+BkL\HV83I2HmDGSFSIW<;QCr1u5>T'WW1XG#^6ctt0"GmiV`LVnc;W;
$aSlM7#_*o7'C'=6$$/R>@Fl?g5f69%2=/+87:FN#gSWCKk4P:$/'UK$ct`NrsCmYGEAM.%-
&aH$r_>-to-Vdo`?!&q+77E0.,'*It&H<IFe@t!]AieU;CRb:+29:fOl(!0G_,Ln24G0".?9o
VHVH53n8Y3dcdbBiqb7.)*<kG=bYlD#55/?Lc;pYu1<,.=!j="e"+$ra&tuDda$&ASic@MW&
ZI1VulBhg#Lo.2lD_jC7H%e:FIRL;\$@hl@NVq*'4V!R#$8]AQHf,'G4cOp:3m3"]A]AU/m0=Le
!Mc+fNou4cn0UIjY?T/-fl$3,R3JTXj`/0:?D1&qB=!)b%Cf7H<T,Uq.+gZ$$.B)!WP@9-!C
0JSNJ"DI.Zn,F%#X,4\YL@F^;U!=`74gB&XuH+4LL"h,6%^D[Slh/P@_[0!@d6o$YLf"QU[g
%$oql/NZNS]AlmEtX^XuZZ]A7:97jC^JYar&Q?j?#tO&Iq^Sg<C]AFgn,4?BOZnpX$>%CEc<i4E
![agp6^ZZ9.1'/37Bc+IK;HH+uY;q_AQ7Y)%fP[;Um&t@n!_6fqG)H5_3smefBL.Nq7m']A4T
tk=l1$X$^,,+Y_(gjJHXK%l)6[#L)2asoI231aQE]A(96TY/T?F[U2%%d9"JA"<2m\d&-4ImP
-4s@CQ<0W/HOFR?k5e(YT.[B/L?Q!i665Nf5a!CO1cD';3B[sp+?hq=T`M<PCF46-mJNXHn*
:tT0^O"K9MiIpQ:Cq%R5T-pDUj&n6Z[a^mFlGPZ>CEH(n\)qacOoIq.)Y8?1E^RNnu3\$[Q`
?B?ufH&[\ti_U,_S#aJBRE%3#EjH!UV.6oQdSo-!=.+WJ5`C80j;63B>/HbsVQGRHlOhZWWN
jX*>/fVijeQkL\7`SFOF"0VRF3cY<_-6j$T4%6?/;g/#f_a%`C7!DEjo/RfM_=$/i>]AfYbDD
*hiXuguc;V*:&DZSnN/i4mOGo>"?@3#B2\>>Fapa\\QL6pg`n(?9\*G0Cf*%nF%Ss2%XAoXC
lPdNp5N<QB?]A%h=RkcgjGa?dY<gVgNZ&qkW6X6DgffP+!Yb_iV>1'a]A-DHH"T8=GXf@@#i\`
JVQqVi0Q0rq=YMWO`h%5P<<R3'fd:ne.XL'\^2eNL]ACMPY#=,$B':8^&Ck[%7cWZ&c'tFGUL
Rgnk5pN34$?dL^g?(f9oNVE5"CL)DC<c1B_'(.3VLda!!+!#VdfVM,gkPHVf0omM/e7'N-jE
0[WOY*HpLqR14/.8=h@c`Fk=X3m!Y,HGG-$YG[#d^8aPBpf*8HhR(Oq:/278hM40^0k>>8E\
E:X=6Di6%k-7)n=Uu<bMO@_;gSK]ARna+KBe,Yb?p<e.$gT1UC?F#7"AXn,N[%<d^6L4M3SUM
W/'4pH?cLQSB4js"i"UVc(>_-M$3U-Yj+A>'45uh`<ReK_Jpb=d<@<,!0Q.o1"HmY_4Ugn&Z
%V(:gI`9(q($BCo.eO]A/GkTD^_rYIP/$%>U1G9BMOOG89piq&f+CjWLado]Aa,QrP1*f/cbuH
N9jiI['^.r4D^`(f0g=jAPXP%\QEH<21QKdr[B[:%%,W!V[NNhIY9<-DfciV+*\-n.&/Eh!+
-roOYt\8k/_]A(%_bgakk>bsg7aK,_)mf&>"#I^TQrZMPG7d<G"EsZ(pscB9Qu0dfA\=_X3:;
;Xdfp:CFB<?%dpNh/-OM+>6_5h[WEL)@`/pk0"25SN>S="%lt"8MhTb-@li]AI\dHst>#A^j4
G-0jmHc"E*HJP>'p]A<$$,_)]A0E0I!'aTFm.`8Gk%M*;+cF7d4ui*]A20.Pe8c,diaTm9O`(MU
8lq2FY9MNW9XJn;R$9V[!7$!F//M?J;_#1Ja@9GT)"c:d*,i"TJ(M)-IoB&!'=[4>E##8K_i
b<hGBV!djCCbt<[^kKms82E%&RAsDIiNth$/5:<Q(f)IX!`Z_PB:sa)/\j84hO;^WX-H]Al.T
ZQ4.H1\CoMXuK[&3c/e5ZL$FG4O.[">7]A2H>$&oRrrM&qr869miREC:;BpZ6#XQfr_En4hbh
ZU5-l#Pr5S\"cdjA&r"Zn'G3]A$h.`h&a*+Go[\q9k@:<Ut5L&gs`4$ob>M6SYi7.t+%7d\Y(
7EP3jZU`REHRCeu.+WB7$;ODEK5pb:p.3Ym2BCi_I7N?+/mmiU2;KBXHtUV<-1K5gOU-h5)R
-o+p1b6@@2>!O-V_eZ4c_WIbD7Bp0l!(3n3*:tE@LH+Xb0HuFKk]AjJW&*,#G-PRq,qmN=6h&
<9)1[?d3K$'m`a@NX&tf1l&5rd[ilAN>!#agO)qYo`Y'5dBnOjZmZ8_d2ob.j9M:`u!rm;;.
_l=</06ViNTcT2fs/7\:-j<VK#0k*CKHY4@51gR]A1lD$O2S(Z]A#8Uhi`%2H0[2fTUc"hk9[W
+\p!@&&a#IE`grWt:+#"1!Cng:BA8&,EZts[=ZkgI/-E$p4cf%&ELQVq4b?to0V&W+us+M2q
X+H'sSYWglLW2h"P)C3(`:hc]A<S.ltbXLS9$!\nE_]A7C^QbeuZZ=qu`_0+fl+;X:V-;V1]A`]A
6-fm5R;Th@fVT$`b1/OL*`E.*XNln\eRM"*U7E/RYIFM=D[DP(X>Xq007M@B-ae,l:J#.\.U
t1C&fPct.(>$lt1kF[-i2'rmm_VuJJK!huZT;X%0PAA*rNfFM7Z3dc[11&45le9]A!AU3mAig
-CVp25Po_aHKEB=<`B0='L]A2@ijg;7Z(,8XWIE6DKg$cPm5<=J^?TOHdd!JHir,rIhB3n<,O
+LkL5WNMKb.T%JkFMm(#nsdN$0`?>B)mp#?o)"^D(nc#Nc+!u]A!0V`)Y^[o-7"]AKsK::XAaW
`FS;AJBcn-3^^1k*Y\=)+g%(BIe=Bk>4OEQkoFaIW`B>'*U$]A(O@qcUqg'LK)?F\\YRWk;VY
TNro"&6)au5js&X"B\KV_G]AC?+*l<?;Oi.GF9>Qpg^FT/<YTX'l^;+5HaTd2N.@7ht*V3SB-
-FsCGkT0&5=`=5e#H)qE+H#H)lgH5<LdS9*bs1"ga-^mqJCPFZ"<8Y=L@)mQki8OVsetu'1Q
V-=P[@dY*VQECo:QV=0QD@7)%4)\KAGK8d,AFO+L*ASXpEEaPPDNDc?#gdVT&Ks$DF&i6_On
ka]AA4<ElemKWUJV1fYG=--V.@%=95>'3#oOpp0Sn@KO5>Sp^X?O_Jc+NI:oN_>!=0DLI$=2)
=JGR@bo(NE3qNS+8'-KF7-RM"7&5QZ^:0_%f_G`g'O^EHNck=^*RnAuo$;4VYlVT)b-j\:n$
m8**Iu6WjG0=5GOfSL8.5;@s,(j'j>+O`>L1`-MUS!"dbFW*hK/\3#LY2f/=hsGE;qWD3Hs:
p<.H2:[/MFsaVcLb$d.7P6Xh8NO#C$X-\ZX`m%o$;Za]Apa*'\]AE8MD2\"\9#@g`^!!_>/Vl\
FYU1_53e$4i_`cQQ1=KL?-q">ID(Ql"@f/qWXEl:ic?^C"*r<*;J^6d\(PpL[M4e24sp=Cs5
3H;qEOa<LQD@!/N]A6ctWgXaBM,/+gjgk9$MYgs5KZg?%foO$OGc&Bc'TX"7X$[rcRr:Uj\&i
A.\G4g2e-GG(,s>.fh/BN(B"lVL8K=ISkY9V%Ta8i5XcpFIqnnOh!BE69?mD\,fqKH=i,Y2?
H8=VBP[q-uh5"qA(@D(Qa\rfepp9Q]ATJG@C!1GV#/sb"B^s/<'#q<"CF8h>Xu/+7"2F^4uQ$
P+Y$b*TH8JgpqQmP,^rqaoX^%gWJ7d[+>%o'*QWtH9G]A\c7B=!-7*,q"H3$ntIT2EVn:bA"Z
(b#_9E"f1nYJUAL"&rM6sJmr*RWICmdYf39[7)>?1**I[PjAi-?-s8UeL!dDe/84W#%F:NhJ
_ReiWDVMFrZ\fh9d2iuG)lM#/72s0C:$.$Ze\UAJCMm7&a*LR]AV1"]AqG\[FBE7:Y2ZfgA,KP
Z<C$H?E<"'s!3]Aea)g-*"!N3?DI+?HTp_=GZB!k=6*XdUSL?8e\,R^@_A!,9!O,NjNTR\%-7
B2,ouZ67mZ?*Q>"1K!)h\9,Goubj>G+^Wj_$0USRB[K^ZE(rfUGta7i7n+p=I$2-Y2+nPALi
pWgZ^)_H7^MIApZ)IW5tqR6("E\]A7ABSqc\9eE0EgMG&d?Hh6e0_;1YS?5(AjR8\2XV/Y@Vq
qO8iF`H3T'1da`<i0]A#,=ZpuLiET[PL7c<Vu:k\HEmBHX2T&8UU9Vm>d[.N^R#<2EApWAs)k
.T47S//(;<[$NH[+:)tbb]AJ@iN#XN[pi_JhDk<.8Q8,"8.KH=BN*]AGVC)ArapIlI0ZJiEp>6
i^0W\F)cZ+ff]AkG1nRcnijJVHV\/i"jdVhc<!p>,.CM@/cHk#0!1]Aj!aUk=qJq@iM+L??E1r
13t)#fe-=+r^Bj)Kh:1=mM*'4WS/f<:PJ%6'8Z:Yp/%0T[j\`j\'^j62O\YS4Pn*7EK_a8`^
ur-,Yjk=g4+O_FA)L^sHJ:@A33#nR%=(JH#R_E[Jq1,jQ3ZMNR#%'cb\d:)VnVW[VoWmb(>[
5Atiho1`j_2fRH^dm'3$degN_CZFf$u'u.7rT;!gdN`BfF:#l=3A9;H+PLMb*@RYEp?1TgQ?
W!*(g[7dnW>d.'Il%,/!*)h31P4N(,-6J4O1`TP`*sOSgBDfY('W_8.5Y3'5R.CPX1&R_'k@
E4[Q%Z"-QY9<Dmrp:qH+lJi1R#4]A@@L2U!;Rn1q#:4ku)gM:7>^&W8VH1HP@i-=-tMc_H-qc
qD8KBgOg[,c20]Ag6E1H,fDD$KHWS6jmsL2"D\t2JD:m#H.W]AEZnc^^Bo-']Amffa*CkhW?#V[
r<9oZV`S$MnqY\Q.HsV%Qn0EC.9,#6sMCt$;S/\Q`1K1>U*&<lNpj9mIqdnk4C:=cJn1Q99j
n&H*``MP.-Uot!8[f7D`)-N!2,/GR'Brbi!?@epC[F8T/ldJ>?5)pBRfqcg4UC)[W_*9]AUS*
NYP+96fZULHj*3Qam$;]A[pq@c!(PtdNeEqt+3Y7\'iS'/c!KH3!3GJCG.?,;]AAZSiSHr`Q9l
%!o/D8Enf_,?90'*i4,]Ag>Hba+_6K]A6cXXTIB"-_B^[`CM]A'_T;aTD*ZaoX_._SuD2G&QjOk
9[Jm,ElecVYMK)\_;&$2\)*pFRW]Ah/fafO'G"8E^skcjt8/ne4'%I`$0P/GCfQPB/,$O9?8L
K&l3\=rL3V*!OAmRCZ$ns>b"g:c?#$PQJ%85ZT,E]A[-o.)`uK:]A0:$q7o3omoqqHhM2$LH4f
f9=rX(JsU?GS,E8Te(,_?\*V*F2Cbk^)S5gNR`\D<%4iRt`"J5g+,-GF:l95]Ar^3rucLEAT6
q*UtiA"n(8ACaH-KGT:7mAFQacca;q9aOn/X;[7/;f082J7r<et=fLGeM*`4.Y$smXd/WrK%
k&o?Un'WOH*":O_J@l4\DBh%lUj5F&8*S<smAV:u&sp3q#Y12:IVq.E]A;eXr5'MC1$(R:f>K
\gGL6>/b\`Y*XINl1I/.B[!'JnAa0opLod[&Ou,BDZ7=l"S'gET0FZRptccVmt4ZUZGY41rJ
hI+mH@(#l;j\`WKslY#1.?SA&]A]A5Q0P7b"X^U$D-l*(UI#[;'l?2UtZZ#1;Xe`37kV$K(jC,
?lUei]A/D,aM!+I]A>ucHpdhG7fR(>7[P7j$)X5pp\_pqgp4`>8l@a!2]AXT#dM*hWC98_\,1F>
pZaS:\"s8HR@@+on5e`Yo!fLs;P+2)]A":7ej7);j%KV"Mt0fXF[L9M4+cV_k[I`\rO[NZX4J
[8bd.&r=I8Ttkt`#.'C@Z%'g=`i1gV;&%?H]A\t`;O_gVi:<(?M,S6/lSQH9\NlI``*$i+k7H
]AhWY*juJXFC0kNJ8P25T2(C>:^&/0k!ij@jSo6QL0=KG>9</U*(iNHIAg2n4jn2\_1q>+k>%
1CU]A)d=ZMqu&S1I9(brk`4,c^iGfcj2998n,)_=Ld1i>.j+QH+1D%q+)pi@"n%Mp@-E+^jbF
j!u]ABX><L>*QRqD,?bP.r*GSCC6sTM]A'Seq"**P5e9*oaj3V2/4t_h7.s5.s6br=k:,T\cU#
6eRT*mIA4gguQeNQ6)Chfj2MC3R/HW8a>OUWFEm9(/>K8>YMla?A=!HSl\1(9p0/;_Of]Ah@F
jqWHR)0XDg`<47abej>"J.Qcpan-;?mX*<e<5^XibL,^&6c6s"j3.Dgr(@Qleu2*Q9[ujB+_
!QT.9o3kVunaYA1I)dCo#4Y%VL#TV+Ji^EAWP'R5<2dd]A[/-XgpE15/QcqAsn"P`)Z#hOSO@
lIJ#EN<=sN!DeQ[HB0"n)?=_rB9R32<V-hC2%aW:dF]AH`pn>qHf4Z>(t9-FRKDBdD9"9bhRC
[XdU]A1&3FAM4hB0)2]A1bYB*SH7b+U+fK-$o"#n1ZWr@VMe[,<>a)"X03=JMQ)8<-c$?'F2;s
m[+&_e3$aQ7]A$aL+g/O6&^Va'Jk/=L0N54M._=3&aPo(,Z4N$B0h"o5/fDa3-%d)N1-fnUWK
6c@U[p)_/)XFk=;Z<D<O[c^%8h5UElbAQ7jJ-Y)8;*0k+ZZ(pq::M3W(?85sAl_E?R*51Eml
MO3Z9RFbeEC4\pO20V0B18'jSeAtLmI_r<^cT'H83@nFF/O-pY`glM=$&Y\<Fl!r[!.^1.WY
Ao_GjhAUpZ$gQs<4>,WBj_^#fFXroP5/JK#c@3#sSDBh?W&drE$-l#6sSQ8l[hDUFl+O2J9]A
OKIg)&=#r8fSJ2Agal5UHblE?DqYR!)X"HjZI/f4"M-T-j/r>%.RUCFuQO*<WjKi`mB/('tT
NrAFI3=<['55IsbH)!XjgqPB_N_H/1?2=E`gYnaCh^bZakpp!gb;J)Q5(XkKEu(=JKR=KiGV
Z>np&H&.$u6O8TnFk]A,ls0^h=mDS/3QdCBlCYZa]A;-;Z>Up,C#[S@9p&a!saQ8]A1q\#=QcN,
X!\o_+l/8hkBn%*YI6+D1#S3M1K/D9PEY7$n6ZWs9k'*&]A[cgkLJ&5MgDB!3q'<lJ8a+oG"p
6WbJ:BiYj2pO0f3q]Au5L^U82lG,o0m>N9@<K^OYGjQ;*uX2=cC0[GAr2$'8T/6V`I+MYB4Rm
7Q!\M8!W`d#()=GYPi=_D^CM1[eX,PdV.%r#"G.4aGMjA1RMhLrEGZcbH5lgoH`?Vf5lc7gC
dF0Y!lDp>)*%?togcD=hZNgUQ*F%iI]AeCg>K3QZ^k4Q39&H)3XB4Zh8I!<"u-f(TEDk29@o8
ekr"'A7)?S$LCOAW#4jadUth@j[nI<E:_!LQm-"pF-L,JFf&.j**[dqam&+f*d:j>Sionh"c
pBRI'MdU"?VptN-C]A)C$n_4BCDQ0-`,k,ThOBRI0I,G/GkubfFoZeGoY=L-'W'<0h'L_q%+M
<,]A?c_3#MetR@@CH8DW]A]Amf*=~
]]></IM>
<ElementCaseMobileAttrProvider horizontal="1" vertical="1" zoom="true" refresh="false" isUseHTML="false" isMobileCanvasSize="false" appearRefresh="false" allowFullScreen="false"/>
</InnerWidget>
<BoundsAttr x="0" y="0" width="479" height="502"/>
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
<C c="0" r="0" cs="7" rs="14">
<O t="CC">
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
<![CDATA[刷新]]></O>
<TextAttr>
<Attr alignText="0">
<FRFont name="微软雅黑" style="0" size="128" foreground="-13421773"/>
</Attr>
</TextAttr>
<TitleVisible value="true" position="0"/>
</Title>
<Attr4VanChart useHtml="false" floating="false" x="0.0" y="0.0" limitSize="false" maxHeight="15.0"/>
</Title4VanChart>
<Plot class="com.fr.plugin.chart.column.VanChartColumnPlot">
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
<Attr isNullValueBreak="true" autoRefreshPerSecond="6" seriesDragEnable="false" plotStyle="4" combinedSize="50.0"/>
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
<Attr enable="true" duration="4" followMouse="false" showMutiSeries="false" isCustom="false"/>
<TextAttr>
<Attr alignText="0"/>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="true"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipValueFormat">
<AttrTooltipValueFormat>
<Attr enable="true"/>
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
<Attr shadow="true"/>
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
<Attr lineStyle="1" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-1"/>
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
<FRFont name="verdana" style="0" size="88" foreground="-10066330"/>
</Attr>
</TextAttr>
<AxisLabelCount value="=1"/>
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
<FRFont name="verdana" style="0" size="88" foreground="-10066330"/>
</Attr>
</TextAttr>
<TitleVisible value="true" position="0"/>
</Title>
<newAxisAttr isShowAxisLabel="true"/>
<AxisLineStyle AxisStyle="0" MainGridStyle="1"/>
<newLineColor mainGridColor="-3881788" lineColor="-5197648"/>
<AxisPosition value="2"/>
<TickLine201106 type="2" secType="0"/>
<ArrowShow arrowShow="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="verdana" style="0" size="88" foreground="-10066330"/>
</Attr>
</TextAttr>
<AxisLabelCount value="=1"/>
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
</YAxisList>
<stackAndAxisCondition>
<ConditionCollection>
<DefaultAttr class="com.fr.chart.chartglyph.ConditionAttr">
<ConditionAttr name=""/>
</DefaultAttr>
</ConditionCollection>
</stackAndAxisCondition>
<VanChartColumnPlotAttr seriesOverlapPercent="20.0" categoryIntervalPercent="20.0" fixedWidth="false" columnWidth="0" filledWithImage="false" isBar="false"/>
</Plot>
<ChartDefinition>
<MoreNameCDDefinition>
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<TableData class="com.fr.data.impl.NameTableData">
<Name>
<![CDATA[ds1]]></Name>
</TableData>
<CategoryName value="销售员"/>
<ChartSummaryColumn name="销量" function="com.fr.data.util.function.NoneFunction" customName="销量"/>
</MoreNameCDDefinition>
</ChartDefinition>
</Chart>
<tools hidden="true" sort="true" export="true" fullScreen="true"/>
<VanChartZoom>
<zoomAttr zoomVisible="false" zoomGesture="true" zoomResize="true" zoomType="xy"/>
<from>
<![CDATA[]]></from>
<to>
<![CDATA[]]></to>
</VanChartZoom>
<refreshMoreLabel>
<attr moreLabel="false" autoTooltip="true"/>
<AttrTooltip>
<Attr enable="true" duration="4" followMouse="false" showMutiSeries="false" isCustom="false"/>
<TextAttr>
<Attr alignText="0"/>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="true"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipValueFormat">
<AttrTooltipValueFormat>
<Attr enable="true"/>
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
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="0" r="17" cs="7" rs="14">
<O t="CC">
<LayoutAttr selectedIndex="0"/>
<ChangeAttr enable="true" changeType="button" timeInterval="5" buttonColor="-8421505" carouselColor="-8421505" showArrow="true">
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
<![CDATA[不刷新]]></O>
<TextAttr>
<Attr alignText="0">
<FRFont name="微软雅黑" style="0" size="128" foreground="-13421773"/>
</Attr>
</TextAttr>
<TitleVisible value="true" position="0"/>
</Title>
<Attr4VanChart useHtml="false" floating="false" x="0.0" y="0.0" limitSize="false" maxHeight="15.0"/>
</Title4VanChart>
<Plot class="com.fr.plugin.chart.column.VanChartColumnPlot">
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
<Attr isNullValueBreak="true" autoRefreshPerSecond="6" seriesDragEnable="false" plotStyle="4" combinedSize="50.0"/>
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
<Attr enable="true" duration="4" followMouse="false" showMutiSeries="false" isCustom="false"/>
<TextAttr>
<Attr alignText="0"/>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="true"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipValueFormat">
<AttrTooltipValueFormat>
<Attr enable="true"/>
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
<Attr shadow="true"/>
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
<Attr lineStyle="1" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-1"/>
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
<FRFont name="verdana" style="0" size="88" foreground="-10066330"/>
</Attr>
</TextAttr>
<AxisLabelCount value="=1"/>
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
<FRFont name="verdana" style="0" size="88" foreground="-10066330"/>
</Attr>
</TextAttr>
<TitleVisible value="true" position="0"/>
</Title>
<newAxisAttr isShowAxisLabel="true"/>
<AxisLineStyle AxisStyle="0" MainGridStyle="1"/>
<newLineColor mainGridColor="-3881788" lineColor="-5197648"/>
<AxisPosition value="2"/>
<TickLine201106 type="2" secType="0"/>
<ArrowShow arrowShow="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="verdana" style="0" size="88" foreground="-10066330"/>
</Attr>
</TextAttr>
<AxisLabelCount value="=1"/>
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
</YAxisList>
<stackAndAxisCondition>
<ConditionCollection>
<DefaultAttr class="com.fr.chart.chartglyph.ConditionAttr">
<ConditionAttr name=""/>
</DefaultAttr>
</ConditionCollection>
</stackAndAxisCondition>
<VanChartColumnPlotAttr seriesOverlapPercent="20.0" categoryIntervalPercent="20.0" fixedWidth="false" columnWidth="0" filledWithImage="false" isBar="false"/>
</Plot>
<ChartDefinition>
<MoreNameCDDefinition>
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<TableData class="com.fr.data.impl.NameTableData">
<Name>
<![CDATA[ds1]]></Name>
</TableData>
<CategoryName value="销售员"/>
<ChartSummaryColumn name="销量" function="com.fr.data.util.function.NoneFunction" customName="销量"/>
</MoreNameCDDefinition>
</ChartDefinition>
</Chart>
<tools hidden="true" sort="true" export="true" fullScreen="true"/>
<VanChartZoom>
<zoomAttr zoomVisible="false" zoomGesture="true" zoomResize="true" zoomType="xy"/>
<from>
<![CDATA[]]></from>
<to>
<![CDATA[]]></to>
</VanChartZoom>
<refreshMoreLabel>
<attr moreLabel="false" autoTooltip="true"/>
<AttrTooltip>
<Attr enable="true" duration="4" followMouse="false" showMutiSeries="false" isCustom="false"/>
<TextAttr>
<Attr alignText="0"/>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="true"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipValueFormat">
<AttrTooltipValueFormat>
<Attr enable="true"/>
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
<Chart name="图表2" chartClass="com.fr.plugin.chart.vanchart.VanChart">
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
<![CDATA[刷新]]></O>
<TextAttr>
<Attr alignText="0">
<FRFont name="微软雅黑" style="0" size="128" foreground="-13421773"/>
</Attr>
</TextAttr>
<TitleVisible value="true" position="0"/>
</Title>
<Attr4VanChart useHtml="false" floating="false" x="0.0" y="0.0" limitSize="false" maxHeight="15.0"/>
</Title4VanChart>
<Plot class="com.fr.plugin.chart.column.VanChartColumnPlot">
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
<Attr isNullValueBreak="true" autoRefreshPerSecond="6" seriesDragEnable="false" plotStyle="4" combinedSize="50.0"/>
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
<Attr enable="true" duration="4" followMouse="false" showMutiSeries="false" isCustom="false"/>
<TextAttr>
<Attr alignText="0"/>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="true"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipValueFormat">
<AttrTooltipValueFormat>
<Attr enable="true"/>
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
<Attr shadow="true"/>
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
<Attr lineStyle="1" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-1"/>
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
<VanChartRectanglePlotAttr vanChartPlotType="normal" isDefaultIntervalBackground="true"/>
<XAxisList>
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
<Attr alignText="0">
<FRFont name="verdana" style="0" size="88" foreground="-10066330"/>
</Attr>
</TextAttr>
<TitleVisible value="true" position="0"/>
</Title>
<newAxisAttr isShowAxisLabel="true"/>
<AxisLineStyle AxisStyle="0" MainGridStyle="1"/>
<newLineColor mainGridColor="-3881788" lineColor="-5197648"/>
<AxisPosition value="3"/>
<TickLine201106 type="2" secType="0"/>
<ArrowShow arrowShow="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="verdana" style="0" size="88" foreground="-10066330"/>
</Attr>
</TextAttr>
<AxisLabelCount value="=1"/>
<AxisRange/>
<AxisUnit201106 isCustomMainUnit="false" isCustomSecUnit="false" mainUnit="=0" secUnit="=0"/>
<ZoomAxisAttr isZoom="false"/>
<axisReversed axisReversed="false"/>
<VanChartAxisAttr mainTickLine="0" secTickLine="0" axisName="X軸" titleUseHtml="false" autoLabelGap="true" limitSize="false" maxHeight="15.0" commonValueFormat="true" isRotation="false"/>
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
</XAxisList>
<YAxisList>
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
<Attr rotation="-90" alignText="0">
<FRFont name="verdana" style="0" size="88" foreground="-10066330"/>
</Attr>
</TextAttr>
<TitleVisible value="true" position="0"/>
</Title>
<newAxisAttr isShowAxisLabel="true"/>
<AxisLineStyle AxisStyle="1" MainGridStyle="1"/>
<newLineColor lineColor="-5197648"/>
<AxisPosition value="2"/>
<TickLine201106 type="2" secType="0"/>
<ArrowShow arrowShow="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="verdana" style="0" size="88" foreground="-10066330"/>
</Attr>
</TextAttr>
<AxisLabelCount value="=1"/>
<AxisRange/>
<AxisUnit201106 isCustomMainUnit="false" isCustomSecUnit="false" mainUnit="=0" secUnit="=0"/>
<ZoomAxisAttr isZoom="false"/>
<axisReversed axisReversed="false"/>
<VanChartAxisAttr mainTickLine="2" secTickLine="0" axisName="Y軸" titleUseHtml="false" autoLabelGap="true" limitSize="false" maxHeight="15.0" commonValueFormat="true" isRotation="false"/>
<HtmlLabel customText="function(){ return this; }" useHtml="false" isCustomWidth="false" isCustomHeight="false" width="50" height="50"/>
<alertList/>
<customBackgroundList/>
</VanChartAxis>
</YAxisList>
<stackAndAxisCondition>
<ConditionCollection>
<DefaultAttr class="com.fr.chart.chartglyph.ConditionAttr">
<ConditionAttr name=""/>
</DefaultAttr>
</ConditionCollection>
</stackAndAxisCondition>
<VanChartColumnPlotAttr seriesOverlapPercent="20.0" categoryIntervalPercent="20.0" fixedWidth="false" columnWidth="0" filledWithImage="false" isBar="true"/>
</Plot>
<ChartDefinition>
<MoreNameCDDefinition>
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<TableData class="com.fr.data.impl.NameTableData">
<Name>
<![CDATA[ds1]]></Name>
</TableData>
<CategoryName value="销售员"/>
<ChartSummaryColumn name="销量" function="com.fr.data.util.function.NoneFunction" customName="销量"/>
</MoreNameCDDefinition>
</ChartDefinition>
</Chart>
<tools hidden="true" sort="true" export="true" fullScreen="true"/>
<VanChartZoom>
<zoomAttr zoomVisible="false" zoomGesture="true" zoomResize="true" zoomType="xy"/>
<from>
<![CDATA[]]></from>
<to>
<![CDATA[]]></to>
</VanChartZoom>
<refreshMoreLabel>
<attr moreLabel="false" autoTooltip="true"/>
<AttrTooltip>
<Attr enable="true" duration="4" followMouse="false" showMutiSeries="false" isCustom="false"/>
<TextAttr>
<Attr alignText="0"/>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="true"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipValueFormat">
<AttrTooltipValueFormat>
<Attr enable="true"/>
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
<StyleList/>
<heightRestrict heightrestrict="false"/>
<heightPercent heightpercent="0.75"/>
<IM>
<![CDATA[h7S(s<87F;maUKC:Ei6$.jLjJ.(?2)TQ]A9&PtN_Ed=`e+3`O9#;V;aNB@n117rGk=MNF>taE
<Zm\;gAnN;9S=Wcr'PoDAH7htQU6rB5VmO7U`b^"7S4f6Y-%cf]A*2[<B>-3a+&#M([iKj'-g
$#YpGAD^!!<[p\6ZhnUnG_O'KWnQDJJME>psog+(I9DHN0.$rDa3g6#$2t\LTj/omG6_EI(]A
:A'E?fUsem),%C/)ofeb`E16eUAUd%!?JdrGC<^Qd;iU<7Lh]AK@6*%DtWu%Nr7a\C;?mhdbD
hkW`2P:[C;<jif`GB*aIU2-LE)3Ep*7^%;,rakP*HDSj"_Bop(p?\/7;Qe8[6oESY@XiHa'o
=OENEWm`.NmAI#H1Z$i&I,DJZ]AVO$fpA9$6\?<I1fDC:8L;3LlZp-`jVpfRF%/I,G+h[2))R
b(bh+'%=M3VBSilorodZ*]A5Zf6;j?L1mlC>;dfRD7$)n3!d76%YnOh8c'Q3F#S(cb:^q5a[d
>jOXS_hmnafL*\MQ6">-ZELV?9h@d$=1RqRPB!)/B8skr0q:AW[6uRNgIOtA^n8?dd0uFrO%
=H[jI&C`bch:RQ>>/3G49EUMcht\Rs5AR<\\tSLO23eZUK\J52\c6>jodL1o+EU>OYZd):=k
u6;n<^8,XFX%GuYls,rG4oShka=rfQ,4nD37%W'*NQ@6,pT7,[AB+'m;65qhiU>gPg^(`<fj
:lj#<FTOZaU3HKPr5";bHGa;.H#6*M.e08kg&%Dn^!sn5VMq8PC($p34d/oemm]AG+RJ8)=(U
Mp[Aa3sj8h\N4UGYR-FdHA\Dj8s.^IWZcBjs#5/[juK,6@7G&iH#$=fjuA>S/qXm\p>g\4IY
4V:VJ=]Aoe,_'!kmbaf.!@V2Ms]A(?p,<T&6mjHQ=^O9)L5_4$)?=9]A?3RdAH;5l+8mi1gE&94
2;XS*WLR5nkj/6K_0AD1/qt,d7`qcO+`2<,O[b.5e<&;qZ7GqORTmVDSTX^Nc:XZ3daeC<:B
O?ptg8#\<>=$]A6(ZfRB[d<%-u+eV#AqJTU27K(RZ=.D:>S9%5Y2U=YGB`'g9Z-fY%;rN=rqg
:PXgAZsU$>D',SYQXD29b&sCfmrY7F^&?HW*1iO+P#'"CI_mYQiWs,1'G!h961d'bKg*8^54
s'@A;YC\_rGD>^UKQjB_^D:pG6='@ar:E1g34aZMgO,I>Bq%00Rjj0@)rQMVsW[]A&U3POLMF
MBQu<ZZ\3UUeTq:DMW&g!D>M\Umnl.;P'M$8jL`?k;Y@$@Xp`K"Y5#JNNs7OJF\Y*6bY.DS(
:*l5k\'6*FEK-Hha2cg&MAP!LGWiT-G'`89"aWZ/miP%]AKj_O@Mef,hej7Tqre%?9]A^SYi68
0c]Ah>2\r`ScneM&4-h(51HC!h7>BLV+35JLfGL_^aRD%XFm>Z13Doli\2Judp7&e+-,p:q7u
L.U3Yr!j"cU#aa\F&2XrpP\>iPP[P:%d:Z<_#Itu.7>!CY3h;VE6Bd"X/=;IHe>)RrE'&>:l
Q,D^@<:]Ag&l_?9DWT)hHdq#Y-(mF@PR2(4uCf9Yft[&A;P8/j+DGBFJrrjHZD?L&?2WLXO/.
T5CVt/k<KR6qrnb+7)!?Q^!D'_-]Ab+X3r@-J9igcWJh+'D\-1N*Zi^AB^2Y#!b391sMJifMp
7Z]ARDIMU+"tOJo"D+HUUdtAKB#0_V.@,k21Z*G<8Kekm-hDb3"F5L;[cPooVeS"5;XM"^[!K
96Hk8d8gdh^!<N$+1\C9rBmuT(nRHSW;3(JRUqkNKsnAbDX#0ih#>h5_L=pZWKAFojn+g`Hk
pLF6>F1q--'NL=59QUJuFa5h5_L_Z@s(Z1kZTKU>O*N.!+,BT44)tPVC*`S%aj(</4%D\)(3
`';E:_&d[qE<.ipDPAR.G6B32;HULA3kq@fqYsatb`=?FdULnM7/d'*e2SE8A,AWF$[Xm<F.
f3S@(JIO+O3/d!_EE2'h$SBH;d5)]A/3g[WN%NRI*i]AW1<IQe#B"DhU5X<Md$OrPkG[T,Q[N1
"1/O)\(Ho_T^%qMigNmLSOkl_3m_qE;?`=hM%f`'"8X3=!l^/K*3Eq"dlZiR\>*tHulc=IP2
:"NT)]AYYjKU;ng4pra1T%`HCt:'1,#3D+3?5-%*"g(ATEN4*H`I@G/P0DZA<6?0U%p<4_8)o
A_tOmarp?:3DE:mL/4Kt\6`cepLBB'9C$#[[YqA/WRnBGX-P\2fR(8WffL/dqGaZ`_n!.6^3
0h91S^r3#/r=jD2eA+XS*/&Fa7TL`j=_)]AS6NI'?T_P:Di@J^bEe\C2IT48b<a36&d,^rr>^
0,htUAFgQC_M&04PfAin?V`>4[!sWo)9(&(KNE=kaFaUCZeV+;S)$6G%\>EPV3atdT-Kc<*!
e/k2kj>MebfUD_09:InID>N%`K%#.m;63r1h.a9VF6D6!.T6'TIT\8gA%nQii?@t/@,7:]A4f
NC*cNXNbKNnYjNAcZ!11+fVLQPj#=LjjJ)q-?+'V0P:uKaUJ)tla/aAa0+%5X!i+eScf2W9s
5+L-N3^U^9S$'I\WH\rjj?J7(QNl=n]A<'G/Cj*j(YamZ$BjpC[]As&;p&@A(9"_BQ#ist9Z=B
neoRtZ<lPe=@,&j7XABDO.r=Hh"M;=m!_JdLZ]A:AebL2gH5^5^GX]A/_$dXBeS31k_=]AUY@$Q
o>jTU!KK>Pd?Kj6/DR&R3G]AL9&$tm)(pIC;Q5!2U7Y?g<hH=.q(c!JVDerr7=F\^ER#*ZMEJ
e?C:gLugO).67W^42u)0\Li9["1"YNjaH5bJ33!$"7,>g_Kl,i21tKK[mbO^U-a5Yu$W&*uP
EA\_;nM\8=kmkO<S8.0Fpj1,66\Q+iAoFCO*OE?a-q&`g%%JT@bY#"*[?U`'Z7`h)Lf%EL%h
=CfD\i='G2$;$[M3f-S)SD@<p-p2tTaf'l4WJqK=I+Hqkje40\m>2uo<9oTb?!%[VC#D(aOW
>]Af%97XM*A:Ad&BZ637TDKS5#64gZZ"(sd,]A/mJ*Zj_Q[%Wb/(cR.gW9UZGh@5h*3jQN._A"
$!hrm#Mfq7@b>j(k?=MQrfLhRp2;Ll4ZHP`+bmW[7R6^<Xs#$aUau*V.IG>]A/E(38dAsr^/`
#78Am('Ko2U\8d^dl/tj;b0u_H&Q/C_4EQf5k8XRY7Vr>J\*cIA/QsG@nNEJh_H#\^S2D$r_
50#??A[QJg0WB%0i7=HZ!#=#SaKibFKkP9Bi%psk,r5K'tmgUMEfN2L6gA2,Q\baPGBb&l1<
1QroLgA.4jG=U6ZP94j?(;'RIe_Yg-?6pA$DX]A0ah*q:[oS6RuK-gBUla&JNS,O("OY[S[6e
I_Yc0Ts!rDiINSoc:'h]Am<2J(WuUaVj1:d9mj1iPeZ&L$uEYV_SrCl01HoZ&!<9D7H0O#]A`i
uR>:Co5:9u;]A9BED5/OBXpnOo+S*>s[I?ZujcgWVmpBf\9Dfp0RXoVD<:Y4+enYhIN_--LEQ
i?uU@TK"TI`kF9`V#%O]ALhH@j1IS-9H2nY:O*gbC;_gH4teBeQCeb/GH/$UO"WJs6L#d-D4k
etPW\7XJlfCP:Wtnn`BMU4k_88hkuW!LW5]A6"kZ*A:_ddQ=2YLRd4!9.>bm%*tY/*HZFq>[n
r@c^SIc>n\-Ig))k9g_ZR9FLuH4:U-87Rse;M0#M&0:l4j?B-;!Ul7LgO$?+/ZI,>71QRi<S
_CTW`8NZ=0`6$/4kFLKf%aOVg-06eVS09K"FX^,&P.J8m@u?0&:@gIK"4(#iZl;/uE3q`hf=
1=R0T?N/aMOW;je&OSji^!_Dh&X.Ji(:q,u-Y'/p7'i*J&09:2TK"^+o8F6[hM%0;djmi/=J
kCO+DCZ^ce5*&.f7,:r_\gd3;&8l9J/`(,#lCOFU<+in!/^@8,%Xu,a.B/"0FV8SS:)?:d*B
g/^d9bM\Db[Ba<6#G9oB6E!=(+[A(#l8l&SDGW]AYgq>8L=b#Yob.]A&EI=h'@[c*_<p.2kLuh
7$\;_9d2i`oY/bG>f7jZjXRu\3t&l#1`i%$l1A*h4!:0l";!Mp'Kq.OVUjd!YhZTM3?%Z15a
`'oA0)ORM!@BpW@q*hLNQTs=rD5p>K!R%:/)7mO>Q"ni<N&^FjP^ZJh]A.N3.`"Y5s$eYes9^
WP@&q*DJ]AUd+#9FYAAaR>UB%SqA[h^L'.p_@+"pd'#7B0QUs"+C"kEUcqOoOD2+Jqf<Q/0OV
IF=i?V#8'UYqS^3!+tn0!e^"P$=V@Y3Pn_\[7n&U9qch`\2[j$7Qo3q&\qG]A7a+8d<%dKjOL
_M!@,;$#"j;mJ,oJhr7/'R0;)XK=JDbYe%hNY#&R(Z%:Z3VlT+]Aao$0ErUg>A`-[gsCo+$:)
.VK68]A*DeV4'=`k?L<iRo3qT#QCKcNf@2H)/m+*1oB\V1/+$3`3MkK&eYEM`?bTb=U=3EOWD
fGN.=!HXZ<]AW]A's)Ol(`;(aK^EU@+4+Z?Hi?102Y&K3daM/V-]A$RGSRH;L,0`:.5RTTM(@$a
JEm]A.3Bs<[>p,7GI5n%=DL1I2C`,Ldh,:V!T"G5tOa%&(/#.KDi>fMYmHoEXoP[f+srU&f+>
@BpWJXnjNl/B3r^"bOWk5;-1cHk+#D?ceO%;teC@9s!6k)ku[K6Oa+lm7=jPA?[Y0(@nj*Td
Rq'ngg+J3Q&9.l8`92[1\[f;(_"BP18Wcd-OhPtDLa7ad5@_W"@A1#5(?-`7#/#kgDkU@b)4
BJZ'h,?@X!]A'U%3*#,3m7\Brn"#g8n.Y'gl%NcY:L.ur_626(rE1@UVcJ=up2%_\><XGc`aa
[CUB;,QbdUk=[)$aZY*H>&VDcnZl55$`^V?LLVN.eaQ]A2bJWZ\Nm'H;4>%)<Hmm</HtLD?Nn
kGmgsAdIrI#4Yb\9jl$hBp*U@Q]ABo!J`fq7:+4!t=m>f@op%kZNA4hoTKS55AG6h+kI>)qsd
qYPM>+e:idDhJQo4U)t;r`G(!c/);17+.Whr(Qp;Z(D;Xr?%^pLo&pS2U;JS!5u&@<0LM]An<
&U"l?qF(bU=aCkX?(&:e.@q'97=]Aj(-XSsu;&%sO=?>VQq!N`FDIf?bd:RLFCHcACUu.^jbb
0.&&K:Mfo.]AK=637s^iG8*MupI]A\9c*`#KsJ'OZlNH`>P&./:uILg!?/fmi-;'uF7?LaDf0T
6i[WcfR)Fad+gZ.7]AA+G!#ICU`Yd.2g@E2\CAbl2WGeXM?olk=1TYXE&$@41E8:5AHaI]At.>
&oQYe!@Y]Aq%j+Y]Akh-VG$\sJpMT3mB/$QtMSbt]A*&7"->Kr2GS#<p+!))GcbUq,$(fg9]Ao_N
Y'H4h@Da!;E+Rn[<'[Fb?R+&ri1]Afai$T[ecNf.jnca#F8#BG2%@LnIZfmBgNG%;iJ(Y2K`e
74j%_D.Hi%n&heVg7b7(nSD75+DC9">>-^uMD6F`oqQWW]A"3B;KuK$ss*<9&rs<qM,-3+MOc
-IUUsQgZQ,q6<obnt)#.YY@8r]A^^-Pq.]A\-OqA/=ol8q%E]AkF:=_K3Q%&e6Y^L$H.aciDO!;
:6]AGcSQg4.Eg?;!75$d9amsr&NL_qks0)f=MDr)s8OYIK$>OZ,UNYK#5\eY2-Z!enlX[a/UH
H:X(Nk:_4jkdX]AF=hG'LPa9A%pTX*lPSp^+$Z3JReb)ROE.i#3Ma)Cun_Q.bQkr7s^9N.Li_
A>$_BK60&d!8.N<M)5g<GDk^dXGgi.9lF_'RAqN>+.:DnTR4f<Wuq_IQQ@E$5'.U'MT7\L/N
Wqj^po_nF#IqXs5Ubb@tO7TU:nHf%d5rDq?bfc&eAE-$W-%AtZ<4nsIjFh:]A#7AeD^#YJ/J7
rD/jE']A+)r]A;%$L,4WYrs.n\QWKkZS?5i=X@mi[9CA+=ifpK!A#C(jbEN/Q+1;oP/<\L]A$b0
t2H)kGaaDP5'hKmH)J6*H+L_/LlZA5nehE$\p[>Y.TU<EnB1'/_!4K3:/h1hOlGmEO+t4k)f
9WG%qt8IPBm5_^QN6J7Ac\?\0;BbfM'$*,7_]AMk/P@$;#K99hfSka,hm<DAjA9>"&ie+=e?h
4-T'iSENJg/iO_)l]A]AFg*qnP)O9"P,&ilRaee\uU63LT3:C$D^lDVb`no1"eXot3-,CF8B-+
)]A.:472DBim?Mugq=X\G^_ksprbGj$^E"1JVlO:NjZK`]A=C[(,:G5ag]A_N\@&-ii$3LmBIb:
SGOi$o:<dIP+t?7O5c.CkG2*jGnF?T:.S[kkn66B<P85'`GAnpSXk&U;oMAD4,fI>0P"Pn@U
I^5po()_p,VQh=,]A?8I)?Hs0nh@#:K^:f`\HV&>Lgr(SWDGXG"\[CYuojode1C9ONJ_`=,(h
jrf!41,7:1_[?9[q,#,(eC'J7dp9)Og^\CZ\RXMkNE?KOL=k=:soHKh88N_sZR[Z:,1_A9PC
CT?6c7-Cg^SJNo_oY[_d)N$?]AA@^&D%/hdmsjRUKZlH9q!D1k9UT*5-Is5=0,=g/h?mrtedT
I711uZ`4-.;@AfH]AB/e6[9]A3"F^[A<B9j2fLs)J5f[(=X0C'KRC(`HFPCB-JZ>,:8.H/pYgX
k2f?OSAKl]A%_b]A'*#1o4A^$PiFH]Adpdp%lYBPi%#OVEg#$r]A>g$V.$7=<?2n,Be:56RlP;_r
U4*AmGl5/'QIPqW.hklh&,u=:d(cjJt$McbKD$L,,mU>)T;K>'h1t1@G!N0F*nVfW$NLMJ@%
jTYf)6>c$$%NHjK\b!s"D*>`Bt7)NS\d>>^_>"h/e<`_)#2$0<BBUso:5p4*K\'FVrQe/1r=
[kKZqR*;<$S^/FhPf(K"V4neUlc:9\"D^qJWZ_<XD8(%Tj09A+pIl6`ji?,CYqiD[s3far@l
`F,2naj_',50ZiT2<`hP,nR?!P__!<^iA;5e+UcD[tY(%G<$BBH(D98gKMmD6mjH,)o;Z0Y7
,r5+j0-p&0MBFNeG!M%;$Q<t`,77b!9BO]A7`hDHh.E/t:XepCYdl&Cn?8^tPA^!a@e7#8e]A1
h*lg+krV3!pj-ApIclHa5?Ea5KR4E7E(<Y=[Fbd=k_;Yc"SSbd#jc<]A7?b+%L#9L_7(82mmA
YY'.";.-%5S5t+iY5UfYb)+-gBZ#JY`,A8SA@mF:22`6UTl__cU:jdPnXX<C3C<>JlCjS4rM
Q:4@LkMhd\qc,bK]A@lJQ8h4_Yc]A6>faE`AOPh!%KZJ0ccUrLt9,g,I78igm6&$s6aF9IT>1@
&!33HhLAe80Wo9-D<F:GaR=?)/Kl:.,gQM=N>kF6<=r#2sj.ZV<F&Z0E!H-%*P=X_"@h$=R!
2WERUCAg1C[4qM[gI@,Aj\q#0X/XCYrBZq6]A^=Di:XNA:4?Ii?+HlM6!j0s;'@)"i?^SftfE
e\fHGnj#?/.p:bK2EQ`6"[n\2>L'2?9NGe7t$FhL4r?L`cc&-"?9/:se95%nc9OP<#A:=XHD
mm9YEEd$m;WMVst>JP`P+kHSpr1m$KsGNC+:RpkKoZ<('?5)&:<;nA31;#!L$eW>D+ngYod\
(t&l#K%Nh1VHoF@8QK,?=6\8^hRk35eg^FdCicq$Qp@s'oT7VOYP'@nspJ'YEa1Z@42#T#h$
ok4.)O+/%aG"[h1p+$;\MbGlgMOURRt]A=F@LLi+0*t-@t14hP-MX9I@]A<M)bb,ii5Jca@Vjf
1oRP=qU)Ja-Y=a_'M8Rt8un5/:d;&t?bWo5Y_;38-R[@$P)9P9*=!k%Haj=WklOOV!4aVr>*
7g-]Ai-qihGdli5%>s2'iK2ZVTo)HIHPbsA8.1oG.dA/U`cD(2XT&cC,gA9.`JdZY`+UVSgjX
dYC9TTm#N9mNp4(9naX'a0*;;E0Y;N3OO6>aL(VEPL`qAY,6%lfa6ZG0B]As>=;;7+TB^3=H2
UkK+hEY8fFrs]A.)DDfYOKU#m+'FY>&fcual:9=_4iY]Agh/8,WL*.:".nTO#-F:7WJIuH#pQi
+\6SPdkl5M7F*Xt9cd50f_HTK20K;@Fn4qgta26D"i]A=?JQB/@P\+JKh4@ZSZ6IT0Y4W95uC
_u,!uj8Y"kI%o0hcU!Bq('[U-=6t^DgZQ*(XUXW0$Xf,5iNq>4oJo;Tp9;._Q'8/C@kPoklB
$JKF^):@$6LkA<LMrWg&Rq!8;fE\-bL+%`6]A5GF*p9-V--.YV68>ChK$r&^,QW)mDt"&_qB5
&,F&I=A^7QBcjKLkp67*3_lQ0,oMJ1^,0B(q3ip/d'h%bL@I_TD]A,7#jG)N:p]AEp'pTq!`WO
&5<cYW$bhh^AA=#F%iqE517o)Scs9GOWW<i\De_O`J,3Zrf:3LbQ*ZHf)n2=>YSA=[`<s7Et
`(Z-dKJA(Td@:$o%`&%_[>!u38okt<TX/J[(0/.B>#V'.8Q!pR-/5r%U]ATNt87!d9('Wo5d9
[,_]A,jo`=THoduaT^Nf7UT?&d0TUQPoRm\?1K)6)f2rMmjtN'T`@K80HI"UVTrCmJ/^5j0Z+
:iWJgGnOK+L5k?a7iC'Q7TY?j';Y*n1(AP3ftt:n>Q;;BpSghMAhmpSb:-f^dJ]A!7YYI>ZKr
B0Z7,j>u`B,%*$glo>(i;is7Mm.]AV&$\dPVA(!PbSW?*pM]A!^TEQHg14(h[Rgd1p.1"F-"W-
j&"O;Brd8/R.EnAKrmDNZ,!u^Gk/AM_<o0g?@#9GcsEnSA=$O:ULmJ>SpQ>_qNeiPl(,H)_l
7YcI)OAqEdlh<335C&E`uQhTg?j=S%^)g;oJ^jG<Z5Z_`@C-'dl!R7+6HFVr3@P7pB))6f,.
WYAfMR%sOD`o.4%*go<)_<GAW?>H]As$4nKV0s[O0Q?a7=[3q23T]A9VnWd$M/HFo:dofNOmdW
fcu*kZj'*U"W?!Xj`FMXp-r!>)l>-fI$7CDchg"6VHN^fX,d0`tB_$]A)+q+TsK/0]AmbL!&#2
n-l.=PZ,/8UUl^[S5<)e_+DE'Ve=n7I^YUF0TC"O>K7"t*J.+\hFF<f:?+rMBb!^R6l&#*kg
OQPSF6_5#/]A(ltT:.fsS2EQ?5+#FLZ6_0&Dmr)oJRguEk,4?]AAiq>%_D(-bY"EdD'Gd%=lM7
Cc]A0c7s=UK3sWk-SR=.N)-qGSlHXnCH&DSGo5!:ma('qiBo_jD*I.Nj%9]Aif'%-#JeV4[rHh
YuVLp&B'K45:;DtY-TR8/Sndt5!AVJ)'a@CM5DJ*9=/:+aZ/kWPHm^PMn.B5eCRJWJXqejrl
q'_!12\&;[1C12>F1S3[YL\<JK^+c=d!"Xn?+04sIQr[9l]A-e4n["-`i5%TT`s3In<WP\?!n
rg'Y\mNrc*]Ad1Y?OgLs_,J<cF]Ao1ZfIY,hl,X+r"MI"raJOgh9Y[kbQ[e1Nn+3i(VGB,!gP.
_"td!'(EWE3mE>]A$2Y.<WIDtUZO?Y4_T&QQ7;?sqE&rL(KiiMA(9Q2?q'2[,;p;plb_pIm"p
tsAd+8PGqC?!.b8r7qGs7Zin_@LkOg7HCK(/r?dS#_Z0(qB`eLbBgrfA^V;p.QG(EhCn)%&c
aq!W8Vn&^Q,lZ2mXKa*043X17-uTDn[9AR(.D(knTEQhY-$3X0&h3u<KPC+.dT@ORllm$3kj
5[KN'>in*!X@!E*gpRUGn,mCW\gc!FS8`PO?s<>@HB*>G"Vd\CV"ekC[c_P`!%H%sAe'8%sd
:.$I@b6'OoSrN\dK\M,8m$@Q;`2'sNKoIN,@SD6c[?9)B[L`tLBePpVs)XB,RCS9Ls"5<(DI
5V^35_ef)=/3kb/iar,-h[V<CSX8K_SWCFBF-\_]AcLN\`MM\^gK[X+Bc\3OdNV?sTk]Ak9(WK
K=f!m@Q+7F7)Qd,C.HDKog3M>;m]A^KBm\kBmEO?SOPT>Dk+ZiC/YkDmYLUB,SF8Rl5f?]AS34
'Xl&n1mNU2"O)HBki.0CHLKT7ZlMYMkDi<%3^D+^'oO*CMLS#-f7kZY2C:ClnPp,2Sa[=a1B
Ab7G-Z_lIZSg%6K^u!h*f[.8D"\r4A4`mPpaS>>f';*`&CbAZE1K#qYBST)X?8L<nUH;q<Kn
;n6XL,^g<a+p*X)&#_Dc_H?4'HA1CXg\k)U)f)f-pCKV#i!=s(O5ru'C+[%c$2o?XgB@I<]AZ
rj&<&2K'tP5-%8RN2AHplj`/n%SkPPmLrAD2+_g<N6nZF3PmZLhm>5SUY)Sa0br6794>b%.d
N>5E]AF)?l'lOMZZ]AKM)qh!"I6L>iB23r:j:p5m&`uPH\Za?+bLB9Bh<\n:FGHVNVAsu%9Ptq
TN,Cg,hq)"MATAd6$EFQ\Frn@jGJ0_`,6W?lRG/XI1?]Ac"JXCXW2&**e'dLZ$HS$:r4-skoJ
$<MY2YA"mPCNcph_'.^;cs#YPf"JT\"c=Sn#Me3@2sSBE63+,a%IC1JGs8hV56Qm\boJ*1-4
uc&jR)KA]AnEPQu07#1\^ooQaP_4!^2s=#+?8jqa>uQ)$,^((WY5'p7=,`:&ZW+@4s]AN%$E]AH
Ac^-4L.]AcWcQ_IN,PlbN'@@kNJn;HVoqcmNeZO^M9EOhH$&OV8\&SZYV9GEW%;n15#gB1TuC
@T,&N8-L6lb2N$PnuV7.$ojes>Ye<l>TnoJF&hUU84d^Z&6]ANJfcWl'r]A1DCDMkuI1A.[l:V
Ji2JrHr&b_B1Mc_k\dgI[@-caART#PZ$kJU,JqQ#l5nKAm')tM?'2W8oe)UIk?$4==/0;EnX
.c[Lmf@E!Xg)"TZ?WdWop\1,4b[<4/@sc%IjD98fV84(lL/]Aij7S;RDL$F4N7Kf,`p7Uj4j0
Bp?Dd7`A5`l4`tSrYk:fR5(W)$Jk!Fc=;08Ti\<s8L=&K+KKA"ke8s^]AQD^G6R&aj$d%fqVl
hhDW;#Fk=G.9oX[e^?tT9pN*8A?&@l+ORl3^HWDa9C?GLPTHifJ:9BKC0>/:04/V'W.c--<u
+u@2Gf>c?_;?*ea8AGY'D>n.+6cF#*L0/Cs+ma^(J9FHIn]AEONb.o0YrBK8Jl05#^N5f<?m8
p7MnVLj2Z9WOa'nCc=cPA8No*D\870H[,C!7"W:.)0FJQSaG)=pe`:6Q8*@(YZ^)11jS<`/"
:!dM9#.q.b&*!^+^C:hMaY[/FCk!'HRbh?KhFc,'-^'?hIid1U\chn5Zs$Y;+j`9X:5O5qQZ
!]A80eqXHere..g;1aa7D;B$C[H554e"\[0cpZ-1&7=IA7nS@IR%1OEW<`DnMp(.EVB5Fes&2
7KiJMp8[WAFEL*^e-q:_Jr/.]Air#dcZk_!`m\4+N$qq!<Ykd]AMWK4N3eY%@7unMrVJCE3X+Y
7g\-LJO/S(_U5<Fr1l]AP@eg$%bsGh39$XnJT&_Mhq&0K7TujHJZ8Zh8TVcFKq!SmB!$Cp8o4
G@J9s^PohoOAqE=Mu+aNBY4r+cA:+@o`gfLl@JR_R"K:)#KKk&g,_d/5lJGc?PC_52IF>!AA
(V04an\)ES<KDGg"?29>]A_nMUI(XqJTE7ZeXEilMt9`8=47]Apl$T/.HjZ1)JK#34XF4nE(9q
?ZFmBsi`]A:G*@u<h>\+#j)3d70f1g4(QAV\Xs)Kpn?',8*,^s0,8PEWl\X/jDC]A/=W*>nlid
]Alkn<6p<e`2oA8,Eq_gTfOET0Q0;Z.JZ95/=4<\1,:>`_;=[LZeS4!3_GZ-WS:$n7IecDVd3
qe2R*F#o$G=jVOm>:a`TA*grf^0nCZ3YgiionXDUt:#/W64]AMnQJ;NCV?m(IP.]AZT8Qn^q1"
Hb&mW,MCjb_h6'unP8\M78"'3abJs7X<7`N^;ZY=b,8HCCii-_NaM>0!!H7)<jfPLZq0JpBU
7gTd,\^0M'?69jZhKm6Z/(!8oEo828/(Ok7pc6=VC8ICF0<SE"A1B*R+E]ASDt1NTHa**_2fO
PQ&YX,<@Yr9VK7>>i^$,8<q+aKK5N;ia)e$2J)U,%:$S-P?cET"SM,6*SRr3gCOOf)[0#QX]A
apaFFt(-_5kfb\%'AWK0PMp`N;]A-;(\c3rN#_.IHfOAsfC%3l;RZ/Oi=0S*[%a&hAEtqJ[&M
?,M)=ZJ;'d.'mS;Dhk@V[*0c,<0]A.;Kq1UJ%;^5.`[=)tT8jum`lK=t^F1CRb0`oApJ3c-#E
]Al'*XR8c--!(QOhn$chu=Rik\7#?P;RtqkLX05.*)(p9pH\^1)pg/@+J'PEP5E`uWfjZa95F
umoqfY\lo+*[`-W]A`Np/U/?jaD!kFm,;l$Z(,;Amj08)[Qm!(OQP?^u1JHrhZaLF<FJe(4J>
mpD_-pW/O<FX[26Ts*QAEa!:6#oTdDpV&)ELC19:Go4ea'?J#<:rEij)Rp&@0e/0nQ9r:,7n
beFr.$"5gd+!Quo/K&gmq_rU.GnoSCaS`(n^'$JhE]A*I5,FMC^WVpmGJ]AmDn#V=Bf7J&[s#`
-F1^X#]AO]A^T(qI+]AUc[S,/;3MP7-8bfonDHJ*F'Ie6Uie,k/,q2#8T6HPmAce6:jbl_aY?n1
n\;T`!:opPk6"&ol^/K-,HSf_0A\upo]AX'11+CuS?\Sp1`..=.k'o6#'[.d$idj*a\m01Pf-
&6fE'XC]Ag%'XPKPue?iqR,jIq_:RYp4s4@fL;rFUXq/hk]Ae:MuR^BNEm2%OSAc>P\mA'e$`V
4q#=]A0-,djE-gBAg37#D?rf;+nS]AtSY[mIk!nW!=fImO9XmLWgn`\6B4qg7n>BB,%t3t+^i[
))\e2F$u1K3AP0gU2AQA`""3kS1%`%PQc#qn0SYji;(:-*I-;g3LhpP-u?KV@QA2/O.!mp=k
0Q4n-h7Z=24-&<D8J5k'9ba.l!2VsRQk3[A=`G-^HVoJ02AE_Vq='6DABNpo3tT,O\ppLDIt
Z;cb%)c#-q=]AI3p.p0\%/-f5`Oe+A@:P(S"Y(OT-UBkE#WN?Z,Tc-k<4@8MjU<[^`oqpZaeM
^Qb!We8ujq;!q0biA^a)B!ej]ANi!Ab%.2Uj?4e9X0tR]A@/7K?QLg/V9KBG]AkbZbe+Y8*S6NT
`Uu"5[T=dTJhQ8jh'-l\j.N)>o\r&02Qhb]AQP<S1\FD-/8SXHl&ZA?AdV11]AXq?tu3F(R<Nr
dBWAlKrOq48ZC`Y1i[J&+h_*V55_4WPg)T$$!<R2!@-\6\jV(QC:UMmA@nlgJNOA:c*\<DZ2
f__b0i]A)e6-*m7l'0pgpqR3G(.bC"N4U?B<^uQ[SMlmG#r8dPEdQZP._$?SWo6DI5X.p?rB!
f:8.E?GD2KSaF@!#p[.,0!r\B]A:3$pqh;*HG+G3HXaiI/61a%[Fm"?UBYK3OFF2Hc9li\XZj
88GaU`#lF2#Efk/Um;.D&(,<=SfD:n^LsQoSDO"f:AW8WsiN[>,.H-`t('$sk'gF1uM3a.q&
W:Xg,hh=WI%oAW.;(J1Stc?SAl0jQOP4.mA>m0:P@^lj1,,24PC0<Sj]A8"VBuW@lG060-mo7
g?9Lp]AEgL1m5F1?-%UCo['+<8CQ)*<oU\bg<DRYlU!o?n&l3(2IK(fIiWo1b+:F0+73IWpaL
0o41g#_an1&M;NTDSi]A[rpHb2.#d'/`l-6j9eT#)G5gcZZEm^5&RI=:-&ka1O<o=a]A@JkYCE
0=tg:Qq*BIC_EFt2l8Y@RciA?OXXV6qqV)&.hlUZTjfL^j2MPAZuF6`0Do(;]A-9iJW`D0bm(
EV2FLJCFde=EQoKS_7PJ_EdXa=7C*IBt`LFrQ]A<luFmY7pH#EP;ieesL?8mc)U%B7J1YgjCS
e-6l^R=3u1F[s/8`0,Rp=*WO/KOnrk!#pb4o(/k=4n*:%UQ1T7tjWS\p,XWM5Z'bCp-T>nB.
OIp#<@D^jC<X6c?pO&?%qr*IHCKG:ffqDW<R>2&kl3MF#LJHJD6d*l@H/t1cA-qs,P?5?#*M
mo102e[7c/@hmlnj3YqICe/L]A7KC=SJ_=*E57Q1d1K&Kfmf/'b>FOR_a++.q/tDCot8mq`\!
1d0M0Al%d^\n<X@*:QM.5KB*(#ij=n/$?l1e,Vc`?^Fdu^D5g^9E$B9Q$DZG=am@Cl0]AbH/4
8at[9t+XIN6Z<BG+j*mobQ.B,Vrm[>W"0ch'<!>j_9Xo`TJgn`@EqrQ>B8O]AW&p3&@2JR(1T
^kSoZCoa%l:J!rR'&"^9acLJ<+]A'4VK&P(K_,:Ih2=9(\d2<Mg(l5dOBBj8nD>un$PA<GQP&
#'TA<33QjXa=qIj@Zj_qL`_8/ibB1=G\1ATgc.oS_^ZL!A._ckC8(0ITqE@5>Fc#oPd)ck9.
p7UTZX@j2,rO'G/c^0FkFL.RFMMXfWUXF6RJdb?e*@a^tjP_.uuA3'Pr72\]AiD,D,q;N)8^4
3TY7%5+n-MdPS)(.^]A5/Gf;>7<FcZ68R>-SPa!fuo#prN)&FZO;J#se[El%5MM77_PZ%HOdJ
:85nBF;i3&!4uLL;WmoR=88b^!qJi;VIT35X5A."fMHqO#-b8bEqL9p#?sc8!l$'14JsB1NB
^q7o[C:.QLLUH7H1l]A1`Nr@e#'/=d9?q)<-p^,Y0@:[\6BR6FD20&jK4h$dljE;MN7%o]AfLr
oid)O9MJ&<m[F]AL8&t,-PoK6fC@^Dp;t^k.^[dkR9[?>?b]ATMd1KUYq##[V34&&=0c`T4'<S
rmUb?[#EFu^):ON9M*5Nma^<"hqPJC8qo#%0K@Y`8"TihRo@d-IGBbF$?AjD>?g%('5BC2E8
$oH?U#fQ>8%R'^9F1)%cDW+P;)(#4&1Ru!TWC7XG:[C,_&hf^QYhb3l:f^q1s7QdAha9+<_2
C+K//,<V^E+9C$55Z(G]A]Ak8<;i<>j*;YTe2m;sdH-+O<92]AFUfjn-mMq<(QASfOa%*T)K>KM
fG[]A72k`U.ZQ&=#EG^6Wi%h)Xkm[S(U@3(*G!\8/)!2W_66[,H8L3/1B/[odF#bUl^C>i+s7
i$t/AFIIe=3-N0GQ-HcmXKq.H=$t+r=#HS/T.r4&b^1)BE"%@00Uu[-<mHQKjUZ[B0Mg(Uoc
p\5'$8r@R"(#[:a6Uc"Ab\BU`3IFWX38^9G0!m2&4e7#H0_JEiCN)J-rT)'83pLP_9YdPDlF
G>/?^]A]ANg>e;&\=6UHu5Kch@DDpR:T1:.$'/\rSU]AX/">2Jn5pi]A$ID"&4oB0L=d.+?FTuM]A
<&SX/T+n-:-kLHCgH(b<'"I/6^r]A>udu9'ah_$R1BfE;VF;!/90+@f.f/<&nBI,KJ-ak1A./
9kl5_[Sn=uJJmW,uM/1U^jk2%odAGgj`b1^Z'Zr(=De^IA>&9bS.A\C>UG$stUPkYSe(N<KF
aSt8^OBe5^=A%e@CVe2==j.nMlrdVB._.9!dWMq$Rts3P(LrTg$oD<'jWe5!I#2'biXN"X5X
dZ#WB#'d9oQ<QG0mSUgir3k'Q%GUd)Vu6hd+R6Vl;cjdq_0M"Bb!5YCsWdlPkr?"pa^W1@gu
UP:!ME7n@j&hhC(-4*rYNW>gjji0S/"U^!i]Aqu%,q^hHaCV<V/1gD1I_.]ArH2=P[$GO+M]A.0
JM(W9X$:TB!83I*UW_`Ch&Hb,*!qq]A3tm<f"<!f-CVIG(l4,N)\]A!I^>@$oH5K0p*Ie]A]A>.%
aA0`TQ7k5K*8*KnD4XOO;+<5lZog9NlUKK_kDLLeXiQ>WX)pM,1]A"\M@h2`ef5PC]A%)D6P:\
aljZabedirH8QJD/]Ab+[IE\8Z\A=nbZ6H`X21u_4F=^IWW5';$fZ\(G&0mo/h![#l._!CIsd
mhQ*#K7<IHaVXLRsYf:[-O,T-m.1(J#[?1@9Q6Ji9k*=9dAJq)K?\0]Ap,XQ("O0<h@=Ug0Jc
Zqc\tQdk!3YC:uT_^b!EZTV-P\6:\@Q6-_\'Am\k'nR>'\1MugCk>T,K`i49!NcrukE9l>_7
E@s>i2+"VqC"k[$.55]A[AF-I90CJ$khH4PBAW$:0M,BD)6KqoY%6rb4hb73DUMSn^0sMIcW:
?X]AgCgo//&gb,`l.\WM=n,@b!:8?;j>SYl5mfc8I6q7i/lZ(i>ZN5(`$#s3TYF<`tq=i]AT-o
W&qo/ckiu"-)FPk+@(-:452<TI0bVaS`)jDKL<`ip`L!La+EdroW,m%CMAQAb24@6<>CLLZ)
'"a"B1?eGnuVG6LR.@_HI3d[$1`\S/,X/#$6Vje]AJQ(:sIu&hA>H/Si28or"p.O*%h!9P)eF
b1DR,!lckI4%qao05a$\Cn!m7D:55ga.UIf4u]ADtC/;K5[NVqOSN`#//Qs@>h(sNI&,oYW,j
a:CkOlUo:6,_$BFBun2Ned@)t)g^s76'O^ja^8[_"F`s5=k!7n@PM?kcS/BMcseD6l\4BK\h
oHo;+h/IgT]A1*/[WO+rc07=#'4n]Agd3=n,HZ#Anl()!U)L5#1P4X\UNITbTT!<m0UX%K]A=sb
Y/(oaAY<gL[(5R*oWS+).'a`S.6,^IWq\t$6PHoj:7B%Kh)P<`RXn6rUi(,KAT@0_h\>A'Vc
72Ap$#^#;l4-]AR9[b'`cJ)5CX^qBlop2]A&s<_aMInH3L/PAXd?K'$Uq.t,pP"]A[c]A256,T>]A
^n0!ja3O7;%OR`5@37^.`\Ii&N>87oQN;\L.YCMKp3Ho+WQ[`b8*U$/?H?5daI2B*b;1ll@h
1*ganT,jBlR#n(o:7X%Y;`/'OP/8Y?i775n@O`=._A8T4kKr85E$b_Q8]A_n_0AeYQhY\9q&<
G2g!nZ)FcNR%]AM98Sg_-Z,[oHEN2T.<ICY>EDN$1=E@iN5=>>0BR+tgV(<2kI%<i]A4<EQ`'Y
G-(#Z0g(Y&K'Z'jt:.JI_>4Q]A^jhA$LAfGI'f]A/T@\c[)0fYnWEs@k#]A9/q[+>(Dedhkcc!.
^nA*4=_#ocFgC0`:k_Ri7dYL]A`$D:QVrT^a%Ual^IV!h2C<B/i478)I12ilMYg"8NKJfp(5=
'<]A>YMMGRnV]AgX5g'!26lp3shN/UG(r:5fK`0!Y@X\X.,B[;b"eqm^TO6ZHjXqt!iIBdaL\:
dA%k+-9<96Kr6$m7(updT/hosQ><=SMtjL$KQB4$J+mYWfV\<,'JHFId^ZqSG/Qe_O[t@i#=
okqo>ej6J&!?RKcQ`@uA[=oBBfpf1m,@,[!e!Xk4#>.Y_/#kcm^[Ib-Fna&E]ANDG\coc)D!/
p*Sgl&0<^%.>q=>=l]ADG;Q$5_h%VQk-K73G\i*+Dh:hcA6]A_(9MfF$Lj;+m03R&f8Be.BNZe
0CrnG:!mt;b50-&]ASGUWN;51_W,@25Ld0Iq@N^\#R'<hm<qC%=g6ngYF4Bp[5#*VK&WYs"Km
_&V\-YSQI_BVp5qh67Js^9hD)6`PEnolCg]A1C[bGC\CN1cmO!rqnOIWL6Qq\VP.sQLEtBn$1
E)UoZ"L-m=8)a;6cMk7O.Nu92B#Cr9ju0jsH,?luT2+%)['T@0<Gh,DXEBpTYO<T;K*cC0D[
Nc7a*>n:$O6W(Eq_he?6?@[:s*A2PQ;Zrf40>?>QFl-)RH(,g#@Z>TR_F4bAPnhdoa(Am5Qc
=MP!8GrcrYDkjJ\,i]A/]Ahjo=B<,'r0jmS[!gk6Z>)tU7[Q&Fbb@t2P!(jp!TnA51K"C>)8qm
*0FO:P2R+R.i>V10fJ/3;c##7i^l]AkmRJp%RLG)Glsa/\^WrRg@S-&(#hQI;es="T=0Sp8;*
4P+?m#<6^:+32"gjE_cD^<VF0UaQ"?iKfB3oX<4j'.)RjhSP4/#kK/Y)L`;?/0m?7e[dTR4D
fk*2b+M]ALU@SOa*=Qf@H:$d:.JS2c^LH5,GOLblu9F"kL>oqE3s'(lncgKCObm]AXu^!DR'p[
3<e6hsOcknrG?cbBf%@=2a@G2I"LgJ<K&LF]ATr9R>Ya<D^:HD$jE\"'^,>cPB95VU*FQ4TR"
84I8k]ANEjq\iu-cFdPV+g&ElE)t)*'maUFi%+[.OC9@DVFdoqAP/2Q[+u<CaIBDhj943RHe)
EPB'^$R+)]AIADI8T@?W-7=Af4)W/"c^m!A=Ya78LLo8Hb.r9,3m"jTESN;"('e7oI_--WC%[
hsff-2tJrig8`YcEMLWi[h:FU.%UmAnG<rP!lu8\A<u8?[naBkc,,@fVm_UL-'ta3$Ktcr,i
l@L%m[+^VcU8>3!\Q#)-HG=O1Ol1*W3sipHd=rp)]A*VZ(K0RVl72``f0F.d,>`6[Uq`E;%D;
kb2'r#>Z:6mr[D-&1.\g1arQT>Br.]A9AN8rj%>$tG'5>_/-GF+6QY<pWr5rCR'6`FME.bspc
GI01S.5H&.1bm_]A@5pQYMI'O8L7l(mD-))/AN(g_Mb.dP#?<M_LTXug:XOKdl=`.)gFQsCVF
:M)XEaA#3bS=*1@%??TV.!:64\T<RurJ)9:#XDl'C%9Nm&2\@u.JU1`6!5g0((Z&@d<-n:6,
Ils&pc)dVOSB_^\d>k[hEI)2!Rq?+o,G*aU;`3XAd;SGp/8VM=ioSk8%r1afX=:'u*UHQJcj
KWtdusOt6HEAk=?F.%o@-6F6X-\!K'_A'iVRb`iC,-K]A,#0Xo]A@^C9<n64?9FPt/P!tEUo2$
F/Wrq,A*Vg2JTJ]AgPNjpp<dn#^_InDN[+-51qqM6O[3pt#K+^HK5WsE)-:e]Aq&BZjFL^d:Pp
i,;^YBdEec426nKrN^JO<D]AHd=DQBaWO;mPkf`3qRT?/1SA>mOa<ErVFh2Ul6=P*\+E3EQ>h
:.LH8LLnS<MK[Z5d?AUS<j+jp8:G[G4*ifN0e`uXTU)eF$QjKN%_o.tmZ,h35E33"6m]AdI6q
(r.i+97bI2VI<N^0f3#YVaVGODs"\cCW8(5UIBtnGN:NE&59f_3RYN^XOJtdCldkT<ZEt7Rj
iqjIc2J8Mjg(":\MWmML$$-A3H@c.7p\_mU%sT8C41'LQbI7Lbm<$pbC;Z/c9MsCI)gkgtdn
)?X/Aj3oAG%kK9klPa$'uZc#_-i!@udJf`fAZUl!DH4uL>IOc3G@mP-fn1Pa+jU?<JSU<i;X
rN\h5q(bmph=@:`\-EhkfGYQ5pY.\&rJYDUp9C$SVXh!PtSK=O:,T^</L?'Biddi4R=78Gd\
j$16,eL%?d>t[^>oA9nK$ik&_BMaF+k(SU7"nZfQ=)Mk?&H\5V.OZY+L(prLQr[F.k*+DcM%
<@XBqH]AgZ5<#:d2E)[7EH7jcKVk0dc?k&1&WZa_jVaSk@j;%43r%kgV,UXc/p3t%91(DIn==
VD:%NE\>Zs[omYIaC+1c^CgY#O]AYRCaqaYMMSh@6b_dn@!\<AmgRmqI+RcXhfLh)AZ8u%u@=
H@Q=GH9r\NQrj;oO]AB'5E;_s]A"h$kLmA!NM2CU`:2Y%6&WP6FRaVIb9=*&2fTPeAa+NDjSZB
Fr/iq)b7T7`FBES:qU[&_?b*VX^K<V>O^X`PW^m0jbsF3Kb5<ga18[o^^90>1?G,(dHuW/Rm
-4A%KfH7+n>J[t$496jI>6.@1("W@mCa.4<*&i!9C@g)4A)$L%?gV>:@XGk\Hrn)b_K!C&at
U1Bs1@uBFicNVID0g"+G&9&]AAl2-aX*`n,+DCGG3@fqukOk5>gjcM<+AkOFcO&8,0SHe0mOA
pB"s-tP4p*Mot&><0b$+WtV6(T<O)&)8o'(cHJ-cE^dppI]AaX9-q=')SWqo%nJ<j&Q_mF)tL
-,[2%Mg'SrH`OagO,$e?QT&-b/eGPTLhh6;oc^!YF>4:3dK&>.7^Rin+FJ5*s3O>!*1?=.]A^
'2Bec[^FEpGtdfq@75@=iEfGd%WDb00kG6Q;uumh+NI2k)(?gX9mRa&CW=:rf>4t0&G66C9-
]A9O:cktFj$ocO=89H<_k?`?L642K[gA"n#rBfo$.Lr@?&^CF0AVI_i`B@%cJ@*?i5[<bBg0j
:K=F.Zc>)Ec;DiN`?=jWZ$VtgX)Wfk';VnLXAT4P93&M,ku#86e&N<9fjAcqQdtQ<)9@nbcW
k/8%h[MN"?hG22XiumhbgDC=GrF3!igjT2>9+bk2Tg`'nl8Nm-jI;rYTqUai8S.P3?tGpX=1
Z5(m/Z7*gl/Y6cCs8OW5q+!>,:2o\W,_iZ,8#RYll.Zd>^H=I%9i(KqG0"kChEeuM*Yk:ee<
UXtuNs6%B[lA*H'&<eU[Z=NISaT,g4,0?;9_gNTQYiNQ/u=2?@Y297di:;5>TJ'=Kg]A?FSB&
Te7s[m8g2b2ecE'J"4VZb3UlY%JIPCH@SPgfJh[bFGhH17tg/,n`jB^:]A4'>;\]Af8UiJfaad
anmk5i<H]A[>lQ_p&J6n.[i4_6:ON`QcdCU^ZQ/9XnL5^eiGW@-QAZmVk51T:AT1T]Aa?C\-"'
gmUR%!$'^R\YFA%+`340&-fj'EF?0S=7X,CHm9Jm\RThU296e[3pb$R2:KOrQ`ieJ8W=ZQ-Q
',[3+XZIY/;9A.M>,d%sN`ZL`nVrlTDA>h/m2o#,5iK^fhn%8^K=TC&']AcCiU6+AQJ8!QFV[
^?:qIC]AYH$JGb&kaW*/Q#Zl2q!8#0.!afLEd_gjjV;k<0-Zh8r1g)uRTcTRpGCf2qE7gWl7K
k3o?X>PRhg`q2EESW[hY;`<<c8Lc/,rYO"/>`+Hnp*"%3\A`-1NaSRmOI+HH;r7'nOE(2kal
Jh_[E:C4`;_.LY8/5O1@@7A$)bE3QiURZQs(B*;^%"2tral6W0g>Am"/Sf't\G**M.>6d\3`
Z$AH7Epa'\4<*hr>mE$P$iHQ-9W]A4m=saL4pD.\53]Ai(V:2_Ro'ufLAhnI>(8ii4%D$H9$g7
q"uReMT_<QM_NRa'5G$WYbWlbNe:P_U)N]AON%M^,QoUfe[5)Y<HL7M.ThCe]A%CUU*f?X7o-i
TtSB,'Hou$=h5R.'cPYO^b"SJM=mcNVoB-Q8VY,7dki<_a>>gG1+Y(b>,!+!'L?4)U#P0>f+
3\5Udb[!Nl<?T%C7i'k8K)7&qn\2T)%C/$aS4N@g8D%J*Vgg)HUs8.LY1R:>9gW6<rkr3Cb_
CD.lZDAO$bE*`C/Y0Na#Z1i[I(2=QoWr?M^rRVLn9%ccDNN.m\;3h4hLq+Pff6\gfP&B:"@U
*<]An820Zq`4SmW_YThhkp&jqJbB?aRSLSTb3nY'#?A:4tl=L`P6,U\qR92a)#)tW#(Jjj@Xb
5iIO+@f9FX#To2t^4c+)X9C/i4>H5iL6'tuA6&SJ^6q=s2e#"bDm#'HFGL'ULVS*X!IcHCKE
Vr8=AN0$f-B[.,`(t:S[i76tH0Ds(fC[e9mP;jV#a'TSM'4qC+#`DSh$]AYS)6JlO&H-aPK`f
G2ZtJuU3K9:#B8eTZ7lOr0:H`>T]A5u\7$`"CSC5rmp\Wj!IhW+5*RCmL#QXUBNGiucfQ@T?\
QJ#!\qj/dL8T1=X6qTdqRi;hq)o*h0p)0k&l3kd&r0X-B1?Hlc4\;$2`TumHn,I(Oj"S1#d2
<5ce2'.NJlc8EFtZltDRc@d/Y3ZT-V/:cg7sdNP^;lV'.\NJM:gX+9MT6=+.HbF(;i/]AJU1r
nIF@6or+bPRO2JT6HG"64]AdC_aD'4,U_<S08r<KAkI/@4LOpmJrp_=>.oSijWiOB!<+.GsP`
Z))_5'r8tNqi%q0K]A/'@V>SjY-7H''t\o8o,4FFE_jQQ"6pa=/nIB\KTWR^a/;gNeHLFAY^@
u>YRdshh\5L,JOWRN%a!r93R"jf1s<Dg:NALLG;%H'9(cLfHPdj,DGikc]AB':$7Yr71^C,n[
a[+KG8SK>916DD@7s//Z*%VP557SsZ&?Ca_Kod*(?c@gorYRGf#&BgC32Gk1jTGN'e^2./s*
j+MrrE~
]]></IM>
<ElementCaseMobileAttrProvider horizontal="1" vertical="1" zoom="true" refresh="false" isUseHTML="false" isMobileCanvasSize="false" appearRefresh="false" allowFullScreen="false"/>
</body>
</InnerWidget>
<BoundsAttr x="0" y="0" width="479" height="502"/>
</Widget>
<Sorted sorted="false"/>
<MobileWidgetList>
<Widget widgetName="report0"/>
<Widget widgetName="chart0"/>
</MobileWidgetList>
<WidgetZoomAttr compState="0"/>
<AppRelayout appRelayout="true"/>
<Size width="958" height="502"/>
<ResolutionScalingAttr percent="1.0"/>
<tabFitAttr index="0" tabNameIndex="0"/>
</Widget>
<Widget class="com.fr.form.ui.container.cardlayout.WTabFitLayout">
<Listener event="click">
<JavaScript class="com.fr.js.JavaScriptImpl">
<Parameters/>
<Content>
<![CDATA[var chartWrapper = FR.Chart.WebUtils.getChart("chart1");
chartWrapper.dataRefresh();

]]></Content>
</JavaScript>
</Listener>
<WidgetName name="Tab1"/>
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
<![CDATA[復新]]></O>
<TextAttr>
<Attr alignText="0">
<FRFont name="微软雅黑" style="0" size="128" foreground="-13421773"/>
</Attr>
</TextAttr>
<TitleVisible value="true" position="0"/>
</Title>
<Attr4VanChart useHtml="false" floating="false" x="0.0" y="0.0" limitSize="false" maxHeight="15.0"/>
</Title4VanChart>
<Plot class="com.fr.plugin.chart.PiePlot4VanChart">
<VanChartPlotVersion version="20170715"/>
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
<Attr isNullValueBreak="true" autoRefreshPerSecond="6" seriesDragEnable="false" plotStyle="4" combinedSize="50.0"/>
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
<Attr enable="true" duration="4" followMouse="false" showMutiSeries="false" isCustom="false"/>
<TextAttr>
<Attr alignText="0"/>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="true"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipValueFormat">
<AttrTooltipValueFormat>
<Attr enable="true"/>
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
<Attr shadow="true"/>
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
<Attr lineStyle="1" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-1"/>
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
<PieAttr4VanChart roseType="normal" startAngle="0.0" endAngle="360.0" innerRadius="0.0" supportRotation="false"/>
<VanChartRadius radiusType="auto" radius="100"/>
</Plot>
<ChartDefinition>
<MoreNameCDDefinition>
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<TableData class="com.fr.data.impl.NameTableData">
<Name>
<![CDATA[ds1]]></Name>
</TableData>
<CategoryName value="銷售員"/>
<ChartSummaryColumn name="銷量" function="com.fr.data.util.function.NoneFunction" customName="銷量"/>
</MoreNameCDDefinition>
</ChartDefinition>
</Chart>
<tools hidden="true" sort="true" export="true" fullScreen="true"/>
<VanChartZoom>
<zoomAttr zoomVisible="false" zoomGesture="true" zoomResize="true" zoomType="xy"/>
<from>
<![CDATA[]]></from>
<to>
<![CDATA[]]></to>
</VanChartZoom>
<refreshMoreLabel>
<attr moreLabel="false" autoTooltip="true"/>
<AttrTooltip>
<Attr enable="true" duration="4" followMouse="false" showMutiSeries="false" isCustom="false"/>
<TextAttr>
<Attr alignText="0"/>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="true"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipValueFormat">
<AttrTooltipValueFormat>
<Attr enable="true"/>
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
<BoundsAttr x="0" y="0" width="958" height="502"/>
</Widget>
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
<![CDATA[刷新]]></O>
<TextAttr>
<Attr alignText="0">
<FRFont name="微软雅黑" style="0" size="128" foreground="-13421773"/>
</Attr>
</TextAttr>
<TitleVisible value="true" position="0"/>
</Title>
<Attr4VanChart useHtml="false" floating="false" x="0.0" y="0.0" limitSize="false" maxHeight="15.0"/>
</Title4VanChart>
<Plot class="com.fr.plugin.chart.PiePlot4VanChart">
<VanChartPlotVersion version="20170715"/>
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
<Attr isNullValueBreak="true" autoRefreshPerSecond="6" seriesDragEnable="false" plotStyle="4" combinedSize="50.0"/>
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
<Attr enable="true" duration="4" followMouse="false" showMutiSeries="false" isCustom="false"/>
<TextAttr>
<Attr alignText="0"/>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="true"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipValueFormat">
<AttrTooltipValueFormat>
<Attr enable="true"/>
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
<Attr shadow="true"/>
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
<Attr lineStyle="1" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-1"/>
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
<PieAttr4VanChart roseType="normal" startAngle="0.0" endAngle="360.0" innerRadius="0.0" supportRotation="false"/>
<VanChartRadius radiusType="auto" radius="100"/>
</Plot>
<ChartDefinition>
<MoreNameCDDefinition>
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<TableData class="com.fr.data.impl.NameTableData">
<Name>
<![CDATA[ds1]]></Name>
</TableData>
<CategoryName value="销售员"/>
<ChartSummaryColumn name="销量" function="com.fr.data.util.function.NoneFunction" customName="销量"/>
</MoreNameCDDefinition>
</ChartDefinition>
</Chart>
<tools hidden="true" sort="true" export="true" fullScreen="true"/>
<VanChartZoom>
<zoomAttr zoomVisible="false" zoomGesture="true" zoomResize="true" zoomType="xy"/>
<from>
<![CDATA[]]></from>
<to>
<![CDATA[]]></to>
</VanChartZoom>
<refreshMoreLabel>
<attr moreLabel="false" autoTooltip="true"/>
<AttrTooltip>
<Attr enable="true" duration="4" followMouse="false" showMutiSeries="false" isCustom="false"/>
<TextAttr>
<Attr alignText="0"/>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="true"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipValueFormat">
<AttrTooltipValueFormat>
<Attr enable="true"/>
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
</body>
</InnerWidget>
<BoundsAttr x="0" y="0" width="958" height="502"/>
</Widget>
<Sorted sorted="false"/>
<MobileWidgetList>
<Widget widgetName="chart1"/>
</MobileWidgetList>
<WidgetZoomAttr compState="0"/>
<AppRelayout appRelayout="true"/>
<Size width="958" height="502"/>
<ResolutionScalingAttr percent="1.0"/>
<tabFitAttr index="1" tabNameIndex="1"/>
</Widget>
<carouselAttr isCarousel="false" carouselInterval="1.8"/>
</Center>
</InnerWidget>
<BoundsAttr x="0" y="0" width="960" height="540"/>
</Widget>
<Sorted sorted="false"/>
<MobileWidgetList>
<Widget widgetName="tablayout0"/>
</MobileWidgetList>
<WidgetZoomAttr compState="0"/>
<AppRelayout appRelayout="true"/>
<Size width="960" height="540"/>
<ResolutionScalingAttr percent="1.0"/>
<BodyLayoutType type="0"/>
</Center>
</Layout>
<DesignerVersion DesignerVersion="KAA"/>
<PreviewType PreviewType="0"/>
<TemplateIdAttMark class="com.fr.base.iofile.attr.TemplateIdAttrMark">
<TemplateIdAttMark TemplateId="440e219c-bbc4-4ad0-ab41-4c18623425ad"/>
</TemplateIdAttMark>
</Form>
