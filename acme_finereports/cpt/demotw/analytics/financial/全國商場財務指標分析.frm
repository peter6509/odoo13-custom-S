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
<![CDATA[SELECT * FROM MAPDemo]]></Query>
<PageQuery>
<![CDATA[]]></PageQuery>
</TableData>
<TableData name="ds2" class="com.fr.data.impl.DBTableData">
<Parameters>
<Parameter>
<Attributes name="Pproj"/>
<O>
<![CDATA[XXX國際廣場]]></O>
</Parameter>
</Parameters>
<Attributes maxMemRowCount="-1"/>
<Connection class="com.fr.data.impl.NameDatabaseConnection">
<DatabaseName>
<![CDATA[FRDemoTW]]></DatabaseName>
</Connection>
<Query>
<![CDATA[SELECT * FROM  MAPDemo where Project='${Pproj}']]></Query>
<PageQuery>
<![CDATA[]]></PageQuery>
</TableData>
<TableData name="map" class="com.fr.data.impl.DBTableData">
<Parameters/>
<Attributes maxMemRowCount="-1"/>
<Connection class="com.fr.data.impl.NameDatabaseConnection">
<DatabaseName>
<![CDATA[FRDemoTW]]></DatabaseName>
</Connection>
<Query>
<![CDATA[SELECT province,Project, index1 as a ,Lng,Lat FROM MAPDemo]]></Query>
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
<LCAttr vgap="0" hgap="0" compInterval="15"/>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.ui.container.WAbsoluteBodyLayout">
<WidgetName name="body"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<Margin top="0" left="0" bottom="0" right="0"/>
<Border>
<border style="0" color="-723724" borderRadius="0" type="0" borderStyle="0"/>
<WidgetTitle>
<O>
<![CDATA[新建标题]]></O>
<FRFont name="Al Bayan" style="0" size="72"/>
<Position pos="0"/>
</WidgetTitle>
<Background name="ColorBackground" color="-460039"/>
<Alpha alpha="1.0"/>
</Border>
<Background name="ColorBackground" color="-460039"/>
<LCAttr vgap="0" hgap="0" compInterval="0"/>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.ui.container.WTitleLayout">
<WidgetName name="chart2"/>
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
<WidgetName name="chart2"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<Margin top="0" left="0" bottom="0" right="0"/>
<Border>
<border style="1" color="-1777440" borderRadius="0" type="1" borderStyle="0"/>
<WidgetTitle>
<O>
<![CDATA[=\'  \'+\'月累計指標\']]></O>
<FRFont name="Agency FB" style="0" size="96" foreground="-11976882"/>
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
<FRFont name="微软雅黑" style="0" size="128" foreground="-13421773"/>
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
<Attr enable="true" duration="4" followMouse="false" showMutiSeries="false" isCustom="false"/>
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
<Attr lineStyle="1" isRoundBorder="false" roundRadius="3"/>
<newColor borderColor="-1"/>
</AttrBorder>
</Attr>
<Attr class="com.fr.plugin.chart.base.AttrLabel">
<AttrLabel>
<labelAttr enable="true"/>
<labelDetail class="com.fr.plugin.chart.base.AttrLabelDetail">
<Attr showLine="false" autoAdjust="false" position="5" isCustom="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="Verdana" style="1" size="72" foreground="-1"/>
</Attr>
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
<HtmlLabel customText="" useHtml="false" isCustomWidth="false" isCustomHeight="false" width="50" height="50"/>
</AttrToolTipContent>
</labelDetail>
</AttrLabel>
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
<Attr position="1" visible="true"/>
<FRFont name="宋体" style="0" size="72" foreground="-10066330"/>
</Legend>
<Attr4VanChart floating="false" x="0.0" y="0.0" limitSize="false" maxHeight="15.0" isHighlight="false"/>
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
<OColor colvalue="-7881222"/>
<OColor colvalue="-6514959"/>
<OColor colvalue="-10237754"/>
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
<FRFont name="Verdana" style="0" size="72" foreground="-10066330"/>
</Attr>
</TextAttr>
<TitleVisible value="true" position="0"/>
</Title>
<newAxisAttr isShowAxisLabel="true"/>
<AxisLineStyle AxisStyle="0" MainGridStyle="1"/>
<newLineColor lineColor="-5197648"/>
<AxisPosition value="3"/>
<TickLine201106 type="2" secType="0"/>
<ArrowShow arrowShow="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="Verdana" style="0" size="72" foreground="-11385531"/>
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
<FRFont name="Verdana" style="0" size="72" foreground="-10066330"/>
</Attr>
</TextAttr>
<TitleVisible value="true" position="0"/>
</Title>
<newAxisAttr isShowAxisLabel="false"/>
<AxisLineStyle AxisStyle="1" MainGridStyle="1"/>
<newLineColor lineColor="-11385531"/>
<AxisPosition value="2"/>
<TickLine201106 type="2" secType="0"/>
<ArrowShow arrowShow="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="Verdana" style="0" size="72" foreground="-10066330"/>
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
</VanChartAxis>
</YAxisList>
<stackAndAxisCondition>
<ConditionCollection>
<DefaultAttr class="com.fr.chart.chartglyph.ConditionAttr">
<ConditionAttr name=""/>
</DefaultAttr>
</ConditionCollection>
</stackAndAxisCondition>
<VanChartColumnPlotAttr seriesOverlapPercent="30.0" categoryIntervalPercent="20.0" fixedWidth="false" columnWidth="40" filledWithImage="false" isBar="true"/>
</Plot>
<ChartDefinition>
<MoreNameCDDefinition>
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<TableData class="com.fr.data.impl.NameTableData">
<Name>
<![CDATA[ds2]]></Name>
</TableData>
<CategoryName value="無"/>
<ChartSummaryColumn name="index6" function="com.fr.data.util.function.NoneFunction" customName="月累計收入"/>
<ChartSummaryColumn name="index7" function="com.fr.data.util.function.NoneFunction" customName="月累計支出"/>
<ChartSummaryColumn name="index8" function="com.fr.data.util.function.NoneFunction" customName="月累計經營利潤"/>
</MoreNameCDDefinition>
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
<BoundsAttr x="1012" y="36" width="350" height="272"/>
</Widget>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.ui.Label">
<WidgetName name="Title_chart2"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<widgetValue>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[='  '+'月累計指標']]></Attributes>
</O>
</widgetValue>
<LabelAttr verticalcenter="true" textalign="2" autoline="true"/>
<FRFont name="Agency FB" style="0" size="96" foreground="-11976882"/>
<Background name="ColorBackground" color="-1"/>
<border style="1" color="-1777440"/>
</InnerWidget>
<BoundsAttr x="0" y="0" width="350" height="36"/>
</Widget>
<title class="com.fr.form.ui.Label">
<WidgetName name="Title_chart2"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<widgetValue>
<O>
<![CDATA[月累计指标]]></O>
</widgetValue>
<LabelAttr verticalcenter="true" textalign="0" autoline="true"/>
<FRFont name="微软雅黑" style="1" size="112" foreground="-1"/>
<Background name="ColorBackground" color="-13395610"/>
<border style="1" color="-723724"/>
</title>
<body class="com.fr.form.ui.ChartEditor">
<WidgetName name="chart2"/>
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
<![CDATA[新建图表标题]]></O>
<TextAttr>
<Attr alignText="0">
<FRFont name="Microsoft YaHei" style="0" size="128" foreground="-13421773"/>
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
<Attr enable="true" duration="4" followMouse="false" showMutiSeries="false" isCustom="false"/>
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
<Attr4VanChart floating="false" x="0.0" y="0.0" limitSize="false" maxHeight="15.0" isHighlight="false"/>
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
</body>
</InnerWidget>
<BoundsAttr x="1008" y="297" width="341" height="281"/>
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
<border style="1" color="-1777440" borderRadius="0" type="1" borderStyle="0"/>
<WidgetTitle>
<O>
<![CDATA[=\'  \'+\'租金收款指標\']]></O>
<FRFont name="Agency FB" style="0" size="96" foreground="-11976882"/>
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
<FRFont name="微软雅黑" style="0" size="128" foreground="-13421773"/>
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
<Attr class="com.fr.chart.base.AttrBorder">
<AttrBorder>
<Attr lineStyle="1" isRoundBorder="false" roundRadius="3"/>
<newColor borderColor="-1"/>
</AttrBorder>
</Attr>
<Attr class="com.fr.chart.base.AttrAlpha">
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</Attr>
<Attr class="com.fr.plugin.chart.base.AttrTooltip">
<AttrTooltip>
<Attr enable="true" duration="4" followMouse="false" showMutiSeries="false" isCustom="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="宋体" style="0" size="72"/>
</Attr>
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
<Attr class="com.fr.plugin.chart.base.AttrLabel">
<AttrLabel>
<labelAttr enable="true"/>
<labelDetail class="com.fr.plugin.chart.base.AttrLabelDetail">
<Attr showLine="false" autoAdjust="false" position="5" isCustom="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="Verdana" style="1" size="72" foreground="-1"/>
</Attr>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="true"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipValueFormat">
<AttrTooltipValueFormat>
<Attr enable="true"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#0%]]></Format>
</AttrTooltipValueFormat>
</value>
<percent class="com.fr.plugin.chart.base.format.AttrTooltipPercentFormat">
<AttrTooltipPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#0%]]></Format>
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
</AttrLabel>
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
<Attr position="1" visible="true"/>
<FRFont name="宋体" style="0" size="72" foreground="-10066330"/>
</Legend>
<Attr4VanChart floating="false" x="0.0" y="0.0" limitSize="false" maxHeight="15.0" isHighlight="false"/>
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
<OColor colvalue="-7881222"/>
<OColor colvalue="-6514959"/>
<OColor colvalue="-10237754"/>
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
<FRFont name="Verdana" style="0" size="72" foreground="-10066330"/>
</Attr>
</TextAttr>
<TitleVisible value="true" position="0"/>
</Title>
<newAxisAttr isShowAxisLabel="true"/>
<AxisLineStyle AxisStyle="1" MainGridStyle="1"/>
<newLineColor lineColor="-11385531"/>
<AxisPosition value="3"/>
<TickLine201106 type="2" secType="0"/>
<ArrowShow arrowShow="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="Verdana" style="0" size="72" foreground="-13750995"/>
</Attr>
</TextAttr>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#0.0%]]></Format>
<AxisLabelCount value="=1"/>
<AxisRange/>
<AxisUnit201106 isCustomMainUnit="false" isCustomSecUnit="false" mainUnit="=0" secUnit="=0"/>
<ZoomAxisAttr isZoom="false"/>
<axisReversed axisReversed="false"/>
<VanChartAxisAttr mainTickLine="0" secTickLine="0" axisName="X軸" titleUseHtml="false" autoLabelGap="true" limitSize="false" maxHeight="15.0" commonValueFormat="true" isRotation="false"/>
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
<FRFont name="Verdana" style="0" size="72" foreground="-10066330"/>
</Attr>
</TextAttr>
<TitleVisible value="true" position="0"/>
</Title>
<newAxisAttr isShowAxisLabel="true"/>
<AxisLineStyle AxisStyle="0" MainGridStyle="1"/>
<newLineColor lineColor="-5197648"/>
<AxisPosition value="2"/>
<TickLine201106 type="2" secType="0"/>
<ArrowShow arrowShow="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="Verdana" style="0" size="72" foreground="-13750995"/>
</Attr>
</TextAttr>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#0%]]></Format>
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
<VanChartColumnPlotAttr seriesOverlapPercent="40.0" categoryIntervalPercent="20.0" fixedWidth="false" columnWidth="40" filledWithImage="false" isBar="false"/>
</Plot>
<ChartDefinition>
<MoreNameCDDefinition>
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<TableData class="com.fr.data.impl.NameTableData">
<Name>
<![CDATA[ds2]]></Name>
</TableData>
<CategoryName value="無"/>
<ChartSummaryColumn name="index3" function="com.fr.data.util.function.NoneFunction" customName="完成率                  "/>
<ChartSummaryColumn name="index4" function="com.fr.data.util.function.NoneFunction" customName="上月完成率"/>
<ChartSummaryColumn name="index5" function="com.fr.data.util.function.NoneFunction" customName="上年同期完成率"/>
</MoreNameCDDefinition>
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
<BoundsAttr x="1012" y="36" width="350" height="272"/>
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
<![CDATA[='  '+'租金收款指標']]></Attributes>
</O>
</widgetValue>
<LabelAttr verticalcenter="true" textalign="2" autoline="true"/>
<FRFont name="Agency FB" style="0" size="96" foreground="-11976882"/>
<Background name="ColorBackground" color="-1"/>
<border style="1" color="-1777440"/>
</InnerWidget>
<BoundsAttr x="0" y="0" width="350" height="36"/>
</Widget>
<title class="com.fr.form.ui.Label">
<WidgetName name="Title_chart1"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<widgetValue>
<O>
<![CDATA[租金收款指标]]></O>
</widgetValue>
<LabelAttr verticalcenter="true" textalign="0" autoline="true"/>
<FRFont name="微软雅黑" style="1" size="112" foreground="-1"/>
<Background name="ColorBackground" color="-13382452"/>
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
<FRFont name="Microsoft YaHei" style="0" size="128" foreground="-13421773"/>
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
<Attr enable="true" duration="4" followMouse="false" showMutiSeries="false" isCustom="false"/>
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
<Attr4VanChart floating="false" x="0.0" y="0.0" limitSize="false" maxHeight="15.0" isHighlight="false"/>
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
</body>
</InnerWidget>
<BoundsAttr x="1007" y="10" width="342" height="277"/>
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
<Margin top="0" left="0" bottom="0" right="0"/>
<Border>
<border style="1" color="-1777440" borderRadius="0" type="1" borderStyle="0"/>
<WidgetTitle>
<O>
<![CDATA[=\'  \'+\'其他指標\']]></O>
<FRFont name="Agency FB" style="0" size="96" foreground="-11976882"/>
<Position pos="2"/>
<Background name="ColorBackground" color="-1"/>
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
<![CDATA[270024,1295400,1104900,0,723900,723900,723900,723900,723900,723900,723900]]></RowHeight>
<ColumnWidth defaultValue="2743200">
<![CDATA[270024,2592000,2592000,2016000,2304000,2016000,2016000,2016000,2304000,2592000,2304000,2880000,270024,2743200]]></ColumnWidth>
<CellElementList>
<C c="0" r="0">
<PrivilegeControl/>
<Expand/>
</C>
<C c="12" r="0" s="0">
<PrivilegeControl/>
<Expand/>
</C>
<C c="1" r="1" s="1">
<O>
<![CDATA[可出租\\n總面積㎡]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="2" r="1" s="2">
<O>
<![CDATA[總簽約\\n面積㎡]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="3" r="1" s="1">
<O>
<![CDATA[簽約率%]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="4" r="1" s="2">
<O>
<![CDATA[總鋪位數]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="5" r="1" s="1">
<O>
<![CDATA[出租率%]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="6" r="1" s="2">
<O>
<![CDATA[開門率%]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="7" r="1" s="1">
<O>
<![CDATA[空鋪率%]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="8" r="1" s="2">
<O>
<![CDATA[租金\\n收繳率%]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="9" r="1" s="1">
<O>
<![CDATA[平均單價\\n (元/㎡/天)]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="10" r="1" s="2">
<O>
<![CDATA[租金\\n增長率%]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="11" r="1" s="1">
<O>
<![CDATA[項目總合同\\n金額 (萬元)]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="12" r="1" s="0">
<PrivilegeControl/>
<Expand/>
</C>
<C c="1" r="2" s="3">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="index17"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand dir="0"/>
</C>
<C c="2" r="2" s="4">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="index18"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand dir="0"/>
</C>
<C c="3" r="2" s="5">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="index19"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand dir="0"/>
</C>
<C c="4" r="2" s="4">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="index20"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand dir="0"/>
</C>
<C c="5" r="2" s="5">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="index21"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand dir="0"/>
</C>
<C c="6" r="2" s="6">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="index22"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand dir="0"/>
</C>
<C c="7" r="2" s="5">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="index23"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand dir="0"/>
</C>
<C c="8" r="2" s="6">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="index24"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand dir="0"/>
</C>
<C c="9" r="2" s="3">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="index25"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand dir="0"/>
</C>
<C c="10" r="2" s="6">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="index26"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand dir="0"/>
</C>
<C c="11" r="2" s="3">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="index27"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand dir="0"/>
</C>
<C c="12" r="2" s="0">
<PrivilegeControl/>
<Expand/>
</C>
<C c="0" r="3" s="0">
<PrivilegeControl/>
<Expand/>
</C>
<C c="1" r="3" s="0">
<PrivilegeControl/>
<Expand/>
</C>
<C c="2" r="3" s="0">
<PrivilegeControl/>
<Expand/>
</C>
<C c="3" r="3" s="0">
<PrivilegeControl/>
<Expand/>
</C>
<C c="4" r="3" s="0">
<PrivilegeControl/>
<Expand/>
</C>
<C c="5" r="3" s="0">
<PrivilegeControl/>
<Expand/>
</C>
<C c="6" r="3" s="0">
<PrivilegeControl/>
<Expand/>
</C>
<C c="7" r="3" s="0">
<PrivilegeControl/>
<Expand/>
</C>
<C c="8" r="3" s="0">
<PrivilegeControl/>
<Expand/>
</C>
<C c="9" r="3" s="0">
<PrivilegeControl/>
<Expand/>
</C>
<C c="10" r="3" s="0">
<PrivilegeControl/>
<Expand/>
</C>
<C c="11" r="3" s="0">
<PrivilegeControl/>
<Expand/>
</C>
<C c="12" r="3" s="0">
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
<FRFont name="SimSun" style="0" size="72"/>
<Background name="ColorBackground" color="-1"/>
<Border/>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="微软雅黑" style="0" size="64" foreground="-1"/>
<Background name="ColorBackground" color="-10642722"/>
<Border>
<Bottom style="1" color="-1"/>
</Border>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="微软雅黑" style="0" size="64" foreground="-1"/>
<Background name="ColorBackground" color="-7881222"/>
<Border>
<Bottom style="1" color="-1"/>
</Border>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="微软雅黑" style="0" size="64" foreground="-1"/>
<Background name="ColorBackground" color="-10642722"/>
<Border>
<Top style="1" color="-1"/>
</Border>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="微软雅黑" style="0" size="64" foreground="-1"/>
<Background name="ColorBackground" color="-7881222"/>
<Border>
<Top style="1" color="-1"/>
</Border>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#0%]]></Format>
<FRFont name="微软雅黑" style="0" size="64" foreground="-1"/>
<Background name="ColorBackground" color="-10642722"/>
<Border>
<Top style="1" color="-1"/>
</Border>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#0%]]></Format>
<FRFont name="微软雅黑" style="0" size="64" foreground="-1"/>
<Background name="ColorBackground" color="-7881222"/>
<Border>
<Top style="1" color="-1"/>
</Border>
</Style>
</StyleList>
<heightRestrict heightrestrict="false"/>
<heightPercent heightpercent="0.75"/>
<IM>
<![CDATA[mC`g*PNVL$DQbYE.SI@/+:nm^ed]A!:Z6lCle>hG)("jd75t!U5":.Re<2(qC>!^h>V&C(>5_
Q@q.#Ve.L_r^F5QX?0&4-YaIJ\`$[blFMhg:C`HbK1BH#q1iT#W37o?;UE1\4<"RI,I;7djH
l1N2,4UWm.jn!l?*:"ssbrcW(.Jc9RU_n,hmo?R2Lp@e>4\S-TCI<P9iB#S*(1KGb8X"/gXo
u5YW'4=nS*g-&KN\Be/=_QT0jDAW&Pj&)bMmiIg_c#.4r"&L,gg,(";qfnt([L#pl^CP64XN
>uWM,Gkm33T`B.(kM<@0[\&YnK"<nF.(W*1tC#(J#jh2^pIK@fQKI9fZal$1J^r,jflC]AkVg
Y!+sJH4RKdPMZ/=S>qe;7,dMk-bS0a=Ie*sZ#3WNkbjt5E\IHSAb%::Zb%mhDWokj")*6!FH
N]AAao\XuVkne%dY]AmlQUa96D10uQGWAg3;Y\po#C6':D[(Gj!S@B/s+>0*;P,Z*Z%q6!j_oj
&HZ7[1E5k7#iaS'FV:i&EDj#ZG5J-7^Z?0rJC\X5:>HYS%=SH-ZfP?`-pnbT:mm=D1gl<1?1
VML+g[neeA]ALVc9?1fm+#>H</tH^>gWTpjY$!?DGRJ7@\)ZV=<gs3K>s6Z[q;bslmcDL<k9G
&/4nK4YqaM_T4uRjgH3.n>\)[2i=*LaY's*D,;1[\RMG6i@G%n%TZFk;.U4"RbVQ&Aq>JK1a
r_FRN8DlmUjF(S7(dGNqISg5$^U!/d_\0`,N*\j^Z?)uii#)Eu\2[@XB8RuMMtc?iUJB*1k>
<H\3Z=5e#Z@kO*Zb&b!SU?#DR]A$:r[i9^-p.]A;Q%A&!*U_N22n&Bh7@Y><@RBudE\0N#q<"4
=8%Ut"*nj$n.CD:+44UgC7HluR)_nSL^>:'Q[&O`oDopZ2a>]AdqaOJGn>'ri:Al]AMfVFRQph
lm(-,m,*)#dSg7d$N:F9Tj(@URiR^PGN:eF_/`=VMRU@k*Gu49U.Mm)*N)UbhN1DW4)@*HP:
/iKf%"1hRjU76!/C;X0T!7*4kbXaA!@spgs_R-DuRt?m7H\6,Y_gV-0H=dh^VWaF6O'%?ef/
9]AqEGEZgR7*@H'\VK^X`g-T'(rFF#5'>sDiq=ArgHI9k8PgdH]A?>]AAH#h*o[l`bN*55b6ToO
8Efa;2WgGGj$uq!*=k#@>_@+amSuMUtuN$EAG2Sj;hNoX<7lV!hQehob-7mI3'.8"h=:bB10
Rc&)2)0l3!>'(8t]A;tPuD-%jN(!i7F5d>*ZOl[7Zh6hO@/lC@GO-UX<oT$;hAH>Q_$J=M%b>
1:7+T.;BM^IKA]AeC`;UgnUJYnTFJV?!?6Ym>bIm-%0b%YhiE3)eiODg"-`5q&B`%NGGh<7pC
^iIYr9qk`CfPoPXYdC]Ao('\_s!oLjS*XnYqH$`qWJrXsX>6Hq@r;?-WfW2LGee^N0b-+3?T1
rfM\Zbc,RA15X!(W9[[36h!r=ds.,faeY#3]AS>'Cng,#]AQNmD>hfGtiq,ugd/3s(X<j+Z;5I
JBYB9;#SjmOXLYX9Dt.Am'D6-T'=2pX%c@Yo.$21cZ(;LCVL29Df]A%s`Lm)btP""_Hk*[*MX
Blqorf/U#6q_mZrlhPnft1H+$VT2(eYX:LLcoFgU]A?TE\i94&;Yi*1&Qo-?#,#Nj/VB<V=2E
dQ5<60RTQW'@6i[?VhoT,kMMH0CD40Es1I5*ne5]Ao$TP\3"T;+l`5%\!cM&Ibq[(6H_FgBAH
j;_0/O(c5V/nEnTA&j2i);A$E=GO+,8I*Rp"=IW3u;5`YLTaLdIZn*RRKO8L#JmeUO\RaALW
6do7K5&KW=4&)=8U-8o3Sg\Z\A,HgLl+"^Hi7uNEkGJ1@A>k!=9L4-'r8M/S>C.%D#esU'Dr
<L`&51%YQ8@\KNV2b$VkmbET"@u%%WQmCmh`mmTpBWNn\5"q_;>)N))^aF-S)AoU4(a;E]AeG
VR1cB^l+Yo9.$E(+X^S7Z`OAX0%n4')Am)B>#j\=W^cGUaV,;E_p5K^,EP1raS;!B6$Q*P>@
pUl]AZ"DZ.kDhUMS.kbDgkiZ>i'L%1SB*^,kn<Q25(2[V6[r&4hDf0&_o"]Ae9RN?D`g(e&fA%
<Pr4""E<,i7:HCK>lmOdVB`o$cSRQn@#*a-\fT/%[K<g/eGWp#6tZBDWY$GMc0,@f?t,Id=a
gg>-_>gdh?b^MXSb(dSce#HLY.SW(E+/S;QabhR!#c242>3i%gpqsSlleuS*T4d+@VdJMor&
uTFL;@B9:bHLR838-7@C0JJcO;%ZP;u"nj>nMf5Ic-RSa`sVLS'WrG/.)TA3oi(.NT(t9=hh
jE5QRFUn&hI@DqMb5t(G:OQmANR4L\jH8$Do&I&OH6RSW&:Q:_I[d$c@I):S1oSmKfl&)0^)
RNX!j3ss*5]A);$JLs)jjhhLCFO.mG$sPBm(q/5u6&2HVC2Jr0W+9U1c"%^08fP\oSa3X#p4k
uA)BQ7Yf0=j<_i&*2>0R`_VAKuq1!2ut/Ic&PA]A,$<X*:_G1^X_[@5O&8#W.]AkQVP%b`uk`0
egIKp9#>lk+r=N<6TDMD.(s[mF^4OOeL/5+'&6u>^`qN4]AkSA#q9Ls!Tb)T*%Yf2]Ah3#Zfd2
d+ddEA-eG5`Vo4%Q#aFcq+jVF7L1a5RK0[)t(C`CN!I+6p*#1ei9QPD`:\%+.-HC8]A`iW4Ma
eqr5k0f;4'>*FbL#k9B1(n"Z[G>T&rjl9D^aE?"gA.q`BHnYlUY\18>'PI^rAaS5dBK=:>9`
$pblCOhn3BApFHmIB82QFjdim@Lq`lpcV%'#psBC\'L)cAEj-a%%Js:%DB+W`MR`A"k;Y"d@
A=mj=:K*X,X)n'&O9q'FGror4\>2V0+aa/b2ZT/0gH,23_tK.Sl8A=WZX#'d>M?S0KTR<12.
GmVS'O.C.t]A/s$)0/[=YF2lEfd.2&LatIG"H=\/qWm%Oe&lt(ePY8q)`>O_]Ahaupr#dcID=+
r2tA7>^Y3?(hT6#K=_mo@[pMa^lndf/<;GC,Yt#enh=E`JG>=G+77YrI)=ib84s_#6nJ,u.k
7Mta'.D7pW9oJ6Wd1s*FVH1tKE>Rr%mk560or+_#L,NR#VY2kUU;4;GU<_cRQm`2P[F:W5CX
2"Hn4q=a9-:_R6(M787(5.Zps)_W3B=_\6]A;p^U]A\4:t\M_X8DF2W:.dG`#Ck`Z<RIHa79hZ
<t/th64=p^mKUS.^e_:%D[^/d[g=.;&9FH%o?ZBR/9@&gkVU)hCk0V?=YBqikm6PTj$7:M,.
!r4(aJ.cD,,5F%V0n\'I=j;c$`4@BEV#ocS0h1PD>?%(eahVf)")^iaoNa0ZK#Gn&r#MNs3'
PUAB9)Rs$+[=\nNLfe0=[geZ)p2!;4S1Ln*K=A3"cV:o1R?%3p&6+3hc"&D5;8.'k1^9QejV
@T7nM$@&6IoS3t<L]AqNdcYpr!'F%]Af6;\4cn_d?1Sh+qlLk(,[+`-3m8Ym#n:.K.a5QSl?'b
pnpu=E-%C<Ag.Q)P?AsHK[O0lc4bqIu.$#.Pe4<c20KVBVd`H`(t"<[=-<Up"u$;H/I"3XKU
lTG%VI2j&>O$]A]Aa?ho"E7o/[5A&-R"C*1*2G4!g>KZBYDAXd\eGe*tRKf7QZ20^XHrU*:+='
+W,RS_@?0gk$i_N)4t#FcfcFVYQ<&KZo@D3KEZB\i6;bi=ZD(ik@q,`p9]AbYAt8RFBiTjAMl
rEnnSo"R7#,3qgP=Di\Ne;tLcNL=96efi64_m6W/s^#@uWjLc="V7Z[2:q'4*'>lf3YY[O'.
Bb!6P=rk'9g?GmNR3bgP,9OnS7H?ZZB_>]Ad[CqEBti]A(CQS9D]AV-!*5H.5ca(YTC!UZ6r7VY
,hmcGY9a?;Ad-Y(_eY'Ji8'7lb\of^4j%m7=L<:/c*M4FDPddYtg3#)sM00,H!8I^kKUB#T)
Z[T0'MaKJr,#TPW]AWN!"9e\pYufs3u<VE3_C3I/7_3#m18KLVdR\HQ6no$GoJlC5nZK3qE-;
D'>JoL'MUVCb+eMZ-&j,XtNk9X3KNJ_"cU8F^MXsmp#QC$*Q,Y^6)$s3T(f2b?`[5FoTUu5Y
d#"Sk@2O%na+qHpkaqP!j<.aAe)r*gkJ?`MA2a7RFgTm"fE7SBmtj99'2a(?Sd63@K$O.V1H
d&O#:OUVQ&Ik%K%a8ZAP_Y[0+l^T*0K?;1\S,p6gs&Au&*'4T'b(^O[Zan=:@e@@!jqrEL%a
VpK?Yseu>CD7<A\u"eh?Z:KuKUhh)7VcN>F,^(EX<2/0Xr\o^/A<Df_`O.j(-)\c3R*Th.=1
8+keL%Y9G7*JX)cEbH9gulOJXJ(We5?:!9?pon">ki1tS!)JX2%`nO591]AlV2QeLN#14WipL
WMF'Cjr<]AS"c&hs]Ae)6gpN>/&7O>V-%eP=7.]A@MK.BX"d)BY!MB/;[AJpUOrR#7f=VKP!QZL
.6$I<LN)INX/ZXWrr%U1/FI@c=q%LV6%_Y40?L,$c[fQ]A)op'UQ70XVdRfo:P-Hn\@4kQdl#
%8o]A=*SmNr)j@r>?&KruR?1TZ0XYZs(?^D<a'TZ,&4p<1gGqSS\Ic_kmK?q=\iALE72\VrL?
2EKZ*`fduD!ON(PjkXSNMM3Y?[-NA4#;[4l?5n)pfj!OqP(cGHmsuB1KhO,+3D=hCYZ"Lb"W
@%Fh1EXHSae]ANN<*r'YVF?UsH+E;2n@Kjc1e&6qWrQn+hBq)?Gf?3H\h&i>O@MXjUibGu#h&
_,4I6CauiAk>n>S,$SQU5lK93Z=]At^V9r/m%&:hub3(01@"dKnef62(QUn;/(U=hmKb!k3$k
&79>cE/D*tf$3>6^BJe63L9[NNHaiE,*X"f[Yp*F4j,@1n$)qP-uFrNRNN"kO_'8XZ?[>Mna
dq?./AIh7+R?jjWOJO+J[@jZ\QUKa^MkrdX)GBuEV]Aud:GK=fY*T(M1pHW]Al;qPAZ>$:e<BM
Y[6bc'#7'q_B762au_LbH!5fd1lDn:s55b>QUq2rhufpo=!DRiVn,87+6$`98AE@hG$V]AfV'
6>)3$aC>nWiR!*9BJObbigCC^S<odQB*6&bK%P&)\G7fQ!*T5pk2.&2PqGc?&f!:R1>fca>4
(g\_Y\)SW#d<T#kd,@=k=EKmM0p+`ONK$`?rSAST(3`7q/aM&ug;1"JMA#To58OHF>1qeq$N
3'LnKbF&P3ugOVH*S--cpqjnC6dk>3Dc6k_.Ub>abNZrHf/\%io9S@0(7IELP?BJ]A1?JR*g.
5!lC'H+%pO.h.(V&eL@Q&[e<!"l[RCArt*C"R,*<U>kl4PT3*F&QX`$h$,%s/&YqW&KlT:=[
:INZ`DcIT:T-10"S':BUJ*XKO_*+4L0cL!$mt9cDtuiLKmQO50V]A/IeO,IcVPYa&9&i^_GR,
4ZWmm'V"3+tB@."<?/Z;X4guW@gMrONQncZYoG/G!j<\-aGF\P7-&g@[P6<QE7blOI4"YGWR
l;j[C]A8,Z6o/#:KQaRk(L\m#:KGY@#X:(Jl)p(:g=P.7C*=T]A:UnVr(/<kk&=.:8GnAktS4^
m;4@J0G"CbP,kbmNZIU#8P;aYB[V;FrYaSQ_[_*gal0P"`'sd5GB#rU#SM`V/LMGkmY4_Tfo
hpiOYPT6keE'0!n\h&ZBtk+aP';<p/J.lKerlaj5fC\I\e?K5@/FL,'b3N_MV^.KsnM0V`<C
=Ajf)!dWB>bj?,\q,:,c\rV1<6!tWgW`$-SueZ+%LH1idm@K6N8EHA_BRFt9B7`09r%ZYHGf
l5&WQUc]A]AaB1Kmu[:ZQ#JkB+X3Hi:pF5^da=2Er7hS7TGa_-Veq:A79i4WZIc$R5)3J0!FuQ
)]Af[Y;W4Q1>^Yc*fp;>s0`(OW8IqaiZ=Dp]A%a_7sK8?1FbOM=H:Ib1[+%HTPXOf[XXZ(,2E+
)5ED&)ZaP?C&fgN''$AN2if<YT"p4mW[6i>:i!:e@DLr)O6>:_40NEj0CeD,iNa-),_(HZ3G
s@;W"8DZ4/P3d(=A6;lQ3H3^%Zq0X[&XM,S[CLX3A[G8HM>=]Ar2(hZXHohUESL^s)C$'Xtqh
.:M8S!uBO,>"c.o4XcYP1=7U4a`%;(paF"&X4$$5bd=;]A\5dQ?(WLnD2'E+TSW88lA;,2_if
e#*J23LYI5U.9[)_1]AS[?`SNZ-a5u^D<:Q@c%hCi((W<7h30@d=loglA[YQ+&K)L^,9/M^rj
p@)UuNNnPOIq=S9GN5h`enihr:QK&S4C6pR+%q3-'k!h1jTi<OP14hQ16]A->8ebg<@T`1",k
%Ir)JZW=P^J4d<J_f![#>r)?L1$\4_W4J8\@78Nk3jPo+XJ<+:qg:n*Z8`M$tIsnia+/59#>
@>H)foWLFT*cs<qh>+(\X;-rj//">dr(NXDqmM+3Hpk8d*#H8a4cGD1OWg>&H32(OAGF7<m5
lB^k97+)17)FWfe\dujnbgSEj7Q([-."&?)X8o>eG!H&)J:#SZmoM'B68-^/<>i81mGDTlp1
mZ+mZtK7]A5]A<1E3Fj5HsS`AjT$NZ/=OHnp=@`O;M)nZDs9TS/4?\=SdbeoC$5L.B;[LN\7D\
@!lp>-h!EZC&;qgCQ5R9%dO$FgK8^=H5=]A!/t)ZcemWE9e'\X`B73(D'HWlka)Hr>iACi1)j
7YEnLhj\YZUP-fs7TQ5%$eF[oAI1:1\W=oh^P1Q)A33W1r;*k"F#<GaKYQA)FmhBe^Z8*,8k
bQ?>:=/SHCIoTV<+4HV*hi\j1U:ePTIT[&Ajocrr5KMV>bHkfGG_[eWjiT<W=-,ba!<2-&.K
Y*VV`BWEZqNZfh76EHKV/lr&^LH\)MNpmLjT?)n(aV_3O@I^O0`kkfl7Vo:\/_pI:6Y1%6I*
!qP]A3*gKNS=n\a3qB7B$7@8+hTJ5L(/bs87fnL9i/B]A83e0C5oIf1Z-QH%htr;#%Io)V!8fA
Ga1fCgIoQb>53e%0D3r$`Y(u*a,%o#%dN?U'1We0M&g8]Aj(U!ZO6/X2-FPUaI<DQn\pr0pHH
=^E9R7/W=Rea#Obu0-r$mDb7DS-T4L$oN,4S=^k6Of@'c"-0e2bu$YY\!4<`a4\^`!M!>M$o
@Coj^.5+/[SKt3rgNfG]A+F69*$^oo&l9"lnh\58tk7';P?6o=WSHPZ6l1U*$r_dOpk:!"<aP
/nCLT-?85FRFLj9F""Ch3o<6Mkl^j<s#?R)pG`8d8_@>+!rM4_#'VtO2WKLDc>q'KMq\8\QV
M]A0:UTDKo=*qU3F!S!iO():/&9IT%E6U(X+qAMcQ/$MN1,"eS1@4A5l0TmX1K#eY;17<%et,
4<XP_EF.ptPn\jOj#3i*JflTS\h/@U5;'?R:L[FMQXH2:4&r*'*8+XufeXa)#O)U=7XfY&JT
.Fp9_EMGekPtPHY.poM&pK"*/f;Mh1[dE.`6[G8^pK/7*uZGo@fd^[9]ApFW@\1j$ic9_?Tt>
?[r#n!hJ:dE[3kJ)Q<:5[IqGK95Lt:G/^rZ,[+WUVdVgSWqM6'Oar#Ru7J;"P_]Aqs?1U+!g'
bH?inMuoH(0ft`C>F(1oSf30RaFP6W]AD-!23WSq[mnmWeOlLS#XSlG[*8_G7B&@DD:GUIc/u
/($9sB%Ns5NBL-+4e<QhmRI!VsS2O2/s:Y^:PEL\6)8,^Sbj@Kq`]A2XX=lidauHBjf0RdTO4
LfFuY1bCm;TF@jb/aC(+N0UdYDn'1n*6gf:C_QXgqk5ZR*JUh9+-NW#L]Aja+QOFh6':'V?c.
.d_]A6djH*OR1]A2=D[D*9;W0if_;Y^cF-kkftE2Co+n:?b;/3M*i(@[!Z&eBpAdH<6$+ALqWt
D1!(*gYLN%&Bh!koAtB1?chHb`_W)`1-"ImB;mpJs_+G`rd+lWO[80uFQKY&!)b5OE+4efD0
"UiT1Z5L7[eRIMQ0TN;$3iRFY:RRsZaTmc%8#li\Om0q:%;`04)0,qMuQI+,7Qr,\BqT>ieZ
#>du8fkC-k*:)QDe/lYBNID>_2gE,b"3,*7&&$mjTqq9deKAk0"4<V_aQU'K8gEY8/(58@@2
'sGiH*6Z/r=%@(,:F5?Z`"8bJ!dEDWL0i8*qaJTCTXuNC23Z>\W-fef$F2/j28s<NVc\B_.W
6jp!1@Q/*RlLenskCnUrZ]A2b:M82e$1>?cB#qaH_MPtD6@Wfd-]A)lS*F^K07GJ.k`=H(oMC=
LD3rX*-DJP'_q*]A!CS\A9[]Ag2gQN*Oe,Po(,3\E)H2MGV<7o#&1q:!.pLLG>5Tm">[b',q>/
f$9)QcEp*o(fnV?s6?M&gsed+,U^GT=2V<W/BjLgR*T%<p6F0Pg;GJ@_ZF(gTYCYo7<O)Epp
B[E.IH783?p8lI-N,d7X"70-A]ACB*B;o4;S8:"lp5Zk:)s4p_7(N`'P,)R`b%ICLU+=A@G2(
0^gcKKP7YE;5l>@n]A<?TZc.0<F4.J9n>;rVWSP.%XJC$n.4q4YA4h>LPi*!k\tja#Y4[%*=f
"X1L[g\]AQ6]A?*W8!+'[3Pf4?@.c%M]ASGV/6Tm!7<H]A$?=7n[?*VL#@7[b,lB-$46ch!6lYaX
u'YPPkU!7OWc`$tmasWmB7+C`V51,m4&7t98^9j=VoAb]ACQAGu`ZIQ_`$,ig$gKHYh8mUF5d
8Uui8&cLS:'WUk'<^-.j1/W@"0lY*%Q[p@gloOj9_/(F-dM6l0PQ^Q;d7<lrG)(uBNp8OO5n
cHeRm]A[i\]A:d'P"GRmG\1u:O+NO;4)X3p5R"JdrlQF*`^<:BMS([30LLf-Tf(WfoMVr[A]AaT
fS0./Iq0UHV#Bl$[@"F=A-pLHbaQE?TtFZq:M'H.F1pJg\qJ1$.)i^2bBU]A:fnSBNDHKuo6X
fN]Ag@'0b8*Wk4WXdAg^I/\`jMd=IAOkqT(-d)<)t7e1@9Y[k[&ptu;4uF.g.\&h]A#/@Pc?<O
<7T%I/B<Qb>?7VFql.?J*Eqr7Tn1_mZA]AMY9rH2V6U@R[<1kbg:YRE+1Al7Rhc@*9fH-+a&R
^]A\pTcU0rXoH'&,nWdsWVRn=(!K'0QMsN'[V$uVgF$@Ia!Kr>pD\)gB.Uh=$Ykq]A5C]Ac92O`
S'&boNGg#b=0r9-to2ZR\QH;a2i?m![JjRHHpqAMojU0Q&GN`CPtI'uI"q(WO)]AcZC%o)dQL
0`\K,mcahh+,A6!$l,,=.*7hZ4<k%@7o1<A,-Di`En&D*G[-22/EU]A^_m&^epq4Df+7l1@J_
1!ufaJa`EOADsfh?cT4VcKTKpJ[DWS2&Hh4Nu+'sH%BehX;OoeiJL)mhFi,jTJ8lV>@^;BcX
nN-jRN?37\CO!Z23Nl%QZM0j!sEqBR(lF$'V'.ES>)0*8bECu2*aCR3,:+d:Y_d[%IFM^@o#
96X@-.!WfZ[YWAHaR-VUr3uGg::kFTI<ESO]AF)HjjQ=h3YotkjE*01J!]Ac:'%<+C\qBgb0P_
(_ZG>`JA(tO'V`;1?Z$?#31np=\bPJUrBjAk(46h`oZ19)oo<D\o>V=^Agu3X9'5X_:j`#ut
,:M(05Y%TMO9Z!UUr(CFeMOPu3$\;Y*+7SP/IZC*JAt0ZUO6[l5/t*$DF:R??gA3QKVtCMa6
+]A]A6Zho4T)96@K^$f4,qN.WMr1j6K(2+$7Kj838XUc;EJ':b!D5p$nj%ag4`dJ_CSYFbos*?
WP\F#kUHK<k'g?0Ek'HmZk#F2oS1^'=:qV6!JT//fgs<p3ikE*S4bh7W7(KZ?<#C4GUY=Wm2
s45NZG?E3pER0I&]AADBVH"r(p_&59_?PDH'7BBff#q[h]A#f>_OU!dp3ccj[i34Wj10jIQB`3
rb6qdoe.8?2!J_eArGoHN['5t0hP3E`f\&4=4+NJL6]Agg"F/LWiH*dq;W(&`XYqI<lJB(+Nu
cWX@XT:2EJ)npJb?#R`G/0+[5"3Wr_qY@<]Ae_abp?O`[U8YN,jdGUF]AR(>jjm%m&f/j.EN:s
e-WPEcZ\NiJ'm?.Wg7%RsngDg1#@ghY8PrT'"bWQN)ia\S#EQq,2ij&>fP>E[!\2g8jsRi+:
>bRtq<^IR[7[cK3IQA%8"#^@E.RuV2X9^.$X%rS?#_smB<kOu$=^^8g[2Dk3!lqgSkK88nW-
R,Z]A<o+?;_i]A\H;UReY(>kO2c-4DU[tlu&05?)ra2E:A:,%8VULP$-_aBo.L;q0"U^cd,,S=
E$=Jg2$KsS'r::C-kFG@E&^KN'6KDk^KU!bcfBijFd7aKSc]ATlKQ87UY#:oJhoW(@rf=N&^C
&@23Qk)MM+gj//Mc6SY'_%Y,3ohoYC+hc?+)HD+?&C-VKGbK0qBc?H+f'A\T0/>%nndV"lB!
Id,7Qe^?ZHmX/gNk8A*Q@AB@Ji"q`J51#1M=^a$A=XoOloS:*Gurd=@A&'hNO2iHLO+5_Z+,
on/j/<?Xt+^b;]ASC`M0T.of;X3JYJ`7:HL27%3RLtqiFZBS1&e"`r#kF68Ge.TER^;(YPer=
8iX*?^hPmO<m0os6cGP3GABs)%1Q<ci/:oC&Uo6d+h(a&o[T#h3O@tYhZ0!Cg'FYKkZ%GB98
Ohg\<:L+rl9:r%\eM%WT8[onIDdY(8^aIH9jrpXn(pn&!0Ur)j'c3gj[dQKa:K:`^K19>`Tc
'ggDe4hT]Aq!hEtRPY+3(lA,seL;uoXO^oPS"(BnUSZ#+i:45bs`#k!(UccJl39&9kN(WA)[T
sfNnL(4VlGUdGWHY^8`jq9jf;Ue[.pU_\dbqsQK<g*a=c\qA"Qjm!5dFUU*+S%K>.o[I$I?M
21Cn76=o:GfFY'h-V2B_.Pg37X?$B,gGs'n6<QcCk4ZW2B2EbCKSKcI'4Ipe7P^W91]A<qiG%
f[1UD"."uiQTq(Am<dOKj:'rXDqo%\CtZ/5F"/RDaBMYHukAtnnO!bR;5Y,7Ro,FdA*Dq$Z>
7o<H=P<q7.M;G9oF1PY[sKV5f;F;Dk]AdHXS-T@:(7ojsW#TU#aJSfh-EB.Rj4O@3r8jc1AgJ
,s=&IIV!0m/W)O;adhR-[24M?A7Gut]A#B8]AK1rlR"b*(GeZi/0VkSk(O`drDi]Aomd9W.30e4
gZ7XC\T=>U7WkO.DD[Ojeql9n_i1[+9j.5JfsYBbeC2HIY&m!9K\5)"-YtD#WX>G'!phVJ\T
<_PE8`kE>*=T@`:kO65:QoSpgD)=DJb(8SfU*_X8H]A7`Y*QD+!Zqe&n,U8<W=j!-XXYT,LE3
t+@gB=Dp$I?a4L]Ak0Y;P?qCp@Nms;P>toa`h/SpA&GH>n(1YEC/B0MdO!le.cQMGC[22k@87
.J*AKjXYqB:+>@H)3fW)O:;`$()&(a.<<E#=o)=KUr>u3o)i,<*TPeN/(ga[Ei!UXtZS9X#b
BEsn2iA<3P[D:raBqMjFW<`W*]AMjRf$lP)ZIRgMc5]AcQ(eOd*P;CCuM!EG=+<gA`*M4c$Qf#
AW4XCCNMS]ABZO9"98GGhUd>IXn1]AZ6^tl;/4B,n*Zj\.L,8(25:g$0;&HhOsiEWok&ni3Ogk
J'K+b<(&Mn$PcA4A]A9U4OF@>SI+q2pkU1ON,KICqb#*q0"2[]Ae=<RffD)cD=8S<-LtOnqIWo
.RtS,'gAfE?o4FV1'.$Z,[@fe.cuRT>&>LAN&7(e`8I,Se4,'Ej[tOEAuRj)Aa,G=#\b+^iV
-"#r5g<-B-+:6+Y,2\g)eE#A;K7<_#ia'"@Z\Xmo7Y*%FALM>^3%3aTWs&hL85>6ad1k4=]A@
U@D;R,uF_-F3GMJMdCH7[VNej+'eNq[,.Ppl_g8%^fX_PU"A>t3mA"e!^2tEJ&G\aS]Aq2Wn/
_-?m_sGsJ"Aa]ANUM-#q\T]A0MHsD4,?mD4DQ$5tIT"XKQ1JmaWDE;j*n"2^ZCHD)J!Bus;DIh
(g&Au:J^;U*aV</tMg156-9%rMMoq;FgODi^a8/E'oun"HQodV=VtqUMqkNf/`^Ta2;-;-jW
_e#$oP^X.m1EXEF?/(O"Rmp@?gV0%I<7Z4ogGNKddWAFTQnlAPPUq"2S#2H77E06=/;n,+DR
@a&AR)"X^p+eHMQ#oleH$D/=')-arEelPjBPGIh[%K-V-1Rm%dt:ek;+dA+a!"PkEjaXPH9^
72[FW@4eti_4\jDdJ@TsHW8FTi(,69*Esnr=9IZG'_bpQZjeXE3l4VY&BnK\dm_f#8VQc(>!
7YO'Y-'2&Z8L4Ss`(m>r8iiBd`H^OPahigIEn^]A+qHgLhF$W%c;DJTmd+!jr\>rgc_\P)pm1
U_iI8om6gN@;/5ge?&[poR9>Cmnk*_,AY.sp\\n;4,tBV;TM?sbgXXSDq,jP]AT8f6*U9\@Q7
P<[&)7#dQ7Z@!tL)5P_EtFm8,!50h-rGf\rP2<f.)9T_Osd<Ra>O5k4*cjcOLr]AYiM+ZV[F'
X*d@O0`LnbL8ReZM_1&F`u%jP:#dMbI2XZkfiOOOiN9kdH,85Bje95Zeo]A+L;XEitb?Fk*%[
3&cl_pBW2'a''XhQZD4:VTAT!V+W"o0'#7j#FBZgg)4IV(G%1YHpV8$oSpf.[94n.L9`V>D?
%*S9DNjr[!^?oCMns-idd&C[Md`a5A/`Go=p/_eX[Zj=`O0#%De56F)QK72#m?2nafli:MLn
OrLGsJ:%^*7#/AGtcGU#sGAU*"H%/(`?M\k8[),L\)#h)^cLUNY3;QY[QL#7UpBIisEUF[=!
K;G4fhdh$lhmZpfJNOs_e.6($%<hE>An%fD/IOCZD[G2XPlC4m%QmOrAIG5W`LW@b.dT\B$*
;u%5`_>Qt1PCaII=1T3V4s83rLa^ccnPoqY*'pD]ApaEDa_=r''Q-QKt^MpFeS[G29k;7T[lA
:OI.umr&2*nfP1<l"St$8Dr9ViD,`eNu=8[p[:V*kFUG1K7B!*E;OLhYOfH:LnJu<&?VPBAl
aIhZDI2@Do#)rr1=E'^*qj^e:7sD*P3t?qsS$S=)V>bZ$W=D#&;Y_f%qGh*_fG3JVLu5Rk:W
1]A/IPu5Q^JT-an5m]A1N?BXYY.)e=?FP^c7SJbU4aY)?4)\o0q.Ob]AYWp!0Q/`M:Se(\U%?@*
btg&C6ZTClW^sImQ^bD&*e'7f^k^EXT!^+QbW4F^AM]AZp#fE$q[p$?e,YIh2_q,2l8R2m7JQ
-^e+cKTq(BIh9u8l$GdRhY\Q@:_9#Q=]A]ADigV,P>E6oK!!O$Nf7Q[T;:5TSW!BgVjLT@I@&s
br's<qW#GDfsC!/PZs]A0m72*/q=tu58^RJa#o]A9?UTZgXX@`7!kl7iJp;\>:9)t7dNEoX&RE
cJ=&`t"KaSc]AM.j/&'_hCm^s(@;`ZCSrZ9r?%."Yjl/rB1cW3O5CFeWq,P;$Xbf>$K[JX'tF
C9E7DGh=A&NVi<*$4O>@GKEp<8=?sO['_emhn@;gP[ueY%8W*UL(]AKfn;gn_AlT]AOk!8WjqM
Vqs,RguRrI)QI"+`B@;Q'N>e;&NF2Hr,Lli>N$,:Hrn-1LFLre0S4rF9R!/s!r4*U=7*(m9`
\[?H]AS2]AE++)^>]AFf>=8(I9u!"t:NdM)?>6Bi)RX"V+s<BACJH@g#2!e_om=0kBPAq#EXH3c
T7GRb!*C'+;BEQE-aF']A8305Qg@@FDq\qdj>6-6=[L/[jquIT,q)s8TY^XC`TP%F.-G!]AHa&
@L#d`bhicHEAjr^61:.;IF.-$KK`h"c<=]AP1*Pq("$S:nnZYkC-`(p!$#AD&fK=4Srfj^[d8
@^C)aCcGk0N,60h(S)DRQ#S9:.G4jF"#RW2V#1aVd?tI5[%>ga&'G(R_QbP+5q7:tK0.@u41
2d-tl!rm,(KoB0/U\gQ!X(X`@ri3@Zjp;Qs"\"t+9O.1RsPC0!=CSP>NRfY[BDb'r@@Sdj=W
uIZm@=-,.2TJdHeUCY6g0=67>#.B[>mt'eT)b)e5f*h>p5VMEuc2P%Q+]AiNkci=HDc=.fJIP
nF6e:*:8pi\dfT&RZG(3J2X:gbsD6a#HHN/mPZCsP\s$^=0pi=$U:X)Gh2E8Q5XEU'/B5MGN
jl'XPBBUTM_u)V*:t\8RDT3+9s+'O.&GY_d5NRqD&0=$)Rgt1QhC85mCBZT5-X(Nf*k:W0eL
"'*'hI@qXh2*`Zt6Z,#gePOP4p$.9W'$'Jb$Fm,+*OT)5XR/>PV(9fDjA;g?NJG:3]A',sA^!
mmB&T-r3!l`>V]A\,>`D5jgW(+)6Prd9nNP1tZ\j4V0'_r86VKrONgB\ek5sp0rT!D3J`&Y*s
#0W3E`k5aMLfOnpT6(J$C.J1Uf-8#]A:g&KF%piL8"CmU<:t_^h>tE0`^!DWHrL5VkcHd76Vu
+ZDrrQT_rX8-DpqY6ULao[1l#9F"Z"1FN9Z6r?4EW0;q;Rn_D=T_ZAS=N%9W8UqGI6MinQld
p@5YPoQNSKZ(m`5Eg=&fCiECs<6('/E<Un.%q2]A7=4"kc8)NVYNs%'8,$D9?m!]AJ3%;)/_AG
6lYC)t1Z$3Q#7l?/OS'dFX4#W$9ch<_IY*#O.a["H$-l9:?dJ\aqCUkPIVR#CM,jTu?"hh+(
./s3ji9"l"09Hn5l%=;d[YOkJ69G@]A,\kT!C.lV+D^`4^S'Y$PkSuMqJDns?\T]A?2;lZY7C/
ol"u,USn_7FM:nn<]A_7@8SapV;*41<*)]A[B[[mP"Pp%R)Iq"%Br*$Rao8L(_TD^h(!H#4_VA
;JeS9MN@#8lg%(EoZ`lIO03:Y3g^AXlT1@u-;F3'`]AF9k(iK%]A]A1-hZel`*dn[BCMdtJt`!m
Ql7<=`Va?[lSFQ(Mmo]A?X-#,i@Co'`mDhp3uK,AM2tX+5.,*!r<X$[^eF[^r9(_Ej/b+^9+=
4DZT.(SZa#Y\DSrh?9&d)55gk&1qW,UF=)#kbjMKO$1KK4E<No+!S-gbM#:>.#TW!0i;dLn.
pBrQ&'=X;_4gU116Fb(Yk#fKE;)N"q=E7q]A?UCLn&b9gNR6]AlD*<CtT0c?LR_*Bj;ZULj/Za
ms$de4o^=OC,U8<qqFKnnO,+r'LU0$+/J)Qkkp!ktk_tPHB[Up5''\i\&]A-[SA-f8<42M'!O
3r&6K7L6n+7KM3_O5R0Dqg-9U^S&a?24j]A1NmR<FQ6-iM$nr^;j3P`Um<?r-&jGOa)H[[(qQ
`'E*Pa3h#<QgL!5Q(tF;Q9TCcdqmi)M_81QL*`4Hp)MX?'('`+KNiI;<`+JE^54:&O\gh9^q
=nd;tXH"\<F_ZU+;>F2a#T.0\I3-<'RL[jh%Z5X[pV=?A!+rIJ_[JHf,(;bgnEE/)Te#ceTA
GNjYO()qO+9rN7gU;MP/b1uZ]AAL/WZ]A.2s3qr7q4g\64SWp/ocIBY+!?XtLkkBO-ehC^;rs1
N\pqClG+ebm>lY5M:;^8i>\NoC]A%.R*a"L'\&S(pD;M<XkPM':`AD6MqK&f?MRBY.kA:O(l0
%r30Pk;PS#D?VesU91Nf*F<p'NjT=i[p#DGdRebphd^1>TaUE&13[ImP?2gj$,jG)PXM?T+C
X]A-W;%$+?V[,l47gj1,/`^%%HhITmQ$jS)uNVm'N^dJ4]A-eKl,Q0A1de+f*Sh*__!O=9CYSP
[4K3;jS%:D"KEI>Mh/t.W)TR_3Qh4'=&/]A5!I,HYZiI.\K/`9C7Y4=4LVFs,`P?F<JIG7k(!
#FbdSnoJ(#\YfN$PH5BoF>a2f+'sRYmo$_`j!Ft!_[h&U@&^t8q20V@]As)8H^jm9fA6-",T;
ND5WZlK9ZOY3JA_$jP=`s9B(WfhX8!;KT>]Aig5Ye-Smelpj1eXk)Yg$OML%rPeF4Irt/5%+J
V+aPGnh=@3kFOK$HG=Bn`&)9M?M:lE6)aA9NNNguLJ,PISnJh9q4fdGr%f1E"t3`$)r&"*"P
%RH[sFoD09#,Q?O)L.@p=VCO\T`s!p6RS1&FG9]A"=A4#6:7Bo]AJ5"<LAXWs&s5e&e^nqCkZm
ESj7DAhlSb_M4jD-?\N.On5M6!Y?3LX@Lf'U`2drdc*.A[aq/A.8n)f95I-qE5e0*JFaiU)D
a$d'"eEG1"+XEkkL>:)WkX;'#aMBVO4u<H'r(cI(?-Y&GO=c&5V*'@WFq*20E<FtQ^[AhmHq
*]A[o[($/H@5\o+4(V1e'!2Un%OR-EM?F%6V+g!XfO<o=[0T"+\j?61Lh%%JXsB+KMfqqaMcO
RTr+j`";V`8#,QP<gNe=-G$Nb!)ihsV8dTXN=M^]AB@>Y$]A]Af>WKo;OMHG-E0s6j<kce9Y15W
&(+J-SPNRo#U9'B8Xr/ML8bMfI^%!8%.V,h4=0GMmgH^5gH`IiVBi$,X;G,shS^,>0ht"Ipn
XfOCC<?R>c2l`&]A-ePM!P:@_As<rrZanJI\@B`@<knGcGDP:RXm"BL"E59(`k;kHs/+H;qY$
:,/5*`rEFs1pi]Ae(5TA:d[JUer9Ybkc7l&VJ,#tJIGD-qsMF42q\:,'4G/HfIH8'?);2mP#M
mJUJV'1EoE<"4Dka;6T+t]A3r[hbE>U&E*bUGZ`.DiWJ9n?8gNXE>T96Xc!+9!pD@9<a/HF@o
1tNb^5A@Q%gCB&"3GK(1'K&OM",^lXk)VV=1W9?@:jN\_"H5,;j)+hq<D@/7>,$&8qelF$0U
1L%C'F>"?_qBaW>$oeNtTkqWbd1dZ)RtGZ3[4f9b%X."![e&dQ8$/1amlD%IA]AmBL*B;>bkb
I6/l#J7f3m)9?i7Z)$?,*9U]Agf<$A-m>c]A=^#R+DGf&1]ANs()ol\p9G2Rjnn\/=4Z\pLTgQq
0<W<hgaYc!<~
]]></IM>
<ElementCaseMobileAttrProvider horizontal="1" vertical="0" zoom="true" refresh="false" isUseHTML="false" isMobileCanvasSize="false" appearRefresh="false" allowFullScreen="false"/>
</InnerWidget>
<BoundsAttr x="631" y="36" width="731" height="114"/>
</Widget>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.ui.Label">
<WidgetName name="Title_report0"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<widgetValue>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[='  '+'其他指標']]></Attributes>
</O>
</widgetValue>
<LabelAttr verticalcenter="true" textalign="2" autoline="true"/>
<FRFont name="Agency FB" style="0" size="96" foreground="-11976882"/>
<Background name="ColorBackground" color="-1"/>
<border style="1" color="-1777440"/>
</InnerWidget>
<BoundsAttr x="0" y="0" width="731" height="36"/>
</Widget>
<title class="com.fr.form.ui.Label">
<WidgetName name="Title_report0"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<widgetValue>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[='  '+'其他指标']]></Attributes>
</O>
</widgetValue>
<LabelAttr verticalcenter="true" textalign="2" autoline="true"/>
<FRFont name="Al Bayan" style="0" size="128" foreground="-11976882"/>
<border style="1" color="-3355444"/>
</title>
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
<ElementCaseMobileAttrProvider horizontal="1" vertical="0" zoom="true" refresh="false" isUseHTML="false" isMobileCanvasSize="false" appearRefresh="false" allowFullScreen="false"/>
</body>
</InnerWidget>
<BoundsAttr x="634" y="588" width="715" height="164"/>
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
<border style="1" color="-1777440" borderRadius="0" type="1" borderStyle="0"/>
<WidgetTitle>
<O>
<![CDATA[=\' \'+\'全國XX商場分佈（點關聯）\']]></O>
<FRFont name="Agency FB" style="0" size="112" foreground="-14898964"/>
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
<newColor borderColor="-3355444"/>
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
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-6908266"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="0.75"/>
</AttrAlpha>
</GI>
<O>
<![CDATA[]]></O>
<TextAttr>
<Attr alignText="0">
<FRFont name="微软雅黑" style="0" size="128" foreground="-13421773"/>
</Attr>
</TextAttr>
<TitleVisible value="false" position="0"/>
</Title>
<Attr4VanChart useHtml="false" floating="false" x="0.0" y="0.0" limitSize="false" maxHeight="15.0"/>
</Title4VanChart>
<Plot class="com.fr.plugin.chart.map.VanChartMapPlot">
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
<Attr alignText="0"/>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="true"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipMapValueFormat">
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
</areaTooltip>
<pointTooltip class="com.fr.plugin.chart.base.AttrTooltip">
<AttrTooltip>
<Attr enable="true" duration="4" followMouse="false" showMutiSeries="true" isCustom="false"/>
<TextAttr>
<Attr alignText="0"/>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="true"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipMapValueFormat">
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
</pointTooltip>
<lineTooltip class="com.fr.plugin.chart.base.AttrTooltip">
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
</AttrTooltipValueFormat>
</value>
<percent class="com.fr.plugin.chart.base.format.AttrTooltipPercentFormat">
<AttrTooltipPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat">
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
</lineTooltip>
</AttrMapTooltip>
</Attr>
<Attr class="com.fr.plugin.chart.base.AttrMarkerAlpha">
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</Attr>
<Attr class="com.fr.plugin.chart.map.attr.AttrMapLabel">
<AttrMapLabel>
<areaLabel class="com.fr.plugin.chart.base.AttrLabel">
<AttrLabel>
<labelAttr enable="false"/>
<labelDetail class="com.fr.plugin.chart.base.AttrLabelDetail">
<Attr showLine="false" autoAdjust="false" position="5" isCustom="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name=".SF NS Text" style="0" size="72"/>
</Attr>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="true"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipMapValueFormat">
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
</labelDetail>
</AttrLabel>
</areaLabel>
<pointLabel class="com.fr.plugin.chart.base.AttrLabel">
<AttrLabel>
<labelAttr enable="false"/>
<labelDetail class="com.fr.plugin.chart.base.AttrLabelDetail">
<Attr showLine="false" autoAdjust="false" position="5" isCustom="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name=".SF NS Text" style="0" size="72"/>
</Attr>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="true"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipMapValueFormat">
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
</labelDetail>
</AttrLabel>
</pointLabel>
</AttrMapLabel>
</Attr>
<Attr class="com.fr.plugin.chart.base.AttrBorderWithAlpha">
<AttrBorder>
<Attr lineStyle="1" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-1"/>
</AttrBorder>
<AlphaAttr alpha="1.0"/>
</Attr>
<Attr class="com.fr.plugin.chart.base.AttrEffect">
<AttrEffect>
<attr enabled="false" period="3.2"/>
</AttrEffect>
</Attr>
<Attr class="com.fr.plugin.chart.base.VanChartAttrMarker">
<VanAttrMarker>
<Attr isCommon="true" markerType="RoundFilledMarker" radius="7.0" width="30.0" height="30.0"/>
<Background name="NullBackground"/>
</VanAttrMarker>
</Attr>
<Attr class="com.fr.plugin.chart.map.line.condition.AttrCurve">
<AttrCurve>
<attr lineWidth="0.5" bending="30.0" alpha="100.0"/>
</AttrCurve>
</Attr>
<Attr class="com.fr.plugin.chart.map.line.condition.AttrLineEffect">
<AttrEffect>
<attr enabled="true" period="2.0"/>
<lineEffectAttr animationType="default"/>
<marker>
<VanAttrMarker>
<Attr isCommon="false" markerType="NullMarker" radius="4.5" width="30.0" height="30.0"/>
<Background name="ImageBackground" layout="2"/>
</VanAttrMarker>
</marker>
</AttrEffect>
</Attr>
<Attr class="com.fr.plugin.chart.base.AttrLabel">
<AttrLabel>
<labelAttr enable="false"/>
<labelDetail class="com.fr.plugin.chart.base.AttrLabelDetail">
<Attr showLine="false" autoAdjust="false" position="5" isCustom="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name=".SF NS Text" style="0" size="72"/>
</Attr>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="true"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipMapValueFormat">
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
</labelDetail>
</AttrLabel>
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
<Attr shadow="true"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="2"/>
<newColor borderColor="-3355444"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<Attr position="4" visible="false"/>
<FRFont name="Al Bayan" style="0" size="88" foreground="-10066330"/>
</Legend>
<Attr4VanChart floating="false" x="0.0" y="0.0" limitSize="false" maxHeight="15.0" isHighlight="false"/>
<Attr4VanChartScatter>
<Type rangeLegendType="1"/>
<GradualLegend>
<GradualIntervalConfig>
<IntervalConfigAttr subColor="-14374913" divStage="4.0"/>
<ValueRange IsCustomMin="false" IsCustomMax="false"/>
<ColorDistList>
<ColorDist color="-10516265" dist="0.0"/>
<ColorDist color="-5648906" dist="0.23287672"/>
<ColorDist color="-8986402" dist="0.49315068"/>
<ColorDist color="-9261068" dist="0.75342464"/>
<ColorDist color="-6514959" dist="1.0"/>
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
<OColor colvalue="-5648906"/>
<OColor colvalue="-9261068"/>
<OColor colvalue="-8986402"/>
<OColor colvalue="-6514959"/>
<OColor colvalue="-10516265"/>
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
<VanChartMapPlotAttr mapType="custom" geourl="assets/map/geographic/world/中國.json" zoomlevel="4" mapmarkertype="1" nullvaluecolor="-2364935"/>
<pointHotHyperLink>
<NameJavaScriptGroup>
<NameJavaScript name="当前表单对象1">
<JavaScript class="com.fr.form.main.FormHyperlink">
<JavaScript class="com.fr.form.main.FormHyperlink">
<Parameters>
<Parameter>
<Attributes name="Pproj"/>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=AREA_NAME]]></Attributes>
</O>
</Parameter>
</Parameters>
<TargetFrame>
<![CDATA[_blank]]></TargetFrame>
<Features/>
<realateName realateValue="chart3" animateType="none"/>
<linkType type="0"/>
</JavaScript>
</JavaScript>
</NameJavaScript>
<NameJavaScript name="当前表单对象2">
<JavaScript class="com.fr.form.main.FormHyperlink">
<JavaScript class="com.fr.form.main.FormHyperlink">
<Parameters>
<Parameter>
<Attributes name="Pproj"/>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=AREA_NAME]]></Attributes>
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
<NameJavaScript name="当前表单对象3">
<JavaScript class="com.fr.form.main.FormHyperlink">
<JavaScript class="com.fr.form.main.FormHyperlink">
<Parameters>
<Parameter>
<Attributes name="Pproj"/>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=AREA_NAME]]></Attributes>
</O>
</Parameter>
</Parameters>
<TargetFrame>
<![CDATA[_blank]]></TargetFrame>
<Features/>
<realateName realateValue="chart5" animateType="none"/>
<linkType type="0"/>
</JavaScript>
</JavaScript>
</NameJavaScript>
<NameJavaScript name="当前表单对象4">
<JavaScript class="com.fr.form.main.FormHyperlink">
<JavaScript class="com.fr.form.main.FormHyperlink">
<Parameters>
<Parameter>
<Attributes name="Pproj"/>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=AREA_NAME]]></Attributes>
</O>
</Parameter>
</Parameters>
<TargetFrame>
<![CDATA[_blank]]></TargetFrame>
<Features/>
<realateName realateValue="report1" animateType="none"/>
<linkType type="1"/>
</JavaScript>
</JavaScript>
</NameJavaScript>
<NameJavaScript name="当前表单对象6">
<JavaScript class="com.fr.form.main.FormHyperlink">
<JavaScript class="com.fr.form.main.FormHyperlink">
<Parameters>
<Parameter>
<Attributes name="Pproj"/>
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
<NameJavaScript name="当前表单对象8">
<JavaScript class="com.fr.form.main.FormHyperlink">
<JavaScript class="com.fr.form.main.FormHyperlink">
<Parameters>
<Parameter>
<Attributes name="Pproj"/>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=AREA_NAME]]></Attributes>
</O>
</Parameter>
</Parameters>
<TargetFrame>
<![CDATA[_blank]]></TargetFrame>
<Features/>
<realateName realateValue="chart2" animateType="none"/>
<linkType type="0"/>
</JavaScript>
</JavaScript>
</NameJavaScript>
</NameJavaScriptGroup>
</pointHotHyperLink>
<lineMapDataProcessor>
<DataProcessor class="com.fr.base.chart.chartdata.model.NormalDataModel"/>
</lineMapDataProcessor>
<GisLayer>
<Attr gislayer="null" layerName="無"/>
</GisLayer>
<ViewCenter auto="false" longitude="104.1876411438" latitude="35.1390021472"/>
<pointConditionCollection>
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
<Background name="ColorBackground" color="-7293"/>
<Attr shadow="false"/>
</AttrBackground>
</Attr>
</AttrList>
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[0]]></CNUMBER>
<CNAME>
<![CDATA[值]]></CNAME>
<Compare op="2">
<O t="I">
<![CDATA[0]]></O>
</Compare>
</Condition>
</ConditionAttr>
</List>
</ConditionAttrList>
</ConditionCollection>
</pointConditionCollection>
<lineConditionCollection>
<ConditionCollection>
<DefaultAttr class="com.fr.chart.chartglyph.ConditionAttr">
<ConditionAttr name=""/>
</DefaultAttr>
</ConditionCollection>
</lineConditionCollection>
</Plot>
<ChartDefinition>
<VanMapDefinition>
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<areaDefinition class="com.fr.plugin.chart.map.data.VanMapMoreNameCDDefinition">
<MoreNameCDDefinition>
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<TableData class="com.fr.data.impl.NameTableData">
<Name>
<![CDATA[map]]></Name>
</TableData>
<CategoryName value="province"/>
<ChartSummaryColumn name="a" function="com.fr.data.util.function.SumFunction" customName="a"/>
</MoreNameCDDefinition>
<attr longitude="" latitude="" endLongitude="" endLatitude="" useAreaName="true" endAreaName=""/>
</areaDefinition>
<pointDefinition class="com.fr.plugin.chart.map.data.VanMapMoreNameCDDefinition">
<MoreNameCDDefinition>
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<TableData class="com.fr.data.impl.NameTableData">
<Name>
<![CDATA[map]]></Name>
</TableData>
<CategoryName value="Project"/>
<ChartSummaryColumn name="a" function="com.fr.data.util.function.NoneFunction" customName="a"/>
</MoreNameCDDefinition>
<attr longitude="Lng" latitude="Lat" endLongitude="" endLatitude="" useAreaName="false" endAreaName=""/>
</pointDefinition>
<lineDefinition class="com.fr.plugin.chart.map.data.VanMapMoreNameCDDefinition">
<MoreNameCDDefinition>
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
</MoreNameCDDefinition>
<attr longitude="" latitude="" endLongitude="" endLatitude="" useAreaName="true" endAreaName=""/>
</lineDefinition>
</VanMapDefinition>
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
<attr moreLabel="false" autoTooltip="true"/>
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
</AttrTooltipValueFormat>
</value>
<percent class="com.fr.plugin.chart.base.format.AttrTooltipPercentFormat">
<AttrTooltipPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat">
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
<BoundsAttr x="0" y="36" width="631" height="579"/>
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
<![CDATA[=' '+'全國XX商場分佈（點關聯）']]></Attributes>
</O>
</widgetValue>
<LabelAttr verticalcenter="true" textalign="2" autoline="true"/>
<FRFont name="Agency FB" style="0" size="112" foreground="-14898964"/>
<Background name="ColorBackground" color="-1"/>
<border style="1" color="-1777440"/>
</InnerWidget>
<BoundsAttr x="0" y="0" width="631" height="36"/>
</Widget>
<title class="com.fr.form.ui.Label">
<WidgetName name="Title_chart0"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<widgetValue>
<O>
<![CDATA[全国XX商场分布（联动）]]></O>
</widgetValue>
<LabelAttr verticalcenter="true" textalign="0" autoline="true"/>
<FRFont name="Al Bayan" style="0" size="128"/>
<Background name="ColorBackground" color="-1381654"/>
<border style="1" color="-1"/>
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
<Chart name="默认" chartClass="com.fr.plugin.chart.vanchart.VanChart">
<Chart class="com.fr.plugin.chart.vanchart.VanChart">
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="1" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-3355444"/>
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
<Attr shadow="false"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-6908266"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="0.75"/>
</AttrAlpha>
</GI>
<O>
<![CDATA[]]></O>
<TextAttr>
<Attr alignText="0">
<FRFont name="Microsoft YaHei" style="0" size="128" foreground="-13421773"/>
</Attr>
</TextAttr>
<TitleVisible value="false" position="0"/>
</Title>
<Attr4VanChart useHtml="false" floating="false" x="0.0" y="0.0" limitSize="false" maxHeight="15.0"/>
</Title4VanChart>
<Plot class="com.fr.plugin.chart.map.VanChartMapPlot">
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
<Attr class="com.fr.plugin.chart.base.AttrBorderWithAlpha">
<AttrBorder>
<Attr lineStyle="1" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-1"/>
</AttrBorder>
<AlphaAttr alpha="1.0"/>
</Attr>
<Attr class="com.fr.chart.base.AttrAlpha">
<AttrAlpha>
<Attr alpha="0.75"/>
</AttrAlpha>
</Attr>
<Attr class="com.fr.plugin.chart.map.attr.AttrMapLabel">
<AttrMapLabel>
<areaLabel class="com.fr.plugin.chart.base.AttrLabel">
<AttrLabel>
<labelAttr enable="false"/>
<labelDetail class="com.fr.plugin.chart.base.AttrLabelDetail">
<Attr showLine="false" autoAdjust="false" position="5" isCustom="false"/>
<TextAttr>
<Attr alignText="0"/>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="true"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipMapValueFormat">
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
</labelDetail>
</AttrLabel>
</areaLabel>
<pointLabel class="com.fr.plugin.chart.base.AttrLabel">
<AttrLabel>
<labelAttr enable="false"/>
<labelDetail class="com.fr.plugin.chart.base.AttrLabelDetail">
<Attr showLine="false" autoAdjust="false" position="5" isCustom="false"/>
<TextAttr>
<Attr alignText="0"/>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="true"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipMapValueFormat">
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
</labelDetail>
</AttrLabel>
</pointLabel>
</AttrMapLabel>
</Attr>
<Attr class="com.fr.plugin.chart.map.attr.AttrMapTooltip">
<AttrMapTooltip>
<areaTooltip class="com.fr.plugin.chart.base.AttrTooltip">
<AttrTooltip>
<Attr enable="true" duration="4" followMouse="false" showMutiSeries="true" isCustom="false"/>
<TextAttr>
<Attr alignText="0"/>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="true"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipMapValueFormat">
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
</areaTooltip>
<pointTooltip class="com.fr.plugin.chart.base.AttrTooltip">
<AttrTooltip>
<Attr enable="true" duration="4" followMouse="false" showMutiSeries="true" isCustom="false"/>
<TextAttr>
<Attr alignText="0"/>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="true"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipMapValueFormat">
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
</pointTooltip>
<lineTooltip class="com.fr.plugin.chart.base.AttrTooltip">
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
</AttrTooltipValueFormat>
</value>
<percent class="com.fr.plugin.chart.base.format.AttrTooltipPercentFormat">
<AttrTooltipPercentFormat>
<Attr enable="false"/>
<Format class="com.fr.base.CoreDecimalFormat">
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
</lineTooltip>
</AttrMapTooltip>
</Attr>
<Attr class="com.fr.plugin.chart.base.AttrLabel">
<AttrLabel>
<labelAttr enable="false"/>
<labelDetail class="com.fr.plugin.chart.base.AttrLabelDetail">
<Attr showLine="false" autoAdjust="false" position="5" isCustom="false"/>
<TextAttr>
<Attr alignText="0"/>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="true"/>
<value class="com.fr.plugin.chart.base.format.AttrTooltipMapValueFormat">
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
</labelDetail>
</AttrLabel>
</Attr>
<Attr class="com.fr.plugin.chart.base.VanChartAttrMarker">
<VanAttrMarker>
<Attr isCommon="false" markerType="NullMarker" radius="4.5" width="26.0" height="42.0"/>
<Background name="ImageBackground" layout="2">
<FineImage fm="png">
<IM>
<![CDATA[!V$='qMA$D7h#eD$31&+%7s)Y;?-[s)#sX:.0p+X!!'fuK$F>r"h7,l5u`*![8q'ZP>rI&r\
2a<?c5?"N!?%$Y[056)e7)tlo#+e#*aq[7&('oD@FN;%(9Ij)d=1!N3sZH.ft@=O9o2o@)uW
_Y'6920Eaa"G_m#S.0F"^hfC,e?1.p2jN5M(kC&ucH,"Fr52N#6A\:DR;;%g<ebslPes;;=r
YF5rM<;gJP\R==b-^jH\[MN.RDq_\3dW!UrmW?"o]A99RcZ5"n4%,8JOf[kn>,phjP%ee-hV!
?dXJj$.+7'r?O1MLun_sJJoWHkAMO$p0&1:I^298E]A7'*]A>OK#?W3.>e,O-)*'>bRle5:t[X
UO88l[HM*?o?/^l6G-"Jk=>2"73o:S$An'CR%i]AZIHGXt(!8I]A8J)2`6[V2c`P7P]AnLTMFJq
`;5D\j:HC&-Tt.PUZHceqM7LdrLmXebZk;0gECl/<hUHEF_P"(TM+="/'SLN4U>j/=N[4Nl?
K*TQq/%M9<)**FGg4*LAs0(/BLI$EIL#m"9`lPa2,&VCjIN),F%5%<Sq]A`IZCSkkbFRd.h4i
XJ&%`U+.=]A_`&L^!dVrN*uhLlN_*pWgCX]A4fhX?St`&n0.enKc2f#3_9YcT4IdSLF>Nu1$[-
b]A:h]AJ7enACW;,[-JkkeSnl2H<joYYTsdPe.]ANIu&0aWHfV54F/r2n/'[fn(f(!N==_FU%q;
905/#Ru`cpr&'B(=C!j6;uJ#s?$KA5o>(Z<n8jj73gQg2a51AsM`V42R)7Ft<7GTXLZ@D,7I
[D6H'/ldkJQl<#;>jtBb^kk/SoK)c;$$h2nO\jB_PG#iu-8c*Ju=sa)KHs3V@RhC+&1s&%pi
`M9>SK5pr_`6h5)s+IEG$gsYAC.:P;aQ#^tI.Q$ofo"bQ;dJEgN+`\'(6!:43"bAkW=73<3'
Ii9/6eMnNPh5&UQk+Y;@%B_J?XpdQf]A=>LP:Hp']AVsXRZK_O6IcP*/!T/lD8QrZsF6m@o4ZO
U3)4J9d_X]A;o:K6&Y=Amg8MK7l<3^`DXNO7[Q3cb$7gV.p:&a\rOP[8K_XW+:-RL;<!7JC0+
2<KV*Pi@]A>Kkkir/EEr:)<W-E_&7oNl\)%Gk&2*1W6@p=R_tAuFq583BtDC:%WR^(^]AQc/WV
HSifsN"Pm2X9uSYiJ(08\tb+\:^Vg$E9\MUl3*N#)Anm9V\82$Z73\q+kj#4F1Yd^VuXG&JM
<c-MQ+>9ZG?eP5Z-*nEf=_`2moAX7j3Bj;8bR8mjJL9EH4Ok"]A=jE`cTFi07LjF\gKC&6r=Q
SNg9o2clQ\BqNcI5GU.n7)JC\N@;q:jFJ)nWelX:U!+>CE(H3r0G$Vfp^lqJ\93]Ab64E)X4s
L?r;:U#HFUbB^85uuL"R@LgB_NZ]A2=87l8KdLE04"IM<<C$Br9%80X-P!a"K?1VQOZ`53Ca[
T\,o//aj0WgEQHQ]A(eN1i^N2,"o-'VlF=SsDuho^\dOb&F4'<]ANjq@)LegkdmnBi-lH^L+^f
<jfLQT6XE@<:jO#WZ9aZCuTaK/1]Acf3_NeRqI\fhF8;L8"b",*"`$^EYD2Ipp(>:]Abk*N?6B
MK3m@f'F'M+*iGL.rpuq8\8_o7e;@7=8>(+R/(K8\^c:HgL\RZ6-4X_dB>W*"J?6T3SA/>%+
4/%fjonApa0BkuMW!p]AG1o`kRnhEPQ'8(H$jMigjt9#=4Jg\P1YU`666cHd!\4C"STi%62lk
l5nj1j$O)`Caj+o2eQ^lgrU)H,<WcKp-[%\$.W8`-9.M<A^fP/?:E1P!#1tD`1TVQ)adJ)XW
M"#Z]A'^,<S\Au,l<nkXA:F%l-&QVW2Tb-XGW^0YhqG1@,@S<3Gr6d2siD(^Q.1sjR2?uSG^P
PViKjWs3n..C_4rP/WO:hNn!!#SZ:.26O@"J~
]]></IM>
</FineImage>
</Background>
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
<Attr shadow="true"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="2"/>
<newColor borderColor="-3355444"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<Attr position="4" visible="true"/>
<FRFont name="微软雅黑" style="0" size="88" foreground="-10066330"/>
</Legend>
<Attr4VanChart floating="false" x="0.0" y="0.0" limitSize="false" maxHeight="15.0" isHighlight="false"/>
<Attr4VanChartScatter>
<Type rangeLegendType="1"/>
<GradualLegend>
<GradualIntervalConfig>
<IntervalConfigAttr subColor="-14374913" divStage="1.0"/>
<ValueRange IsCustomMin="false" IsCustomMax="false"/>
<ColorDistList>
<ColorDist color="-26368" dist="0.0"/>
<ColorDist color="-26368" dist="1.0"/>
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
<VanChartMapPlotAttr mapType="point" geourl="assets/map/image/new3.json" zoomlevel="0" mapmarkertype="0" nullvaluecolor="-3355444"/>
<lineMapDataProcessor>
<DataProcessor class="com.fr.base.chart.chartdata.model.NormalDataModel"/>
</lineMapDataProcessor>
<GisLayer>
<Attr gislayer="predefined_layer" layerName="高德地图"/>
</GisLayer>
<ViewCenter auto="true" longitude="0.0" latitude="0.0"/>
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
</Plot>
<ChartDefinition>
<VanMapDefinition>
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<pointDefinition class="com.fr.plugin.chart.map.data.VanMapMoreNameCDDefinition">
<MoreNameCDDefinition>
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<TableData class="com.fr.data.impl.NameTableData">
<Name>
<![CDATA[ds1]]></Name>
</TableData>
<CategoryName value="Area"/>
<ChartSummaryColumn name="SUMXiaoLiang" function="com.fr.data.util.function.NoneFunction" customName="SUMXiaoLiang"/>
</MoreNameCDDefinition>
<attr longitude="" latitude="" endLongitude="" endLatitude="" useAreaName="true" endAreaName=""/>
</pointDefinition>
</VanMapDefinition>
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
<Attr enable="true" duration="4" followMouse="false" showMutiSeries="true" isCustom="false"/>
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
<BoundsAttr x="10" y="160" width="616" height="594"/>
</Widget>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.ui.container.WTitleLayout">
<WidgetName name="report1"/>
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
<WidgetName name="report1"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<Margin top="0" left="0" bottom="0" right="0"/>
<Border>
<border style="0" color="-723724" borderRadius="0" type="0" borderStyle="0"/>
<WidgetTitle>
<O>
<![CDATA[新建标题]]></O>
<FRFont name="Al Bayan" style="0" size="72"/>
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
<![CDATA[2012907,1301025,723900,723900,723900,723900,723900,723900,723900,723900,723900]]></RowHeight>
<ColumnWidth defaultValue="2743200">
<![CDATA[5989626,270024,515500,6286500,294571,515500,6286500,2743200,2743200,2743200,2743200]]></ColumnWidth>
<CellElementList>
<C c="0" r="0" s="0">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=if(len($Pproj) = 0, XXX國際廣場, $Pproj)]]></Attributes>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="1" r="0" s="1">
<PrivilegeControl/>
<Expand/>
</C>
<C c="2" r="0" s="2">
<PrivilegeControl/>
<Expand/>
</C>
<C c="3" r="0" s="3">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="index1"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="4" r="0" s="1">
<PrivilegeControl/>
<Expand/>
</C>
<C c="5" r="0" s="4">
<PrivilegeControl/>
<Expand/>
</C>
<C c="6" r="0" s="5">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="index2"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="0" r="1" s="6">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=now()]]></Attributes>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="1" r="1" s="7">
<PrivilegeControl/>
<Expand/>
</C>
<C c="2" r="1" s="8">
<PrivilegeControl/>
<Expand/>
</C>
<C c="3" r="1" s="9">
<O>
<![CDATA[上年度經營利潤指標（萬元）]]></O>
<PrivilegeControl/>
<CellGUIAttr showAsHTML="true"/>
<Expand/>
</C>
<C c="4" r="1" s="7">
<PrivilegeControl/>
<Expand/>
</C>
<C c="5" r="1" s="10">
<PrivilegeControl/>
<Expand/>
</C>
<C c="6" r="1" s="11">
<O>
<![CDATA[今年經營利潤指標（萬元）]]></O>
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
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="Microsoft Sans Serif" style="1" size="128" foreground="-14898964"/>
<Background name="NullBackground"/>
<Border/>
</Style>
<Style imageLayout="1">
<FRFont name="SimSun" style="0" size="128"/>
<Background name="NullBackground"/>
<Border/>
</Style>
<Style imageLayout="1">
<FRFont name="SimSun" style="0" size="128"/>
<Background name="ColorBackground" color="-10642722"/>
<Border/>
</Style>
<Style horizontal_alignment="2" imageLayout="1">
<FRFont name="Verdana" style="3" size="128" foreground="-1"/>
<Background name="ColorBackground" color="-10642722"/>
<Border/>
</Style>
<Style imageLayout="1">
<FRFont name="SimSun" style="0" size="128"/>
<Background name="ColorBackground" color="-12335421"/>
<Border/>
</Style>
<Style horizontal_alignment="2" imageLayout="1">
<FRFont name="Verdana" style="3" size="128" foreground="-1"/>
<Background name="ColorBackground" color="-12335421"/>
<Border/>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<Format class="com.fr.base.SimpleDateFormatThreadSafe">
<![CDATA[yyyy-MM-dd]]></Format>
<FRFont name="SimSun" style="0" size="64" foreground="-8750470"/>
<Background name="NullBackground"/>
<Border/>
</Style>
<Style imageLayout="1">
<FRFont name="SimSun" style="0" size="64"/>
<Background name="NullBackground"/>
<Border/>
</Style>
<Style imageLayout="1">
<FRFont name="SimSun" style="0" size="64"/>
<Background name="ColorBackground" color="-10642722"/>
<Border/>
</Style>
<Style horizontal_alignment="2" vertical_alignment="1" imageLayout="1">
<FRFont name="微软雅黑" style="0" size="64" foreground="-1"/>
<Background name="ColorBackground" color="-10642722"/>
<Border/>
</Style>
<Style imageLayout="1">
<FRFont name="SimSun" style="0" size="64"/>
<Background name="ColorBackground" color="-12335421"/>
<Border/>
</Style>
<Style horizontal_alignment="2" vertical_alignment="1" imageLayout="1">
<FRFont name="微软雅黑" style="0" size="64" foreground="-1"/>
<Background name="ColorBackground" color="-12335421"/>
<Border/>
</Style>
</StyleList>
<heightRestrict heightrestrict="false"/>
<heightPercent heightpercent="0.75"/>
<IM>
<![CDATA[m<]A.A;qKU/\(=Ya'g/UU.$/bbW&OcL;(t8hR[@+eZoER;;,P\0jrqrgKEt2Q,KQ*M.S*PN;5
O=*#t2cITgU"78UuVYKJ6pZdsoa$.[K+=rGM);s8W"CG^+VAZhIU<mruP4?#+B(CidP?rFGF
G1M4juqs??+mq0e2$-nq._9Z:,6(`tC)YT+-L\8DNJ$gLPD5_5#H1d<lrW/F\-";@;6,q]A3R
ng`Bp9G`S^9u;\JG#g5^/*>UZ="coIV]AnaEl=a@):u$@8obdDr%%/1\#m/clI2l%J%hL:B!n
.5**K@X?lM81C@YmQX&<fQ?G[mcF'iTc3BLtd+LO!S"/Y?-f=:X(hroO@nFlj5_Q/#:-KV[[
8QA2I\Z"YV="+'bOce6:C6WY8L5FAQBZcr03Ffl\`1586Se$(Jigk/&kk+.[7OKk.!rFo$0W
3Xj_MhU1/[$5Zl]A8KLPFJ9>_KF[q/EL6OHD'3uU%U4>rV"nRJQqMJH[u("qYuK*/P@4C@\cs
i_&+Pk`(s0':#/O6K,>IEl(k8Fl$LM3j3AXj%0!b^;Ic&J++7iWVN??^XH:Nu'p:t6S=N!--
LoU?h_r,MW#ea(OQ-!ogF3IFiZEGmhq#EQPeqM*%6Ej.pYr!-=K=lV/pKI*m5I<0j88u#]Ab8
W"aNOK$K6nn3[sPEKXb6LF;\bTE_<GRZF6<X#WN))a!3o6am"RbN"%1sebF"H1fb`k]A<BbM?
:$2C\T(M/^PDdi`7p'0$?R$$Cf]A^a.Wu&8;RpbH^bX_balpihP%HeOk>U"K^DX)IE4]AX\X%[
rp$p3&uS?!hfu8A"3Ec1kI\+uXCUgD+>@Xec:3]Ao70Dm3)J28i&r^cJm%8N:WG$Fcf">\Kkk
J(G$[]A/&7k7!^HKU`Fa7NQ.qs-eeJm:#jd$&\C]AD5g3/>+e?NnP]AcCEV?<WR.eTQ2?Hj//@!
q$u0;/Ob!cs%=e0Xq6Q+&+QngGUak&$_OI<3Au<gXp+H/!3kW^UKjYb>!69KT^fad(Lr,D8d
=['bj-FH-MW?kG;B(\fVk+g?-t$Aa+Ig8@^g='k;mSY(0!1>Wud9a_G(P_tkNGL_kcag^%rT
\700,GFN-L:e&?FmXb;,@Nt[XgNB\?^*#=K4tp_Q$pnjpD$YQQ@;!0PU`r$i6HFu(YF?r^/*
G$@1<&"!4B:%rjSS'%O_PK/n-W^HV>>5U^4LsRZY^N"S@m4Ug-+cqCpJsHL#^^`n'JNR-^%:
#n"@,m7cajEDtbMGg,9oh^!oVeH9$2a0MM,+8:6d:6+Qk?9@_<4>NNi/2+R.A+$Xb!XKuINI
H7j?KVN>DBbMIZ(OJ4J%>XCdSR^(%RR0/N]A;Nfpa.d78R<q64<^EEpeWLQgMb\UXg#5$1fgW
/CD%?Toc?RN%]AGCfnNVNj&&)us0RRNf$IL5oKYA42t3jmb5DjPS9eLZ\hK/^-YR,d"1hoHQr
d#?m>PQLhoO[[$)glZL#f>b_Ph"2UJGteD5/Rr<*j@dbs'WK:AHb8k;O>X?rUe(MhD$p(-<^
:]A?mB5's0`N*Q_8?JB[bKW<Cm$eb5:`9%lg)8-XteIX$<37E=[X7S2"Pic(r'^o!5PRe#[_&
?Ak(!XghtF-o!YJo^*[ra\iY^mWLcoE`/IUm4HsX-NCCK"RkPtEmc39;e-@j\;9F+G<K'E&Q
?RT6oODT52PP,C`T`Bpn2)@pnr\:#PAds&O8B,`Mr0AbA)iXt1l^;FM1&\n,`/9Ufi!Z+<KB
n0\$u2\8u@hD0:F`nnV^1G`H3n.ghtCF'=)j/r6L;(#%kE2P@W\fm6V8I)'bgo$rFNE7!['O
@7$k_`=3@FVi;s@]A%+O\WoX<\Uj3BG_C>l,hufi+_F?/d&W\$(1:)S4<M6oVTp)>tCVIkK;N
$Egd``mBPsSD(La]A*gJ/$>(e5O3pAK,ZOIVLT+-_jV*(=`u<bj"k#o2$EL(X5\$T$BR1:k[j
tghtkteee<+FaHR0]AhuB_'-tc8-pX#VY`5oo&!cYEj)5Dj6[8lplAqh6I.q9MRBT@ND8IO?Y
5'sriKW:ol%@SLMkq50W.01Z.>8jTS)O(K:"<Y=(Oj3";(97C*S[5i7%h-1G3l7J<bEJ/-t6
j^T6YdfkWIr"4#Wu-U"+$]APP;S[*>YfuS%I7:0onF-aLb1SM]A-r@>Jpht3&$9W(m5lo*bm+M
_VIemUeD3'o,%e#F<^VJXp-e9>VV8=$!,hfSea-[Ce*9i8O!'c6k:0]A'8a1;mjZ)8Z^ZQh1)
rbB(Y*-tj,"8`d!mOC?#ihLeu2.fYS>m%^tNdrKRBeEQ+k2A;+<,Z3HWltHA/2+8FS0KiXtF
]ADXWZ-&'>575d!5V%M=$38U6Wl@C;UbJ1B4d`GIb]AdWrN9PklidD4jiU:E3f\jFqdt=l39f&
ZFV#C'[Orl&c:-R2UEHmAF38a:`@1Ft9iq,UM[NTNt^FTQlDM@[":6V6&A5<Lj'S![&-Q=W6
$UI:L=H:h'o^N(6<"k5DgDWd$=j53hYYRVd:<s/+&`"*G'Je5.81,&X45TU)[M=5a,6N.$fo
TKJRAS$aPD1%_!%[>sL&!Qnk?WD3isa%q`)kiUX<`"]Ab62LXW-0j>)a'J-:FH'MH?7DF)Ocq
f)bgrQB1qS9%m`XZ(1pOk)>1cU!mTDq^u.40i,@BKeTdm=#sQP+P%/lm(7bab5-BbdF-nL1g
8diO]A8`Ya.m-FYEuXDqH[+guJ"\%ULFcM&%g6rnpFeA3M4nd053K`HP>4Buj*ggF*H(G9b\C
-`"d+"^lG=]AqRc9o-FNZo=r>RI$i^FHO^N;rZ7"&ENNpkX6Wg7_,.RAXjGo7<M%)+kp@cIb;
a%%]A!LreuTlf3$l)mPj4%2-`HGTh.,_"F4)B.\ZFb&r#OOI:C_dNK@pED$M/Qbj*G%6=PAXV
/+Enp4[6f4e_*CiU3",>SJ2"T\a0]A)OG?b8G\6+h.U2onHAGH9^cd(b+qJt5qI,#OEkl':->
HSif8q/r@NhtG9IfJ<?G-Ea\BpQE?E6`<0*(e8:W1Z3GCmLQO"B*f<1C=.StU"+I;\>@Z,7j
M:,XI>[AkN/IG>l6mTN>kX6Bp_>rf*fHkG8'0Y2l#MG>D_B1S.$m0SJ<_W!JGFl%cW`#nkhc
8LZj%4tCO/;ds64CA,P;op5topa;qFQ_jn]A`(o78jEiYUS&0NI:CCuXt&,Lg@Eh^HF(\aPrV
LD6b/FEBRRM&nkB!M9%Cah@U!ZHNG3tiiM;@Grc2@_b@[ob7jc>-gdP4WnduY<2'hqu+oKFo
2]ANq[,ILd[$-.FAH')mJroG#F[j>;ZCte79-Sp_q'4OU<oG:OF"s%G,.0<KOISFD^Sj/*FXT
f4l^J7=kbs.V11fG$UU-n]A"gIu3JLnG9+a"%7A%#lYh[pJlsVNUWE*_2sm#ICZ.qRU_m42^@
gfC#e5Md5qBU6L`*4dD^s=P('YCDl4U:Z4<qRqC"Z8$NPm?S,)4cQph#G(sEOPr[PT[=?56T
R&U8SFQWIrkqLbd8n1np'a/YEmDs&do_]A%Ca.@[82qoEIA96O:c#8cg\Hi"kpI?'kNgc08lu
87pe/bdH)JE9&ftl(,@(FHr>#%8R3)#Q-r8HK/U:??=nstfJ[Nq^K,[fd`Aikqois.']Ae(2t
dlN)$H%ma*j))kT="QJjn]AKWXEmJ6]AB5RJ]AcgTVe/?Ts*lbBuHW@L4eZU\FKhWhr26"E?/bV
)M!2M0P`He'c&rUae4h&+jGXufZSG<9::dSq!8XSQ^(VP'V2/>N"/qpT'!K>+P"ONuii?0AY
2O$+P+EBmC([]AE,t7(V7miNCog+)KLkRmn+[lr^r5WG.20h(kS?5\;Q+4m8&gBLke<5KFqUG
0I5&s4?hHN=/sXhYm2oo(X9;5F3*H\>UY#Cb?^+aYDN6G^7!sja"EPDp\(1J9.N\.gplDojZ
p:G=FR'12$]Am*5T`]AM+9YkqqN&NE*5<Ggh;);_RnCtgEtHN6C)!U";aFD-eQ'+1JW9$UrSaL
<ooi:E^hg:#^ob?O%!FMV@@EXE-E/pd37l8?pIrh=sk9R8tRVJ*c#sYQ$j/G8@guja:@ERER
T>^!P*CH)UM>h_sFDknR#Tppjia^aKGL]AU@-P%1.,u(rD@l;hIEbC*)!3n2[IYGm@\@lOB@M
-CJQ($`X*!tYIfVH;0EMlYClK=:38l"!HY8<K_Ik>0WV2*]A^P^i)YU,sPE.0O\T,]Aa399jZ$
%m&.WXc3M>YF:Z^2VUTn6l.ePt>jP!p=%VCm0q$ThS;!3DMOZpOSoR<a"q_0VR9@kS2L#<Fm
;P8tVJYo,*C.2)`,;A>J-KXTQFdSTEU/!cj1)`A1o;11Y9P/sN\QH_lG\@kmW"c:C<%[^R^<
(3GSDgW%[J^LIaV]A7h*7k%"kj7L6e;+K>%E7cji(IZ\dN`jMCNnhb!$>"CJ!P>?;5lJD`tI#
fF_-JNFsSX@+>,;>RngB8MD3o9ZMCRnK$aZ[39;.Tp\Tnmt;OgQ"I+kcCjRJ\0t+J<S!Bjuh
:qTqUq49iFNOFcteX>kDBK$2gA%eON8lP&'1"p3MZ="524m"HnapIJ<r`QZIg)'sJmV*sN'+
[q%+Wm?dPm]Atn*0\[<p%/DS-n'J^b_.q-&/O>kFd+\l2<q)N/ZVH;e\$:rr8LNZ20>#74gaB
jrjGU>7T5g&-&:R3Cp4_Z2!Sq\d55[Y;%LE#Qh9FWF9FV#VgX-I^9+9!(Na:t'7dcgC[uVnb
GeLDRbgT3-AYVXbO7#nj2qaLgO1WH?XpC*]AitVEboXf=%5n[Po#h<eZiJ+5!BGD)aX@=Q;^5
]A`#:da[i(PT%i&G+6i9#l+9Tj0ac$R-C6-TKCTdt.'*>rp4DCt6;fhjp_,)=XX\oXo#2_W5`
qlDlJA'jkch3bt-jAHuX8%c<^(5aq@?RGc?*>/I;:OouFg\)NNVB'E):(]ATu>n0l[]A#LU!YH
rI8+fWAp*B9@Gjb-$Z3(s60S7)$!"*:of!X$7i_ilYFORagLbnFi6[et+GYY$tM4Ft<GlEQP
6s2c9;i/2sr6&.O(o7mo+BE\D`ajGgZD*J/G1`nnTNGDSP4WK6Sa]AAc;+n&n"=V]AV^^h=H^!
Z9bWfpTsOr;BDAk;XlF-KWO1F"brOZ9/*.,nTR.Jf9?U+3<sm)?qsk:kILgt@Y<0spoD5cJ\
\u-ZgCZU@uoQcaS3AS&ZN5lY[PER`'GN]As,2XY==q!s4gGa*2NeQH<"fFF2uYiVjZFV=Z`kf
q1hS!Qp+dh1NF2I/.ZlY]A:G0s\p]A=ptNK_#g[^jrG)fiC*P=eaq.;h.DlE68,eM[gXo>^89K
.mCn3!?5*IFa5FgU@#4qL(81d6hu,GL5_%qESr!qq'Os]A>H'LXZU6<=juZ!`09-p-Lmn-<+A
tE$PSni[mFDhd-1T7.%V[<$eg>H]A66J;3jp$CM4S2YV/<-(?P\^II<LM=GCB)JFci&ZWBZKg
pEl5GNn]A?3TM4cYeJFtXPZQW@Slf_/2D"J5&tWD`YeuuOjdA%shKfo+ZUju-R2l7,_P$[3S.
i-Ac,sJEnE)6QG7S;V%BA#8HWV1L-:XgJJ)7e4LQH-ph/uFqoQ`H6e"\OH'rArpBk5V9g,5%
=V?<(8Sr]AG*T%toIFOS&]AXhdgRg?+K*=($"(]AWe[<#gHc-HBBX[hN%3XoOBaUdW(gFO/O8V:
\lALelaN=L)&'7Hi5cYA+eN.Te#ij)2dROi[S-3`ct8f^)`O%NKm/Ak5(E.a=^]AiTt2>BmZS
&'&Dd0;*YO=-0;@uHO?2#IQ$nh>'dd7n'?eS)EE",V`?>^QI7B&mKA;g(Tjik[&`F<bldqo'
F[<S=:1!>N7kCAT7qnRp8oSSTNBK$&@F!mJjuQRo&moI"TXU0Ao#\bDhVZY:coaC8dU7S_dG
8LK:SN^jpE!p"pnXiPJY[$H$+HEKE&>J-0k3eGH(&A\/Q.j0>+h??/]AGXZ!);@1Rc*U<Jl4a
I]AIE\+7@[XQ#9Xs4;c<-SS0hr/k:=a$79S^cOgcsX`W9EJ!F^J)TL]Am[OAV!Pm?)qAm?G[]A;
06*(*`8'q+bh%Z5![76QDgb3F^,8Jae@rPS<&SB<:Ok8XE2ni>SEkTTHY(fC;+9g\""ea`03
SDTo(=sF?TAQ<mYOoZgZ7<aoWst%e2>IN&TY-GUd@WR"5m+Z(AJFZt4j'b7j97E-Act&mJBJ
,U?8mk/'NE#[IB>5hm>B0Pi(.371`>2^+skBdD>%'L@r?PdW1M#=X7DY+TrjDoG,PMW5BqZ?
J7eVP5n9jgUMG!Zg:L)d9"\SNWPt#&oHpRV*<j?^c'p(6b8AQtd#9D9=imh:L>L*\=/lWF^]A
%^V%p%-6__^2%,+;91pc@1f?&KA^?G:@1&86Q(:HA2?g]AK!l`%\"C)PhW_[jmJZ0]A9(=8EO`
cXc>4e1YCiU$(jaf8h%W>:BrH`-?QO=T&f3&8`]AMl+5c,;ZPg+kCaH`]AigIZO)YA.2e6dl2h
A([9b8/FBX6&5L^E&3f%0A;T-hfc>1!E0-M]A4\a7cD'`b1C9q4[%]AuZF=6^+_AO^pt*b#M,7
jLE$$$cs^N<M5oZ=+QR2E-/BBnJmtWV;.]AKU%G`uE<noB9',,UEPsSKhuWg5n>^]AD3hTYe]A+
`HOll)uc(`$7UeN(Z!>'1usB*E9-pV8(PiYC."qT(E"(-NPPhemP@j/E[MV5.+ag[^,;`8i@
NWH0!i0VLX"J\9#3WN;SC`@apo\bXFK(srMKX8;=(AlO/;fQ3dNW+=RToVIQ>$CH";;_"RW2
5aK^':ldaE]A\bL27:dB)c+<q+Rhk@NYVh@M;5j5gR*HDI:[gn!i_\EY&>oOBEpa4^,/E0Fn7
>coSuU&Bs0%k[a#N0U+hh![<\53!Z%b[eRsp!iBdN``b%6`B'!Q,4"^LIf^36E!0@TTcUCl=
rm?\&)#>?hd>?`FrVS@oqJ5mBlGX_g+ZmDrYEM%@/G'^W<CNkLd'?lQ,)pkDo=Ni'\?1B.P)
r3PHVYj-T/A!pcU=/+J+MYaK(55N5lARNDXbI!m>D8EGViZQRaPNK.U&&CNHZM%C7ln'l`7T
J\og6:(T*#c]A803%93u`>*C]A`OX3.G!r>G53fs?A&gJJ!/FO<^bU#%Ld+69_`*M%<e?eT`gp
omG+4s`'i*s2WK2kH0Fa!h\-;4j>7&&QI-+[RX`\IcrMhK_HB7IOiVPt1Fk-htU=-riRDOhQ
-YHtF]Ao2/KTL&5=NCUpEo:V'Ip)C\6R2r+0a1]AJ^`a;IPDB<Ut+olO&]A*>Y-_Hk(NVIcS+SN
1[DNg=/?FnUd(o+r:GGlFLWS@,/]Agk/?JV9?UKk1AV!0Y^%'\V)SBRKj5&#-oXjpV$I(7nUC
Pj-135qNit)`^kk-TPp:(<D3kJ<BlPf33*m%>"iqoUo1q%Q!L,1+^92/K=g-j'0&]A7c)gQa>
lNU.;g<E#1u:Fa1jLK;mn2,/sD:PWkY@mE/DQ(=jKhH8U7*]Am/]A=.1^2N7uS_3(c2*i)9rqF
5u=CAKBWbCkVJM.Q>-'_F1BHT^aO&Ig!;ZZNslqT#;$?7fDrb]A3KS4?j*Y@/XUdpc7IPS-`F
VJf'8Mq*Y0Sh(b[F3d*g27,1!R`\,TPl.(4+Xh%O*&cNbNSclSC3e=P93mS>)SCT`Q]A:DnB)
OO&8Wa&aR5AE.#2;S@ubas^+,FoA9Pm\C,g(_JPI#%WuDKH9[\l`0C;N7t_"5PdNVRt/[u.M
Dc5\,^Z4b<G]AQ6@Ut+c:WMa'-*c-4XPJ7G)St9McN[+rf/t+iF'go2;L7pOB10:ER1IA6)p:
"5U99AgM:@B9P3P&=TG$LE'8cjqiiU"Bnh'_Ch]A-H<#ZQ%&^kc8N3o/?&KTJL1h^W4R0mr&I
&p1QhrJQPF6eWrqZ'Vp+jq0?9U7Tp)qc0Ecmsqd.!9\'Y>'6N7shNUDSr^\:\=QcTYK$u:+6
QgXH4]A>XgPP#f@[b`32dsdVQ)#lU2.`@^J>E*6PH6,_ZdDW9+"K]A[(dqS3b9r>9eX3ap(s/b
X\NXs%n5`AR\@tkEuF$8=2@(,/,%i]AIn0a3]A]Apgn;9,SDU'nq@#FcHbPl4Tnj3QDQ#L8!Z6k
k1pY+qsB&j-5lC=7I.,c#fmq1PLsDEU`IgKfJIY8?OO)JVTgN[MMCF8lQ]A&0N+a(I;iTVm[`
:re>tZ>(<_T&0EE<LJY$E5lTbuW;9U1>"CpKit0W/&4CU?+gkIK<7V_>ef;,8/gj7d'A7)1i
<"Gd:Enbl5iU&/?-H%cSrb@X<m-\')O3BR@b)X(.;*$0W2(W_#NKP]A=gW%A44odJ&rh'o,*b
djl-2s8dV(jMJZSLf#LD`h2TM$PPS6dp@sX9.ikU?]Ank\CR`)-q0N-,)T)pfWMQ?F=QkfgLT
T@keU.f(DVUmds]AI>EQm?i6WEI5FpdjeXro5pf>YU,#RdY/I'Z'#J,[VG8GQMDCPjS]A(q2Ua
UjoY2[2OX_hn&[#L/]AS#+\l,[8P^:^('Y9UrI@mPi<kVM=[C^A)gSCB?,7r&gQ=c3jNI]A9M>
Jl&p7uF1/.2#`2_7BN!prb6F,+U5Ik_g1T\7)M'<ga?.M6kcQ1a6KMiMgq1*J;Q2p]AF\Z"`S
A0tL%hVf.CUS(2!CM(j/3s!(@Us%)RSbClrZX^Ii5ZXMT1q&EBr`7W(4U/Y!)G40(8uV4)?[
NYr3.AXj[C/hqn1aK*)o]AB6g]Aes(Z5EG;.mJWI:2iE)6Np]A1PQ#@;2)6GX:d:&d?A1PrFUfW
De9,o]AelM]AKc.kTP6Vnd447q=(F0cU8oC/j[,W@m6,RlMV7L9GCX9LA5B$RLi"$+oIO1A;_I
9]A:6snY,ZKD@DkSS;%PK>PL)^(tK3RU5G=atLV9OXaQ^#0!MW%P5DUM(oLOPM"RX@Dnj,<[d
6muOf\.=MWg]AsR4NWteacTt1UJQds'@[&b%+_%L?eO*/Dks,>1JMq^oVTKU;J#[CrBc4_LQ)
-4,$8.2GjN@H2(:.^Rr+i3g,0riMClmB/5UgfUmq4Jr(SqU?B3_;=0!(Z7RU,'`A5n%;M/?G
D[HpE"VcC%?5$PSEW;cH5tTndBtrTm>qqoD)Qp,ng/19Af)@)^?.U"),L:#e7W$qr32>?im4
>]AD6t\4Yd_7)Sh=Gu3$J6-]A<iL59'%[K:ijin,ee$tk2RO-=G`nfX7!WWfqJZ(VU9K:remTd
7!A>47Yg-05%C"-rKB7NQe>9d4#M=[N\`)>UmoNd?APq_Etr4<=TmUL9XX[8Do!f#<%'cgTR
OO%)!2i&DeaRK)3@),3Lue2fU$,S!0l)02&X[We4TD?&[$=q%=C,qmDq8>ffK!kk,hM`6;We
9L&5FF8<?4J;F\qKI::7&&gt(Km\GQ4qsQ?rgb#;+-++]AlC4I&3\$$$t2uBiYX\?Q"hTVmPn
-?dJSkup=($T&<K79q50)bZ!)$1nJ+\,a7;KuOG?A6l.:on*L:duZ>a%SN.1Pp,hm)?;4^!q
j,AECa*.nW/mD9bktp(\)^qU]AnV)6?rj^3?8Y:l,+jKh6Cci"i$-OH%D]A'0i&c6Za'7k/g/l
<:9GWFNZN7bqehHOT]AdSigh<ljj%gfq:go5b12A),V[MoH8[I.3BfC`ssG]A0s$SX]Ab43kZ]AF
l4O:B]A#')YY*)itc`6BBQVOLLb7#]Ab\`"m(>MQ_<H8DSrta=W?O!:[&hHP(GGOJZ$8i1M,Tm
:e_Qq/Dtg;LI*m(lc2KjR]Am_O[8JeE0#R7/:&3`8ZZn$5bE`m@cLQcU/n-Di&CQ.R=lU:SL@
^;:n`oE:AF70;0^K>o6sF:aW!OKO5:/L#??up2,BoYPElicA'kkL]ADTqmOa<ajQ\gk:-+/;,
$)E_M^U,EDQfD;$geGF?A&8->5_>#`=?N?S@IW?RJbff*HcYhPH$\W2)Op9#chJ+Ld65CnGT
oLP9_1;"7mRoL%BL<kOLj4a.tW*&/YK2%60>3a"&]A9eEgOC0TI*8D:NC'4=RGa2TSXH@Z7@f
.T*U;DYH0+U:0VS*b;7Q%&uDg7r^e(F5qK#ca(74YV.re:F:q`6TaPoN3MjX(H6MHB4@TnP*
(`Gne-YZ-"KQ]A%d*\E1h%?6.ANT`!Ko"L88QMj2BEjq>8#jk\=KX99.;D_?(*Uj<f[%uHJeN
!f7gZZ,`l2rI").enf0JPCo\g/c1MKpY-!QDk0Z#9(3_isGn'aprb<`AZU;Pg(:h3>#^t7ps
>oSHoHi"DlaQ-o5j$=$^TnjSbXri-49Bu:e/7,J#_XL9Pb7=XT_X6(Tq+rX1Ls4_QD[;/gWi
B,mKbr<pe5^[=L4'Sgeb<Mjf,4V0n']A@Z>#oddLtL&q6RgM6\t%t]A4,PcY\5gW*1S9e""o(>
WQmAq3egSV8"=T27j&9t2>S=N>oehNS:`@l*QrK*af`VLXIlT9ATds:^)^ZG7B/!<uD5Y$#7
<oF[Xfi^Bi'!g!\YLS[kmh(;LC\Iqh`18.e`%a)bP@93ftsG1.I#s0/&A[j5L>r1ps;>!'Ql
r.GA@2=cDE_:qnq)7PDB#n"<bHkE0a5>Q%c:6%@-Z^KR&#Ue"XM*.uYBm<e+,0[Vp`Prr.?p
P,oR5+?4+=P";]AG_Ps@;gj!nn`o!p,fS!dnmM!;sf7"4B2FV@4KTb?/.dKI"FF10k`"E8E,8
MDt)O3S+;6R%i%0!@K(&$FFK,5P4>d+?`*h=4q58n,VL`/!%O/Na#U`6%5:4Wq:mdH4)Pu66
Zm6L[?8*Qo:DY,VQY?j5`i"W6g2pgXJ*1=BE5BF=U+[XB^&BRtCn_*or70uN!Gsoqm:$u0cG
3n45Y'H94KSBO/^)uP4JHtI\Ium6ZBWAp+=cM-G51OpipD$to9G2bc\@tm0j=Mg4`g;S4;RN
6gYh8dD8ar/h@:7NWYf/7@W)M;5UqgB-B4rXVnC1X0frf;OO+/EXooN#c.LC7NIa,QNPZlWe
RN8GL?54\dR@u*2R8g-]A=R$J)".SZ^EQ6`4C!KF'2FFaC]A/N55d^\Q\G_!#N/u:!i]A=%g3DF
I0f)75YlVj[;)kE36V^D`pTdKs"ui2ZZU@`bIQKPYk%[+KolX_/BCG([>@6T1HWh]A<nUL5]A[
L;ZI.^Gg[FuF6sYilc9j%PtSK&XJNYI$QU)?S&&e7-XGsO@Ps-GhNPK,oX>2W_l`/<XR<i*H
>WGP55s=:jRDJ]A*bMEZ^Duk!R`!sBq1%%e&k!M*2+^0Q-=B2u(X[Ed9((2oE<jFifm^ZF^sF
BC]As\-q3c_C<]AQ(<@Qtq6Co^L(>j$B*$cATo*a`biA*5hem8Z7WY([IMn@Mq@k&hQXune?D"
D]AAIB'0S48qMDQig?9:c%_&^sEgkIH/tNeaO4V7H>AcqiN$:@@Ye9P[I,O4&bP%o:Wnt,a!j
f)6Y@0Zmg]AL1t77[YZgqL,]A[8XQ5%PGgSNj?ek3t154nQMEg8c)QEWdR=7&0H^Lo]A!:4*2Xh
8'MM0!N;IYL7fAZ[3WbSY>V8dbC^JS;=M7W$!dLHm"FTbHrpD9pXN`AS?4I"VHm<7chYg[1^
ODM#_5Yh>@-#(F>2rsjrr84;d,!oPf36Y72SZi3(<Rk9`B*%5(WI!3/Qa*J+*h[Z^Kn(XmGQ
K0EY)DeAic^U/GROM:iDGQ9<:R/bI$&&Vk)O`GP'5t/^-n9p'\AG5"n!5qP@Hc"b7<8gaDMO
:H/5*2tV4X;N7BjaF>?"'26$dJfu@8_G>f:AI?rqcCJF-5C+Y?CKaqb(B@#sBBK1r]A*Gc1(f
,1XM[iWi.-MrT%YY*o#k7i.?$:,Wo%iS.l?,1aX_+Si^XL&h[f7]An&e[a7WN"OCVThn8VI(*
0op@9jNrSP'f(uLq0N;;jdbX,?jZDHL+V4@1['((]A9I%p/k_.7GB`[TBomKQV4$3!#%?hO:M
bY787ISV""2@c$_%J<Q4DdkjdOd"6q>Q:&n#lHXqtX1\rSkn=3oL#C)EM+XoZ"njW\c2%]APQ
:r[atsOPb\Dd^>lTi2dH`Y[VNEZKVK22bEG!-Vf1@IG)M04eNJq:L',j^oGt,ZA*/533dg_G
\-qK\T?4@Af6Mk@K<o?m!U,qO3E*l5rAN7R;eH5:U$3fYJ"gA2kmMd`BFVFTmM.uI[&,r&G&
K=S&-n57ih1#1;W3?@=T:P(e*XI%?%@niJ)[&G>tFr)JbF.Si$-4r-2)2DQ44iD[qkA6\*c1
tr0(mZ5LJt]A1q0FlDEgK*8Z[s\Wm`a#J<feFPOI-0[pr!Zh?rG[br(^Z@GkK#"8YSMr(DR\b
hT=MP&u#4Ur/">HO6D\pm;R@7Rr^XIPZ0\f"nSsXS$DVItE@[)#A8F77hT<]A+=l7.,_KVOgN
I"I_Vj4\]Al,oo'^GL2W?n"?#]A^K!#RKu"J/bCoMEaH=S_<K5]AT%f`MPZk^jX+B,PX,mg%!r%
1mdKm[M$EZ\9K+8:Ft4S!@N<q9N'+]Aaa./L'U`*&ci&lVR\:W"R$6@G2BH[@m,c^RepAFp[`
@.chj1L\HUHbM<)I5nN'Q3Sj+Po>@-F;aS;7!6o:072(&Ql^GkX\4cLN$kc+`p;ph,*gXu*#
=]A9ogUgMmo5q"\U/6CJ#R%;;>7J1aAp<]A6gsEo;%pD%=\L]A<Bn:E,:^MS6m)>*fed=J`fSDY
j5XjBRF9DOIur-(M:J&[Y4p9=T?'`J>_.;PL<<u1h7D[ZA2_A!Xq6TmX?<,)tk5^#U#ds?Og
//JoKZJrC?YKe+QL`pG1TKT]Aa,P>NsUPh$SO(c:FcXkd"rLC'dAYKAIE3hGRa=-`*[MR,p"*
IW*UGm`jlUf=1;a2nTS4R^JNNpik!V('"]Ad0(b^Zdk8>p-R2IIm0f9(p?1_WXN!Se--q7k"C
!''Hq#=MT>2&lT9ug+/H@1r'E&PRmip]AaE0B#L`sZC(#&g(0[t4/,)\t&nr2U",3nbndQBU&
hmZ(oNh)8sfE"hIWKr2c=p$R*0>C+l;ehnVR@P]A6[iq;c;,pKPN-R77V=J8UW8;@_;f8RKRc
hBpCn4IO&Ra&9<?g(r)]Aj[8QViYGsF8_2402T1r<b8?j6,9g`e&od"W]AegTY/\hjZb=97O:c
cWfj[-aleFSQeY"nM3hVfIC[ug_r"I.ZgIt/W%6e]A'824+Z)Li,dnMUQ^>/aO[o"qjQqLq_U
1&lg$.$WiYAT*t?"h!Tk9L9pP/Fe.b'"5Vh3tMr[.^KXS:asD&N?[cP;A"<E#L2iuoUX@n,s
^c9(hJj)-Ng&[(5oQgp@OA'!rt.WrM]Ar_]A1u[I0I53V4f&;eiHFYc^$)hg9D[2dhnu'l!!)B
="g!s1kZ^1&C\.050N52I?3Ybf[G1c7:-j$?<n\q-O28#XUR/`nM#SJa'U">H9#?dO&JS=ZG
mF]AN3U-g:p!2)0+0d+?WW*7tSck;SP]A4A=.Q^[)+7U"f2FT^C2S67caV2YOM>Q&dBJ%F_g)"
'@M5s]AU9&F[oCd[7"aUCQbk]Ar7QXA3k+lg)hrBJNU@c[mfNkQ9FPGPK#fCU.&np_6KQ3%WF2
aCEEc8WrtQOUFhbfYk>"F>LU`_LX;+5qXo>rI_L@_/,INof[a$pZNj&m\=SOR,UNm%8tiENr
s("B5s-s:-1Pi\ib"P0bB#ZHX!c+AmF*l++%8hSDTs$_&$h??_3HgM2Hm"'N[!\S<4o\4Q*%
`'I*+0YY2Jbl5[qAcq.jX\E`)aFMm4NcqO8Nkf2nQI+VoI,X._1]A?tiR_oX3QAe&lVqg3kkC
B2J^UE+^i5QY^!T6$Y:n-tn:'Y^Ej_8W/i/q45_Hf5%A54NH0-gVJ3]A(EBcpne9hBQ%CCUmQ
5-$FUs;+FH!R$WgagPT@:#eFgNe$JXM3iW<_^olrZ]A\J;QYEL13I\k&d)I9SGu/[_M$kk(*e
=:dfM-@+,S2^:;]AM:'#)Q3kSdJm/chUYT<hlqq/-LohF#mLI9aRJP7Oe:QPd*+#fQ*A?_4-E
/!IR%kH[0E@^n=FuP;+83(eJQ&6M!,#>;nq7YT<;6Ef<(95*Vn/HUEkf%lO%9qr:?EI+o$nA
J*RsQSDZ7m'IppjK/$hF8H3XDd/4ba=pZgJBS$ss!DC[$VW?lnaAaDshf&h*goCSk,f!#\!r
++fFkS1YKH'R:*C1UP@n!m-9qVm^*?1bp$[IYl#A$l[B0>8?8iepMeNV($IVKnF7III/!aB"
07C#@f+c"tc0T01o?rqA\_=u*I9U/$8=0n`&1"O1osY0I%f]ALi!4DeT0aCR.ot;D.FS0S`3K
2bo=[8t57^pQAuWhDiL$VPapQ=_jZg!:gccBqf$^Dq[V*XK7pn\T9gd6_>[lX;LIpTOp)&,j
j?rC$+:3g/ebSG9k.8l+8f&VTs1>l+0N>8N0Ht7n?F*T$B9jZ@8W>!b:qr1s+QnU`or!(sSr
k8c8(:J,FDhjG@%t3N8-hL0`rR7u*Dhb$BpoI\#J'b0gsdV_d'/D15pXM1I\&d@PgiMXG%oU
'j:&Wl-=9>;/nsris<BnU^GH]APnJh0jgFrSsdn!3!_mA^[rYbil0A@UUKH*SN"gqm;G#@aO(
(m[*;#'dM"Rk:1K>m@%LI?/b-a4_18Hh[nC'"Nm>9^4=#+616kNsLubKmfe>pGrt.!mBQM3H
p+#=5fTHs;%J&\AV'3B,;gb2>S=RslIks3'%7&gF:(a1DO:3p`HaEgr3M#^1M0W,<hr09@@1
c'HFOV;t+#5E?(5$d'(9<]A)5ce"(c*W-i]A/?=lC$';/3't\3_>sg\b#"oLMrN5mSsF5(8NYH
((tARWo3/:!pn;0H'28VS]A[q[1VAM/jc8om*f%HAWcg>Z.=qOWiRsm0O?f@S@#rk\"UeZJ/@
3D2`KV@'LS*8_A:!r'GYUo`Ae\"N.6Q#Z4+=c?s!3tTHc*$ukjlq2JQMd6:W<6q0mXH;\VMt
V"MP<c]A?<e.6,&aKUBN0c9_T%o<0:U8UMQoi<9*ZC>$pV\LC8"NTC")J>00$bZ)4X*:mISo=
_\aof6ZH@fD5.8R1>t9g;3hR<pa>I38-IQcUK!8OMptBU?:0:.Ns$81q[+uH#$8>mra2T7OX
&mgGRuQEi[,l-Un*q=E9u!d`7$C@Ifbu>!FWaN/+Rp?U5RqrMjY'*`KE&sI&#q!g1_sjl`61
-TkL.5:14g##OTtlQ/XOO9A0)($qte?C8^mnp@^b*aei%$):6-:0okJQYP4U_56~
]]></IM>
<ElementCaseMobileAttrProvider horizontal="1" vertical="0" zoom="true" refresh="false" isUseHTML="false" isMobileCanvasSize="false" appearRefresh="false" allowFullScreen="false"/>
</InnerWidget>
<BoundsAttr x="0" y="0" width="631" height="151"/>
</Widget>
<body class="com.fr.form.ui.ElementCaseEditor">
<WidgetName name="report1"/>
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
<ElementCaseMobileAttrProvider horizontal="1" vertical="0" zoom="true" refresh="false" isUseHTML="false" isMobileCanvasSize="false" appearRefresh="false" allowFullScreen="false"/>
</body>
</InnerWidget>
<BoundsAttr x="10" y="10" width="616" height="140"/>
</Widget>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.ui.container.WTitleLayout">
<WidgetName name="chart3"/>
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
<WidgetName name="chart3"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<Margin top="0" left="0" bottom="0" right="0"/>
<Border>
<border style="1" color="-1777440" borderRadius="0" type="1" borderStyle="0"/>
<WidgetTitle>
<O>
<![CDATA[=\'  \'+\'欠租指標\']]></O>
<FRFont name="Agency FB" style="0" size="96" foreground="-11976882"/>
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
<FRFont name="Al Bayan" style="0" size="128" foreground="-13421773"/>
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
<Attr isNullValueBreak="true" autoRefreshPerSecond="6" seriesDragEnable="false" plotStyle="0" combinedSize="50.0"/>
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
<Attr lineStyle="1" isRoundBorder="false" roundRadius="3"/>
<newColor borderColor="-1"/>
</AttrBorder>
</Attr>
<Attr class="com.fr.chart.base.AttrAlpha">
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</Attr>
<Attr class="com.fr.plugin.chart.base.AttrLabel">
<AttrLabel>
<labelAttr enable="true"/>
<labelDetail class="com.fr.plugin.chart.base.AttrLabelDetail">
<Attr showLine="false" autoAdjust="false" position="5" isCustom="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="Al Bayan" style="0" size="72"/>
</Attr>
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
</labelDetail>
</AttrLabel>
</Attr>
<Attr class="com.fr.plugin.chart.base.VanChartAttrTrendLine">
<TrendLine>
<Attr trendLineName="" trendLineType="exponential" prePeriod="0" afterPeriod="0"/>
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
<Attr position="1" visible="true"/>
<FRFont name="宋体" style="0" size="72" foreground="-10066330"/>
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
<OColor colvalue="-7881222"/>
<OColor colvalue="-6514959"/>
<OColor colvalue="-10237754"/>
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
<newLineColor lineColor="-11385531"/>
<AxisPosition value="3"/>
<TickLine201106 type="2" secType="0"/>
<ArrowShow arrowShow="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="Verdana" style="0" size="80" foreground="-11385531"/>
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
<newLineColor lineColor=""/>
<AxisPosition value="2"/>
<TickLine201106 type="2" secType="0"/>
<ArrowShow arrowShow="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="Verdana" style="0" size="80" foreground="-11385531"/>
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
<AxisPosition value="2"/>
<TickLine201106 type="2" secType="0"/>
<ArrowShow arrowShow="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="Verdana" style="0" size="88" foreground="-10066330"/>
</Attr>
</TextAttr>
<AxisLabelCount value="=1"/>
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
<FRFont name="Verdana" style="0" size="80" foreground="-11385531"/>
</Attr>
</TextAttr>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#0%]]></Format>
<AxisLabelCount value="=1"/>
<AxisRange maxValue="=0.5"/>
<AxisUnit201106 isCustomMainUnit="false" isCustomSecUnit="false" mainUnit="=0" secUnit="=0"/>
<ZoomAxisAttr isZoom="false"/>
<axisReversed axisReversed="false"/>
<VanChartAxisAttr mainTickLine="0" secTickLine="0" axisName="Y軸3" titleUseHtml="false" autoLabelGap="true" limitSize="false" maxHeight="15.0" commonValueFormat="true" isRotation="false"/>
<HtmlLabel customText="function(){ return this; }" useHtml="false" isCustomWidth="false" isCustomHeight="false" width="" height=""/>
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
<Attr xAxisIndex="0" yAxisIndex="0" stacked="true" percentStacked="false" stackID="堆积和坐标轴1"/>
</AttrSeriesStackAndAxis>
</Attr>
</AttrList>
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[0]]></CNUMBER>
<CNAME>
<![CDATA[系列序号]]></CNAME>
<Compare op="0">
<O t="I">
<![CDATA[1]]></O>
</Compare>
</Condition>
</ConditionAttr>
</List>
<List index="1">
<ConditionAttr name="堆积和坐标轴2">
<AttrList>
<Attr class="com.fr.plugin.chart.base.AttrSeriesStackAndAxis">
<AttrSeriesStackAndAxis>
<Attr xAxisIndex="0" yAxisIndex="0" stacked="true" percentStacked="false" stackID="堆积和坐标轴2"/>
</AttrSeriesStackAndAxis>
</Attr>
</AttrList>
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[0]]></CNUMBER>
<CNAME>
<![CDATA[系列序号]]></CNAME>
<Compare op="0">
<O t="I">
<![CDATA[2]]></O>
</Compare>
</Condition>
</ConditionAttr>
</List>
<List index="2">
<ConditionAttr name="堆积和坐标轴3">
<AttrList>
<Attr class="com.fr.plugin.chart.base.AttrSeriesStackAndAxis">
<AttrSeriesStackAndAxis>
<Attr xAxisIndex="0" yAxisIndex="2" stacked="true" percentStacked="false" stackID="堆积和坐标轴3"/>
</AttrSeriesStackAndAxis>
</Attr>
</AttrList>
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[0]]></CNUMBER>
<CNAME>
<![CDATA[系列序号]]></CNAME>
<Compare op="0">
<O t="I">
<![CDATA[3]]></O>
</Compare>
</Condition>
</ConditionAttr>
</List>
</ConditionAttrList>
</ConditionCollection>
</stackAndAxisCondition>
<VanChartColumnPlotAttr seriesOverlapPercent="20.0" categoryIntervalPercent="20.0" fixedWidth="false" columnWidth="40" filledWithImage="false" isBar="false"/>
</Plot>
<ChartDefinition>
<MoreNameCDDefinition>
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<TableData class="com.fr.data.impl.NameTableData">
<Name>
<![CDATA[ds2]]></Name>
</TableData>
<CategoryName value="無"/>
<ChartSummaryColumn name="index12" function="com.fr.data.util.function.NoneFunction" customName="累計欠租"/>
<ChartSummaryColumn name="index13" function="com.fr.data.util.function.NoneFunction" customName="下月應付租金"/>
<ChartSummaryColumn name="index11" function="com.fr.data.util.function.NoneFunction" customName="當月欠租"/>
</MoreNameCDDefinition>
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
<BoundsAttr x="631" y="36" width="731" height="422"/>
</Widget>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.ui.Label">
<WidgetName name="Title_chart3"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<widgetValue>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[='  '+'欠租指標']]></Attributes>
</O>
</widgetValue>
<LabelAttr verticalcenter="true" textalign="2" autoline="true"/>
<FRFont name="Agency FB" style="0" size="96" foreground="-11976882"/>
<Background name="ColorBackground" color="-1"/>
<border style="1" color="-1777440"/>
</InnerWidget>
<BoundsAttr x="0" y="0" width="731" height="36"/>
</Widget>
<title class="com.fr.form.ui.Label">
<WidgetName name="Title_chart3"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<widgetValue>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[='  '+'欠租指标']]></Attributes>
</O>
</widgetValue>
<LabelAttr verticalcenter="true" textalign="2" autoline="true"/>
<FRFont name="Al Bayan" style="0" size="128" foreground="-11976882"/>
<border style="1" color="-3355444"/>
</title>
<body class="com.fr.form.ui.ChartEditor">
<WidgetName name="chart3"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<Margin top="0" left="0" bottom="0" right="0"/>
<Border>
<border style="1" color="-723724" borderRadius="0" type="0" borderStyle="0"/>
<WidgetTitle>
<O>
<![CDATA[新建标题]]></O>
<FRFont name="Al Bayan" style="0" size="72"/>
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
<![CDATA[新建图表标题]]></O>
<TextAttr>
<Attr alignText="0">
<FRFont name="Microsoft YaHei" style="0" size="128" foreground="-13421773"/>
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
<newLineColor lineColor="-5197648"/>
<AxisPosition value="4"/>
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
<Attr xAxisIndex="0" yAxisIndex="1" stacked="true" percentStacked="false" stackID="stackID"/>
</AttrSeriesStackAndAxis>
</Attr>
</AttrList>
<Condition class="com.fr.data.condition.ListCondition">
<JoinCondition join="0">
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[0]]></CNUMBER>
<CNAME>
<![CDATA[系列序号]]></CNAME>
<Compare op="0">
<O t="I">
<![CDATA[2]]></O>
</Compare>
</Condition>
</JoinCondition>
<JoinCondition join="1">
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[0]]></CNUMBER>
<CNAME>
<![CDATA[系列序号]]></CNAME>
<Compare op="0">
<O t="I">
<![CDATA[3]]></O>
</Compare>
</Condition>
</JoinCondition>
</Condition>
</ConditionAttr>
</List>
</ConditionAttrList>
</ConditionCollection>
</stackAndAxisCondition>
<VanChartColumnPlotAttr seriesOverlapPercent="20.0" categoryIntervalPercent="20.0" fixedWidth="false" columnWidth="0" filledWithImage="false" isBar="false"/>
</Plot>
<ChartDefinition>
<MoreNameCDDefinition>
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<TableData class="com.fr.data.impl.NameTableData">
<Name>
<![CDATA[ds2]]></Name>
</TableData>
<CategoryName value=""/>
<ChartSummaryColumn name="index12" function="com.fr.data.util.function.NoneFunction" customName="累计欠租"/>
<ChartSummaryColumn name="index13" function="com.fr.data.util.function.NoneFunction" customName="下月应付租金"/>
<ChartSummaryColumn name="index11" function="com.fr.data.util.function.NoneFunction" customName="当月欠租"/>
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
<BoundsAttr x="633" y="297" width="366" height="281"/>
</Widget>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.ui.container.WTitleLayout">
<WidgetName name="chart5"/>
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
<WidgetName name="chart5"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<Margin top="0" left="0" bottom="0" right="0"/>
<Border>
<border style="1" color="-1777440" borderRadius="0" type="1" borderStyle="0"/>
<WidgetTitle>
<O>
<![CDATA[=\'  \'+\'當月應收、實收分析\']]></O>
<FRFont name="Agency FB" style="0" size="96" foreground="-11976882"/>
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
<FRFont name="Al Bayan" style="0" size="256" foreground="-1"/>
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
<Attr isNullValueBreak="true" autoRefreshPerSecond="6" seriesDragEnable="false" plotStyle="0" combinedSize="50.0"/>
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
<FRFont name="宋体" style="0" size="72" foreground="-10066330"/>
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
<FillStyleName fillStyleName=""/>
<isCustomFillStyle isCustomFillStyle="true"/>
<ColorList>
<OColor colvalue="-7881222"/>
<OColor colvalue="-6514959"/>
<OColor colvalue="-10237754"/>
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
<PieAttr4VanChart roseType="normal" startAngle="0.0" endAngle="360.0" innerRadius="0.0" supportRotation="false"/>
<VanChartRadius radiusType="auto" radius="100"/>
</Plot>
<ChartDefinition>
<MoreNameCDDefinition>
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<TableData class="com.fr.data.impl.NameTableData">
<Name>
<![CDATA[ds2]]></Name>
</TableData>
<CategoryName value="無"/>
<ChartSummaryColumn name="index14" function="com.fr.data.util.function.NoneFunction" customName="租賃合同"/>
<ChartSummaryColumn name="index15" function="com.fr.data.util.function.NoneFunction" customName="多經合同"/>
<ChartSummaryColumn name="index16" function="com.fr.data.util.function.NoneFunction" customName="其他"/>
</MoreNameCDDefinition>
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
<BoundsAttr x="631" y="36" width="731" height="579"/>
</Widget>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.ui.Label">
<WidgetName name="Title_chart5"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<widgetValue>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[='  '+'當月應收、實收分析']]></Attributes>
</O>
</widgetValue>
<LabelAttr verticalcenter="true" textalign="2" autoline="true"/>
<FRFont name="Agency FB" style="0" size="96" foreground="-11976882"/>
<Background name="ColorBackground" color="-1"/>
<border style="1" color="-1777440"/>
</InnerWidget>
<BoundsAttr x="0" y="0" width="731" height="36"/>
</Widget>
<title class="com.fr.form.ui.Label">
<WidgetName name="Title_chart5"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<widgetValue>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[='  '+'当月应收、实收分析']]></Attributes>
</O>
</widgetValue>
<LabelAttr verticalcenter="true" textalign="2" autoline="true"/>
<FRFont name="Al Bayan" style="0" size="112" foreground="-11976882"/>
<border style="1" color="-3355444"/>
</title>
<body class="com.fr.form.ui.ChartEditor">
<WidgetName name="chart5"/>
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
<![CDATA[新建图表标题]]></O>
<TextAttr>
<Attr alignText="0">
<FRFont name="Microsoft YaHei" style="0" size="128" foreground="-13421773"/>
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
<![CDATA[ds2]]></Name>
</TableData>
<CategoryName value=""/>
<ChartSummaryColumn name="index14" function="com.fr.data.util.function.NoneFunction" customName="租赁合同"/>
<ChartSummaryColumn name="index15" function="com.fr.data.util.function.NoneFunction" customName="多经合同"/>
<ChartSummaryColumn name="index16" function="com.fr.data.util.function.NoneFunction" customName="其他"/>
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
<BoundsAttr x="633" y="10" width="366" height="277"/>
</Widget>
<Sorted sorted="false"/>
<MobileWidgetList>
<Widget widgetName="report1"/>
<Widget widgetName="chart5"/>
<Widget widgetName="chart1"/>
<Widget widgetName="chart0"/>
<Widget widgetName="chart3"/>
<Widget widgetName="chart2"/>
<Widget widgetName="report0"/>
</MobileWidgetList>
<WidgetScalingAttr compState="0"/>
<DesignResolution absoluteResolutionScaleW="1600" absoluteResolutionScaleH="900"/>
<AppRelayout appRelayout="true"/>
</InnerWidget>
<BoundsAttr x="0" y="0" width="1362" height="766"/>
</Widget>
<Sorted sorted="true"/>
<MobileWidgetList>
<Widget widgetName="report1"/>
<Widget widgetName="chart1"/>
<Widget widgetName="chart0"/>
<Widget widgetName="chart5"/>
<Widget widgetName="chart3"/>
<Widget widgetName="chart2"/>
<Widget widgetName="report0"/>
<Widget widgetName="body"/>
</MobileWidgetList>
<WidgetZoomAttr compState="0"/>
<AppRelayout appRelayout="true"/>
<Size width="1362" height="766"/>
<ResolutionScalingAttr percent="1.0"/>
<BodyLayoutType type="1"/>
</Center>
</Layout>
<DesignerVersion DesignerVersion="KAA"/>
<PreviewType PreviewType="0"/>
<TemplateIdAttMark class="com.fr.base.iofile.attr.TemplateIdAttrMark">
<TemplateIdAttMark TemplateId="be6b7b22-961d-4f4b-8a30-02289ef2f4d0"/>
</TemplateIdAttMark>
</Form>
