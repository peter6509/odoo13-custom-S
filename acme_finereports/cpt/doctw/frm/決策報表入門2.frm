<?xml version="1.0" encoding="UTF-8"?>
<Form xmlVersion="20170720" releaseVersion="10.0.0">
<TableDataMap>
<TableData name="ds1" class="com.fr.data.impl.DBTableData">
<Parameters>
<Parameter>
<Attributes name="地區"/>
<O>
<![CDATA[華東]]></O>
</Parameter>
</Parameters>
<Attributes maxMemRowCount="-1"/>
<Connection class="com.fr.data.impl.NameDatabaseConnection">
<DatabaseName>
<![CDATA[FRDemoTW]]></DatabaseName>
</Connection>
<Query>
<![CDATA[SELECT * FROM 銷量 where 地區 ='${地區}']]></Query>
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
<NorthAttr/>
<North class="com.fr.form.ui.container.WParameterLayout">
<WidgetName name="para"/>
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
<Background name="ColorBackground"/>
<LCAttr vgap="0" hgap="0" compInterval="0"/>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.ui.ComboBox">
<WidgetName name="地區"/>
<LabelName name="地區"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<Dictionary class="com.fr.data.impl.DatabaseDictionary">
<FormulaDictAttr kiName="地區" viName="地區"/>
<DBDictAttr tableName="銷量" schemaName="" ki="-1" vi="-1" kiName="地區" viName="地區"/>
<Connection class="com.fr.data.impl.NameDatabaseConnection">
<DatabaseName>
<![CDATA[FRDemoTW]]></DatabaseName>
</Connection>
</Dictionary>
<widgetValue>
<O>
<![CDATA[華東]]></O>
</widgetValue>
</InnerWidget>
<BoundsAttr x="130" y="25" width="80" height="21"/>
</Widget>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.ui.Label">
<WidgetName name="Label地區"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<widgetValue>
<O>
<![CDATA[地區:]]></O>
</widgetValue>
<LabelAttr verticalcenter="true" textalign="0" autoline="true"/>
<FRFont name="SimSun" style="0" size="72"/>
<border style="0" color="-723724"/>
</InnerWidget>
<BoundsAttr x="50" y="25" width="80" height="21"/>
</Widget>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.parameter.FormSubmitButton">
<WidgetName name="Search"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<Text>
<![CDATA[查詢]]></Text>
<Hotkeys>
<![CDATA[enter]]></Hotkeys>
</InnerWidget>
<BoundsAttr x="230" y="25" width="80" height="21"/>
</Widget>
<Sorted sorted="false"/>
<MobileWidgetList>
<Widget widgetName="地區"/>
<Widget widgetName="Search"/>
</MobileWidgetList>
<Display display="true"/>
<DelayDisplayContent delay="true"/>
<UseParamsTemplate use="false"/>
<Position position="0"/>
<Design_Width design_width="960"/>
<NameTagModified>
<TagModified tag="地區" modified="true"/>
</NameTagModified>
<WidgetNameTagMap>
<NameTag name="地區" tag="地區:"/>
</WidgetNameTagMap>
<ParamAttr class="com.fr.report.mobile.DefaultMobileParamStyle"/>
</North>
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
<Attr lineStyle="1" isRoundBorder="false" roundRadius="0"/>
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
<FRFont name="Verdana" style="0" size="88" foreground="-10066330"/>
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
<FRFont name="Verdana" style="0" size="88" foreground="-10066330"/>
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
<newLineColor mainGridColor="-3881788" lineColor="-5197648"/>
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
<VanChartColumnPlotAttr seriesOverlapPercent="20.0" categoryIntervalPercent="20.0" fixedWidth="true" columnWidth="50" filledWithImage="false" isBar="false"/>
</Plot>
<ChartDefinition>
<OneValueCDDefinition seriesName="產品型別" valueName="銷量" function="com.fr.data.util.function.SumFunction">
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<TableData class="com.fr.data.impl.NameTableData">
<Name>
<![CDATA[ds1]]></Name>
</TableData>
<CategoryName value="銷售員"/>
</OneValueCDDefinition>
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
<BoundsAttr x="0" y="0" width="863" height="254"/>
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
<Attr isNullValueBreak="true" autoRefreshPerSecond="-1" seriesDragEnable="false" plotStyle="0" combinedSize="50.0"/>
<newHotTooltipStyle>
<AttrContents>
<Attr showLine="false" position="1" isWhiteBackground="true" isShowMutiSeries="false" seriesLabel="${SERIES}${BR}${CATEGORY}${BR}${VALUE}"/>
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
<ChartDefinition>
<OneValueCDDefinition seriesName="产品类型" valueName="销量" function="com.fr.data.util.function.SumFunction">
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<TableData class="com.fr.data.impl.NameTableData">
<Name>
<![CDATA[ds1]]></Name>
</TableData>
<CategoryName value="销售员"/>
</OneValueCDDefinition>
</ChartDefinition>
</Chart>
</Chart>
<ChartMobileAttrProvider zoomOut="0" zoomIn="2" allowFullScreen="true"/>
</body>
</InnerWidget>
<BoundsAttr x="0" y="230" width="864" height="254"/>
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
<![CDATA[723900,723900,1524000,914400,1066800,723900,723900,723900,723900,723900,723900]]></RowHeight>
<ColumnWidth defaultValue="2743200">
<![CDATA[2743200,2743200,2743200,2743200,2743200,2743200,2743200,2743200,2743200,2743200,2743200]]></ColumnWidth>
<CellElementList>
<C c="0" r="0" cs="4" rs="2" s="0">
<O>
<![CDATA[地區銷售概況]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="0" r="2" cs="2" s="1">
<O t="BiasTextPainter">
<IsBackSlash value="false"/>
<![CDATA[        產品 |     銷售員 |           地區]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="2" r="2" s="2">
<O t="DSColumn">
<Attributes dsName="ds1" columnName="產品"/>
<Condition class="com.fr.data.condition.ListCondition"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Result>
<![CDATA[$$$]]></Result>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand dir="1"/>
</C>
<C c="3" r="2" s="2">
<O>
<![CDATA[銷售總額]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="0" r="3" s="2">
<O t="DSColumn">
<Attributes dsName="ds1" columnName="地區"/>
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
<C c="1" r="3" s="2">
<O t="DSColumn">
<Attributes dsName="ds1" columnName="銷售員"/>
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
<C c="2" r="3" s="2">
<O t="DSColumn">
<Attributes dsName="ds1" columnName="銷量"/>
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
<Expand/>
</C>
<C c="3" r="3" s="2">
<O t="DSColumn">
<Attributes dsName="ds1" columnName="銷量"/>
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
<Expand/>
</C>
<C c="0" r="4" cs="2" s="2">
<O>
<![CDATA[總計：]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="2" r="4" s="2">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=sum(C4)]]></Attributes>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="3" r="4" s="2">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=sum(D4)]]></Attributes>
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
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="SimSun" style="1" size="120"/>
<Background name="NullBackground"/>
<Border/>
</Style>
<Style imageLayout="1">
<FRFont name="SimSun" style="0" size="72"/>
<Background name="NullBackground"/>
<Border>
<Top style="1"/>
<Bottom style="1"/>
<Left style="1"/>
<Right style="1"/>
</Border>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="SimSun" style="0" size="72"/>
<Background name="NullBackground"/>
<Border>
<Top style="1"/>
<Bottom style="1"/>
<Left style="1"/>
<Right style="1"/>
</Border>
</Style>
</StyleList>
<heightRestrict heightrestrict="false"/>
<heightPercent heightpercent="0.75"/>
<IM>
<![CDATA[m<j1]APLm9]A.$h5?Loj[A.CHT^#='e-`aDFS'd5%^aR"Gu&.hF#63u.7/;gAS-r[2U6,kU>+X
dBqA<9%n65!l=OG"bZ,_XrdHVRcg5.CL`oK;lYAcKT1I&q7i^"1p+HIpkTIlqU[Y5".%7fWN
Sn]A9\X:'(FdD?.J!?[eXjrMJdV@QOQt+*-GSDb^H`:"'ep,EV+jMqYf"58\S(jSH#Tf%Qs$1
g',DjCe@t<DIk,Y;p5]A2HlF8niCHURV2*&7_*uClfHSk\%4ggZ2F-0G"(,`bH?mFhgZaGBuT
7%A)gW0;tbh,Rh'l`,PU_`mA^d7H(PD2*$@XPOcgK"$tBLCS+M6QA/`\(^LDgC\BMCoFP7BT
0,?K#Ti*Rm%d,8Zi"+!'>dr\+]AZ<>/gNY/67(EdWP8<-sia@hQE<diSOUrP\.7'0>BQ;*ZdT
,0-oRm/bp0=PZRo]A$*aXG^=l=k%&VVj@XI%sfCddrOge;l!qr"-]A!?^rd&+`RTr<f)!)UK8=
]Af\a\7c3Ssk]Ak0c'fh\_%cu/JeO9+.u-0J.b"n6G?'/;u5IVm6bUXVFQ2m?hd&XCV432&UA_
T/BNS):mTEQ_`Gd0)X%*^9eb>T66TV5KP-]A%*LL\i90*^gE3eE0olAqn"U8d7^2c\[g,d*?O
<,U+(rZILU<Xn&$1MpsiYBKHRtPE'kQ5WE@Zr9[FZ$n:V1^r2THOdr0WbMY9RGTp30apka]A?
U@?W\8u<AMM0$S?J+U2.RK>H@8,2p4AgGR6`X4e-@IY$&do*7&P.*)i.RE`FJ"oHsp8e-4pq
[Ec^#5*F4W2U^V0ZG`?k0@.(m'h`%a:&_;$i"h:qIY-OGLgUl@IP&<H@En&%lS,6eb7@RbRH
?,#r&pVVkZKW=E4uq3L6*i8.aZ:q2=F-2k&R#R(j,IT]AH/6r1B8#k+hGlgY3jO%[2IcejmIc
*N'Z]A-<s;$R0E"XlF1>]AH+u%-QIiVOr),R$6!A\6.f\=f!rSaJ:%XSdlO?;>(KZU'"m/$_9!
m_\(!_U\6$.=rq1KM>6]A&m\-?A[b'.F@%nk:JN5jLCq@T#FRb)U3/JUkb@#5AAfTL@/:R9;C
r[rRgkoi$-"QSdr.6/#cGb&%ZMV):;S7@DAY/q:sWB*M0)j8L91do1i:s#PS534LA\#GMl$W
g=O\"qr8Wc27*V_oO4o,PSk^mWc$J(<QNp-FFEic8Qo`FD0]AT_-TI4gjk*[MdW*ggAle#tV\
t?]AcW,7DmU6Hpr/WmSGU!YfZZ4)c748_LKFgR`]A\8.ND".IH0j)#2p;#Xk$omNM->M*7BVGK
X&#G>B^D(&`i2fho9/W5J[0\L0"K,NcB9ujD4E3q6,B2/;ld.N>m!;rWp2p;E/gsEeT^#I*7
oL<uu]Ad=,_EI"8qs,K4%:,gFnO<Fq=CE^>7cXfL=,&P<3sY;n?Mc+4oTXEYA\+'Ej6joU<Sf
"n]A8I22i[;8:P'UjNQAon7THu=JF+Q$20PSk<AGF+%)cc?eVKD=+p9,(>[_%*p8=K4nD'DC0
-k<A=c/pp$gcuS#[CWo5((feV5/=F;?/]A$>nf#G.1W^M3h%;e=<A")>Q6^*X6H6+p+ruR8^`
Ym<QaS3DE/![ni]AZf^sLdHJS?`m;CZ&+!]Amn@iXl`nI#h:T0`/b/(46"b5E33M2keTD8Y'*Q
c_q@a!!(3_NMOh;Z?hoUt4P,8;HUF1$F\To9_0,m$?$0#=2W*ic!+J3mMiEJ;q%=f%L0IdLV
l/'3iU!K+<:*IQj!)UlW$HFt-m:'*.USKh^+a\WiK(LIQ3bNIn2a"cHMeASa2c)i2J;4!#9`
$-t'>W&1VYPM^Ghm[rT]A9Zpe5"f)cROc_jZe+9?>+7LKsFu.E/>6Vg0qYRcANH.X+/uMQ;5E
qZN2+OK$1gXgEZE)]Aiist@H!eD+P6L4-q$Ybj[]Ai1bn_LeE:&oJ*$RaVse!tp@4jNO0#*h,@
.V]AK#J^#(X,[YieXnaS.p'JeR>M&/c>B0p(kM0>R7$p+%^9#"[tOs"oo=PqtIHBWn&!kskNH
13_nTBOk)L#`u;*7tM!4_jY,_9tLNQO1>s4Z<b#EfL,_mhpS`-`:05c(F]A#Di(u^W^kL@p;j
EYMe&KuT:2n>s):D3!XXWh&SfYGT2r/O6ijh2^W@T)1;YXiYQ1M@L'<I'\b:IB]A&gKUfIsVl
P\s6A&5%8#i4\arUrH#e\k2?ONX^+sKto%"#ZZh2.u$Z$M&5IJOf=iN5iTf6(6D1cg4U@'2C
V`3(I1%4&XU08jDHHs]AMsk4#DT^Ym!JM!$\'jVJS+3ai0J<+P4KP*CdnrmreYkOgEXe]A1nmt
Mnl+<@Xn&/r8GF;\Gcb-JeneZk*g#l1Af:Jh6J^/ITog*rpN#DPIY1hkKhMUle\j7LhL:S_E
QFI7c88`9<&/DZUO2i!C]Ah.*$F0K9)>qX*VFp0+Mtb-1o5DC+gfIBiUf[('k`oA^opXF;'0u
UgH\jGgAB=-QT9AR0cXfPGg$WZ0[.aZ5UHeMnc5GD9osG]AC5O@s6_Z#cZN?"1,K\k7b+TNg&
Ge%h\%;KHY[[=RqcngN/DiWUp8.B<h/g$JQcA[?:I-'ZKLmTiib<lQtSg.0.LIgR@"&!&sT!
'J%Q^25]AMKmd7kLPuc2J.#YU3E$EbM*9'L)MrS&^eGj3I:oA\a!#iiF;dEHt5gM99,a92mla
)Y[+@hb:9P8@lQMLK[8.6K*c`\puYBTlt5F-OtU<7+?U9(0#q?'g8WUdc8(5Q9IYEA\aWi=M
!Y;TH#oEHb1XDAh^.0%&,VdFgk?R4B(cDU/Oo'M(#@qJ<$A83JYB86[t]At#/eqF3Is=fAA@3
P2l[NT..GkH7V-mQ'ja?@=6uHcZ"BsF%S-dC4pt0;+GTB#CgL/8RoV1^/aH*;hm,tC\Yc`A8
[9D5(X(@:-kW7EJSC*KliS;0GU"c33?4e+,."H&7-OUJUT(u'(ju[&,?m/bE2Gbd?#@sH#KS
ZT<&imHXQ\7L6Xlf_FUcVMO*[?M'5W.La;0"i:3Hdnk(%qp9[snANG/?8\pWdmE[B8=sEkH-
mMDi'8WV_8k[\j=4=>q(#B#hC9Aedrobe,BZ\uFh7]A`LI/ofqh.9\5>UpJO&1[,_)H,Pg)!N
ACE58Oq9o%3a#pqV:eO3g^D[X7=FAZehnH<p-/4.X-=ASq6s@C=G),+\+smMR[GUkDa<V]A^$
4'm!O\6Y0:?!4ZAAh1EUM;M"g$qTjiEld8P(.c[r_7G@RCg'MjpL)W%P\2oeC?WlJEr[_Y-7
!5b<F")Qkg\\`^VP(,GM0[q;kO&dbTAp^K9"8N19+05ar/reT+Gj1F?'iU*jm^;hNoB(Q!/L
"#LAS%92B\cnSUtp)8GM&qqf<)*=4_s%X^Yobl9Oh1fk&umT\h)1Hj)8U4I\imCSPdA*0bV\
m!CW&h2$+s,]Aqm83=[@.LRtrcrc%4C%YHqntHnS>^:S]AZ8bODL?%!S]AV]A\(DT?RPUf6fG(Fn
f;e2LK5b7/ju2F6lIV(/s]A(KoWsK2Sib0QNkJ`%CJ$(KRm$"DDsnt8:;9h\7"$i).1Ur9Mo?
]A52LBDN<s?*/RKCHK3M*umQVTDf&i;E>PZt=)^6^gl1&mNu3PY(Z7.PafQ\X90UN[=J4qIQ^
N%%`^s7s^Z`HFq"kh%N>LX:aQTF@BqTs[S`ndtT^mJW^c_!Hr9ji.;H1]ABJCEi\E]A3iFrRWf
hQsOeu?9U5jfZW<1G+AH50npYc*<!`Y(T!]AIM>W2=8.oo8O?pHI4XhnL]AXOb61K)Rln5*0M:
0%q-6;XXmis+W6!iP7fe*`74>cYn0+NK\i\2D"YueK#<4N"5mB8ep>ma*S8`fi[GQoee_p7T
*)$PcBP-G.ho+U]A26la/Xb(MgkCWR0K`j5`NX(fk808cVFs:q*pkD64hJ)%L*BVZe)O^H>Qg
<Tko6_r[u.!pQUBL/;I[O(JoDani1Xr1H(6/(O+<ZOBM=dEq/U[`cq+aTW7HlM*^=*YFq\50
l33aqd!I[eeRX[>Jp1[0:W2*iST,]AUX+6d^A/riaZb4E2.<G6n#sHfV!X"'JK*NkrDAdTNfK
%i-1R0L7)RamdSVo4RR*>O84/NZTH\7hZk@SZ@@aM`$#dPc*_c5,eS6L<Grn=d>@XZ[&6=0V
u/o![DQ[!!1LQ^7o&Y$6h>Y-3PY2*+040EZ@HK>U*IgN8PpcW,=ALe=,cMH3/B]Aer)Z^oqsl
G>p#WReL@nfZuI^=BP!Ld(S.o_m<-MTiG0X.uoWB,`o1)qF!'N9=OjT"_CuerF>I&F2;QFW)
C9)tb6-aeb6_oB1M1C2*9)H_$,(2@`La8p+b^a(IWdID_l;G*@PE"A]AV2S/U0tmsfa6XitCJ
PFX3B)9P6"W2e1=Y"[0]A@)<=bT5PiJ\OqPI>2+26omef.mQ0Z>q/VKpq9iUB>%%r*,Nl#q,#
//\0I["[^#@5:6#N!<-mZCcHQSg*A3HTQJP>L^bXVK+[HN^PK76#Ms(XMOKq$)1i;qc$*%kb
7buAVKWKAH8N^,&SAmWj;B_IDAraAIgGZ_l?YbT(ooBIKq4dmC0&qWs:T)<rjrGZ*HYM7"%;
)]As_GQ?FW9T0GZ<)`:Oe_KN,"LK_Y1M1kG>^tg"<9t>IN0qXj(3+<;G"S\as-1_&FHfF`[e9
)*%<D^GShgcuV(BO<arihqFD4j$Z(<u-DB]AqU5&:bQ#Z;807=;d@/aQ!;"8c+TJgM:!g!;]Ag
P[RL=!\kYi&hNCbG%SAUZKS;YPl8=:XtJXE]A8@sJZh;K9WP#5nlA0%]AWMSW4fV=4?^`Q+gp]A
ICA.1Mou.E1Hil2_8D5E(`2J,MiK;F&tKHqL?(iS;c6a=kfSaY(HUpl(m2&Tq^WY5Dd!J^]AC
NR*]A"RrUIanKJtR$!5&toT4/eR!30=1;DjTb[AE,\R24#e2meWl,U7/[d>Wcm3k\A#HLQ>lq
i)A&AS!VKLlmY%G2,-fiDgXua6:F9R+=ii@mVnJ#ELZP_gB<grQcd!T?+LDiR+C\L/.C0]A]AH
[9<?#LiVI$%UCjU)Y$bqdm9bM%O9eOqn'V,F#CRQk6+f9;'1<_UB^(?8#Adr-AVp1XsMuYhM
RnC[D7GErI?hL3c?6VL8V^U@6qGZ\ARN.s<WT@?,?o"p*Z2Y20C@d<_Q2h4e2%SJ>+FKB/I]A
Z!:Q<c+4JPBLkV\QU,Wrr`_BDkTOWYF.:bhZo<"Y[E+8j)CP4%ch/;0R2`08'V#acd>hNG@#
a=3*)n>TNY,+d6[Neuh&53R3U[9D%r:'Vc_hd?7bs*a=__H@Dh8.:+#tGB8GN,J,^&U&7G9E
u?(ufJGpuFZ"V8C!\t=!UJV^/J\WqD1rAtL"4*cSP:/<G.0=3cS]AFrbGrUiLdenE4M5mIol#
!pA$eJ&neO_cQO$&"PqtNJrR[Fs."2@42"2&+^eXZ([fqb`S/@h2>g'9b]AJ/hs]A!ad?d9@oi
<;NU28&n@XAef%BqJ[jN\.cpp)WO6N$EJ#?s*caB0]Ac"m@RR3DU!:g-etd3?kuU%_8Jf?`jB
1/;]A:PUrEGlA%$OGjaZ`V5=5@(5NfN#DQrY146p&\*W*LDH17SMm_q1X&)-OnQ_YXt[9;D"q
s>YN=b5!Dt-Q*p)?bP!J1Xk>XH7MH.[.\nCuJCu;j0`@WW^#-;D")`dAn@<3/&L._m7b@i'@
m<#uPqt0r(/ja8Zp>*r:&iXS1b!#lZa01_:>dhbL*JYOFVZfK,c3+Tf?@&</^uR.rBdW?]AoC
Auhb%Jb[g4ATaWT-sgftKb/_;,6Mf'PQ2]ASSejTS>3Gbe'4LY.C-q<K$N0cF!Oq0N''9:HQ\
%i^\q;NC'f.AdH!nS:FPhoM*4m>'^BeV3L/eA\c9%)9DU]AXh5,^mlup@ncc#+u&0s4Z:[^G0
T"j/.Go-!iZdoP=_;+O_@FdGZ4ol57c"%+IkDC^'E.I]AUp6mY&_+XV,NXC'8bp8U7&/u4S0f
'I,pTI7nUjVb/*PuG"t:+'ue/2pV\`QUb7EU(S_aA;_]A_KH5W6-*3TM29S\%m*]AD/1bZdi-&
_W-%!nn>a&fhWH/6QFXQtfX*$rPjt(P^5*CO`$C35I;6ek[M`!I&%NXp7RVqVI680Q7PRWQ>
JgV;DZV-ddR7ARsDDR00.#'+DOK2F\e5Hpo@!QH?YD)sf/Ab9.=H9)dM(SI0Yqq)*mp.;`QD
Suk5m?YD9M-3k(]AaQ2Gmd!flE'["]Aj:j5S*:[',Wi@OPW0HsR\W1#l,GfKB^_!lVD/ilOp%^
IlfUr2FE/ZBG8foDG1n&h5ZbgFk<Bm#[Rr,r!O>#guh52a^KCKU.mM[T.Ur425Ig7I]A]A)+_`
Hh?`r<Q9W%^Lsbd67e&TJOR=9[al>.N?niD.Bq=P+AI^988BasiNMRmj/1\=R`c*rbjJ\-;C
Cdk25DF2?ba>DhKgV+uF"Jg,mS-f#..[`2BRAD,4u*e4UDjpakWb[S0dP_JgPr+2H%L<*HYc
#":A&/95Wc%#9QR7U=?j_p+^+u]AS&IX>$K`2'7?M6fa4[Z$VDHWIDo0,-82<A3/@s<_=X2)@
@72I!K#L^b^d4":>D!M21qDj:pD=:>CH77"Sp@L)P(%2K[:$ie*eUJHR(o1Y!Y-SJL-%f`MF
Sp"P*847@sWI4+Dk2)3(DQ\=&C07]A*:tK4K.4_l(j/h4eei49Gif50:kZg//^i1TA(C5Ib<J
;]A(?>OU!3,ns)lc7YPDeV,\LR_&!M+YFD_:;^i:[+58:*6_ErpXWCdrJFh!ZU]A!)oPAdpd"_
N^m^?7+p@K-mulB:G9Vau'_bXj3J)/Cb?A5/F-Y7[=fiR(/EXO^3QO?W``,Q>!hhH>"M9"Z-
j&OHqPB[)!)>a'lE9B=q>=;[7n+R*I[Y.s0R93R8l9Ub0koFLD<)IC2r%Vbo78h`4"I>UEMI
=YS"]AQ'jQWB_24\Gs4RE7QLmO'kl#F!^-<HVA_Oq5^KRUfjc/$7RZ>,.*7W]A^UdO`l!7=<f;
.LHIDobf.<e$6n%a"H@U,,*POtE4.je.,U%8fL\Q5[T5M'H/'6)0Bii<@I@Lj"Gf^)VEG.sZ
2?Z9pDgGqHWC-Fo1bu/jpc%AC7Qg`23im[QkO%Cu8P__hphr_NH&XK")1g(3VH0/C735dh]AT
#ViFA#*chMA[0X0K#0P>@R^^N>jQoJGE38Bl5;2+>.V`i[e5K@O>():t6M4/L;B!7HqfWaIm
7%AB`f,o+kQ'N9X4X5^<[>@ZlC-abOL>]ArY9uKR%,55+3SISK7"iKlco_LtRO.r,>t#\R*s3
!*.&ZNlGQ>/r6)5$*r<'>79"@puh+8'P0]Ak(h,A)0)#ifDAih*&dZ'$^?qX3q;-7rCoN%J_;
b/(c/*KdbBr277ujW\/77bab`ETRA`4g_Zf.G=rT2^:ads//b@mSE[LPhF*82D$CJi+J8qB5
R3sX0m8oZ7`#L(SolDUUC.ZHk8NnW#t0Td(HVWJi2A"Jf$"#V?Edrd3%_2UpTdeYNUYZQ;>f
kMMU+5gGJeR[q%%PP>>njdcY:s2\h7PhfTV'l%sW@3sO<)RO,J4S&?`nnVZFX/7u&Pnn&T9l
!_Fgb.?#o9d.-TY0;*#<Au4U(,`VO4aj4G>AH"R5"2*R9J-#FRS@D2)Cg_AgdN=".YO,P3a`
`!1r*?!!jfqa<0_;U3^Q:qDt%12Z7skqMc7dFG00Y9#N>a&g:b*6=HlBI!sCrG'Ol3I%CN88
4ih:[AIgR8IKrB2XkS'?f6d;5L&%0HAj#^Vk1$m2;["anOrGnhL$\$d6he,!Lnk-h3)j`*Xn
k9_u_0/!Yc(5"mS(p#DDnZS>+U[a<!G_V&IVT!KP1ZI_*uNp;QHf5Q!eUji!jAK51$H!fHlj
TG[mC6<O[S_K-LcZ"@L3F,g-PqRXJ);b%jDd:uLnTB*C;HgL=]Asr#T($(lYT?m,sCr]AV:q1Q
H5qSl`Xo;g3uHbX^-5?^9tJ%Q-$>>%%&SS*.kD2[6/)`MrNSp!):_a;oJao)WH:\/?Y9Ti%+
8a$="h/IAa<Bf;<]A;[Q4@H-W[Co\b<(1e,pdmJ<8qH;D)'TcOB*G*#8@1$hO?e1oW&m&eu1B
W.1Mm%QoZg?T^W6)X-.\j6<'E]Aaol?p'e7@YqoJuA7#RRV.jG@'Y2\8pd%8\rL-,.eU'^Zfg
lR3u'F"4rLQ<]AMetWH\-iqWHIP9c6I`M*L))?)%KM7SAE-=$t4N"j>b^V:QgKMRNUs'JXj(I
.)%,X@)upqaAJMDsZ&fS-o*'-!s0L[c_D$oSUfW4Ur_X)UW)$r)iY3lqK$EEq$^so,N0oBa&
a91K)!/DTBR5"4e@S>4iEJ:uCGrgbD<*Rej>bB&GHf(t%`XEs;:9g.^eeD]AW$>A=YqmAsm6e
E2)Waj/\>!870lj!O'Zc@@rG@Jf92eOrh";l9gB$[$Yr`kHNF\pk+L9J*b%$IA>\pbO(O%Y4
ATPUB9C'/$hIXZ`M$Q%\gJ$s5T-K4k4aP0#uIjS]A#ipE?$so'[pATN"No</LcL#FKQmbHRH?
icDPH0M]At"NQ[73q@)l=/V@8dGY/mR'c3/W*=87-@_$T6V=LR9P_&ti]Ah]AnhBbfnkhFpsEF?
L$#*eAIKaTHu2faNrB&F/KphS%)VdDOEcD(DD(V0:Ji(/UO?b!/FTq2StB,aab8;""^4PT0+
p8Q<]A)O4[[G_TZD3tq\W(-(BAHC0FE%;0RH6nbgh?-_#7,t8YnWIEI4dJGnY+:h.(JFY+Aj9
UYNHLhC]AFU'RXZg;-k.*]A:44?<k(sC!h:M7@:9M_9'`a]A`m2?XrMP$n@^[Re/fWil9>!dL0"
+)=`:;h5c[LcJCRlV==4FiXjR#Ar`6u"UC]ANO^GIupFAPiQq*dq3ae#ZK0hh=sOE*S"5NpT<
j9K58gFiMFo:5&?.n9]A+OFGo1rC#%@IaC?IJi,W"pAebp]A9'k"L-mWtTN['NQfL$0*[$3K?r
;kSU<tlN#^oioQ(RG0U<VXe8*^)sLQC5an'"&%fN#s5d[-<=RV*N/U_#kf(Z`eYi,pE487Ob
VJ2\fXnR/[IIF/OoN\j$uu*ijs*`3<ME?qm0)Y81j>(l&H%@MLSpBtHJ"GYi[_d652i3DO"R
'L',nIQOWLl:(2]A""t3.HOH130$0D?E(oIOIC>qC8$0Ed<XC'kWV5^0K;PDu9]AMZt&jFDE*)
(-Wr]Ak)6/Pf/r<M_a5/X![)iK<+8M0=-ST,=!:FI@CO'31UT?AN[q!;0s0e<(oZQH_:3YM)[
8??7qn(G:]An(jUK$'o`fk1rb/P_Z1H@R-<]A'I.*W+CU3`1V\D(Nd2CsCpSYBjm#)u!;*uKDa
i/]ApC(*$s!fPHH%=_t2Qt?s5NT5(pUf@^K#@1EK&`f4J@l.$Zh,[?Vriai&Y:1.%;n;/?`R=
-L)tiDl05o?bJ\PkA+"?$;PLn^;(NYIO>+s7&)&B<X-Taar`=Uhk`)Z:C)`WSgX^M&tN3TY!
5\-3W/`!&)0ZQmE=-#/UR[USrH&5J676Ve=@/:n)Q;.@C+/YZh*f_P=cj>=4X0CM&'b*%UrV
2U:hl!Oi?Vp2mWATq3Z%aZf/3`g*OLRNK>"eB["DrKIJtD0p-n74nWRUVp=(YE(975<<Cm2s
F75rfA)nM@TDTbP$<'9N2cNC+0maMoke$PamGF$*Gp.TD/IX<1'UM(41lEL>RN#o\0[,m_.W
hH&jVPi2q:7TAkYpicj0i/j\*IUI5hAlcV1rYGg&6_kp7+_)Wo@gZqQYK+:2B9-!@@R1D!Bf
7dZ9GTrhDUJXY<]AT9Dka?T4qta#O9Me@33"G>8h\f-nXlmJj^Yk6X_0rnNikP&a`eo4T@*+2
Tn_ib<C3tdd;$(E!`g%6)tnVb^!qP@n;?Bo:]A@>N2]AUF94(_fQ@,*CN`5]AtN'Z!Du:)t#6_6
obh[SPVS&gist#!dcQ.B7'g5OS/A(#5KWXq'`1p9q@u!-+pkTJlUpWX.0"fJ3_!r'mmVbJs6
\Ts6Uq5e^;A#PLJK?4fS'gi"p(k[pLchs>=9N(Rf"DhD5Gko/WqW7VcV=u1SsZf0hWZ_]As=g
?c1-3jD?q[I7EON)jSB/V=jr7]A"rm6EWRH-+A[&U![CJ<P0i58UX]ABNpYAk%RB"Onrs>lC7,
rc,r)jC!8k(p&hRF%O0r?-E4)D><pO56#UhKkW[RpE`h?Jm")B%iX6GopGHQ@p?:=G`@UUe1
)KNPs6`og=lA@JqZElubFf]Adbc]A)tC4Q.p/,;M\@bL5:#oufL[q^?"M>cd."Cj,="?W]A4ME%
`ks%,oL2r>/Di5'RqGAD#1KY^Q9lC!pA!Op;K!1-+EZmNp8KebZTO,@[d_R>a5dJg3,da3TB
KrllSKY[<Os_`V8=H'l3_69$W;Eh'<ilKhAu<q2Mc15n&VT(()$$V+7uGaD$>F6&*AJpSN[<
>&,r'NpYnpNG70WckHkC&'A*J2;dh[W'(oL=31i(6*'l6>i\YR!smgNp/OOQr>k'cFp:FSA7
l@e23dA92MKY5@a+7Z]A+IW,Yj\/B)+.E.Nn]A,`,.%<Qrj'BpWQlR);]AdWBUFQ5;B&51RUn`A
P8E\?1U)7j3'K1O>duW@IMtRpT#cGmmPB#Z6OXH/),AXWNQWu1KZ9k`Z<#=/,;q6GqgeQrJE
)HZR2*LIX\uI\CZ`7b=*-_j(nP/Y0,e5nNaO1BYn:itDj#QEfTI6a2pXJE1=,+2A&P";:I14
'mi[dnU6TYSMc+goag?CjT]An4'Tr'ULMN(fe1k'8L?G2Z!MYpjQ+1oYGA8<;10mQ4-[hg"5T
l`\1bQ9-8_/QtETMktLgo_\^#(d91o7QT9,gD;]A1VnnCTqqc'A`pZD]A:iT2mpU:'F$+>tX1k
&Q$;Ud\_j?7m>>i"[7op8t+0D+DH.PqT[U+0E9Oj%7)?_jc%4:,#AJMuAHZc6TR6_Z9SC2fI
Z5=t"%uck1ndD&*Vc2cFf^>W^M[N3^N$)H^JV?]AH6q26-\pQjPA_grkrb57\.*-M@A.0a0><
06Y\a?o1Ib>e<3')si:=u^K5UD9YaZu2cbD&C>Z?0$-OH*l<>M?.1M=+M-WTdYM2d7"7)/UV
W,p5[OpM8s4+?HWC@-GtqCH!`d`)d:+3D1]AfGI#tW;kIM`>K2\S*%;QA=+p#sY0%e.+Z.B=I
E]A;]A95iAe2fhLFZTU/m?!O5DU+^S.>aD/;m6W:'.Dp:3#U88)N2NB?LFS]A"h"$aj_5AWRD'P
UM1.Jn\1V?V)`JCThkJ)uDdHR\>QmliFYLD0!$]A9>U3te=-q%Df/JW\o!b_=D(F"fIR*%+k-
$iR$X0Lbkr8uu29)V3^XWPb+QC=/S0,0`<4a"rZ%$!da.9M]Aga_hkm&l^F!$K'7X)9\]A%$=Q
pF5j\K)g![^'uEV)_WM=Yb;Ca]A%E^9Pf$&#MiOrdkV!^WO6'VSr7&0e=C;-*8/J):Dt0/%Z3
8OE:-ii?]Ai5C:n0b@>2Wbm'Dd"-hR4T`E)JTDZ$?34=*MT,lG*ZM59^_Reb)KkI\J(2%D]A9"
F]Apt.Ocb*<6>,UYF#RcRu;ftQGRCE?!b_64fd3)a)]A43<7(Y@L`'74"ld#G8Qr;ZCWGmYgrW
<4roM:2J"_aQ;-+;)j%\Ojj0JOcnB18oUAU3!;UG'(3QN,LY*%tZ\nG/3L&tBp8E_T%_^2_J
mbGq[35(RV?)[b]Ar^qaY*mci;-DEXR`\7'*@l5GhRiMIG<R'E7jMP'b^QVDtYj0/dEkD(Jr`
Wf#Zj\`1$P0@4GRX6@rUo;;16Xogb413X4T(ffq=QXJe:CtFT"b3S5H[9h=PZ%;J<h"P)Z=f
`q^4gO%eB=<EZ\^F8p21fe2B\c[Y6of=C(fPr2nS9gkslg%C:5)E`[OWh,]Arls,;Y%<;1_:D
-Q1A(&>7qoD.eRpAF$0dL+q#rMt^`PcYc#a^$&g"O@<LQjDFfIG#R7,id"n:YnZIGQ.jHBmf
qG`Y5f9h\X(9=*[pUN*'8%O:?..N-f-rY=DA9]A5)NOHiJNO>W^e(&QO2RDf`*u&LmW)>Bq?d
Aaa>KmfXAbb(_Lor`77u5ZDtOk7]A6Oo67s(O`N9c"SE[d5*;6fAp(X>eCjS:lh-Bi_dF4ASN
qdla,!GhM_P#VpOMAji]Atc4_QDLTo4QpBl3.b(&Zp'QS#Nfkm<a0c,"+lP7p$es6GH;U.<CJ
uX&]A1OaKL9dj.Cfo!D_,Fq7+BCH';DN6m)rZm'\#Q$*UKWX<+,ZWtY08D'0Xi/$"`Q[\:hC/
r-a(g3pZ;Nfr)Dnf=Z%GBGuCZ5O@irAP'o7"K+P8LKCrNGQPbs5q&TBcA&UL.j;78H_Wd^/Q
GYIr=I2-!U55ECBPeRZCt]Ac&]A)A-gYC?cXX7._WFAA1tHX5n6h#XnEFKLQf^%jUk+u9G=CXh
q#?a5?3X(H+>2p?3M\4Z47(Di4&lZpT\rPM9=p+T?@CFmG6L:R#K&a=X,".'T.b-jJ9t\Mp,
^>)MR.^OA)=U0l;j7Cr6Xc.b^fUAFS5):@88oV-RUkor9UnunM33,AFKC+n<PeCm;TDo,BU)
K9G2Vn_l:=ed40jR]AW]AH^Pmo:T.G&P>`8j_6j6QEV9E:0iPem3.2$ctgb+:NQrOoMXEUs#+$
2_.POr<:_6"_`mr,:2n1.?XPd)c2ooQU=s'eV)Jrdb?(U/l&sg_SS'<L/W]AKA9B:2]AG2`\p$
VsWqe_QhJ@VKC]AJ4sW,3*$re2>a&[(mo^)%r&A]ARU'KrWnbQ^J]AEKCQNE#QCP8rt2ZKMDL-o
CmS:7FDn-X3%38GgGN`*fD%^D,oqO$`1H.th:IAZbV6o>n]AqD%EmsUnfW@ITR4(J\Tr>M.Ah
O!oZ@qSopu_U^BX1e4>>T#-5Qh[/rrA6CV=_>&;)_?riuMYSFJgTS_),N\?(CD,@#,h.A`Lb
6>Ya%4bs0YWJE7Pp(8pApjApA7p#j76?6B,=-Y1R1TB`3NV_RY5n:PLm+QmUgd,"0S7;M7PH
",07[XR*u:qXNF7,?,IoApT"AIo-lbT4!?m%;B*Z?^n]A[qCfSjc*>jlUS@I[$nL)quba9^:Z
VCBQe%%]A@c8hGHo<)gGZ]AgoIJXB;71/H(L$fKpcfJX\LG(O=$LftGV&$APV9XdgeO2#j9klc
-Ife*'nng7IlgVZ3aAi%5+jt(N7?G3+Odo+%&Eg;)6rte?bk5?4;G`^XXu<_(/e2&V4]ACl1f
c8$X[>:_Q.;U0RrM3C0l'QQFQJ%CO.ctQ"$ilUCM[R;]ACjYiC?0m!f;m:$^_FX>4+#[#.@WX
DZ8ti1:DoZnN@b#(*IT4;6=IM%4'G,\O,_a*(s$)?<[Uc[[%p8``kJ&A67k)(IU)$d`q-lNQ
RoE[$kPrHZJh/:Pc]AFK<C+X>/9B@tp%j3f0)8dIiBpYdh9D1TTh#+apj*MeI(F3VD7r]A1eMR
.eiPNH,fotlX4kn^Lk5LAC=BBcPjL]AA*XZ#a@b'R+::B,YJq@<FJVtmf9AetAf6Q>sb3uB?\
(.inol'OiPgb.,DfsU(.UdnRM]A*5L?:L%u-V,R!lq;,%*`5O3Z'CeOIMcXV?f_+pMULibVr5
1O[Iqt3INkL[+3@,Jr^8(/go7pYgjZ>oZ"<T+gT<0'K1CXI4VT@EI0(KRWblKSlhqrB&g#U?
nZKZq)I[l5'97E*T]A+8[/dW:=hd?MnSjmBZYZir430+OF<%hAP29k@4$pNT,#Y3_?LO&<'_Y
s$Di?_omU09gm0MXEdsB=>,!aXO:N2J-sWEq>TU&CMQ@XHir$T(L0aN`>BgJ1P^=M!.[plY9
I+7`X%-I;$n*Y?1&P-"R+Ib`2'3s7B^),kL?c2.+BQGG_L?-#C<%f"956fTA(HY%0ka#hTa[
/9:h(AdDDWh1@ND?[p92NQROSDJ=#FAp>2:crN895`jBE3gmOXhVnRH5a+DpH1Qg*Q0mi,e&
TO2fP`otr@sET0U^9@ltWe00@=$)G3Jl;JLI-=R*(MgXa#:&[\#H4"4P#M@SiOqO'eTpV8,?
t8g$kW&\M1FHk,)u2aoeO9=O^HP4"L$XJ[9CPl>DIa2h$eXdCX**<t)uebE&V[*L>M/li01%
U=8M_rhEb1Y@NX&-)Lm%=n*6a?clqo"K8Drr2r~
]]></IM>
<ElementCaseMobileAttrProvider horizontal="1" vertical="0" zoom="true" refresh="false" isUseHTML="false" isMobileCanvasSize="false" appearRefresh="false" allowFullScreen="false"/>
</InnerWidget>
<BoundsAttr x="0" y="0" width="863" height="230"/>
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
<![CDATA[723900,723900,1524000,914400,1066800,723900,723900,723900,723900,723900,723900]]></RowHeight>
<ColumnWidth defaultValue="2743200">
<![CDATA[2743200,2743200,2743200,2743200,2743200,2743200,2743200,2743200,2743200,2743200,2743200]]></ColumnWidth>
<CellElementList>
<C c="0" r="0" cs="4" rs="2" s="0">
<O>
<![CDATA[地区销售概况]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="0" r="2" cs="2" s="1">
<O t="BiasTextPainter">
<IsBackSlash value="false"/>
<![CDATA[        产品 |     销售员 |           地区]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="2" r="2" s="2">
<O t="DSColumn">
<Attributes dsName="ds1" columnName="产品"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand dir="1"/>
</C>
<C c="3" r="2" s="2">
<O>
<![CDATA[销售总额]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="0" r="3" s="2">
<O t="DSColumn">
<Attributes dsName="ds1" columnName="地区"/>
<Condition class="com.fr.data.condition.ListCondition"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand dir="0"/>
</C>
<C c="1" r="3" s="2">
<O t="DSColumn">
<Attributes dsName="ds1" columnName="销售员"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand dir="0"/>
</C>
<C c="2" r="3" s="2">
<O t="DSColumn">
<Attributes dsName="ds1" columnName="销量"/>
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
<C c="3" r="3" s="2">
<O t="DSColumn">
<Attributes dsName="ds1" columnName="销量"/>
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
<Expand/>
</C>
<C c="0" r="4" cs="2" s="2">
<O>
<![CDATA[总计：]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="2" r="4" s="2">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=sum(C4)]]></Attributes>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="3" r="4" s="2">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=sum(D4)]]></Attributes>
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
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="SimSun" style="1" size="120"/>
<Background name="NullBackground"/>
<Border/>
</Style>
<Style imageLayout="1">
<FRFont name="SimSun" style="0" size="72"/>
<Background name="NullBackground"/>
<Border>
<Top style="1"/>
<Bottom style="1"/>
<Left style="1"/>
<Right style="1"/>
</Border>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="SimSun" style="0" size="72"/>
<Background name="NullBackground"/>
<Border>
<Top style="1"/>
<Bottom style="1"/>
<Left style="1"/>
<Right style="1"/>
</Border>
</Style>
</StyleList>
<heightRestrict heightrestrict="false"/>
<heightPercent heightpercent="0.75"/>
<IM>
<![CDATA[m<X%W;s2`GG-X`D?;"k.$C;Z(rF@=:N6+k3(!CH-93]A1cZiZsG6k_9Z1:1&W<$W%06mWJJ<G
IXm_@Qg&[#2d=+Y&r%(a4P<JV5:Z*mSuFhVR"-=MNV@chl&=[9W$N]A]AX_;]AD&Y(BC?:`mif1
>A\kDTk007bQYfT<I5#<ZZ`lH2jpo0$!r.s4lJJ;\R0/N'p=?)O%l)*$`bVW*Ut[66pV7PPJ
[aa7BjU<)'e_,;4$35W_QU[\]A]A@pRL!N1W^2s"Gd\T."jML%JD7`\Bo%Zm1A6&1q'[,t4<o*
(kE3]ACkK7mh&5,/pBR\;IdZg([R&ei*WMU8!$GI/XKEfe9\U9S%Q?/R>I/k<)MX;c)S?7T-r
<*9NB/9<E)-#YcZ4Q2.QBaErDFhqCd,@*I*l?Q;e0n?q_Y2WZC_niM]AY%?BLF^G]Ajjq7BeCk
Ql"_dVJ\WI9@R55'.3Spe7_YI.&F"+17GCh"_%rEtBsJr_Gt<eYEoZ07f-mInAcRUj?r'i)r
-[o(AQMl%!CZ=]AW)"54"R?*Ro\H?<[c_YJ:<4suhe[mfc=[Hfj8qcV%l?@/(eJsi3)/5(.G$
*'Sh17C8)d%Vqul.mq,?53hBb`-(NWU9@@o+dAj*?U!:pD!$"J)EcZhR/B#,&\f4hR/sX=q"
>"P*gG+[nM,)g%>]A9#69Vb68ZOCbN6)^2oV<2-8&$\%\Ju*aqk`"kWJ8]A>OFm*T-nNrr?TFh
g:pniKp[,![!@S\ZT\7=k2PE*Zs>SZr^9@XE]ANL]A!VW=,b5Qr"a7@:FQ_@q[98Vr1a+r7'h)
JQ;?8+*K;PI\T^f;=5/Upo3CL6b8<d+?LGi3T2bUphAbTRp[2!f=VOS4WUkPrMQ'u\@-"*pp
p>]A'qA1k5<bA'5#S`Zkd;A)4>4nW&N:mCTrIn>"<%$!pXA9)Kl\"hs14<jiB:IAc0HAHSXN`
'pl+hL?.0RecO&j(h[tMKZ-!MNU1\s3-s\edW99I7M89GBSO7hamm8>,(0L()+0I#62"7ofL
De_eZt$J%=[R\T_`9\F^Z1@@PV@q:^_%Q(Gi$(ql0,?J9%/-lQE-jYI^^S8+eNG/H<lr[Y(`
\44BG8%Z&q'SQZc1]At/S:YE4%k:=b9TPmM^I^C[<2@Z*hr&f:aTC?sb@e]A^s!c(<7O!b]A2$8
r2!UOG4P$8_qGPA;Ztq.[=9*cm.jNcs4)^bd$04"eG,W10Y*V$=)2UTAPUUunD5>&/N8$d6B
,7&a'.,Ad%A!pRMSiEN'Z:.ao7IVggMdj$_s%@UpkoFXQ&R;:M=;K!RWm]A0m4(Z>0Q?bolG'
Js&JAf(9"bJ,Vo/R4Y^%U[L4NY,6Th,b)u#\B=+Xf4baXAkep[,fp>AF53K!$N'5#9*5TlE(
`'\d3@m]AdA\FJM5)+[3IaB2'j<CjnIc0,\;_V3-!m)WSKIapM0BJJ(GIXm_:lfR5`bY]Ah`,>
Yp28dG*kAaji-9UBtT*fL[qTDmpnUYCLu"^ps$^d'F##]A]A55JQqe+U0&(YpPGJ+sGYVY:tpl
amBa?/-H;gj8O_CsH(>i)EJMlrYc`,]AJ`<;*qiac&C]A%V)4BbHP-Ed40o#`2)BMSD^hC>U,6
aQ0EPt0If.bEX!B4#AZ<S"#XBT9_'D34nuC5VEFsj[&Rfnb:^Z%iU&87qJ:GWYG8[?4LMa*P
:*2TNm1UZHqa'+TEh-F-YJmgpXmg+jJie;o*t79>si5Z*&W5LBKWii>O?8>LX[:OfGHc,0(D
<7r*ZPugn/mnru+(_n@J<?75Z@)+/3GVoWIn\n=7cECa2N>bWReKHN/WOlcL>iC_GHqflIbJ
0kn%'b,,sZkBtR?XO5jiI\=gK?srOD!dlMg8Q@lbIMr4Zg2ko,R)t_O_IV.[Ur=QWK,`VNFK
_[-/toGO-t$K'#58#2kO+$\p[X`-kbQgm8^AM((A!*C$3D_YQ6D,r+)Ks3*MW2RWlSCAp3+V
Q0L"'C+?-=c<qeQK4?':b)sH\"U/_-]Ar*Io0ocP2G`&.mW5KkGijenYI/8Y^q'-TGr<V#knW
9W!Sl:^i*m"V!aS@q(FL'=]AKj$G'Ff.OaeErQ=IjIP/"#Tafqr(-]A(n)t_HW;a<27K?1Zr$^
4)?lP.`Ss_O'NlmZ-j,hq(c0i#C]Ak[CP1N/4Uq-9LU9Gu!Z2VJ.;KAYO]APEP8Gq*V\(a[R!T
1\0!_!YjpB@sh5\pC"DQQ,,(]A1u:2JMBDf\<%O,Z$P3'i7J./r!5=2[6>Xr4(%`H[m^]A'2Du
sFirhH_M7]AS)h+6N:)"!TP18(!p9Lh]AP>Jda#WBXbh[A?2]A7ariJWc<+i`M+s!0UUr+6YMF*
&eW_nWcaYI2h*pO03RiDL23KP$@,/NWOYGkiShOFqk,(a;X,NmA(A(88mi[d0B`9SRV=/_AM
enZf`[U,XlMQ^NXlQ-(4^@7%>!qRh_p%/$H#4T25j]A8,L]A0fV^0b/Eq$K:CH.oNpigI0j.nO
7f`CCXHEG"cCLi(U#h/C7H]A2_-B1[1aQ.Gf=jP,ruCVn'rk`hqI"MiS+^m")tMN["B+:Pr?m
#*pLNqKK`_Kt+kj8q)2t7k-#UA3+cTI8rU,c-fRQq&?QGX'q`>58V*_dEBWi1iQDh-O;_=r6
\-b6ZX5$)WT'amt'ZTQ]AgHd#j2;I6RkV]Ak5u'4-JqpbG.N.0[boDt('rPh/W/2?r.st3Q13a
l@SHc_\fur1'&JW$G?b'mMeu.F,,rqLNQ!Xd&^Y7pmJ5UI:8\NA'$.FgrE).DYE?Ylk7EhK!
ebh??Z447CZ_VPBF6M6_qS'AB0'c>)#I1;fe`JljU5.4qPp!JiTaB%@Kt_"47e5tWDRX5.5K
aD;#pNqmF+%KE]AVm*>:.f7UZ!g$1LudHo0n>km(&G.^!1"DXV>jcm0(;;PqThOHRg=OJAaV!
b='Gj(:Q`tbVT/LILeiVA]AP[lB_2!GNAoao66*Ai%<O`!]A;s1J1!'S;90"*78S]AY0V#U]AbW>
:D6TC0_6.UO=Ri2sK4`:,d2W_L5DTbeNg$qXun\N[uU8+'.'g58gfkqWl;g'$<Z3C9rn!jB_
AGLo@r]Ad+Quh+a:<`od#n9J[',&aa1Kl[?=.cn5\Rh/VVGbY(j@I0*?R15"S'\Ub$1hQ4.Ab
7NbO'^_L+]AnDF-1JiikmnSkc89flTs3RG?-Mu@8FEGST`s(#eS!pPs%?Z.Urb*f!bW)m/kZ@
!.\$pWJDff`l%i<'(N:B9oA1+3U6du84qS+0L6?bZ5Z!";e1_EgUD0pfkUAS*tY.q`9\T.P'
m9U<\O-&Ol_i5po<mAr3a/2s+!pXFpY1AT4pjZ&_QD>q:3"XF;qsERZXiHoA3P'L]ATD2N8&m
nX>9HFt),=hm+h5[S"NKOf`ETE#Pm/^dpmSkb.MAS#<O1n6PEU#g<k#."FYp@YHmd[rpXO5N
R[e8Bf!+6Y^fZP-)#J.pS^d[iBq9/Sa%6,M,Yoa)Eq_W7b"CLC)+93^5dOYR'j9'Q5'Bj;ZQ
<'mN`Y0W=2GR`G""R\(YBI_&j(Up3)QZbj]AkQe,5pDM#88VJS5^Zn)"G6"tCr=3lQq=8&WQB
+B#m\Zf+ABr=ARq"E8S^r/B;PblJHe,h0O+Z!_]A2A[reG/!(['3PCd90<8kG_(_+/&Kl8A7_
X:PPYXF=N0d96OJ2=4,tcX=rYh70WU:o:dgN3aJN5eW]APlibgdI8)Pd(S>[LQrjL$B1*`*qI
d0@8-cu0iUk4A+/@?*"!)uX-:ar:Z_BBoPhJNb306Aa<&Ff3Qio4t.a]AX);jsc;)peZ(jsld
!,X=<mj9bKaSZ'oLOk:Q873:1J'_RakXHKC#bNe@0Qq6/DW$C:90?o7[1eMftK6Jd;d_<=&]A
r]A5?Ys;=pcUOCd)5)5G9V7g4<grH?J<\EQ:J^bIQCjb1aKiICb[HaaB_<`"@bj8d\kusI)E>
DHG,n$$G_R]AWC,J[&n0Z-S2)hPqG:5F:I*Yi"gRFhW>qO%ZGeNd<gga5U>dYau7?ka:-JFWJ
c)_<;U.ChM9P7U=l:s=6eaH0qYa+PE*0T$a-.CJ'W\,0i=V``+g?$4Hra#N*M6Y`#1[on%@k
bRb2b<^lG2;%,MP#$c_o)+l@[Yd!QYVQ;h@K[^nEdh)5&JIb3`j"%r4JQ9V[-D.IWME6-?I^
gFldfRj]A`5R6O+=;oB@"XalPSpi>]ATD"nW/j(;kCR?<Rl5;TrpT]A6C[F+K#:B*1VUJ@gB'[P
VCdo<:OLaA@UWTj(f")A,LmmJZr@IF0i'QJM<Z%<J<!;V*!g*:UtJa^7u.h/2,J6hO!P5QI8
]AXYLoHZTO]AY=UksAI^?P%4%'l!88s80RII[fV50uC]A4do?Yj&3A#@T(pIKlX*2dOrMMQUeYb
X$BMH9HST8C=4cB(pPY`#efRf6sDfuMGuo5'8QB#qe3D/>gp>)J[j?;9ceSqCptNR8]AFqAoQ
<nUhC`7ZnIp%SdWaW!F9Xc2JR!d^%$7-'S#S'<q08EV^#F+2kccp53kc<s';@<1@H^]A'6mNT
!c&IXEW/KsP8o(3Z9eM/#h$[eO<p+aHLHo8,C$<MbQ>^:nc<8$_36+hKBiaVr-OVt*"2o[F*
g`;fO-Kg&U,C>T&"dEf3/:t5-3;S##T1TB.(=+/=nE(H?+%J$qQ$*s#1;.6SlJFq5(%rr=#T
`\h/T?e(,5soLu.@"=SG_a2"A%',7o.oYH#i^\NB=VSqcnJiR)7dY'io!e4au$+d057&2^M:
KEfEsPrdkRmHl(92lG%=>"kPUK2JFIm%U'O>h=.bg<\k]AMDZ<Wht2F3LDXXTq8IbJj.KLjqZ
+JsVG9k%KUpeo&&CPr5J!WW'aR=&g2"dG_@[$tkpaVl!U+jYEkX7AO_Y<$0J03D%6_i:(<4[
sQ2QO]A3SCHgmH6!G7]A4FE;6*7]AnOd`(6V)UZ&ka9OOYTeoI,Jj_au>LV^)G?oWQmh`G2O4+l
'`&_63X69+p"[<YBCXh-<@#-WW[m5]A8O<C.s\nL@Dg'dkcgQkI7.'<_*gjZd]ATJo"Oifsr$b
a\@?V"+4V-?:;piOkiQF)-QIUd2cAr)Sc=oZ;gNDYBI%uq%<bKf>8Z]A,o(A78H<<o_9.siGO
!^4ONhM]A_nITZHV6uf/ni?\"Pi1YHmgFD[A":S"D`"1f!k,8t<HG9;@a**'9/'t55f)%$6*U
]Ah,XqJE+3SNMK$d>p[d5_LiWa^0YTHb0)o?)nU9<I!!B0m:a7$3R8'XY2-Tge"^1It>%fn8<
mF+irN**aU#c$Q?^/B/)nlM-Z+b!9f)<$ucGeL..g0[[94Z3WOe+fNo:%4L@[>W(G?Oa(#T)
H21a9\!k^V1A(OA`$M.BNBLZ"MM9/@]AtJNRVD,->SQSD(`fYtrB<,O:U37<0+r%RR[]Aeg:*M
K9<J86R7)_Qg/a2dX/Z8n8]AUA4Q'5D@-C\;)uA_9sh_,sdq#W@(nH?'6N#HsS7DgRjT*MtfJ
Y?h[%^=f>E4&Sk7WUNQT5LAfkSj=j]A>s8Q&+&/#,0D]AihcM7&5Z<6jq.LpEi?L=@f60PL='Z
+jj_A)#N&c;HIQKh9!"[A=qlWWE0cO;(<Tt1iNH$Z]A+Q0)=7d':i_l6>#B+BC5/Z\b"/3#@n
>+N<lEc,oTIX^O6@Vkfn/5"`02<0,g]A4&`NIE&8bh#lqo35.d=LUj*?DRM+XQf8Bf'P#j7l1
o(B*e)6RYag#u<S=*iM\DE3fCUYp[^3Q^S;is`uEE-NC=sfM!c6tUUgo.&?FpbK)eMjX_nb4
hA$r9/WLA6En7mAh1+WPIVr%Nc@ZiNB<)d2:Iml*",eZj#.E)oQih;;,WL-Sj`J59Jom/38.
`5/[4hMu:DF0YX`!V1r[qU#+sY?c(e`[p_ifg:pl4b4sfqN^fT:$4,G:H&irB+eB<9;HG^1!
cajIUn,JCka#_o*Y@WG7;)B+TUb?6mb#]A>#'trB"ISLleS`!X1X%$`8^HSB]AnsW<0:Pp2>Zr
`Aaus5[\4:YZCsAi@>%_S2Y_@c]Al0ss\Zu@ZWst"<rFBM^%%L6;>g@6$Vn@%L\-e3o96hM,-
7Nj[:(I)AknaWWa.+,dh)u8F_6"F;:93qKH+q245O\&F?:!eoV?!<;UOQZR`qt126l"oq1Vh
CRG@/a9rGJFn"Pk0Y#rf]AoM0>u,?4ONTL9"QGPrd8ZGPTD*#J-%h*>#6_2Ps6dHGIW!2WEkH
`M72P@P3m'D\C9$km`u*6HJ=_Tu]A/D'ASV9"iS3!I>.`EMd>=t*UR?er'?ae+8bY6RnIN7nb
q#J7H"A&DbqX-4'r-&hu4SlB48_Fr!L:<ND(mfLi!Q,7<kUnoh4uf@%C-SKCqnK8`:fZD8df
@fcWaIhE7d#lQI1ViV^'E04eOO?h=5C-?e1PqNUR,I<`X6QD76n.r*`AYHS*j@V0XG8>a`4r
#qVHUl-p^LlO1:9,koK0s)>iOR&;GbA0_=0=nH0*>0]AOM>;=INM4[,k']A%3[g.,`DfSKu<43
u/=ZQRdjF`Df3V"DS&uumFpZXHTqf'Y89e7.a>kEYgFK5IKKNZ(-nF]A4s9HM\Yj?o_S7,LdC
E>$UOJ!FZrfmEr`Cr4Ff[NTFa+i+qaB7lXjSujG5gmN64[[/ptTH,R/Hg7C^TPS9Wqn+lV!:
>,Ns*+ODK!C@eOr+bMokm`Y?ci+3+7;SfBk]AeZVC5!$]AM.i%EI=*!.NI]A53U:Nf#1h;nrpF\
g[oHMAWXG>3PpTEUF8R&M)7R_$KGo__hne0..1!9d/[<NZf+fCJ"e3Eg&2R\k?[NMB:$m="U
%HpDI.>?Yc]AK)T@J!Cc^bE47:PMU+7ICGu?hmt7&q#:c)-Tac(i7),cm'=Y8BsN,jcHL"UY]A
]A&c7TH=45&(HJ7[G\[;NC2(OL]A_c*2Z^QV9fDiWG-UCW_:eNC?Z@4.ku2AoI4IKIEXPs,2HC
UuAAhIf,2nrqc0b[s4o5Nq7^0Nt3'&S+ZeRa_k).om_DU(EN<0^GW!AjUS\rqocLP`b^G?41
7WsYOk@<T?W#BENj.q657W9hnG8^NdnQUk!"C4/^)`Dp?6u;g@*TVNjIo@?Mr!.g#`+1fl9m
9n8?B`(o1`*CN`!g`UD,+cHo'jJsWlmiWldr+?U$Hr]A-XFA8E\_[#V+O0&\-E74UAJ+CPX[6
2]AJVqEro)/ZQi,cT<3>]A3@s-d-]A_mrM>)AZ]A"i,=jQF`RZ8K(>JB%A?fMYK#%]A#ifg7MD:n\
HXFu>WYVF5SQ^%2aapp[IW%mWFtC<<)D"*kIEC#]A(I[Isb_7t;l<$D!LDq'!7JVj8=$rj1f_
[!PLFZ>ac[GHffT=dYCU>?qj``Ic0Xmhf7Ge2?VT>+\d$TGM)KC$f3!)LhBpl?*#j)m;B/B[
*i-K0QHqg;)$VhD,lj#qA+.558D.n[@0L+ZiY2%ck)g@X(\'SRu$;QUIl(T`$afejOs*`.&!
]AdnZ#i9F3"r6htF&TjHKk^%/]A/6Ym$hroX_[La3Ia]AS;H($9/5%plqN2s/\N$e?!QV4c\L':
9V/TL>Q.0pu3!WL7?lg<1g<Y#k[os_A;r#cQkH60YF)o):fMV6.Mc=a->&X#4.$m&>o`B#US
`;O_c\,(R)N"[H)RaXTep,18G!@4<m8``5<Hu\N09OL3+-YMYm0,%t_4NmOK&:TmC16@fP.:
V7;n6o(dVRdh10_rEg6@IqWihm\rNc;9P>9(;C/]AKU\_?h99$-G]A5NV(8[j'[3J.skl.iM+C
KOqq"KeRW%-$ZLK`d-j0b<RP]A?_'2D7]A:U)IWRggDd7k\,tq<=`6?/>:JoCE^<Q=`DXAjb#L
Jh5E^iBSi$OirkM2(^NdP7?Y!`KJY?VF-_:I^TrpeSF.UDMG:F%&t'a$[6;%9mr**n/>rQ:(
DP0C`#&PPDH$iT%dl`j%0eb+kJ-Ja-MUH"Y#Cu^p#Ckfel51`Gq,f"8ntc?/!>mH,/hJlG0^
#S&dG-k]A"O'gl:+&*l5g40p1Ir'.poD.WPK*W]ADdRXV,U]A\c3#ins*KGVAO:)5_s0<f=I3#L
nY4^:T"!aSOMisNBmC7"56u:U^^<$#i<b'UW]A]A!Hq6=H=U5GH:e(3:Rd:R,rE]AEl&o6%gSe$
RkQZ6Fnn`'unr+R35KiP</p'Bt&LBO71jh,&rLY>5F7\g@1%PU&Sl\!juO.\dXV&!0r69NRc
h3Q8CjVd0*egQu'Ie7Ao;c(_2kaMA%AZQcVIHJ(aNS?9SdaDUBeWh3nbj+*Y=Vd:=00J[_e(
L]AAS?td"[Ib4Kj;]AS!^%ubC4&lqI<j:=P")0I6lrVm'BeCp$Zj!aY'>_Ek@;cH[t:dGoW6dG
2C7XlCs)L;g+^Ad5DG\[)u?^]A,Ds#@IGj85HN;U2S8d9Ntn@0&lD%W#L2:q=6`7HhgZha\e-
^5Iadd"nm;'X!0^$_cWU:i\uM;&)Dr7*YC?OcW;uL5>:=%+(RUW7)A-;\Y:CAeieTHT\EUJ"
7d6C79prcSFfre<P^=*P!QgLX?9TTEm\A<-.#%;M,RMqU;HWRj#JWBTF]AcQ5PkVZCiJJYp_e
.!nHAt+u/.UKc=%a[-[bA+i2@ub@?aBICO`&\_muJXH*DCCBaA.+<`BHRR"LO*n18F_HH`'1
,itHKkj=njlO/;j7u&b:f&rm:oc#D2'mSucp2a3+6@`aL+N3#)i%$nTt@Pe>*&Z6ardoV<.5
(P)-_HW$%<>[/;*ac$8MsWdQq%HDd^LRc'#k0?a!f#7O?=m@1&&L5$-c6*M5cJPq=*[-D?^e
Emf>3i+,W[pUARDmj"HU->5KU0J_Y7ZQ5guc2mr^HQ2br/+SlWrYG~
]]></IM>
<ReportFitAttr fitStateInPC="0" fitFont="false"/>
<ElementCaseMobileAttrProvider horizontal="1" vertical="0" zoom="true" refresh="false" isUseHTML="false" isMobileCanvasSize="false" appearRefresh="false" allowFullScreen="false"/>
</body>
</InnerWidget>
<BoundsAttr x="0" y="0" width="864" height="230"/>
</Widget>
<Sorted sorted="false"/>
<MobileWidgetList>
<Widget widgetName="report0"/>
<Widget widgetName="chart0"/>
</MobileWidgetList>
<WidgetZoomAttr compState="0"/>
<AppRelayout appRelayout="true"/>
<Size width="864" height="484"/>
<ResolutionScalingAttr percent="1.0"/>
<BodyLayoutType type="0"/>
</Center>
</Layout>
<DesignerVersion DesignerVersion="KAA"/>
<PreviewType PreviewType="0"/>
<TemplateIdAttMark class="com.fr.base.iofile.attr.TemplateIdAttrMark">
<TemplateIdAttMark TemplateId="ab57b28a-ca60-4321-a847-34b18f6bacd3"/>
</TemplateIdAttMark>
</Form>
