<?xml version="1.0" encoding="UTF-8"?>
<Form xmlVersion="20170720" releaseVersion="10.0.0">
<TableDataMap>
<TableData name="File1" class="com.fr.data.impl.EmbeddedTableData">
<Parameters/>
<DSName>
<![CDATA[]]></DSName>
<ColumnNames>
<![CDATA[公司,,.,,日期,,.,,流量]]></ColumnNames>
<ColumnTypes>
<![CDATA[java.lang.String,java.lang.Integer,java.lang.Integer]]></ColumnTypes>
<RowData ColumnTypes="java.lang.String,java.lang.Integer,java.lang.Integer">
<![CDATA[<Kt*q">L<R@o86YnZP$1M+Jg6,,B_uBEesY?(b>]Ad8P:ND+T2#4P-LWgZ'e=8L`c[\k!HJ+s
W[FQ$<EhiZ?U+>L4LTTLkkD>Vc.4#3b)4'38!81boo/.p3$lA2"X?W`XOC`Nq@cP!Y&IBai*
^M5LKeLnu8kP/?U_jjfqANEk/CJh(M+5q9)%IQoGLcS+_67Z`_V+AHX;W32L_o$F%A-^13ca
:i(ImYNed-EVg(6J1KCEUqT=`m`tf[S1Q)eA_c9O19J4c%eekFcY2,4fSNthOLL,4I(7eEVG
]AlHSe:24lTW=B[G?ohD;p[?,")1h;\bP"Jm!oO0Ji`A)nb^N"XVRNO3c(.P;;oE14]A[VQK-T
!6kTIXR!4LfN,9srM.EU@p.JEf,N?KPZ7I'MMUHqC87q=eA`Jk/&\4MnG?!EXUT#13@3:4&\
>[Yrr<~
]]></RowData>
</TableData>
<TableData name="Embedded1" class="com.fr.data.impl.EmbeddedTableData">
<Parameters/>
<DSName>
<![CDATA[]]></DSName>
<ColumnNames>
<![CDATA[名稱,,.,,金額]]></ColumnNames>
<ColumnTypes>
<![CDATA[java.lang.String,java.lang.String]]></ColumnTypes>
<RowData ColumnTypes="java.lang.String,java.lang.String">
<![CDATA[HbO"YMp6TTCteloIH&G(]AptB(#!fusHqWeST%7O[;kLKNL!#c"JRtEiD1($nO!8(E#*Jue~
]]></RowData>
</TableData>
<TableData name="Embedded2" class="com.fr.data.impl.EmbeddedTableData">
<Parameters/>
<DSName>
<![CDATA[]]></DSName>
<ColumnNames>
<![CDATA[類別,,.,,佔比]]></ColumnNames>
<ColumnTypes>
<![CDATA[java.lang.String,java.lang.String]]></ColumnTypes>
<RowData ColumnTypes="java.lang.String,java.lang.String">
<![CDATA[HTl#ge&dSFFu4.V)K@oqE-Cnn)T+Qs3]AW0o!!~
]]></RowData>
</TableData>
<TableData name="Embedded3" class="com.fr.data.impl.EmbeddedTableData">
<Parameters/>
<DSName>
<![CDATA[]]></DSName>
<ColumnNames>
<![CDATA[欄,,.,,值]]></ColumnNames>
<ColumnTypes>
<![CDATA[java.lang.String,java.lang.String]]></ColumnTypes>
<RowData ColumnTypes="java.lang.String,java.lang.String">
<![CDATA[1ZYnsi%j:K1&q:~
]]></RowData>
</TableData>
<TableData name="Embedded4" class="com.fr.data.impl.EmbeddedTableData">
<Parameters/>
<DSName>
<![CDATA[]]></DSName>
<ColumnNames>
<![CDATA[欄,,.,,值]]></ColumnNames>
<ColumnTypes>
<![CDATA[java.lang.String,java.lang.String]]></ColumnTypes>
<RowData ColumnTypes="java.lang.String,java.lang.String">
<![CDATA[1ZC5KiA0IN0`qC~
]]></RowData>
</TableData>
<TableData name="Embedded5" class="com.fr.data.impl.EmbeddedTableData">
<Parameters/>
<DSName>
<![CDATA[]]></DSName>
<ColumnNames>
<![CDATA[欄,,.,,值]]></ColumnNames>
<ColumnTypes>
<![CDATA[java.lang.String,java.lang.String]]></ColumnTypes>
<RowData ColumnTypes="java.lang.String,java.lang.String">
<![CDATA[1ZUAOjYGgP1'IX~
]]></RowData>
</TableData>
<TableData name="ds1" class="com.fr.data.impl.DBTableData">
<Parameters/>
<Attributes maxMemRowCount="-1"/>
<Connection class="com.fr.data.impl.NameDatabaseConnection">
<DatabaseName>
<![CDATA[FRDemoTW]]></DatabaseName>
</Connection>
<Query>
<![CDATA[SELECT ${int(RAND()*1000)} as result1,${int(RAND()*500)} as result2,${int(RAND()*800)} as result3,${int(RAND()*4000)} as result4]]></Query>
<PageQuery>
<![CDATA[]]></PageQuery>
</TableData>
</TableDataMap>
<ReportFitAttr fitStateInPC="2" fitFont="false"/>
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
<Margin top="0" left="0" bottom="0" right="0"/>
<Border>
<border style="0" color="-723724" borderRadius="0" type="0" borderStyle="0"/>
<WidgetTitle>
<O>
<![CDATA[新建标题]]></O>
<FRFont name="Al Bayan" style="0" size="72"/>
<Position pos="0"/>
</WidgetTitle>
<Background name="ColorBackground" color="-15197385"/>
<Alpha alpha="1.0"/>
</Border>
<Background name="ColorBackground" color="-15197385"/>
<LCAttr vgap="0" hgap="0" compInterval="5"/>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.ui.container.WTitleLayout">
<WidgetName name="report5"/>
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
<WidgetName name="report5"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<Margin top="0" left="0" bottom="0" right="0"/>
<Border>
<border style="0" color="-14669005" borderRadius="0" type="0" borderStyle="0"/>
<WidgetTitle>
<O>
<![CDATA[新建标题]]></O>
<FRFont name="宋体" style="0" size="72"/>
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
<![CDATA[1728000,6019800,723900,723900,723900,723900,723900,723900,723900,723900,723900]]></RowHeight>
<ColumnWidth defaultValue="2743200">
<![CDATA[15163800,2743200,2743200,2743200,2743200,2743200,2743200,2743200,2743200,2743200,2743200]]></ColumnWidth>
<CellElementList>
<C c="0" r="0" s="0">
<O>
<![CDATA[活動投入產出分析]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="0" r="1">
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
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
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
<Attr enable="true" duration="4" followMouse="true" showMutiSeries="false" isCustom="false"/>
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
<HtmlLabel customText="function(){ return this.category+this.seriesName+this.value/10000+&quot;万&quot;;}" useHtml="false" isCustomWidth="false" isCustomHeight="false" width="50" height="50"/>
</AttrToolTipContent>
<GI>
<AttrBackground>
<Background name="ColorBackground" color="-16777216"/>
<Attr shadow="true"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="2"/>
<newColor borderColor="-16744320"/>
</AttrBorder>
<AttrAlpha>
<Attr alpha="0.5"/>
</AttrAlpha>
</GI>
</AttrTooltip>
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
<Attr isCommon="false"/>
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
<HtmlLabel customText="function(){ return this.value/10000+&quot;万&quot;;}" useHtml="false" isCustomWidth="false" isCustomHeight="false" width="50" height="50"/>
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
<Attr position="4" visible="false"/>
<FRFont name="微软雅黑" style="0" size="88" foreground="-10066330"/>
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
<OColor colvalue="-907154"/>
<OColor colvalue="-15872"/>
<OColor colvalue="-8202753"/>
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
<newAxisAttr isShowAxisLabel="false"/>
<AxisLineStyle AxisStyle="1" MainGridStyle="1"/>
<newLineColor lineColor="-14075297"/>
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
<newLineColor mainGridColor="-14141347" lineColor="-5197648"/>
<AxisPosition value="2"/>
<TickLine201106 type="2" secType="0"/>
<ArrowShow arrowShow="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="Verdana" style="0" size="72" foreground="-9273712"/>
</Attr>
</TextAttr>
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[¤#0]]></Format>
<AxisLabelCount value="=1"/>
<AxisRange/>
<AxisUnit201106 isCustomMainUnit="false" isCustomSecUnit="false" mainUnit="=0" secUnit="=0"/>
<ZoomAxisAttr isZoom="false"/>
<axisReversed axisReversed="false"/>
<VanChartAxisAttr mainTickLine="0" secTickLine="0" axisName="Y軸" titleUseHtml="false" autoLabelGap="true" limitSize="false" maxHeight="15.0" commonValueFormat="false" isRotation="false"/>
<HtmlLabel customText="function(){ return &quot;$&quot;+this/10000+&quot;万&quot;; }" useHtml="false" isCustomWidth="false" isCustomHeight="false" width="50" height="50"/>
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
<OneValueCDDefinition seriesName="名稱" valueName="金額" function="com.fr.data.util.function.NoneFunction">
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<TableData class="com.fr.data.impl.NameTableData">
<Name>
<![CDATA[Embedded1]]></Name>
</TableData>
<CategoryName value="無"/>
</OneValueCDDefinition>
</ChartDefinition>
</Chart>
<tools hidden="false" sort="false" export="false" fullScreen="false"/>
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
<FRFont name="SimSun" style="0" size="144" foreground="-1"/>
<Background name="NullBackground"/>
<Border/>
</Style>
</StyleList>
<heightRestrict heightrestrict="false"/>
<heightPercent heightpercent="0.75"/>
<IM>
<![CDATA[m(@U+eEuuphH`M`.SGpNCC!?@"slpn.8-sJ87g%,eu@&/%nZI+P;!Y*Q5QR!A1L!/D.[T="u
FiH)"X;<hsWY<n'Cauq0jC"je$JkBO5c)Ffsh2k<,C"SEgo<dG/[_a'juK4*KsH\tE]A@A&g4
KNZC3BYjZ0dGo==4Z"(hV3[;=Z<hQPYq@MO/]Ab)MblQPQd2#4!/_,0`K_\"CJ-,-hK,88DW@
Lb<h3B9f4.rZ0ZbZaI;\+2hK"Z-g=%uNKEH)iP<&4kdqR,QSValg,E;QtE2)ZB<'[<NpsfX^
#aFf22Fl*E>nmT)Tnh@iaVn#!:;\XO!)?@A0e4k./c9eS$%S^;4:U%HU.G/=uabbN@1e?utG
P3'_ERTJ>MilZJP0b3:0>3ZuZhp;5'+YUujF/f#Pg&M8*'Qftp?Ij<5hljZF=q&>%Eg6*Qj+
p/6iZd%S'j?/o"CfH$o_t&FO18R)hf/Kl5+I^)RpE^Ta6:Z6WYbX1[@BYM"fYhtah,bLT;YE
3\D^(\4M%XEWVr3#70.Q66M"cg0hn%_V497XiRp0L<s[[od(PO=65,>$&s(n!l7Q-Z<Upl'-
"1.f$mo50T?a::hIFWh;e?GPbh++CfKmYdVYWRJgGPH-;qHW(.Ca."\8]A?BdGa\E,PH/!"MN
56_X.8cGn[/"hpfXZThm7$RX@9,S+./;G3o*A/;ZJ)GL@3.)')?'0ZAm"<3?)@.PKU]AZJe)4
?nRP2@dU7"H%VjZL"4$BRPi)=l4^^QitARqYD,m=AM>XSretQhjF&PZ)to;^/J@ePJIG\//0
,7\@=bG!AK)VNC>VAq#t>$3kTc%?CO'MSNL)0?^Vs5oZi@^D"t/0fQh,PlOq$*(J=?WU$T==
9!@)F";a4Q;%@4<0"DQjQA$#-I.p^.;Oj@BoXkD2a*(tFI2t#>0o`$;N=9PmC?Yog51:q+ta
;B]AOG:`IOplYC\%!B:rH<02lF(^i>)ddNfM_H1m\!o5PnZ+ak'Ac)lqg[i5)rh7j_oV_i<8r
rZ43l^+'>=*T=H"RCYQ!Esrh&GP/Up!BER7gt),FI\rnWT1!@/IP3(IRCI<">eIkAM%/`'/d
ld&r<nc/Gn:%UHNMbTAI(5j\EGOF,R0)Y2+/34q4T?.ocVUF`.8*O,1k;OdXmVCf$7N7)LF(
?<lj2nP>M\;TiOUNs,JBboOm%psC75DfcE+=&G]A%MB.s*"#6=Z;>;jEB]Af.=UYlF@#>lYJG=
ho,kYqI+]Aur)JH5/[$LIle&(Sn^0&&4IW5,edfYF^C`\XTZh=<->3lbY]A2_I6C>"Wn%*Qc=n
mSTUSKiKQ45m_MbC2=R@DOJpJGkpFIL)@+S<X:tj$[*/=?Phh(tXk.`hQ)[:cDLk1RFBsZ_+
iQm[TASRhM-Di:lX#C7D>,iRCiW4t>IUP=canlPUe*?uo9F_W\fdU2hrX]A"8d;g:7%2c+9u<
lXR*/#T\62+=]AL#?iiQ_i_@CAI1/Ad!OFPRQ).N$c[>`.?Wckia-7aiT+t;HMKuOR<;8)/"7
DMYksc+[n<W2bX!_#O:cWG6H*S&`#55_aFkAl._!r01ksBXVN6]AP/"=Nj4cYJ,f78e!4;+)e
)oDt=[\nNZR$%'<'*bqM\LqmW7\-<p#;IADC',!>3mYn^4*>AT!`"$X%(htE'2Mo&Z[7aFmK
4%cpG#I/E;1Q>e[9*$s+G[(U]AfV+C+L%r]AkHdGVc!%DF.jM"F;KaM9.j?9u2Hub4keW&=q`6
bPR8QUc*afqi/Z\RH?PYOH(uj056kDMGEDk[,lLk!?HpXMmCI0pEVL"&EZ,_?AJGqFJZGMZW
Li]Aha9?]AFQg>H3rIOfZ6'986ubQ0^UYHN0W$DsjkTTi;?Ug0$WS\)X&J=I$ho7a[?lrd$VIc
P$MX`Yu-rV5-MmmChBH8>_i<>B!Mn[9I;5'0Zo>YaGYoRmGCJD;<S[[n7C%h\hZPnFV$+Y-r
8%=tip;Cb9jIM>.tBh/h"@_bt:T=_O+7oj,kIu#%Y>9@=1Ec`YBQegO%]A\HO7mk0K3X.ncKa
Gb&U&#^`jM.4%<=IZY^*]Ag9onZtBg[U+%I3@,jC=bMiTcJ1nQ3k>&uNs@OK#]A7k+V@H8`qmO
`/.`O7$qNOh=^rWWjSb^;3O=L8?@YGb@[WJ7SRU3V1jF-2?JV)L7I5<m?c)LGOC?!s6ppgS9
9^M+6p)map,TTBD`^.DLDE/!(]ARY=VN2N&,N4F)cRUK$0e)AEhp6+#o'6=d5$2%WpAnfqEhn
Q.>C*F:-.&&HA*=2MadiBX*M<B4!j(]AYq%a&@Y%*N48$Er.9i2hY<CW"LcWNlE$C!6/^_)cK
95H-19PT2sK`]A8"8)Q7J=SLm`5_%[t79P.s..7Rh^,`EIFeF-GEIa^/bSEgCHeq=9YL!*qHU
7ffM_tGRaM(1B!@\R?DmR((5ciesQSB[2^jKc3^#YM3titCm[O;S^Z[sn%;&H/^.oN9_Jb`f
M9KiXO]A]Aj@-RRRjFeF?$&8p`0NZ&?gT#"M!o%e:_JhT4#P)T57^i2Ao<#Bs4\VL1^8rFU5\l
EqRJMH&E7:[5o-u1>6*KF)T638Z"`D?/!`t013gPU[XUuqTJ4orVtC.DK7aH5dbRo0>k*[K;
Ea"U+G_MCNg;=:A4#iH[3']A6<`&+/TK]AhF=F1Xd=lor#1.(*VRDt';--gXJ&Bf:0-$<Ol%o=
5+G=B'dR6W-B4mD#PFeEPl@8ucC/nkZOi,@[B("!im_t_$(*s7S#m/X+H$6e2ASs>$0"snFO
@2;`\fi5lcI3Id&ElVmF`jl4md&IPeAtIeGofrN[c+RT<E32Vg"F%i0CPu\QSt#=#mA8_r!l
u2d,]Ab-MY><fd`P.,4">60RWm97M<h#$W@-6KQQLGN34#5ekhb!b>^JcC7-l!VkK-ibSD0I@
EBaT4O<=CI$]ALl[AkSXd,2j:U>3o#EgF%1(baD&S@\b?NYH4\d`ku:tHWWg'DQ_?X.0;/(ac
$bJ?A?iO`S=(/mGZjQCXVp^7eOs?q;Ej6T!LLpJ:!g'm#WEd#N!a:*WTkJ`%<?u!MN[L/hXJ
=WEfX_J<:\eVY2ZI]A]AhP^@OAKF#l-,t>2.eE>*E;PICPP3Qp3/Xm<@Spn3Aa`,+>`VL[#s94
P)lE8=b'sqq<[>pYsVd1UjE'ADjN4egps\MK6DCUi.u,C;4#)Z$=]A\kib1o=]Aob#h;(qQlSD
c<jpFmt8,p2FB9.[+fki;m/HL7A\ubC:\qA$CO+ZkO#\&g+@NIpspRS5abCYh)KYK7pBpt6N
ZuY,mcU8J,mJYCnlAuISWgcU`F@_Vk0H(K`Yq+Sn+eGo_M%BFRk7)ugpPT3g-1Ll3f%jPSP#
KuW83kQn!$JoZ)*kF9bV7nPCJ'oR6$=eh-I;gDdC>MoUtQ:KMSP[7jiN*"FO`OG+K9=r]Aon9
0-6Bkt!H*Y-1W$&'),$)/cYf"59a]A`\ork@2fca0GmpBDXT3@?;6e;uIY>j`A(t,/3nBu+j"
1V3)=kQNmSg&1'^#K_HWqDoHFmA!^^>W3gVOa<JV>DtYGOQjHW7<8rpAn=!>N/O'+79@i^n@
q("):__C!ma_==Yardt9'%?F[5ZBhPrK/P!/HEa`,(5"pedce_Amla3;'kGn!9+B#Z8O7KhE
[^D5DiM<%p74",ZYt>q.q&dE289J;Oj\o*OH[r$3mRIIk_d6arK5Wor8gA5bImP,re69VqF2
qS^JqaK2JmJAP`KHVLKP.T2O:oh-O?0dlO3<tVgD2K-:o3N914-"\Z;"/JTh+:eQIputUb`t
r%G:&JGPHn%rg$eW#DJfc1`Sud#PC/m_@"(',15K!5B-/*$*:RS:7),".i]A&f0RBQIIai@2r
8`)#lTDrUOF^:F\^)ijfNh.e5dN_p@eF/f<eCk!SaMO3FSq>@V\*QrlRiCb:9<:h!+3Lt<?F
6mjb*+QJ/hese6APTH68(Ya*?*]ARkcs*i(CC1KW&TuBL?k:G3fbR:9D8+dMtEhOjQ2Rq"F@i
8^Ln[b.%cU^'B,;F[Q-5HBX[g2(;#q_Y'Gt,1DJ'dtIt10[D3A7+sBQ[u3:u)ANr^+DCJ2B$
.4(3N7hP2sPkU;n0e4WV_/?ET'oFl1'*"JeT&/M.hdhpV;,/]A_oGQVW9n>H5lX98ci;A9mPn
^2W2e=7,=SX-#aB(jrj0qH/>Y#gM!6TKFX2mjF`!ar<9F3JpY'E%CpA6A%G;n?"]AnX%Z9'&*
rdck(?$n^RM]A0%;5rEqngi_lR@s.\6/;XVC_ID21UFuV8qGW+E[5C;D@Y`RZ;*L9mP&K2Tj(
N)kPlSg)-BL'r,9t]A+q(X%QOZ]Af8O@cU9,AfR6bp]A16]A,ORA+O\pJ#fh&C3*LpAHuW0]A4D]A`
n"8^?=.('spE`r)I7mT)DH,"([h<p6qsf%qh`noA;t]A&+8g*)lfh6ruD%1i;PM%&(QQ0%ml#
T1e>1kIDA=*WF]AIO&4]AuHU"0Y^9rD,gm`$D-Ib#c)jF&.$*XB1,S3:ofl;O"*/p_9ZL%0;g+
B'i)e&FT=)E8geD?nBSXa6UYQAQ2tJ&Fe\#`TaM/LA4+ZF9C[\jdV&83mFmXY&,LQ=o2_;V[
JQ(#D2=Xb0W'1?*kJ7W*]AqtZ5q;c)ZA]A8reIWE,r"9A&`L\fud+;eu/d4c1[[uo<fJMd&WU^
&Us)VN8Yl^[RGC"R]Aa$OVP@e1VQ8I:W4g52ZSK%n9S[#SsIE,:(SRSBb??U5psN$EW<ODqmg
(GV\T*`1&Nl:`0JpPoRs"jg;bb;^t7Sfr:E]A12omXK"n/Y%_=@pC_65%hqkf$'0/3"$JjMqM
_N"]ANi<N%?Z56]ATjd=C*IU-ra'P1$b?)DrK"t(I!%_WrotkiMmr3Zrp-$Ratg9/6*hAhF/N>
Y-HpEengZAS\sE`=ggD/9]A8k"j8:`;MUuoErMtc4q/'Y).M(`I7JoCEpM@;qF-O7(.cD>4_)
5]AR\i-2h\4ccn]A_b.I-e&tX,b>S8S$A9<m7JP"CC=FD?X1cYEl;JL>335nE=L-*$k<_6[\d@
%JFm+K"r=2L[4>=M9:8VL,?["rs>kqP=19'kUDimGlAhY[DpN^:;SR\Ahpr,YP=/Q*$!KR%<
p/n;[;b&g1$C6QneNNb"8",FAGo^4>U`a"DTm3!"'E]ADIIl#!q<f&05@)-JiE:nnjGI]As'@]A
oS&OQ,odhX#82/"M)u<r<I:kiZ6g3#5mi&n4a8O-#&"[:hQ&%6(lpQ:C:JjA1F*F+2hO`DK\
T@VM5CG-bHNh2ekRBkHFsJsP`#iR.:kRCpkD"/:F'\3K\1ei\"GJt8C+dq%Wfd3>p<eLq__5
Zp-i5YgY*a@=I;L<,0C%n_spB=8'DQ9'78Hl[uH'Ee0&NnOQ7oFCqT^#[usS_md=B/jan@9'
[jBf0K^GKF-]A0e_WWngs6DG#%`QaPG<@_@`,c)rl*_%1#W1Bo#gKdCfV+CkS#GG+=j"@:.XD
6$anfA[FAXek.*"?3JX2P'nn:`ddo\WNlR"*QI7[nD^ss)Yn\f6\@9->\a&2SXlgelp_%fVn
2g-"F+@)20dtAd:aSfZPQ@9oW2X1]A_ne?=`7l2Zar%#SS,JSI/@F+lmiVaI53R%Z@9(>>@7o
FF2Ejn?^3jT`INdT1Ld#8*</m$,R/-@N\^'Z@f\pPjYRr/$]Ago-CP+E+(.9B(V*N>9Bg`60:
E$8fln=X`4RaWlK,7*Hf$o8bb:%CsIu`9O(Q>s`#I[H*<g?Bka&7_]Ab,cl62Fn1rqc%iXXf[
>4L4bc"P%3<r4N<g/_H+2,(R3j920Q(='?$`,9ha871!%GqK?EiG?qZ=V>kfa5LQ7C(M[qK_
ce9\\M6/Va1Q\lgSLef0La0Vk&"Xgg\L-faZlLtN)]A0D?(V.9jG`BJU]AmY&J&@RMYYOlS/1I
Wi[_cGW1%K[%&U&@LX+Le3/.Jp>=*P8Z\.&p2g2%3`>3>nn9aGl2,.Y#oF/=lD>[MKUH]AKY@
6]AE(-(R]AZ5CJm)r/rj>O*_&=3<DPR/\Rf7Bh(VIN@hi%D*[P:56?]Atflo$MdC]AJ-aRg'AD<8
L38SQe(6Z6h<C_(D_(RZ[!AW!M-2XlQ&qfNSTbuE;N-%"Zt)N,92KnS5/Q@q4!6b#4(3g_<@
tJ$#hnRBZX^0;Ji;!8"K@"^:5;W\UgU6e_<h0]A?".RK1!K%]Aj+fb`D8>]A"ZW`7(FQojZ?B'N
#P8\b[FpdF.@Cs1F_qWOb+Wb;)\(@<#P85`*"Y4@'\5t@obkG5rddH$"&]AT9Ib#8CDd]AMBn)
]AMah4\7a(rV$2D1?BT[eSEaD(>j>T]A,5C(#)`!g"oC@P&5a\:)M4;LJ<aNLhXm#,o!,"'DWU
0?e2+iP1S*f8Ro;Baa.EIGGoV=M-8nk)Z",?LLN@rYYe8!e5ojA,A-G;q>jj%pV,*&@fN6tF
aVT;HN=&rCJ?;^.ls&$Y+TQTd/%QLZhdhum6?J&?C\g-MKc\'BLoWjZH'F(C)]A`jQiHUq6qo
2>^#+1ph2%OXd`\$NQe+DshSCkaNdZDCr8PkB4aM0#4YS>X^rrm%s74]A#1B48$R$B/Eq^#<g
o@iQoR7e`&qa9r)_?RmK8VNA?L^X'i&^C"=WK")]A#G,sPMgHI'#"4u\^"/X$iGjB*0OdP>lF
@a5,5K(pgc&5:kfk2`VmES+ZG,c2UhebIr%UlYGba3l"2V;7d!DOY$YDZM$dS-o7Q=l>Pa8;
k!5N^.^]A4u/F7X!bKT;@'#eQ;T^#'TU"k.)GiDK1>mFrO;\9sq0/MjYIRRK5,STT\AB$[1]A9
>?P/R@\I/'YE13n:!C_HirZTKta$cT_a#[[k\CRnd6SiTTU,%SVQos+Ml'.X$b1,A-]A9NC\(
W$'?ediKtfR7l>]A>gP"$gZ'X;+>Nq372Z2Pq"=.Y;#C'BY<$)i*jm;-k@p?`f[P?[q,43:G*
a.1T4^t'$V7[,dag"&memUkF>q/[n/\($3.FN;mbTa,e)m_b591bmgn[pHSF.o)f*P9:aIje
_lF5NLo5]A3,f:J6(+b,#<E#?!n`'o`#4P'B*Q6</p`DC5YiUL@k%$G'<NFqJboQlO*n#i.%M
5@fM[ZcB,MNf<0/,^4`PTRG"*11HQ]AD@5Jj+H\K+RY3T=u`_#?b_#"9YL/<MV[pB_Dnb#*Lb
c@iiQ$GBm5/ad*M=j0.oUHm76d"=".l@/mG8h&8>Pn*dhSI%mI*1=#MkNeA+Z:MDeAN=%'e_
Sr??50Rgioh-\5e1mN3Q!6hFhC'Z57SOd?'iJ)NZ+K)G0NtB*\#?2d&Z^S:HK/6h"ER,;00[
,/-On6,>GB=:q5]Ao#2Mn_@*]A1m)UiRkc4tUH<k\2=cRj@e%54NTY==D4\T"lR`hX\FthXX*T
96mVCXc8>'0f)PoaEa!eQ$h^a<jH%s3JuiJ5YA_hSb0^DCr''?bm)n(W:$lj(R>oQcF4$Rnl
V'e"0fXoXOY;]ALSaAMkZ2N.]A)4]A1Ja'`WoA[..&D1TX9>mJWntblPgVWAf'i4&I;APpeKSZ^
24Gq^2rAk]A-"R\Yiu[OKlWf]A'!#4chN#PMq1^;/qeA^X7b,p'^P*OKLOiu"TpL&1<+hSOBN?
6uDrU^t^:deAbo[.U5M"]AVZa6KWD3+;"<#<.:JL,FL,V=(S/[Y@dZp?'Ec<.uekS=!\!3IE<
NEF@gg"Xs=0[\(L^pE8;[-/E0kkt*YdVLSaUaU\gE;UsV)t0,&7/n99g-Nl8qk@nU:l,E0kB
_pqGtU\HDsr@TQ"\SZ7DGY]A;rT1XS]A8.1>?5(GN2r68bpQJQnCHe[N\7+NY]A3-',bh2OM4;]A
0d3U[S`Yk0+QfE^ka[f&8&UUd5j6&W@bYR%&*[8&VM2r]A\9!`S!(WYO1+U9JF)"h7BrM*A[7
7gG'Vt35ujEJ=:"eE`(emC%k:Ha",eRJ,aNg90UJ]A]AA\/G;S/hugmZ*]Ao'&,d*Npo3HGnm-[
JO5Jcs-4m]Aksc<tquKgUmIIA4>NYn#!1.07Ye4Yn[u`8!>4JM\nhMs^&sFdG`G:"udr=WrSS
<G&*=FaL]AG"A.h)#8-)[/!G@rHq%F-nC@(6=IDqnKgZLCSOYAiLcR%?Yu`eLkADLP,YaZgir
mo$icpn;Ad0<g/+)!G'=]As(-g&\P()m4`Yf__oO&W9\j?EkG&DR^CE#nRP>GA7Y;2N+4_b\%
[mF9G<WM-FGP'GcT(M[Y^OF&gY?eUBeb6_d"(4/Z[b5<*X^.[Y-.@6DGo)Ynf_nmbj:PCYnb
e9.']A[DYfC3lHSe9-/`9<dZGQ&,:-:D#Yc8"^U9<.\,*"#Je^.s%"[&>n`q#PHhc-.d1Gij`
R3Bj,A(Og+mYcqdYM[D0dGe/ma]AI4T@8F22&97J6*[Y(<$/`Za*G?+<#*kWGsHXd2Ud.VuQ0
pSFe_BoD(JL1^9>IG,Z3+qE+22Jd,a>@?SC/j3^+$PASpSr>u5-pEp37S49OCVU?S6`MS.+7
;@Q-tVdJRrH)e3V`+rV]Ag@sefrKYVd1B_APgMVJ"kES\LkRXP:tnD8b:4%Sf.HG@&^1!o#J;
*ms`4+5!uX5%!]A)2W"qM,*9WL"+2DN`'f7X<S$`Wm%2l1dDQJ2,FahZLo/WlYf[`lI@j@s*A
@:hV]A4%Pb5VT\pmqNL*=[pdP*DTc4(!`>G%eSAt5JS*:%ugEgLU,:1-n5'7"KGOD;cU6:Z28
csr[#PKi$N1naK)L>PGgZ0".ft*8#!]AKZp8d#Z,X[5.KUiY>5,]A*g1cTPX7Rc8C4u<SpRE;$
6/10U:[eIhTHnXqEf5eW8m/_#Po)>u4)siendISYh[Hs^g(XA=M`rNc#CtTY;Jeuc\Yc4bZh
::s#Kp&krKMt$g:JClar?F@%Ct"4(TsXRE.eJq!Z-L!g]A'5W=r*n^9D,I5e(FuS[D,s%S@<g
0:WSd46LZU<&2r4kXb<g;mT7&']A>(eAeNRBb*9o>&]A#Zn`gSQrH'OUjVCFC]AR3CG/L4CV;F#
nB$n]AC@H.X)8-cioOG.^[1tu2!d>mQL$T*'VUtg9p)mqG]A8]A#kERD*l2ef`Pb7o.C/O!QSY$
uP6BhX?R]AGZ_LAgMbW3I>P>(iJCD_.B\X[>If_BI+_!NZ3[Z\(*`^6d<Rnp1U*:p*BP"*B]A@
[-67KA"ne"Ma^&PX]A0j@oUV'ccZ6f5(1l(":"3q\,b0Gi/j8@%]AlZVaFg+12K]Ab@Mp+,K@iJ
q@&!p]AQ>a8p5&ZH@S!,.t#qb\usaI7DN-c8D4q"*N8:jAk?G>g`3>i\;'3.DGTKY_H,ud"+1
o[pE42btF+U-nnC7]A1*b-W*J-p$sO%9P<tHoaWe=g<L;ZbbF-6[1F*upM2p@Zd<U6X""Zn"(
#lsR+RV+-DB6PR1@LU_6/ck->8HJ,Mi7$4o_8)eT53NhnC8N6#?/_(Nc+p8#BX"q4?c[?6Rh
]AE'GHkeBWa9Y\j7VRVUJrJdf8<o"$%t2V??*7Gqc%m>r3>38H`]A&Y$PX`ER%jWW9a2d1XG3M
jlIlcMgKck8tHV,&ODdXdhq_UQAccAQC1iB9>Q=N-I\;e=(l?)O#%`?LAD,&msEThdXHIR@t
(tOFM)ls_S*;:KH'8QOs(US__=I*=/F^7$2G8>:/9o*<1dPH,l]AdhP0/rY,If,A]AYc4lmUs>
j]A["8(_%/n;Lg^!5ru;LtVL1uSlO:DSoEZ(W4:l[eh!jJ$RHOs0K:/-qK`qW%oZ%cZ$;K0Xi
]AAjfLY,%?A#XY++r2@6RfKLg/lnX\a\-f#FuMC$YV'W+@d)^2`V\tKZk)=njGKgo<AU;k:."
<"R6HJ\8E<8A+)[Te\Ae=?$-+8IM%TC>\Xtg9d=>X@+'2N8Qd?pd.#/'3Dlq8DE`]Au%$XH%-
p0QX"k]Afr""UE%[X"tVE?e-ttmc?a!OS=48^Q,9rVrnI1rMH>EGrG$d%#ME'B='DbOA+aD]A7
)?NdS)bE;nG=ir&Cq>A72gZ*\0@I"VR"k\Ylq181=bUKd<BrAbKJUjsDJRRn=b+8Y'pdc/:(
#%ul97*f.Od`r[TRk9@f1Na9'UY&i'p5<B=QT7DV9j/mU#E2T;fC2RWsqKd(JGG/.nK.=l'3
2&dF4QV/\&duf<n,B,XIV[NpQA.^7M/7Yo1$9=BG+NNO)h?+45'(>A89a@(dkQs]Aq)m_0?2u
G,><k>aoa#:@k@6Vb8;[@/JR9]A`5Q)GVFp#O2M4ZB<78Yh@=lr#j!)-]A9`^VH:/30#eSNV='
!Yi8)`TLFhmE0jtS[MsSq)raFCDZI/BaND2P/8uN>m4<q25O>PWIrHUVo/b=*RRp0cLnt`B=
jt'IVKJkm>DY1&A!?LP%:/RT!gi=FbOWh/\_##6pX+)o?_u/k-kX70Y$'fMk/1Q&I`.4mZEn
N2nFQqSNW52EBlYEe0W\DO0Y!<%cl47SP&!qYVkk(Q9;Ld+cMQ8/S_ooOl:SD@28Z'$SeNq!
7T]AEMFqCQ"5r#M!>bHQ#0#?qcYaT4++E=TdsK-Gni&18HBJem>J%8Y$*ZuY?>@o\K'd?04RO
<bPZ()oDlsmCJuA?K?9khS3@S*-j_anR/]Ah)3L7gn3P7'GgoL6/A&Q.eOc<\/r0rQSfG0-Rj
m9oKjqb,b*+230eXlQ^J]A]ARkD\#rg(-'oE2au5Dek*NHJ,Hnb/H0Vp]AEb3@\I:2S8;H3K\eu
Sc5Abt6a-+Z`Fh9%pg9Or?b$^pq4`5`+CCrjd]A8tdiN)ES:88flf%qoo`p"Vj15a5Xa[8Mb$
M"ie=1g0isa7Mb/L<l/Y9GkhrZ8F,q2o'd@%;+T;pfV%Bk_u6j1i3Tb1P#i34Zj6Vn25u!D;
\#+7)?<RqN)6ka&_.C8'>_`bi(Nd$%?Y3@Jog<[NNiqVEk._jCQ$]A-P6Z#s,:ifkqO8Cb7/#
gq7cVi;>*?:mk/G<Yl*A<LTHVJV?FtpDA:UFSb6!".M(7;HID84S?Du6.l^ViLk;'\VnJNHu
2R@Mc!WLouK)ccr91W7NWn#UV8oY:d4nR]AkY5Wm0oAg82`ZB<i:+#3I*8$9dRGq@?j4sL)%p
eAql#BTjXKNLP"GpL6iVT<apb:L%!k=8-)H<8kq+0f2WM]A(c+5-/=#<pp^),mi@UDKs(8GQ(
_)fio(&2K@r_?VD\c"Yn9Lp(h7GG8YmZ`stm6sNjoq!l(t\bRTSJT-WSEC00PN<sZ%1f'030
7JQ[`'681qK/Lo;&?9jLW^S`9d4l9*Q7A&E&cr`YAX[o!uCT0BB!Zk]AbcK4RJ";3FL`mj$p6
R'GE6LUDF#?=#58A@6`!nUouk(Rm#a]A#BZ%d2lIh.f3Ij'/5PV/1_1+U*;M+6n`M;Ym]AF,B+
9OI5`PDRF;(<2.,riBH=K+il**=jXNFj\JQP=P>Ai%LF>KHcc:C";YP)';:]A@TE&B128_O.>
IaFf%HB8ON5/BS2W3EM?dnLI&%YR]AE\=?oaRk.\n)96Z^?Bt=BghjQp[P"1X#/G=YhX>K,UM
cb<X218eK<o8*@WhWN7p@A3t&LJc-a_Jk!JPKeprsXPKMMoFco2V/I)dPXBRVG&7<9EgdPI/
9C4:5&XarIKY7U$mNCBVo$m@2Pqc66@]A>,QZCuq-t/0*T>G[dVh[_Q."d1&3A3$=Fsm9=^aV
9*Z?WJX:n8X(%f^,ZX',8<Ab9Aa+78VK[`lY:#oe9^"u1C4!0(ZrokoSAo!#=-*d-aIiQosU
M@""dO=5.\iDF#0ZD20l^[]Abil6G!4FSbM='KYSrI<@5-cMjqP_5%O4Pd#b9L8O*Y_J<[prA
%SR/<2:AIG-53HtFQ1^Znqlef*(n';0P0f/-&o[\dii9mk!=.7\,8C%-tuXao(SC6S`W\E/W
RCed(q-_VcLM37)mTm0o($H$EK8.C#I6\Dg@hV.#e!D0O<XTYBEO`1."`%gs4c"sqT"fV7W]A
>3C1#.@dOO[@.KCo?A8l9iJE5VH<jH&LN$,9McR6\SYVR9oOLBHtZ'Po=l$=7Rk@.,L(!Wk;
]ANKNT#Ma']Anjd6i@Wn?>L#g;*7M[Q$WTT7DH2Eug=S2`q).OA&n8Lar`(680I]A?ZQ#W"=iB"
/`2g,Q,Wp(4dp_47N1WLhM]AZcbM.kV:lIM^,S*K?^aKeuJ*NE`Sr#>[<G2K#\L$cBUV_b'3'
5bJ"`/JYmd<?+p-'53l$Ou8IT3nX'318_+h$>W'7EV'==6?TUH+C?<P)Pd<HW`3`NQ48Olrh
_bj2hqDoFM#4,>Mj2!oeNH$hTZjML;gDoKCp%1K]A"Z-hmbJZX*"V'UTi!G`n9=c;@UZH#O\_
-SKSrh9GS'J4$cU>2kDm?%mWL"p<NKZ%Q&+6AZn!>=+/H(ecYH"[de8N0"VjsH)\jmHnH;,<
[IJLkWeJ\In?GbV#:B+m+-_nuL![W*u\)Qg>#<!XJRDu'tZjj1s$RWggj7=W"cH*6\+AL!)O
:MW'S/?9XFT/@JHZ[A`%S1:PtB7(SOHZgd^GWb5`]A/$,'@J8r=;e1)q$1,qH\.P^>>EuBrFJ
r)C66io/#@fBL+l*YC`?!'1VU,#1RC#!H(WGArRpKHlC/$(7Up&<A%DG%-(^$]Ak:H+eh\pm0
#q&eNngU'3af*-mE&@]A9<iuVI.X/!C)WegXt+l0fHiEqGGhuEi_k[3Z^g_fi\GS-C3D*/.LC
D/<0$QX4*KKrbqdcJ'\66Ct2Sp\>c.C4#`9K=J@bgG>P5(L?j2P3$XW^Mj=\=2X?GXcFYV.D
-7dPsGK9S+KJfl';A?@O_$b?6j=<po.CI$^no#Q<gFd1t_gMHCfXq?\cn]AEaTh>%;U>WeUN=
$D8F\\ulG4%iEk;BO^*j>7_@D3$%5F?!KA*q&f2)/;>6h]Ak'a$j^1rUJUJ8a_*.d-"8'F[d-
<EhMd^-\L&N^>g(.2?d!58`^Sn=DS`".-]ATcDfknA_eTui<G-d:N$p2R/t-a.F4G?3L0JKNj
[[B1F`V(VDM2qmhL`C?$ND#%t.&UpM<fE/!>BW.!*9=LD7V:/H7F)u,4heA-@H7NWM[&*2r@
F_2=8@Wof("qpM.m"=11bDN/X!Z$A5V1SW`=h,4e6A)T/bNG<9$p6:P7`.boZHd:.=jg,ZeV
]Am2_e:d+->cgQ^oV7jYiJPBY49o60hmLE,L%%o9D_"S5naH)..)CFdIFs@Bj*eaOuZB5Ck3S
0'ZY\Td%32Se!7"QG2K"n@=G'4OcP_FU\/Z"HBb&k6o*h=3:?HabMTO9Z\%6SLkSRKi.X8X/
`49o8_hUN`(<_"dOXh!BPRW6\,%h63h']Ak0r@N_!uY1=.$'*G'rSF#e1HS@s=$2N/IWUKB6#
324C*N#nY4R@(qS@heAao$f-]AbR<b*kLrf&Km7otQ"P&.CSi2TB#9bH4[dcJJ@3c^Q%)ohZF
!(MqD?"IY:A"-j!?V@8N+JV#PU@Smod/)qZVgQ(rZpiL9ck4#)'tO@^^H+>biIX;M]AMbf1.(
l[h+4B54[df,h".qQDK0s4rPG;HBB(":YYpE*8>H3*qbn.KZ+9L#Zi<;E:D$qFZ>>Ha.;!1(
b,8!+12,gSMbsY)%Y0$RN)UR%L*C@'[5sh59#Bu7YtHG?G+nbT]A,R^`YE:R[BmE8Z]Ag%:>.k
74K/%8A11d^L\(d[%V"n^6D^K8NB,qjD"s2D/*9gai_m).#]Aq(3,Mcsl%9>ndCT0Mn>=+WD\
un2T/^V:E`4/:O7iVha/S+99='YN!%R<tEV7+L')fC@ZlFX)T0?Kgo4qf7BT/[!-]AVX=1_K%
[=Q[be#`/SW(UbhV07>[&WC=naHF3YrDu$k?LN_FNOjqeBsHD62rCm9cpDO8Jsm2#tEA'(%*
4/e!H5\U;(Puk(#fnf6]AS#a-jnsMeip&*WH1=U<*QGc\>%b9=t&r.48Mu*\i=1g%1+'aG+-%
Y?Fq%pb6OO*M5s-dS<,T&tZ=@WXnd$gKtbITrraY^47#4T"^&;W#YRMiLU@U"qV`(O^@41Ij
"$502LAsEE`i6Wu(Ak%6pEac9HLQ>n=1;GD;Y<"c>gknnkK_<+-7]AVX\/]A>'a%ID$DMp:skC
FYlA*>@A-m;StHf4rGi'DT6WDWqQjQhA7P:m;.S<r(8WAf=+94DM(<@dYpa2%X==8>2o.fpr
81h^AqR$2.jpt=Z7N@nL$-c;H@Nd%G8@Q<Qc]A:&R0Jp"8ud$T7nj>d@8SjqF[65-2CQ9o&c"
O6^TV!nUU0A;IYdQ@!(S>9-%E7%?M[*n*W&r1ga"KZGi\-hpa2uC9<)VkX.)-31AVF;h9>Et
qD,G#M;c;G5Ll5Hapke@l9.V?I-X/RB2SfBO6oge#lUc2QF6HsqiH<2Q=QeYDp#VAZ))MM*k
<f<]A=`oEL!qVNO)W31WJuI.a?hd,l"B\qlc_io)L2l1fi:J:L'6-"H6[>G5&;RuU]AQ7`oR7a
7l0`)kFHdVuO-=RV@6p:5=em>W`*6LYmd-NaY;6l?oek`4\n'aJRFpf%lTa'*PidROgueLU+
djoGSiLj^:bDGm?45Uu=G<1G.Y$Pj3u%L@j!W`<c/)^ADTg-gfMqjqroV9WlmVM6kH9NpIqj
2tEPhN@lc"B/`O^mZHQ6JQ">6GY6N(lpJ:#\2ipH.\Z1)`\U\3:Xft#aaR'U&):7Xs3]An<2p
RT]AT/#)`TAB9<S%_G<A`ds:jA6Ygno&%X@MjN[dOK]AhB+DubY2#kTF'aPYWu/%,8LiW+QaA(
1JEBOh;WXl<f>5=,/=h95c[gJc!"rtb>(eV+j=Dm&CiN&P#sC4CG;ATA4oo32Z?d3e-n0hLQ
Hp3R<4<>iL5C+HFYh&=\H$^-fm_22G[^3_pR@K"BbT#DgX1]A<]Am\$e`;dOgb._%j)P+]Aem'1
B!*-=\0+&?LrC2DXK[aQ]A7Uomat:?`'BSt"c3ocW7-dGV'Q&SI\B:gS;<Y+@e48]Ahgd1l'0u
&(=karm`+58%)L3O>F5h3)ReBTO%(/cN%/hfOmkn0WDd`$OB:W[qT+omSc&L#=%Hn`i#$,e*
'C$=Y/41qJKUFu5)'E\?-sf:!qW&Y9g5>ZrB5]AB5\VW<^Ras65ooX)g&CY]A2^R#PsO)o`u?H
A0>5/^IhZ&l=?-*g@l]AXm'_*_+cl$/TV5oD4VJls]Ar,%U+8<`QcgF,\>qW&7b_l0",k/s!!?
sW$6(@*P\=;CY6hTNF_gF3hk![_gXRQ,0,K-ih.&F$F4Ut[4a;Fr-i$^AFBdX"uj#,Y2aP>o
4fnM@&/1CBtiX(RaQVfmrYOoUVO`qe@DB%cpf%5o7mLINMb.>3MB"%HBCrA'hRK7<lqSFgQ)
\4p=;/grc?!2Ou[T9I:fudilp>td8.c^7X!U>c2HNPf[4GuOLsXm+6'/N<",RM(N)2VZtFoY
CN\M&X7kKj6Qc6BroLIqI_/e/Z:?&@U(I;-_rY==6FrL.Fq&eCJKs%IX7LRj]Aob8fN"gg&Td
C%4DMK926/b)<s(QZCa'K?b;YGE0/IJU/F)@NqRY\6Ekd187jZL2aQPn&(hMc&++1T[Q@t=o
e^Mi\ir<#;NZdSk5]Aj%tcC>B"D)i6rWidRW4#OKcH\q@Eq1ra5s6etQ5=d4+06OB$G&]A4A07
mY"VRd+I*H9T`C(_rC+Oc^fSrt6N[BCM<Ln8afDpi-,&[E<OA0MT!!dZ%89YTeE'dh(YgY%C
s^k#3c=4WZ5g-RVDQ_l;AZ;EgSQHs'SiK<*jpV9F4XS`_:f6b;S45LRss@u9>ekl!uNdo^Sm
>=l5538]A;9'#lXOSX[0n"9d6c+^!q(hfk==KOq@.h6QC+W;"n(-o+WtTg"#rad-!*D%=_HD=
-r9fT1n0&:o=G-.D+lH+cb)0UD&fg2bR:Nk<!eE)fo'/LrptO;4"_kcF;6G['=DSsaj_O1*4
KX8a?#d.]AW/a(aJ.;BWu8Rr,rEZ@F:<1o7m3i^XM#4K,?a/dR.t-`6U4dX[Bu.ZtFXO\-lsq
]A7-]A2j/nuK4LTJ,g""eF62=NYg;>1g-_F(8"n/:Mg5Xp\C"2Z4jK.*O;O`[[WiIZ0:%RZ+c.
Nt":I1_q$XN=!uQL@+'APi,ju_`_Y#B`W&C)5l*/pEgUC[ch>3tS?]A3B'$ja3';@1[>db>JF
Akp6POdhkq$OL(=G6YXdL?Fee6g%FV3dO2Wb40,Mhq&WZ!I@c6m8Z#jr/INS'VZ!iLBbZ/\.
`Aeb!),$qsrj,@ONkb!,gi`X8nZe[oA1U#9F+MdUoiTqoi_-M0kP0`c#@+kjupag;?2aRPmU
;Y`7R,<VRQhJk?GKF:rn;kjq3i.#7Xa<cG_R$18qpA2fsVQMTl=f_!s"*`NmnM7:R^(YM2:F
l0XrR$?:=)ANIOnIeA_AK:qgjSKP#$;2O#>5X;Roqn*Y"*-Z(q+JNFX90mFK)MX<Vg,=="m+
oo"`4(?WVn#;Ku"siYaF*qM1gdV?c1SJbW<J_W)E,:EVTD+F(2;a"<hKt?l:uZ#Rj;bN]AJgc
/FjH9p@N=<r"/TmYN!f7&=aMs?g'Q1H%^r0,%*\oDiANT.Mi>grb.2P11tLT>HMfBB#ja<pq
e;"aYr855CTY)R!A:rRY5kQc'j;g"<kCbR"c#RK-+<ujA"=fq#()IOE)BVQfF>ABk,,t]A!]AJ
0KK><$2fCn2*8W=RC3oZ+Uh1ZTVtH$fUENI/d.k.\Ib1Qp"/t"g%qk7&HJ\(H,_K7#"1_P>W
Y^la"$4=D`6?;GQ>JfaMqYp<'+cGoj9(5JKkcF08J3q6&j3u3pQu;JQqb]A7s*[&`_a;`MJ82
"7#2*>VQ3Xh6K;(?Hj'>!\+EQk2IE]AW:brrjjk&"'hc_%.B[ffDa$;''9P@EfE:>PP>:cALM
E,ABLrRXIKBkkC!4V7MqK4`"G#(sK;!p9gCHs/bGem.),\#XDn)XqeheF?`"JhR_B:UU.YDS
`-nb^JL2fWMqP_ForeDbo-a:Z@,!D$8#PeYPBs*e!8&&L=si^VVD;-$(k/\G-RPoqad1;j/f
cL>p0B\i-"7Ib46tJ[nB64\aq/iD]A,p?7f7"CMR]Agc'-:LK"+'=]A]A(BT.X(.qh/3:p)1iC7i
j)KjFiCkeGI(q/2EmEA'n`N,r@<=$QZZT*;Zo1cImX#Z)EjMKoFC(MOp-IOEsBuJ_i`F?W*%
h!,nIa$`PW)Wnf>r6`N9BF=hIX]A%TqpIa,a/S[(>8dAhm%d<-bDHM,jMV"Sf+6<CG]ASfeB_5
N/cTrP),MAo_+&lN]AP)_k%M#TkFMFa4@RE[Sc=/:n%C`8g&u4bibkr@ag<"+,@h1A^Del.Ce
3X&:/7s&7J>s%_iJ.ALl#WG=1Ph9p5<jS$P&n1ET?,`D^Y&OVV(8f/it\H@=j"I1);pm@9bf
!=B7(_Ye+T*GOL8+9#:LmQ!=fYG^l2jd-RP,']AfuUn-CH3K;eik;WJN>7YpYbRs;:Xg`=2-e
4W\%Cn&lPNF[eSS^E9M*'mTia=+4s9g.KDks2C.^/8"S&68l-ONo5W=g=?o7bc9!LLW*RkI/
g$S../j4`XELG&&9$!ag>[pd/scfbN64XC<"oMaFpgC-k\ch1&Jc(RS8.I9d9RMQlGMW*^DO
*^#/b=9N=e*ZgJ/blFuB<p:]AKp5aVm7.M@^31$ntr.g[c."eWd+p?Ge;O)F>gu$0Ta86]AX+=
oTeimZ^fVe$i?Xi$nH=XPD"I5&cDHYi\:Yc)60+Z,f^,]AV:qSYU/e7d=E-N6q=lSn*R[G;bu
8cW[FOS^-=8,J&hE^\0JSTsR<nTVe5Xa,3#t+B[SO[p!\7/4AMqBLQa>1Ddng73f<63!:4;\
41h=1>O]Abf5*##:h]Aj?ebl&qQV:Nh%u,ctLkJGZ$4\UU![:%A`6?.b+d,#,]AR"mCP0G$Y!<J
XtrQfCNq.VH@K!!D[>Zemb7A]AsVc=r/nf9`*(2]A@n!>M:Jrb<Jn9Y:7(5.JVfC</doCk%P8p
,EYCDM5?40aNJuA%+=#s'Y',I_XBga&j`'F^CjPMN[m$r99;b9A2>mW5E,q6>^eS5IZdep5=
6Mm_tmT/l0b>I5V$>arq12$_SIpB""'Sgh+`3@#6;nPHpuo4jXu'-*I"l9F+r)BJQU#%0P_f
bJ!VdN*HTR(>0co!mH>_7FcR]ARq)%2K]A<?`0r>M(Mr>W<imDp9JQ(N:#:G-LmW'Z++fe0T2!
?o(4L5s#9E01P"J]A[uSN2>^NfJ@\hin,(^/\K\@!ON4"@#D9R(/W/R6um4X6CrDF:&Ubm^9K
j;;h_]AWY<R8:L$/@#1;e%^44=CqUU6]AI&4_E:;"i>"e`C+QjhSVaGV0@`Ks]A*HqpkQC'J^CU
-jVHsE`D9VC3(nT_iI,)icNU$AVFc^1]ABUab+rk_@n1E2AQB+;*b'Ns>A8lu!heJcCJNp8CV
(XYMDhT.Z\F+lHb.*1"8%*h0+ZC?C!"sqLm-OfcKI=c`V!%1XU3-jd;\ZMiMXNdMV`_f>'s+
]Af*cu.6:[Q7n=L#SqDlL]AR=,><FQ*<Kr:=rR^$[0N'?XrATsJ:Ec%sT(m4afNM1gs).dF5n?
!C>!qi-3$Z@Go<ChuWcQ$CbtYuHp!fDFTIFn$&rVEu]A\kFE3nI>BrVX$GblAK#-"(U%e?X>j
%@,tM=;Qnm]A!b,hCfqM?lW[tUs0kc4urN"'+Uqn/d)"=aF!9S^oa4Vlf'>Kc<K3/#g00M$MD
=)3,9!$L8kNSD*!"2_J:Z1n`GYB:'g%^ZR4=VE<N,A/FK-l=lFn*luFD8-$[9CW/rTQ-dY3L
-.,*BgFHeGij=@->#Rmk#LZe0qdeOV;R-Uq,0L]AGVaW_%&%?A=9V8naG$.Xk5S'8L,7YT6bO
jD/A##0=!%Pq"-W[.\'87;"DXLiJjktH^PRnfClak@F"Ti_5YKDT="E2%dZ3]Abd*,dbS9^n;
hqTA>Pu,4aaQn_giLYM#j'd4_dWEI6%L`!.`9H8SJc0&ahSn`N`H)tA7GN3JK":IPa$W/-"1
^G83:ldHU$n4WVF\]AajD[RnGA`C$XR8=Y-LM>AOn>.=tu>.\`U:8q]AWe[c,":s\aOcH+b2';
1B>3ai'W*s2HKsq68IEo.Y4]Ap@<EZa?"Q2_fVHhYbMffY5F7F*J=U"!1XkkGfZ72Pb:;;U+4
cU&Q.cL3RS6IN[AKkp8#5P,f.\%n0dOLn[T,F.aMFCW'M.AoB*oT9P3-Fr,jmXE0h7G+ZPn@
SP_=^CQ,)3IpB)-@c5dm*"^A&]AM`q=]A[HcY0]A^34-p?cC4clB<A#>s,37*bEoa3BjrT3&!]Ad
R_bn6AOm8>IE2)Pl!>A`eO2nA$bV-UalB[*>&Bn*^lj%H!7YsZ2>Js@`KNeSu\l[V:jVX(D[
eO*u5J-ndsZMGr.qWg/;fBDCl4p(q9&V:\:$VZ3`UBbeoS6E+[+#V^s^s/6O2i'IGDS=-tV0
S@'\cAj$.t/[7iIP6+0N/`uC<`^d%Q4*T%FCRfg\10g(N%9$8*'Y2'hc#tKc-;+3m5ADG\Wc
LM*5&AH%Z4RfdAcAb@M&[^OA/pmi'25!*R2)E["j[NHX^4VboS@=b?e0T?.tDp]A]AlnR\l_2o
j'S=V*62NG%BN6Z,HBj<F%R1cTLUnrr1u#/Z"_sG,(+'#k_fG:@T0@ZAA.1j;@T22Dd8[^XH
$\`t$h\/Nn/06D7JDmnj&C>Jb9i@!HIQ'b,(lcdZ,5b28UA.Jn?G++e0XT@f@&W;;pWtBL=N
U";O-T/3h]AU?pX46AEnLD:9^-&NhQ&WHBKb1d!lAq4o;8#h[`0oIT@W%VM_!">0!"[^AMK"H
VUOZVkW=&$(&YYjB/Z2Yl0qO\-H"@3oZD=6Cg]AOoMrhWrXE2rkde8ZrJYOgQ\\?/8D#$q.q?
X(?bA#J:&97$0/ge"ODZWE&"$&I%bi]AD>gc5?,E3Y0ZI'Y:5bXJYW4hSI\3l?-52A3tsNC<a
2p)HKRBX?Uj'K]A)#3&TMlBYmjVT.mO#1_j&a+ZWMT'=!t4?TN!#1OhW(%IVr=AaeoMJ^<IF;
tBm>9A(!%BTOo)4!1-Pq*`01:<0TBLk<?/k\Y=d`P'$(eH4uZX+H\Y4FtrRe+1%Vr98Oel;1
sahrO.^T+PV2SLA&HR[^YpFidma4JF>]A)&eXZcrfB<oLgb>0$QtAr(J!MhCCTLW)P:,Nd)Za
eZ6o%;d\pqAK(<(PE8*"T+=5URN5b-iX:152lE5hqa0H\#obcV$@feP8RN<r?arr%^uhVT@L
0RO0AirlN<gOcnn]A_uSNk1O>k]Au^-\k%nQF4+t\QV-PdX:9WCH$!0QhS>/>%72JI16JXUi+e
fi>>TC`q<\Lk)96pk>9BPbdfh_F2aP,8F>g37I$A4MM\^Sf@?j*=BVWo'\:SiVJ'rA8g%5`j
.6*a<UbaX3I/<o\mNa>887^!iM8SKEP*\717pj=R<%/J5lH4Gdlut%k9l7F`WXUkk)JaqM08
?j45O02T?D&<2;jS]APA!PCR]ABd(A!&`2jH,0^G@sRCNOJ0DJ!c60PNccN<Vq:^D0pVOc:A/Z
/"!(G^Pt;i?iTj5oCl6MF6Td8qL3&]AfO&G<2[kJ.5Kug3_Jh.EV[A8lcRNts?#hlEC_(&/2b
=.T=ke=`1Ebd`T?bFm^EX_>UrG*5O46\\qK\jl4+H,8?;jYBX1$MdkU?.U;OqR,k<stqA.Y3
\rhbX#ZlW]AL_:;HM/pOH\)aKZ'4ESY'1GJHUA8os-6K")L6'r;&_)V?Bmj0it\MH6Jp+O;BQ
0FG,I.%/9_f+O#W&G_d=&nEri8X!YhJ7jHcFlBf*:9Gn!@<o-N`HIX&EMA7WI-G&3W,gde)%
.9dJN!V1%KO]A"0W5MgDji06;r_ZRrWO;Wo"\L!scOl2P%++9[%]A=23r'kPlsPrk='EX./2>;
kOOc?iOf&?^;R#E_R`]AFj-C@dpE-(?8$Zjh=/i*UrMsp.7n6)4R]AcraBN/,WP.2qkIYLiB:1
D$QKk%mVpZgEWpTYLSYX7j0S"K\BZ6u4#I#6!k6h?VpV#f\29>pnG&^sM]A7)H#W/!/91*OLN
D4H5F_Jgn6fTa#]AsPG8pJPmopMLS"rg"$)5]A5Io)@f4#1<o5DB?Y4*;jWiJ)\,co2lY8rc4A
fMr0D0M"Y)NVQi)c5M&,>?@&)R`7B8@XLgQ_d:XH[ZHYKi@4dnWZ>rp4,R`D@u:.EeRb11?u
&e\309N4bL]A!7*p<9fDe2'o8Yf4V<]A#1Oo-39*gej#T5s"jlO8Ze%j6#q@95FnW=B*8mL0$l
:*VV6Tj]Al9A$T#<DfMk54T?MZ7omafO8AIU0439V!rqBpU^c5Q>DG%WcdfJf8aZ]A:-H=(s6l
`6?DTS2#B5']APVNd?V%-u\b-2_DV7t"V5gACq"48m=m>(rIcJdO5]A[IotjT8B(E\$hkOgQ!O
$]A)MnQB]AN8S$'X%]AZcs-bD46u:oW[eD6i8=$n#!5Ec!V"F_[P+X,2e&eHW5\pQ1'8,lVAE`H
e&hKpr'FSlLt7Dfl'I\DeA^H#untCFKN*Fd4daEq&IL@"J`1:!@_&Es!`)_T*Q<`0CL"1J.4
^YL'^4'crpmarGVVVNBpbGGOHpjPqC\oC"+dQ;gLOk-IkCt<Nu&ChNj_;$*b4ukR#;RKYa(m
HCUbR5Ebl45`Yre>M&Tk\P+_O%6YWM`/^('S*5#'`;f/"1J>+Vr^1(\K\(m?PM^kXU1[.BWW
F.CAU<jX<tCkZP#D==;2U?9dQJ;]AoVRR=RM:RaORsC<Hk#,F7?NusI/O6?O;SH6/e&/2I*8<
#$Dq@dZV/VZ/X@otR&SP?/0>@=mZo+F9"ogaB1UU'&rY>#9'`,?DoG"jbdqA2enp4To?<e=b
#aI]AiB`H@,3!IM.n0or+=k)pFkj>7N7]A-6H1Hl_>G3V4^'"NmI[:/i(s.HK(bf+&KE5"ZcT:
j17D`W8k%>ep[1J3,m\H7LC\T!^-%ucNf,Ar%(h8T2^U=&^Y"ip7U/3K[CNFQ<D5r&GYVVqK
=S8;&7"ptq&V8lB?fG!uBNsM=:2J/AhjK_JEjcYq.6PMGY"kR=Uh*WSeP'KiglIBn7Qu>+kP
s8(>mr_IhV\)FKA3ahB^"SDD+sr!H0QkLR8'/4kO4=fqTPDlSiU17X^f]AFA/k#eK#thKA[aC
f6DegKrQ@2PcpN2]Arp-HAMP*8'e<C<Ok>@=FkFPq(2k;]A/f`aQ$pqJFDZb.EhNk+!cre4.1q
!?/j(P-X<h/Kg6s3\c!*?4$B*%i.ZDU7"n>G+S(.g)1A1[Y?$('T.lg]A$r`RBSE:S:N8E*p+
q+>%e?A(N+DaaQ4tlGk-p_J4!F1"%=dMp#XLH1N]A)b^WO+<W$]AeH4;]A5nKZM!f"beG.'Ek[m
KM+!7APo8Vg/dHi!`ed=!g/Bf$6^[F+Pt\L5in.R/lH]A:m`IsiJ=tFF;RrXELliqgLkq3ZJ;
Abe^BoQe:fqqb3Sg9uP<YJ'n%CsSqopDXm'[(;MC[5o?FY(ekK'K'2aNr^@olUr_t4E,kHbO
qBho3BSTL<EjI[(^,uiZ?C81R&h%"";\Z]A29lMbGjL?Y"bj6Le.c8s1JAqPLKWP,9n+$3ThT
\cNmYRtMoO)F$j\2l:^Op,HgQU8FnIC[Y@WRSQG\SVK3=VB'-d6+S]AI'C.D!(b_6:_iu[9R_
&@NIXI4DjYD6W)eJOC#='6,f_-3;Mo\OSuuTTJ]AV:*`Sm$d1,Ujl7UOWiB)k)=Qlou>`gYDA
kbJDq8%ibfOX(^^92P2B9;S+0771efK@o`\bc*JClRR^6F&_u"/nHS3]Aq:A3lPRU%mCP8_,N
aP68Dq,<Qs7r\%7O.c3*6);Q@EVTSIXMZHs5prZ.c6Dc4A1B]A@hZ(6sj`]Am,%0ZN?=EcV1%H
C(KX@a+$YeuMV,Ok63)?K[]Ad<HN)=N=.baFW+D^d@&-JUA(9IHrb5/<5+>jio3q'@MbnJUk$
_$/SE)bia"eCXX0-]A'>,ntZeRMj&.i8328\G86FY4P^2BUc#=[W//<Sm5(B516b66@*hR.bd
+?h:X`uBJFbP?lNnISa,TaeFTn`%b[8,GKtAAau):(F[_kaf0#MRgZ99E36,gcc0%jCpVWBp
Na=nt0p+HNNP,?giO?8(3*W!c&8YG7>&$[lR1`#H4sEQMr]AVP\+]Ao97*B,2_!I#1cO:5QoT$
:"PU2+u7_3ffEK8Z4ERlta43U)l+D1'DB83S(XrXZFYOc2QlB%k-j@\LB-BX<Gp"i85*e\%O
2gD76lW*mfD+R25>nP6?uFd.5P=gU<J-D?@,nc7FR`<(H[5J5`Pl(ePMp?%1YQu!JthRp8dG
f._qVVUZJ0Gu0.0!FZQ]A;ehN\2WBj`t^(e%g3Z%`$:LnYFsarD!M*[X[ML5NDQn#"QoYNCJ2
<VegM9slusR[6rF&dBg1FPoq,21@7Gn<<:)ud5e?.0XGgBg;p0XQnE:tg8oj'=R7A(i'h=[>
WFELFNc4.V^u&m]An$.KteL&Vaa0pqo&n!=qqssIDldkLQBQOn8)?L@'^$=o4n_'[:Om'<?Yc
!`lilWZ%g'jj0S#n!:I.OYeeESQ<Kk[/tGRF[h`X5=Y3ak`0*33I!7k.$!:KK>NY&t[2`6HW
WGAKoMLZ5Do3)uh]AO>Ja(2RUH\5M0rAcX2FV[#MY^XJK(E5eWl)=<&7CD$CZ#6/Nf%MSuN[>
Dt'k59\#uI*6Q#fu/NsLeapqH8!Gu'FrAOn6'&WXZ9m5__kJ05/r[RY:41?IfipBNCJie_hg
h!'R(g1QbbMDo<_c7Nmt51PW.o\>lJu4,M-HgnUHtM`/c=Z-IumW)NGJSOck*Xn.,/0\mm!J
DRR\,(3+8iQ>AM$A>6?us)o@<,h9$IZ[rKU1EEk3YFJ%rk-CUZ<>DciiQEt"Q%a8T3f@EnbI
OUceAn&J:-[hHs/o/iHZIUjXn$fl2[BaQ]ARH'm@AqD;_mhiC.d^#+*tIW^LS?%7"#!0Y'<Rj
50-cF),_Ij>95&gjfRgtK$iptWO"FI!7AUhf@9obg9Y4u'eA0!2HIuaKcpt7<$5I%d/VAMnp
F0trI7pd*>.FDp+e)6oXf;.^Q-R26c\/gmQAseMJQNUh]AM^E!_(uUl)%K?FUh8,"&1'VujkX
uT'%9Fk4g6fb'`l)`bf3$f#e=<e(jFEH;lUhQ8-jY4BM[#:/:h\hKrBJ>'0pT$p>"77BN]Au_
XrG@E#te'^\:RX^6'SV`g(*4fNdb0kf74?!)I'H=>SR>MA\UBc\fmH`6MEQHp9k]A:]A('Z'8R
t&ijo:3-=N!#Xe.X95KKBFe)"LhNmgg<2O[22I5iM";g-PR+>,co93P!bN9fQ1J+3BKuU"mC
X<ZP58(OE)u9S>bn42d`7BhuPJc->%r6aTtl;[VZi"s!=&OZ93r"\!TV'Gb`fmo/`D(-]A6Y(
3W(T%CRNWT$MkgJrb,A64#Od`j-J7H36l.Q>jGT6>e;WBRRAOguMB%F4keD/[<&);#HI/J&[
RgR#X^5'tE/"7hpGibc1!nCMPq_Y\!?5n]A7GW_'2\2?6nlUX(k)5;_XgN_`%7f#"KM*Ca9Wp
(]Ak=)i,Y,U^dUOrCYMX]AU/s0s]AYFlNYpC[ge(R6K]AC)B0SG/WWXM=5r^]Ab*r5aAhE2@%f//J
UI[]A"NZlPf0.9+H,st<tWiaJ-p:e)TFk*]AIdn_3+@UJ="5r$F&L';Yp0&Jp;QNh(3r(9+s;*
s-f\7ida;He\GRL>M6;OTVNdQ7Mk7R6$)W\YFIJSJYeJWkF5pH..dJoH_?Gjr_($$$RAsW(M
H>!i`aod8*+7d]A?X#Gc%"s"o]APR$F#cB,?KiHHU#=V&8d4#,?n^V/^[5;3PV<YS,N^C/T'2I
ooL5`)_5)8*-nB9m>iqXadaWfaNl>8dHmMfA,fS9\PSN"772=Zd2a9\Xb$Oj2LK06eMHM-8j
R=]AWWAN4sY^LtW7O-,E-_8uLmRWj8i5ntqA]A!ed)!FM+FCq*i17p+6t[/N9fPHl%lHfY5[1*
0d_dHa53?E3#X5h1J(a:sjpj=Mj)X)@.&Wa=YFA-&cZU$7*tic*tW[mfHm'@G00c05LRbKe-
hRt8`e_@#,D5gD[cd&*pA6CMMEN8Xo6lG/M(AS@.'c:gUog3QL_KRARjFfg@!_2Su4d@7NBW
`KJthZ~
]]></IM>
<ElementCaseMobileAttrProvider horizontal="1" vertical="0" zoom="true" refresh="false" isUseHTML="false" isMobileCanvasSize="false" appearRefresh="false" allowFullScreen="false"/>
</InnerWidget>
<BoundsAttr x="685" y="0" width="275" height="180"/>
</Widget>
<body class="com.fr.form.ui.ElementCaseEditor">
<WidgetName name="report5"/>
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
<BoundsAttr x="685" y="136" width="275" height="180"/>
</Widget>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.ui.container.WTitleLayout">
<WidgetName name="report3"/>
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
<WidgetName name="report3"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<Margin top="0" left="0" bottom="0" right="0"/>
<Border>
<border style="0" color="-14669005" borderRadius="0" type="0" borderStyle="0"/>
<WidgetTitle>
<O>
<![CDATA[新建标题]]></O>
<FRFont name="宋体" style="0" size="72"/>
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
<![CDATA[1728000,1676400,1600200,2095500,723900,723900,723900,723900,723900,723900,723900]]></RowHeight>
<ColumnWidth defaultValue="2743200">
<![CDATA[6112365,2743200,2743200,2743200,2743200,2743200,2743200,2743200,2743200,2743200,2743200]]></ColumnWidth>
<CellElementList>
<C c="0" r="0" s="0">
<O>
<![CDATA[銷量分析]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="0" r="1" rs="3">
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
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-1"/>
</AttrBorder>
</Attr>
<Attr class="com.fr.plugin.chart.base.AttrLabel">
<AttrLabel>
<labelAttr enable="true"/>
<labelDetail class="com.fr.plugin.chart.base.AttrLabelDetail">
<Attr showLine="true" autoAdjust="false" position="6" isCustom="false"/>
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
<FRFont name="Al Bayan" style="0" size="72" foreground="-6113837"/>
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
<OColor colvalue="-1441703"/>
<OColor colvalue="-149760"/>
<OColor colvalue="-10502420"/>
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
<PieAttr4VanChart roseType="sameArc" startAngle="0.0" endAngle="360.0" innerRadius="80.0" supportRotation="false"/>
<VanChartRadius radiusType="auto" radius="100"/>
</Plot>
<ChartDefinition>
<OneValueCDDefinition seriesName="類別" valueName="佔比" function="com.fr.data.util.function.NoneFunction">
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<TableData class="com.fr.data.impl.NameTableData">
<Name>
<![CDATA[Embedded2]]></Name>
</TableData>
<CategoryName value="無"/>
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
<FRFont name="SimSun" style="0" size="144" foreground="-1"/>
<Background name="NullBackground"/>
<Border/>
</Style>
</StyleList>
<heightRestrict heightrestrict="false"/>
<heightPercent heightpercent="0.75"/>
<IM>
<![CDATA[m<j7_;eO["B,o&nWq<9WZj<J0<CXMe"[O7Sds>(J;\:6@&uu0E#SFTm5V>tt8emI<"U'L;7A
,G^,!pt<6q*>EPR-6:E(`NJ,`iR(#g#9(Sa!MmI3-^^kFBilI)D.4Gd;PM^"3)[hR.fJ]Akd$
,J+;F0CoP\-\))FHg"nkR%_VJc'&m,6rSI7/Dk"MP6$g$6Xg\B'p[7hC+Rtn0i#P._/E(ME$
Y>'Jon&%nYoO2O@hJC=msA+VDb3(UQa8=>L!pjqqnDaf]A$$_!^\?.O]AW2WoXZhjjY#Kfgo_Y
gNrr*F$[7(TS[$oYupOE4jPV^fQL1]AK=fV(.+-Xs/MG\P)*Vr#)SOth2>U5'LRbqTE0SgTJS
-]AJ>rIGQTp97m071R=^Vrr(R19rlE^<^e6_.+go#T7-N:^LI_!qVV9RDQem!/mZ'<<,-(F-g
SLga\^eta.o)j&-uP7Ug!BA1@"-1!%1/E-IP6>%<qb2Z\i:,2m)\7Yr_3=:GoGpc<u`:=(!B
#bTL8gl<:Eh4'0a)-;t5K,BOCo!5.,5\4""P<ciGQ2S"m8OB=S;"YM,O3!I<07CO*?"M553D
fHpM4;;k&TncUO3lMU3o1[Dp0*56ZISkJBSnTUX1INY&lg;rk<DlsH:Ve+DV'GYcqY0p1]AX7
;QSftEsUUVZ3i16rJ>*gY78Kg]A7-;MqQ#,`7oBjoLs/=i_[?p5cor66hCe@"[kAP'K;"&We<
r3Z^bi7_D%J5C>2iu1DZ1@#_)`EeaW>+ZI%;k@!O5`M7!DOZu`/qPa6f/8l$7o=":05_ue/;
c9l.B9@?CS$J%iu4\jJ?IXD(6%l[WLtK8""55'Jl43n[06WhjisTfR3ceqZ4g$.1X2qDM(LK
:*>X#mU4;]A.ZSW%Sc;Iio2kPS%Eu[a5.)]AF0-N5b&e"8KJC,=[<S5dl9-O@AdUfs9<]A7L[oV
!m^M0L[p>S,^)b'kb5<fpR=NH)'7p+lWs\*2`iG&`tNWMI#X^(;>9:8%Z$%rs7*,D@H<RTmD
kD.5RCa@SH!MX[DiCq'GZkPPdM`Q:1pMnh7We>OZ-$rGE__S"KWNe`*u@H]A2Y-gNeRPRc1RG
_Dp;IfUk@N2q_217$Y5n;>9Eo)qj$Ao?DK@NX)KopkB;72rqUSb.S6Phl<$]A#[$rupk>=`*C
`26_rO-HYfT)uB;s,TI%hoDA>N%.4n^Z-='f]AHg%(:-2ibaJ&-)R_fnc3ZW`04]As+pGW'i@)
'_'gpbBG%Igo?0IGKJg.'+)$^PaD,U<'05RBgYL)7:htNDklM?QemH`ra5$1@*bk/%.b^_n=
C9EJs$=^*&.o3b"+8;#n,\N/C"q]AOqNT_$H"gfYq;W%FFY8DRfF4Cgrmad;C$$!Ed,905=#+
,d6%"fBfmcrQ=9"MHg?1ljUJWDIq6,$ZOh"*`LVR1K46tORj#apm^:X<k==6J6%_jjQO$8%&
"FfRS$JuADV4DF,_gdF@[i4*J\m]A&alq`\ecF+VL6G0_HiTc_9HIWI*R"W%7:\3$:gHhY)$^
hoW:,-+X##5X.lSJ=$AS3f$$$\1/Q]AR8g(2Y*dD7U:N\matZJ6u]AiKgXcm8Ye^.5'mJT<ldY
Ge4=LNBj_)DE7I+Y:!p[AUS]Ab,WI<@,PH13<.2ch;.??Nt+^qh(>p0:^U8diV-DllIjl2:Bh
-A(hc-;q[>b$d*BoSle4td/u6E:mfJjh$[@?D?WZ_Zfj]AG]ACeSr'Of,+uESA=(5^P0l`Pq0J
dH;:3KnGu\3cf3Tr+k.%u6*VR-&Ol@/mI+b0j_m(%N?C-.RBqpQP[i/)p3!;e3]A)8hYgsYAs
$5Xmsrpb\9L9K&u-p`1l;'5%"e>71Ac')o;(95c#?C?q8q/)@=IV*bg?0td[QU@0>RaMH):U
/HAFhtX'Aa#@^1TAZ3O0<#V[.M9$j>+R(MZX%i6A'LO-\Y(jacIJQ!2[=9iNB`J5E/[,]Ac*9
a.)RGX"80>8Ld\7f4B73IG;-u>K:-g_;R3oDW*cd3&7UI]AaBmW$A/"/Us.#E0!-F.M2aDt)H
XkTG'?aO2&k8]A-;.1d9.=)mSHYNpL0=5*H\U?lpR*HQ1Z`6c9Wqo%h*G(AY-+85i_qrpq/fN
Y,7(GV3eu/*e4tKBr'S8H4-YIf[hsOO4[E1LsSK39'`b^Zn)Y3@AB,/!*9*K'4]AA8=T(;Yi^
!fY2HLY8t6JGUh%r8%N!ipMAOA1e`Y6*\N>Fg>rS$.>kb<*E1Ih\WKL?>"l3;;7gXSDDh.j,
!X$r8U)G\8:$B]AS9-WK=8Y)V,="J<.-@jc>m&'ckXGgWGaPEb#ksIW8C`rH$.FaC3mXm*q7>
`k2o7I@[N?Aq5_-c7iH_mYj/(H1L'aRGML">:!KoJGO0RPo]A!(0:#*.O,QD8.B5_^REZ"&NG
XIf0h_ET"W4qNsS]A5\jXhL-mj/s:emX>1O.g%ntWXKF8aDu(/<`'[8m@naq6/T@!UE[H)1(5
-s<gJ-A+H)Pu9C^/3grtR6`I)@#Tr(HNVBt04.-.YgLlUUUb;m:DJ-l%,a0I>6K?"'"B'"R-
qg4465hZ=V,r"^a0$%rkD1]A#/:*gc!(6BK?XTXccGn%;=\kFC,TDS>._:]ATtNmtePkj*cT(E
+f(^A)^)VJC+^KPh&k12+COfT"r+Y,BR!gF/`r*9bU=>+\(p0uk[9BB=:eLH=J[>P,;>-(=D
iLg,X]Ac0-]Am2sH*5i=RN8O]AXqe`0LPlb*>*:f%]A)n*3A$Y+p4I,c,Zk4jMuckampA<b]Aj.9d
htqflZ#4b4@?kI/0lc*`\A]AV>)>",'F5a6>qS]Aa_$Z5QKT(U3K=j-AZiONMT^M,M,OCfbn&%
SnRCK1e,h-0FehC,Z-2\gP@FW-rL+CJb3l$4X0;4@^2UR+s=S1pBk"e+Rd#5Mrf\H')l,OY,
2<<eW$pUYR/$UO8KB.gQ[Fa[h@-C_,=[/.kK!<qa&dssMO<`@g>AO?tP>,g=B[!;+Dd$R'rG
PUk9uH#i$b_83[>mnc)P^/g[a*E>/rF#E7SMp*16dSXIHbEMe-r^Z/";m$53V#lNLAY7N/LD
D@/VC]AqnhV5<n<5lT?T;ds+n)a7a]A6okb;p/'d(YefGtoT-K<]Af/6o'rd*6e$Q8&lh;!1T]A<
RWS7n<&^;Urs]ASkFr+9luN0(.'^t9Aq)iaCV)Z@9WOb%cgHc.DJ\Qa#4q@B_W"3/!PR`k9Pe
P8DH(O72*Ib_4C4X!8J<$a45c?^J?<"'f^9r;rbd<s[fMf9.T:9Qla'4AakA=S8A5r^pX2l:
l;#p8V\=d``I[n"GWr\Jp@M`U4..`mklo$mg=>/QLCt2b0GkDAmD-$?Z?,URVV<97He:BohK
t]AEBT_8lQ41L+JVpfcb]A%[B8PkM/fh**bJ<c:%*I3BM!J;[(*EEQFmQW1UK]AY#1Qrj_2nD2_
p;-W):Xm.]AR=QN7r?PLHXAtO5gL@RiKfpNR(8#1POTn5*K"h32M:,FfT)M4E@$<8U%7=_rTl
fX.R)DsmJ$DBB[nQ>6">-&\sp>6C:/TH*4GC%A&8L)!F2e=SDR!7`@/R,(CdN"JMbh\`_gQ$
XG)X]APXls5Dll&FAt"dMrN(.F.F+9Nab\UE"\P,E]A)pLl#`%V)m3DRg>O)uCQnT#QPV<kZ8m
bm2F`gLk!!EV,(H@F.Vh-TBgoNs;:iU-N&mQ?Bl55@XsE2ej\cdEPd0Ym.Z3Gh%I.&K*kp]AS
:#&cg^kroQtE_VqN-3Hqj%o"2NPA!OXEqO1H@0rr#h&:J7=o>@X6g'iTdqHq6q1p\DH0:N>!
,VYAX`#X7r?%.1M*8TOJ+'PhY6G6URd5.h#Wo\kO)if,ZB_[ic@MA+d0nk^i1d<;F`N#WV'7
6;_ViNh6W2,3<"'hGojh<IVG7ci_$OKT9gnReE<k3sS]AaHY#<%;!hLkUgYR;pk=bT\9-0<8?
@DqtcsA&F5'7PsNQRT&nR^;g!05p9c#CrY)TCNilZA&?BiLUZl7V)ATY`eS0^V8eI9+do<&O
`[0"CLp('/pR@5EcKJH\E+U2p?d4=PkHG\H\PV]AKWM92%8sFBR"-k\>1rB*,^BAb)cjtkdi,
_[?IH?aQleEpmr@p"`hcn_Po''fkTed4=R'4(Af?j)H!/[7=pa2u8n"\::0uk]A]AGOCSAK?V#
=:c++p\lBD0Wjfc&/SHMNg)AGrRe_LWcGK5Ofe\F)Rs7)NG_lnJ&puqb`#@P7$e)3g_N,]A!K
p\6oY6)3%Zt?ghaYcc"B:7'/e#@-H1\rAk,')+CP"sC;#%9[KL-ht]AiGJNu.jXll2*G^U/j$
J?R6#KLpb+pbfdj15dXuRt*lD`C]A5_<r$nnXS`:F%:Tt>q=D4ZM'Dlh_+keqB/&G5]AHEf;&I
8Aje"cc_XnTSNV!gb$qO9m$LnOT-l;I]ADS`p]AAisgq>R<KQ'YS1$e[!F4PGB!7__>)[@-R@*
VCe[cbV"f2&F[MXPqXiHqj==i@mfRZ_h<pm1lMjp8c::!Fo4k?c/uhUVV<$#I(_T?+"nmU:'
E'DMu=M:k52\89trN#E0CXreTTd;Z*t7!VSg9+ALn,UncpTh%aF9[cg(#I;^1rl?_V\Ns1Y>
e-;o0,/u#KmiB%K^OGsd:+HbC;2uc(J!V;Sst(6)'BY&G%S6aPBb"l=u)-M[\<.nn%K*A5Zo
JWd*[DT;s,WnZ5[:P;?2qm6F/$VEFJdK/4R)M1PtYTH@XfpI5*i0\j>?M"7FR'n2EC^Q@]AT^
&UAhr$HooL?RE!M"J<SNXYdM,qdtFQU:t\a)BEb"W]A2+VXKSFGAXQ9>9V?ITIO*#[]A"S+Ub;
6p9</sb\TK.=NE*$R2Rc6Pn>ufR*9_a.H(7%X0o-(N"5(dguObc*uhIqlKPW?G7g6;trZ6F@
`([>H]A8KVT!?qWQ`QWWg]Ak]AA;mm,Ki#3mb;33X]A^R.CQR3g'T@aZC,),e3tS#SMbV(1+cE_k
:F+rj\G29\Hp3(c@d]A[;=['>ooUh>PA]A?aA;4HT;X4g?QUC.7\@kW@Occ`j\pj\qXBPI@:[?
```6JKKH,<j$5Ec"uD1[ob`+Ffhb@0!.;T)<-%73kmH8O$i8^lRaZlnsfAmV?,DANhnU-gXD
c2$[u@*]AGqpZPO77aspJ0l5(g?"af,aH"X;XtUYk;#ObThTl='/SZ]A@Y[63-Vqbpth7>+3<j
;edJ60tm$)mPi!1h)t'5FQifF)2"V7Ij%BA+PC\X3:H.`ZXZ\g#9#Qn,o:=aLIbVV%X;Rr%p
+]A51u52oP?nKl"fu5nUA#e"dR#<&(1P3<&9Dm[as9!sT*pW_5GU$tbl05nhO/0t?"V/'9KK5
+nC&oKqXknCt_/^Z]AZ#j:n/3Y3\CV5`-""W^[-B0NnI8;6+L]AM8,(c[/gT6[(!E?TCVAq<f4
["(5+gfp,aBMIqoJrXfi9C`[f17?2'I-Q&aA0f%ETm8Rn+6V4naP@jp%'X1<RVXmeL'Wse9p
$S&hd*Bdh&>V8n"ar7I*,pbQc0D_D:Sf#mBE*1qLbn7P9knU^lM9a:2C!JFA$JK;HitIS=rL
@@iWj<R`q]AgI:$Zq^N%&^oY9G>'Bk#-AjC=lZR?Qh$.&?,`^&H&/sBD0YiWT:e7G)$+-C:cR
(o9kUq5nQnk9bE_h[pX,>ki)R`B6Nnr/IUf/oda(:cr2l#KCiN+n3:p.[%n4"3SLdHJ-g&$M
`/%;gFR>#A\8IakEWc0A<-\!-?r6LX$;Cp>e+YX.1U0dBk%EJ9h7"4WXkea;@C)F7G\UL!h@
6D'uUrR<"KtO#e^UiQ0$X;l:WT9Efq]AJIFe.S:W,<$D>qXheT4P^1t%7&X)oZo!COtJo\3l_
EkNfn\)*?,^L&h<h`msB,DC'ClA`-_(F_J?(:Ls`<h#L4`?%`Me0XC4%eB<^0mQ!VT=4+T2`
!-D,[e*bjKb$%-#$'/]AIc52UR)OCmnFN\J,[D*#eRY)i.X'E,'^2"O&L`thPI/<L,IUQ(8h0
U"`2cA-)@64IT3W%9Fmm@Q4AN5Vi:tNlT_@I-LV<TAM.57;r!e-]AbUUA:Xm21m(sN[FY5`f4
dEqCGNH%Ypi*;JBnd^Z1(L6bUqp4?]A.q;N954*9]AcoR9k@e>]AT("";X@N9+Q&=O]A[2/E]A4"d
C_XG4K_;F.To3%L+H$oXaC@DkQ%2mB0K!iBY:mKcb(Z%@3?3C9k(hV,\=Ff#DSMK.11C++$g
j^$/>FKf#PQ\1A37.N8#^?Gt&/A!dWf;8,M]AOWu$@7Xse<eUX\&KXD;U'jh'>04W*Aqr<Gp^
n%3jUis6l%a0Ob%[[HA*JVS#VNi;g7VerMk&B/o1>rt#p_mk<lRhiPP39aa`(-UNUHd6iSN@
24P&]A4Xg\hI.]A`)rHm'3B.fiXh9=(Kh\2u0.8N3Xg=3M1nAB>2&dtjQF&M&h+k4Hoi+k]A,&X
-;0p/rHXocOp0h+a1'$fCK%l"gnm(HM$6CY0^qpWC8garI*hYW70#=g<)]A*Iq3EM$2:Br;,%
gNFbY%7Q0<:/d"2\XF)/4BH<'ftTmt>5/t2k\XI#R(\9flp3@&B_MCECY95.9k`YNI$Ni+Yg
KggBbpP]A$t>J.c\dj@Z?.=3)#G>AVZ?D%cimt8BdkWh(=B@`1o(CJOpXk-!HODG%V*EJ,^.X
=Uh6F^>O\Bh(+K\Ue1bj:etjFao:(/;:a-&AIGP"?*p%k]A_+k&]A780L=;(nQ$is?!1nfS4aW
9jN>I`&R]Aso4;2A>T7`T")PlKLm2Eo,0+\.*ENDT?Gfj#.nq=3+/\B*ES)Cgc(e)Q%.o\$e'
$/l`ZLmJk!6\`o`-N<^&(de<1CIf9A_N;>($;G_#TKN#iO(&\5ci@"-%1dg+o1m$fC^c9.3f
n704aKGVW@/kga"kq[q]Aa%dejTmR<]A<r7hotJ[i.H-V3.*S0N*&W_S?:l)g6/=643HZ/qhUR
8WI7XB."_CAO;u`M=VlJ#u_[7G:"Ad?$cQf&Wc\=:eON^bcM2H.KnNWPf0LcnAt>.1BLVBqY
i&&h:SN[@U@-o45j7,X_.pWLurOs)c4guE,8+jNR1;D\4m:J036uBIXV(F[#J@B1$3[*6a>A
SPS_f<as<*bCBsgroqt$1/1mm[%9@)papf1kOl+)EjIYapZ3sWOh4Olio"eRK00)6@Bo9?]AB
*oG'Kir;$$fF?V6f@?a:j'CM:2"bfX/XEF/GR(]AF70Kg22"+_6,fFLnRRDLgQ7K)nCg'!O<W
:Q-:]A'R0ZqpBkK?Gn,5<#uN%8nuloUth0]ACVbYQC.h`L=LUR_1<e1=<&4(+f%4Ig3DPf.PPc
J!W<+,s&k<QgYQ"6:7PH"0cp9N\*so7=aaQo:]A)!,g&l6]Aamn!ktk=;[=.rB7L%S,<^BcPZ0
6h*YaEk1ju\>*fn509\\05e3e`W[L_pmh&IEB,5_6JKLT$:#Cm>sL9o&PKFI=gMCUuMrABXQ
!LaA"tUJab-9_T=U.e[?`6j3.[1@HRZLm$>CV>7[+R27k7;P1D1n_!KDr[r+i:IF=ia7V`eU
,0+BD?[h&D5>1=gH&*u-mUK\/sIq$A5<Imr[c>6*]A]A_Kh'h;bMF]AP3ltR>G!_?!\]A4[g8j0:
3s'dO0A8tCBH5)"H\-bH&Ai?gohP)n2(;!6sF^[*bmSXJ1[cElLofp=#@LAe-Jrg&H4NO6;T
FF$![8.8q^$:_el&=sh%2%IJqOg.q(b[@5]A47fsc1Sn.9/IoHgR4[W6aA>%%-t@_N+6VG:Be
m35PB<M';N5)Z%K,-Xejg4;,>t4;EE[T$ClLcY0!%.k<3\_\qF92q<sJ1+4I@e'B0sL,`L7B
RZ)1>Vd[hnHTjB?Wh0"9PhnR_@<?=d2"N'#,p#cZr0+<3N3@QF1C(<<@ipHi8E$9lK,B*6**
sC\UjD5g!)iDO?2PJd&ooqAmUjk3\5OkQQYfB[*1_$%7pU>1i^ee@-C)Rt1h>rP@VhG7UXW`
@r`GqRKC/`=G3&0T!1CWU(pMl>gXC#oE/7Y)._M+G)\qB>@+!k#F9&m4L!gC&o!t#X\)_:2.
^Gs]A1,hG0Il0Kp]A3dUaHhcG@CHSA&eGW-"W3,GHcbW-dbDd@*u[54?6G>a:VR&QGkRH?YsUM
cm4RB0VS36K4sYS-.W+-`rh`/)jnFtR3Qe%WmSeY(,Ak+BjqXKP3AV_rn\TnI?XqXg7YU<6-
=;Xq[WB;1/qmN%M2f$I$aRsg1a,1'81qN-l)-i1V*J817Eaf4W0d0^,Y^Su]AkCW;Fg_e1$G8
>NJ"fB;R%6qfcdFt`,a6SdqrL%3`Z.oEXH;uYrd@IpM"iVNA6B$rEkWkfQ@_RX$X)MZ<n;.H
J_Xk=?+$r?63;B98EW.c#uEbgrUl9m"o4t0@D&#3Efi?k=iOuNMJI&+E4Z,VM&ZgZ8a#Bu-U
S^+_V*O`^Dd@l--@s!p=\n2sHG0gV9[1hDcoq2kmMIe-&pY\Jd^Fq:7'a/LPK,gi;-@6L=T?
o9#+*nS$J\_uD7WY?'RZY6XeN^IFW`?pW_t#W_Fih0gl'^`as%BOFq*B\8!f$eU\c-+'Q))9
#3cN!$l=&,R^H`.qG_mf>pmELA0tJWC?)XKVjsrj&DQ#qTM57Q*[bmbHDY_^<#7cWaMq(CfL
?#Ml458OC!PX#iRYJj2<S,uH1t?qm=4]A0uT?`GC`D,$m2-s(2Q$0Z`AY!mEh/V"&h7I\l-EP
8We^<>'@-K?9aK;Tob0sAhk]AqlWS;Du&ceM2qCmiZ?r"-"t5rcoI.&:0JG9Z/oi00@uC.di8
%lCo`b'FS0l*T#GrntbHq,h(I&naOoNAFGYdb!-\0%<)2Ir2VDO3oS2*6b0n6FdJ?"SDSe/N
Z57S,F!'5s"XA!&\bD.#s"Lr31`U)XaMM!0K'kata6N@'?fA]Ar^cb[<l(F+OBQa09SqX,P,7
gf*s1-[KV+BQ/-u9E):?W_k->G:]A*7@7HZg+0N7obCI*Qe3]AO0H2FJa)'Uf8B1Vu]As'?BD74
NeeXG;RV[=>N>I85IaTbd^h&2(Lco?WpO[kA7rcK;Bbm\)L\ZqpZ)o`B#ZgE$]AN1.Jtqf.q6
XIdsR]A"Ol9(cE`\u_A>1@X&b.d;!I06\fQ<(E;ILQ7/AlInM:]AONVso/Vmco6m??ZfR*:O6P
=PAb9&<sZD]Al/qSBUq^Z86qq#<S#KSWO6Bm%u'ga1Bn=[Pl8L]A3PN`2A>0H/DsdL%0pukM,&
6Da2EX%(]A6]A^j*ER:Vg)*QS;'>[mliBiLBQ74#c<s'</<hkkV1u:2]A76AX.+d-BRC?fMPb+5
bgkAX(OJ\fuo`?5ba*&$h&[6Wc)t9?cd2*u"@jq>D&$a&,XiOui/Pc%*CQLc`<4eCk)aVsIp
MUKX2]A??*-&]AN3BJ[?J3W!3%<[c9XcXGnqam,<bRJZtQh'J8;jsWF:@Z5@,+re[#U'P&.*)`
>.X^tCTdi-2"Pk&gmZ55@,AIhjJo^+uG9i;K""et98:8sNM_<Q-f]A*rH;e4m=$PMkJ#blQ,t
*d-GjPt<h+pk$A5/rq6F%RW3m#'"?Eo.f(rMUa8&fm72EIKK>OlpT4E%I2)7r&I^5rp:$&Cc
Ktt%Me?n']AY"Z$66ch;hAUjfJnGeTrO0Ia>@i*d\3j0ZW)rJUr;:tN<=4_\TCN-MV"1r"J"7
:N[MGOR'#6a94Ia#;KbauSS*jX=1o=C%c_X15ct3tZ_2[=j#dS%CD)*mp0;mtd.HhS<LEqW@
#`s=HaK!qA_sfadn?kFn^>`"XhZVnX#>'>]AJUdNI'eAJq@CMI*gS.]ACP8^nbZo<:iVhA=;^i
Ee;5p`[@N\_,)'d%7^7uYRmPQjjWLtVb.bY&$E@gIsY-:;a!cJ0h:0U:M:Pd9i#1"b+4Es;l
@RKfK-=9ICeq]Ag+ei;%jO;ZWr@bo,>\$5H07lNrg($8Zqm*K![J>l&u-?*=P`9]AFZJ<-Tg,8
e4qs%7.DenN!;%X7A=Ab_U"aW4KH67;?H1<D.KO=Z%)c/d'eM/kU=Ah.Ii)FFsE-a+U?.uYm
eF,f[)qLI%NK^t/&KB&.P=A2@mD8a]AP"BfbD,S*iK['=I"!!a0)[39#Lr4aAmCb04Ii\tAnp
E2$[7Jc.Cb1Y?Tdn+uN<fPh.>!)J8mUV^=0ha&9Q)%hASKqdM<n]A/SQE(CNA<7)C-aK+gj$l
8rkd"oN`na$MHG/jR@ge;a#qMrjk4;+Mle=t.>l<4^M=m`th"7L0&_1#h)^Nng9?CTd@6)m*
/]AZ$Z^8b9+Vh[e;)dC\+B;`Yi$hbRDNku7NT8ZLl:8h*F4WXduFO:V9j-<.srG0\?\*5,AOB
gf^MPWHmRTCXY5t\/'2VP&8b"oIk->E?'A0-:g6!$uR4o8>-c0mGW2^!I>mN8=QiY#%(7!L)
GeK4GS3:08nEk8bRV-C5iF'pn2'jlgB$_QX7i+>O]A2F]A^@isF$kHp.oU1&Et[)O/AIZ)6ihn
<g1Cbk%bccnt>,J'8CdC(7P7M,XUCG-;]AYBm"oF3[K-B%RH*3Zk<Ou<VrHCMstMVbAM3?;ia
l^<jSm3Nj8dA.Qm?_LY?0#qT)D63DeSPQ,i3;6T;oK=$k>&1!7s-86XW!FglMbUu[CprK<_O
iN\=f=S^(Y>GB#a-s@6Pg_ce*AHWgD.h)c9b=eobgV,XdIjQ%mRAs'+8Pb8.<Y4oQj)&iC:`
$Oqhm>TO1IaY8c^5`($=g\bC:fs&QYIiGm%4=&E\H_.\V9q3MH6;YAWUf:'"-8bb&V6j>\bn
b!\24l+._Vc@2_S&M,Pd-)T6crAgRU')iCR8Im<C$G8*:a+6!-mo&^<IrH#LpSpTpX7keYM7
oWe53ZS`W5^SKt$3lE$;#:^XWOan0p6DT@,&bA*S"`a-aeW=9/n*JBDL>E-CBE7=T*hnUXK#
e:;I$=_nhT`4e\SPPs#.)eO=c=J*Zd.TgD!'N\cjsn<^bU4qtj6"#/5bpoA4@V:2"<4mp/'5
/5c#e#C`)<o?d/?39.Q[ggUrl$0T@f,RVC:R4&_VK>M,Wr`+FeF`^"u0jG<Z+oP*B?pG2E[$
:B$Ta591I5(LG7`!8&%C`l+0'E\9V#jWLF)fZqV%JlV@?)79S$J%9U`akSbIMELqOt>SX&)&
l&Td;3<s1C>V=k>6EB>pM#Y!-.OE8W\=Y2'2-LRTtcb>.Ul+V5@\p]AtS4LUKl2HocdQT(L'd
HGuS.b"mH;\r\6s%?(^>,>;>bE"e<^kh3oq9e0(@[V>R\(K5NNo+n%d3U4L:HH]A`-;BfiWjm
8ZF6L?7k><GLB;]AgoSu:_V7V+pY,.@s8D[jD<H2#*B6:,^`RTJ9)]AJJ26?rpMB>mhFE,_5"Z
=bDOMGPtah<#gd^;'eWu6/cauVp1<(]AVSBRSL1^I^]AGoKQm3gJ-b4"Zo8^?-q`1.uH$"LH0"
3.%4WT<i4'cjYAHqO7%Ubl[<]A$M%LOZC=@W2]A>f,CP#\S!"sk-Y)OqV`2T=It9Ie0JlTQWF0
L@J#_m1Y13LY(3CNN-0]A/iOT926X?\6ZF*g]AfWXkT_K<"[lhRggibm3:llYn-k4=4+f.VrSo
c-sDB7A!KV2rmOS+1WfII&q[>qjR@MA*D>C)$f>>nFm4aD/'U1!f/A8s'oO_$)l$[X*PK*rp
3S;V"!?5;>&3>AOY^]ANkQMs#Dc9R4h7M+3_9^;PU9Oq_?iQdTd$]Af$uL=URrpP0q:Zg$_N$:
,C,?a#jGD03!4s%K&?ZgMtk,>$Vsuk0,=qTOt28^YJJ>O8,h8/<>F!o-H*s>pp&K#o?E'.pS
K_+lJg$?W^3YTnBIrVPh07_:LtH_B"c>X+9H,[#<Q)1_U`jW$biOO3WUXJo3iE:G#rj,aKZY
B9`]ARTUBf:C_NTPrQ-;om_I';cm:GSrlJ:CO?3XPYTDG!#mj<=QUW_<F[%aEn*GV&S=7a7?`
oKMZfcfk?:`V'ULeeiu+#h19E)OQ^'IFcZCt=M%$q['p2Q7q9eur.<OuUH7&OrSj<FBm1N2T
[EQX+>V0j@=A-GSX+=Yj"8Jlh85k%gGJ'$I8G7V0$']AM?,`-WVf,*QN&B>pUph57`Abo%D>7
II0(fKmZc-,8ddcA&a,J1Qj6"Hb'oc.`i.@:pRYI713<'qfUp5I\@L2;M=1=6#fe"j?H7`6u
k5iRY-@mU$8ns%)OctKAi:-/"BN0?P_udK"=Kt;j*Vc[Y<^WDAk+;Y/9)GS*.1$oBYbYh[bs
a4kNh`m&p;D]A,l5O:8Umg:Zhf!XKSPR!^:;e3Ou`J?iSL>_4r?ur:/:U8iF'D2.+jZLlU!aC
lU>8m&8Okj>.h@o3*X8=i0O@TBKd.>2:#D9Ho.uiD66:p.K^j[d7:NU#d"7%"HJ[s/MGWZs`
*"%/FFB\J*A5\&h_WWbArDG:qX=(#De4&&D,%TB1j(I(O0BXWSp!4]Ai<=.b%^Og7\mV5*Mkb
F.nXfcDoCIo&6:Z!CQqMrR[<ng+8iA$cYZjc7uFU"+).SI>1ZP",dCHL"=K!\:j?4+pOf-9I
32NPRONZZC#,97)CK^6-NlSKDeF5LK>-k[[,Mp%H8=POoemI,4T*6"2r(sl>N6g:H@]AiLB#k
[s6Ej<OM6=M_e#CqN8`#7=/'&j4tf,K/_<8u1rU5-eBjBsP_#HQo/o5OI"oCN\.0LGgu]A/[@
i#\Z\R<P3p/52i\%$[-H-OO-G//p#Q1)la/N-\AB)I-s"Bt/JfY+nr#a_lQE:1]An=8U!8$+?
H7I!EHsNB2lCFp,N^>7l=5A7GXQFD&;QNC-YEEdL[=CRXC35U?Vj+u]ADtRk+)[^Rstm>!m`8
WLoY@(NXEm:>K&<W=.,!cE?;PE+iQb)cmb3HNbU3s7T"$b9HdkV\2]Ao>^(_#.Q%dS*dJ:gB=
gUW2@-h.Oa+YtktPd,%m?0`]A]ALrAg62pDn:nQK>SV\0(7tseB9PfRi3s?kdVmr&(Vk1l),o.
G9of6Sc%\I9R,%kSF.f0-'9"DkIP4K>a=_^?\BO/kW7RIfiFE*8(qdsIHA2)>M+`/B`1G,f2
poNqg^mHnrg`eu:Ye@QT0cg&Fm"a,r!b_NIl]AR1;SDr<bh,AbdnB_C)G_09oD.u2HsLrJ>Ed
d@nRKe-r/WoH5H[S+=_r.i\938g:Z/Z&Ci^_7/Ju<BIQN!BDCTbn`p$RYWF:!7H*b%9fReZL
-#j6MA+U"WlQ!sH3r[uSB7BhTJ=[D!rE+?Zpo+IRs'C]A'5P9O*i:hQIr)@b33X`gSL^Rt5Ba
JaHGrs]AZd&Q:Pk#FCB@OFO:4$ei-[-oBDW8C#=9F6"7B!qIMHUo5X/.`rnEqV#)@fS<qE[sg
@\/J@d91IcVaFaC15RU[%1UE__hG14_0,(o!Hs%['2dKlJ<o4j(6GoCH3YpY`RA`rI?g[oLP
<CZ<+'ZR/<]A@Ni1A(V'T$F5h%79V8^[f`QGj0Fr]AdMeYgN<s.btYC'ZhdXuaoaYO3qkLNEZq
m)pE*0&J,Dot-Y?-'Pf7F60NAUU50UTm/1HFA_%hiX[@fI/a[Eh9LuMRE>6Jbqr\gs2-r@Oj
_h-AUA#M<JYdSr0.g"REM/rS+?N)gplo*iV;`W1!?NUT"R]Ah?aRCi1e/,M*jN4ii83YSnb\k
V)`nt+(kn0c+O1[e(gH0gXH6+]AMBL2\>:Ae)c0dia]Ad40/SJ_oNfRheGH\#*6+#KDJ@`&(J9
28)U^kVgKKip<oGde9<4.hjiR'L+i5qpIYK`7i1&;A7@a]A@1%q-!VKpVUTr[db[dar@5[mb=
L!t!gTQ5E%K8a)$7g0WVti=P%HDp#P]A*@)^4s7N9`e/Q7+>[h$I%)JneIlIM1.Z$G)C&E6Ka
FNX4ZURGMbt^#D",6,us.:C>F?NGOeS"jrVK[e;S]A<r's0,e3dgIHbCUOP<G9EDl^JA!U-[^
lYT]AF@)ad"-`*qkA,h)G(icA-A_Y2=di\(j[JKDQ0<=p-.qYZ-&0[*=^(EJZj=VM8&\_HSHZ
S(k&p?e47al_l$B7K;[I$NhcMf\%<5'(,\Dt>i%fN#e-:"S0L!O8^hT&qid_-H(PLcLt/U$t
/S<)I2_RR=7T\"':a'6Pb?Y0Ln6bhN?SbYaBE3d?"pn!\Q8XR6^mLBr5s&/Ug+8tOVTjaIij
f$HLqS=m#pqCIR1Uo:RFF!pp`l@&Um=*lHDjgY!me#C&s86Qqrrr~
]]></IM>
<ElementCaseMobileAttrProvider horizontal="1" vertical="0" zoom="true" refresh="false" isUseHTML="false" isMobileCanvasSize="false" appearRefresh="false" allowFullScreen="false"/>
</InnerWidget>
<BoundsAttr x="685" y="0" width="275" height="224"/>
</Widget>
<body class="com.fr.form.ui.ElementCaseEditor">
<WidgetName name="report3"/>
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
<BoundsAttr x="685" y="316" width="275" height="224"/>
</Widget>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.ui.container.WTitleLayout">
<WidgetName name="report2"/>
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
<WidgetName name="report2"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<Margin top="0" left="0" bottom="0" right="0"/>
<Border>
<border style="0" color="-14669005" borderRadius="0" type="0" borderStyle="0"/>
<WidgetTitle>
<O>
<![CDATA[新建标题]]></O>
<FRFont name="宋体" style="0" size="72"/>
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
<![CDATA[1714500,2503860,1939264,723900,723900,723900,723900,723900,723900,723900,723900]]></RowHeight>
<ColumnWidth defaultValue="2743200">
<![CDATA[6480000,3810000,515500,6480000,4320000,571500,515500,6480000,4320000,2743200,2743200]]></ColumnWidth>
<CellElementList>
<C c="0" r="0" cs="9" s="0">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[='  '+'現金紅包投入與發放情況分析']]></Attributes>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="0" r="1" rs="2" s="1">
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
<![CDATA[85%]]></O>
<TextAttr>
<Attr alignText="0">
<FRFont name="Al Bayan" style="0" size="96" foreground="-10502420"/>
</Attr>
</TextAttr>
<TitleVisible value="true" position="0"/>
</Title>
<Attr4VanChart useHtml="false" floating="true" x="35.0" y="40.0" limitSize="false" maxHeight="15.0"/>
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
<Attr class="com.fr.chart.base.AttrBorder">
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-1"/>
</AttrBorder>
</Attr>
<Attr class="com.fr.plugin.chart.base.AttrTooltip">
<AttrTooltip>
<Attr enable="true" duration="4" followMouse="false" showMutiSeries="false" isCustom="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="Al Bayan" style="0" size="72"/>
</Attr>
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
<Attr position="4" visible="false"/>
<FRFont name="Al Bayan" style="0" size="88" foreground="-10066330"/>
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
<OColor colvalue="-10502420"/>
<OColor colvalue="-16118480"/>
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
<PieAttr4VanChart roseType="normal" startAngle="0.0" endAngle="360.0" innerRadius="80.0" supportRotation="false"/>
<VanChartRadius radiusType="auto" radius="100"/>
</Plot>
<ChartDefinition>
<OneValueCDDefinition seriesName="欄" valueName="值" function="com.fr.data.util.function.NoneFunction">
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<TableData class="com.fr.data.impl.NameTableData">
<Name>
<![CDATA[Embedded3]]></Name>
</TableData>
<CategoryName value="無"/>
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
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="1" r="1" s="2">
<O>
<![CDATA[&yen361,16]]></O>
<PrivilegeControl/>
<CellGUIAttr showAsHTML="true"/>
<CellPageAttr/>
<Expand/>
</C>
<C c="3" r="1" rs="2" s="1">
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
<![CDATA[44%]]></O>
<TextAttr>
<Attr alignText="0">
<FRFont name="Al Bayan" style="0" size="96" foreground="-149760"/>
</Attr>
</TextAttr>
<TitleVisible value="true" position="0"/>
</Title>
<Attr4VanChart useHtml="false" floating="true" x="35.0" y="40.0" limitSize="false" maxHeight="15.0"/>
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
<Attr class="com.fr.chart.base.AttrBorder">
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-1"/>
</AttrBorder>
</Attr>
<Attr class="com.fr.plugin.chart.base.AttrTooltip">
<AttrTooltip>
<Attr enable="true" duration="4" followMouse="false" showMutiSeries="false" isCustom="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="Al Bayan" style="0" size="72"/>
</Attr>
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
<Attr position="4" visible="false"/>
<FRFont name="Al Bayan" style="0" size="88" foreground="-10066330"/>
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
<OColor colvalue="-149760"/>
<OColor colvalue="-16118480"/>
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
<PieAttr4VanChart roseType="normal" startAngle="0.0" endAngle="360.0" innerRadius="80.0" supportRotation="false"/>
<VanChartRadius radiusType="auto" radius="100"/>
</Plot>
<ChartDefinition>
<OneValueCDDefinition seriesName="欄" valueName="值" function="com.fr.data.util.function.NoneFunction">
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<TableData class="com.fr.data.impl.NameTableData">
<Name>
<![CDATA[Embedded4]]></Name>
</TableData>
<CategoryName value="無"/>
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
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="4" r="1" cs="2" s="2">
<O>
<![CDATA[&yen29，172]]></O>
<PrivilegeControl/>
<CellGUIAttr showAsHTML="true"/>
<CellPageAttr/>
<Expand/>
</C>
<C c="7" r="1" rs="2" s="1">
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
<![CDATA[65%]]></O>
<TextAttr>
<Attr alignText="0">
<FRFont name="Al Bayan" style="0" size="96" foreground="-1441703"/>
</Attr>
</TextAttr>
<TitleVisible value="true" position="0"/>
</Title>
<Attr4VanChart useHtml="false" floating="true" x="35.0" y="40.0" limitSize="false" maxHeight="15.0"/>
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
<Attr class="com.fr.chart.base.AttrBorder">
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-1"/>
</AttrBorder>
</Attr>
<Attr class="com.fr.plugin.chart.base.AttrTooltip">
<AttrTooltip>
<Attr enable="true" duration="4" followMouse="false" showMutiSeries="false" isCustom="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="Al Bayan" style="0" size="72"/>
</Attr>
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
<Attr position="4" visible="false"/>
<FRFont name="Al Bayan" style="0" size="88" foreground="-10066330"/>
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
<OColor colvalue="-1441703"/>
<OColor colvalue="-16118480"/>
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
<PieAttr4VanChart roseType="normal" startAngle="0.0" endAngle="360.0" innerRadius="80.0" supportRotation="false"/>
<VanChartRadius radiusType="auto" radius="100"/>
</Plot>
<ChartDefinition>
<OneValueCDDefinition seriesName="欄" valueName="值" function="com.fr.data.util.function.NoneFunction">
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<TableData class="com.fr.data.impl.NameTableData">
<Name>
<![CDATA[Embedded5]]></Name>
</TableData>
<CategoryName value="無"/>
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
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="8" r="1" s="2">
<O>
<![CDATA[&yen4，999]]></O>
<PrivilegeControl/>
<CellGUIAttr showAsHTML="true"/>
<CellPageAttr/>
<Expand/>
</C>
<C c="1" r="2" s="3">
<O>
<![CDATA[已發放紅包]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="4" r="2" cs="2" s="3">
<O>
<![CDATA[已發放紅包]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="8" r="2" s="3">
<O>
<![CDATA[已發放紅包]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="0" r="3">
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
<FRFont name="SimSun" style="0" size="144" foreground="-1"/>
<Background name="NullBackground"/>
<Border/>
</Style>
<Style imageLayout="1">
<FRFont name="SimSun" style="0" size="72"/>
<Background name="ColorBackground" color="-14736834"/>
<Border/>
</Style>
<Style horizontal_alignment="0" vertical_alignment="3" imageLayout="1">
<FRFont name="Verdana" style="0" size="112" foreground="-2297870"/>
<Background name="ColorBackground" color="-14736834"/>
<Border/>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="SimSun" style="0" size="72" foreground="-983553"/>
<Background name="ColorBackground" color="-14736834"/>
<Border/>
</Style>
</StyleList>
<heightRestrict heightrestrict="false"/>
<heightPercent heightpercent="0.75"/>
<IM>
<![CDATA[m(@OE'3uD-.Z0lC@Kl!G+t1m892e\b&L,Z!$OB9VOW#>J!\-N9H4<;.>!`[ONhAoL8.@`3cq
,?F#U.;!^?Y%YSTF5ple^ebpUU*81:(W\[9*C1R6>I0BrSE[iB"8_h`fWgpMN4P\*nkA^4#m
(%PcAWI.B@VfXK1iE<#W+?16k9']AsYRIUkT_dGn"@r1R_s)mG8/m*Q]A+"tdg?>(qkM4']AJtQ
0Y+*;;&"BceZ/'ea2-]A8aXa/ZW?5oju&8lA1IgYoAe]Au[ZN5N`;p2nd+:SD7%\I2)m'7(c2n
7S1B`<q+[!emVlQNj><^l\^3mDnROfL502o#m<8f4oFk9gdeuc')Nu)+'[`c'AHUQV+;6>fa
%#a;n<U9N!)"q/1,lWqGIQdtE@P\JMN*&QGg[F@(NDAIDH,&2mU6E/JES`I>;2IJ=]Ag8b#rA
a/M+9UATb_m/!oYD]A%#5\2mW2_)t-cYT'Dms5ZWN9+/EdSmGZCfJBIRE@&]AY,l-MG'0KZ12d
'nLcEZfMX9B/H5VL_t<SQpY`Q+@[:jOk47YuiKO$cmS4;b[."s4;g9iCM;p/7@3q"FNo-AME
?Tm,Sl)U-H@NWD)!c&/NRdp,ML!PC.9ji<-tCNmrJ#92#4Vgc,n1(RHeNl9;iRs+9H$d&R^l
-mec?aK>R^*D?nd!Y+U2otI3+@P%3(f8WCo;#LV5Xsp7#oIU3!.Ubp!nmo8L95M=7F&2;9MK
*to7gkLr_]AgcE<SU&JgIm1Hs),(oY?EB98J&eu7]AI+Wd?E'c6.YiUPd_fPGV*f#$Jmts8ebB
\OL?Qta+g]Ak"?bjVc[CWF>Il-l(3J'UV?NFu3?]ADS9@$$[\/5Hn*;mS/Ks?"=riJ+pD_AbUp
0R)KkP]ATEr!Yl7)Zil'r22=`S%:1J+?$15FshHIr[ZGQc)LgJ=`icMV`U&m@!pR>H`bL6T_O
auI6]Ad4GthY\S`R't!?Y[&@&I?scIV7</O5/#jTkKD]A9??GjD%l8=P%N^s)ri_R#T?jf$pA/
XR_qqTCdSH3JaA.h_JR-E,YCHNsY6$.k*glBQ\+dM.FNF@B_*6/2J]Ap=hhOjR-qc!T;9hEI7
rHpj0"s,1#<''As4Gj)N>Yj"ej&.]A$2]AVVga-E'DmH;;GJ`FKL?JGL0GNuMEe5N>lL0l,Ui+
q[Brm-t2S%hLC5K'Mm%gVQ@r."I*[0+!::5(e;loKW)mq6pQ<]A*Dr\Ep%)!52Qa0#Qrsg?Q\
i9[S.9f)bVZ2b![tkohYQ8gW?q9-1"#[$r"L4)FTuh"7Q=:p4m1m.'?'/3@Ycr&rt.)OPU<^
m90Iee34.h=q6M39<:\fP$%sDWX!+Y0'G_o#!cCi;'Sdrk9F6H7Y$$$X/]AUpT9p5KE&CF-X'
\ih9?/3B&,6i&-g6I6lPIJc?Tb<q$-/6^'iV>'>?tD]A9OD40R'iTW.*$43K?<VWV:m#X5egm
/b2ebF&/TPdEdBQESB%S'`lgCG"[4bd-gX>`O/oJFuYJA&s;-tAoW1P!$>ir?ot9##Jen55!
3l9+u8+\_o&fYI2`Pl"/McJkC9A%Ep(fP3aV]ApRk_j3NEnOkU$<oVC,5.Y$Ii8Mml7R=]AJcm
JZgdW+l/0,?(QUf;-k^fANtjX'Z6f'F?oPX`;n:roCCj3S-maA;:.KMqf]ARAqT6Pf<.ndi=p
it]A[W10[rE9\_Q<HM.^V;?#ilaMfrk3U"D3oM?t*#H0OK1\\!1f0/s6$9A98j%%GU'RpX:AH
3gpp^6&&1K&8Lofm!>_eK1L(nAtTpdW,IU\Vi<*^ZhAmSB9i,?M?g(`2qM1P"-r0D1m+^t\<
*#R9RLPU.dQVMP-W>HR7=tkaVOgUlc^D%sR[4F>RdgM%&QI@)bO#o[fH3l/cp4<sa4)eudN`
%^nRP"R7aO+G*BEBotmdb;6\SiNTeTp#um\(Dd?uphO%bla]Aa/;n-h!0apAL3%"g']ACQl:FN
=BMoh.@ij&lehV5$0Q*lH+?CYN4P[q$CWG47(e,jh<J:C6<F;G'$.(%Y*-t/c2k=`*2lu^]A`
MuLX>j*h\4T?=mr%6mWcF[k.ChFj)cp;M$Sr_;_?j=N*%h=tOl`s*YdE^%rCh*J^hL)%]AXdB
pnmdK&IJ6a3=a&A2:jBhXnMsT#7.asi>g?^(kU@JhA/(WF)+(i%gCOXck3BqRc.N^f7A#+M7
O4dda*Wo%W0UiS_[>iKkH?ehm(&<fYhfd9DbQg?*0O1#?RMDRD*M)1q@ct>g#c(1B(uS_D;N
(T(:P8l#5%am+Xc7&++O#`B\3UK2[KGGs&DsF'9-[1BO;#kYCS0njo#ulL8_rI']ABUicV$B]A
2<ifsqIHITY",779PaT*Le3`Cpr"3%TBuV6(WFBB<]AiNcNM&naUO"%k?e92#oP2=lS8B$>s,
<WTG-n^;<R8s=PG#(;ko#C4rVL*CV>I(buin^%i'kth<<PR?-3jkANX$#I6hHl=RF4Y2@N.a
jmqdhud<@c&IG/Z$lZPsFA3]AOt(Vhp7jjc*_Z(8'\*!4sg`X=1oN/Vu2Y,`i5AXSkYLGNQ;I
DOgK6#^;'r>kpAUKbm2JZGeIUPN^Dg&>_lXj@_PKEE.GS(5fTojK^FT<2j_\$K#b[T4jaZ?l
I/lUlmCgq*QlI_3jB)Mn]AE9gUSJmh<mF-%t,Grb7ku>=6:s#9iceR@jYqW/!@FVTf]A"YNK'"
H">ZI2_'ZX4kH\RO4)WtH:?=o_.JMt6CkioWM'[2m%]A5J^KVUBL@QER5Y5qICecXr"K=aC\-
=+%L$AbHGA>7K_&h^Z^oP\NWLi/n!-jWXIl0u!2Qt&,jR5#Y2c,MNZLN*DAo.,up<Lho-Ij_
-g4p4%m^Zbk'Z7c*]A+(o5BksN<,Ag->hFCSXLA08:H7M"2/\1=Eh:Hp(^E3@">3,P-t?,bL:
-`1Aug=4f#S[IO:lB.;4X[[.1=O\LRDZ`X,'1r$Go]AULPNbWgOU,qE_,LG#)PW>foNL%J\b-
rPB)]Arsp&Yig1"tqI@r+-jD:h$ga8PX(o2%s(Ehg&l*N)O%HdkP"t#.Lpu^2.04jdO[[s-CS
s+Z9Wbe'UoT_KU2#o.L"'KcS4"P;kCJa#8HGkl>tk`CN5>G^qd#[^=T)^PS.<cu%L^jrF,nQ
C^/pKpg7b*P3I5*?Xt4nNuC!#bQr4[O=:!aqk\(ZDU['k$&)=j!A^NX-`taqU<fo-k]A%=*.>
7An&Q@\[p$/W)p$.bOU/3k2,p2NAr7JPGU?T83;A?>_^_fUL/pH0rD6_Wls^jDXOKVSFaO'A
'TXLP<JPY=k/Ca*kfC*>Us`K)5sG+\*GM`Z2,t0fBqq8*9is<P^YLjY$Vqu>(d"BSjgHRf!B
jXQ+thJdIVU#'A;TK%%%SureEAp@ib8l)-rI@sX!WQR[@+kKf[2a2NZY6"Vpd-`pd;j]Agf\H
?(nut)I/m2PaP!A=jMRU[RSi98Z1TGh"80P"gR&=IX)AJ-.ZD'QC:b6+gq0Z16/.JQ?-RR"3
_oJ$_VO1S!PMMg=tY3De"Y8%\Ppn4M3:nGgBd7%L'F$%cC`%i3&cu6:cWCT,8Vf_a4-:Cbik
bupLrPIXg`T2s')3%ABDC-lks[C"i+Q$QPFm4'@>D05AiYifL<n:W%^Y+N,T9eV;=:9A)e%*
H5`=//LT4!;Jc4Djmm>4A>)*VGNsFq6$!0R&?[$gGZ`fi_.0.g#.4Pq<W&3qK>qmef(d+Xd@
i/6cO5l@A$k:08FV4)grfeDRFO6pFj6HfP0HFN5JB&^s"jIg%p8OORO*:>osf<!]A<r1I`-Jj
D>m0gGI+5]A]ARe"R>PVYjN:,nLN.ZFb+#1PPQ>[Mjp`%MTthO3==o^2E9Q>KH6US(:7^em8uj
r@r_o8VB[n-u<EN7mP/+,6US!4UZ1GRtX`Lm!tf.Ya30GX%R@Pfk.SaMq(MOm\-0JVY;@_`f
]AuDQa!Ja;tD\Ju2Vp2&)-rN.HE#KY0?>]AfRc%k;&>,S0$:Iih?rBk4`a"edqfl]AJVr1&j`<.
O%'2^L,)FH`Z'm6@!4,J5;Yg-P(A:GV>>RBK`*`EN'Cu.qMrP65#Hg=Eh@%G<+";e->Kj#/7
LuJALf%U5,#D:EFZlEFcpE;4o-XqKP"2h/iZB,!@9\uS(S5pEN;"b!g03W`GI)KSCCVZ]A:4F
a)(f<"1,DeI>jMf?VoB,-kib&)Z<mh2-Pu'f;0Anb`:2;UDMt1NC(^D'D:J7+"ZD4%3S7D`D
FhFB8CR@7qs'--\2,m737Y%J=X/Cc*;@gHb7P<=5-@sjWjKaX3Dd`'q:TaUq^]A(e07$A(*`Y
ue-HUhY-!o,a>&A1!03hXa+3k^97W(fIi5WX-8*eYDH<VFIYV_cb(mVlk%]A9l;*kL/UO*ih+
0sO8&MJjA.g%=I*jBtWgnO6r@PlK%;=*hR$+.pO-VnJMI1A,*BW!^_n.$p^)H`O^!1Egkr>i
PLi<IRb_^^jdg\=$<Y<u3CVlt""-SU3c),H#>?=0s"sZ6^5j^.:\RH5_`0$%jdJ]As5*`K@)%
sLlcdnDO%*MLM3W:qQuOifc>lOcTtR#mg<*1C*aR5QJ%1MY4(^B3X!$/Smf[\Y73EK_JN?50
Y1b\=P@As7j>Ucq0<mRakolNi5ppMrcA>>=[3&OE\uJ15L!\n*IFsSN(]A9jeRTuc,!*SDI5J
lI\9U&@:ji6@6tep0#'@J:$!Zu:Vt`A,2*39i+;e]A#@AB/-1S7Tjr7b?r\?dM;6:Z/N2r-3m
k@7NI<&`/gGk(8R)(:jfXS(7j3?M<&pIm>^i,D^]AQXbm6`ea4*R`W>bk/L(r&/#YY-gIA)AW
EVMA8ubWq0XA%`E6N[FsDH2Pt(K4.$E*%Eu(-FYbH(cm8(\DL-6Sk8*K1F4%RJ6IuSBl]AYl.
V@7P)$pgBD"G<NC`Ib,IGR2aL+8d1I6KUY\7lq\@2;(A.!@;L9O=U"+4Du7t4%7;FdOXJ1!$
@L/?;)>46a"F63!=_Pu&3efLgrCLf'!MVooVsce)/NBS5np,6B4h`X<lV)3,XWDRB&Ve-a\N
UgEJAY-Ja9>YCj_BY3sJo!M*)!;8Q<:&Y0b/D\">>:q2R&;&X678b(aEUA2_N`E3j%qa`Y&F
9s%ocbu)fpJNVNtC4e6P;?ZU.r]A%b*n66Do-Rdh%]AM]A0ib>d2(QL_sj$:R+C)L5K!TsG*P"^
L[SLrY$ikOP2W)Q*,t<k8#AN0<?:CQK8JK?^_0GHMMik&?ba^PD^Y\$"&!nO%sZ>'$Ip$dG5
/)-lSt/.i\ZGW/[G*UL0SfWA?\S]A#t[3W@6u-.SQ$"5/mIb_-pNC;&e^Eo#o7BAC.s6RH.0'
>#<NSoKrg*FW8,3j.A^'<=mEU7<S'a5[($Wd.TISmL_$+04mbK4-VS7j$>,_;HX3A5ClR(B@
K3WQt._JEH5q>A[*f*I[b'&^P)m)QuP)U>=RqU#nQ(E&Y1P[hP:TMhs6R'6e_BeDFtOkPJ=D
q^X=rM/.#+;]A.)!)/qn;c?[--81)s665E]AjL`@bndja)`Nnk,eb'&&>I]A%DU5pE(eU?i_!h[
NT2#Bi&kSIAP3b-tjC>3Dr7!LeX"B)TPu3tTdn:L=$P8AjWJX7I-&mp3<TjB"=__/pG1.7Q^
q!n;]A@p,jI(6ZVVh4E>Ha6.pY9noD\d_%j/TO<UNCbH(I.SE!X4>)r>P</`pEm"o$Y)H0lt4
?^qkK7EjDM#eY>BP>-o\u@(E'WSZ-Q+)@[fXqfm-_$]A]AFC'BD;kQL6k[`uT?.#k=#(?34^KA
qnMnuYO!tCiO:E$7.o!)rldpA`ghh95_l'c9'+-jIW(?</C&#sDs.-B:Y5>\j:"@@n)keg(l
<!,L.?Ioc[BHQ6Cr:X>"`fY83XBHMSf6BPnDp3fD._LIHr7.=#(tfAMRT+%:`=MX)PJ4F1@Y
"1c*Pt_@@-,Iqq/i\t)[?HE2AnSUiBeEqIe.bc:nnc/31G6:iT.-o-RpR<8cd(Ef?Y729C5S
JH48Ge%dPb1c^bl;RqY$KW.!-7FqLLQ3.-I\N8aBP8>[<"cXpFIT(r/u!P`W'_Ko0rCXkFF_
2"N,:b:<TfQ=+GV+@OPG(k3Q`G`4\dA\W""]AcWl8pa>bQ)^#1Y@mYEH8kV%M7C\Jd\iQMq$q
#M(Q>no>@\)?VdN:\SPQo=WONmY/P!a1:'2[lqq8[%idpJT3AN:pMRii1)7*![<En\KQ9JYs
UeQur+Z_"F-Xn8h29n#W<0b=k?@HLpZPKN4\SaX'Wei6mI4;dg"aS0!``D]AWqs@ui-%p,l#u
=B:lV*:TaflO/i\/9i@U,qHDDL.]A@bUgl7Q2dWWgF*jPl)3sMg>_P4+,Sl.Vh&3_^nK;jmt!
EHcXA\?<rgCenXNGJR2!li>5[T/UJQb2Kk4S#:!kiG8_:G92mVkKCNTThQD&#14f*oapNm*9
UV/ni;.D5g6FKYs)gkQ(UOMg$TO0]A[X=tH\t0!T*Q!a!j,n;*BD4q!34>)!n.<jR8_Aj/jZb
ukGqc&6(1oMk[qmG_)s!mFT)6s:@epg^DLdMb<gdPKXi%gB=fHp-/mp9VhHZh=9Jqc%=9t[u
?0QV,Z3Z@rQ@\>fO'f?TOC@\tYKXK1@E1m$W20E266Ia5<Rh0t$9^=Vh)E?tei@1@XBd?6b[
1,gPn/B(3O>"\`/LNXlMHmp0(42M3'mr['W`H,.1fM(^Qbfkp)GNRLlii5Q/rS.EpSN0F)ST
j5C:*UdgbTNlDh>>mZ>b#XOFFKEA[87<_I9%_<'>AOX&jXAa?-><pp2C:*'R>fRDG1N,4bjO
b(.U0g=3EGTD66`O:eL37DDNC,&%#/7;CtAg%Y@^8A4/`M%>_?j^]Ad3onOgQI.L/bYH2:p^C
+c[ogKGgUYb9LP654Q-6\<+G@/4]AMgE&,\]Aa.kM-t@e>h0HQIP99li?!N2&j]AfH=4D+.7\q2
PZTfHHEub&"67akVA;d\g;e4Z!%*93-ZN]AEqC@9eHK4G%O;oLD/&c:;oUKe625P4L8DSe.:0
RT'\B_8i9a;X)BqStHjPJb3E?AKS?<bKEqn/b\Mb9\_:%bo(M+(9pigd+-=YPdQ'acdDG\(3
+HmWlT:>"ng&NXH<p:.d/7ZW'o<h9V&R&0I;qhatd;i&d&3aT&iOjCK6^9UVT<>X;WBhL0H@
']A`ThT::`Cm1;*E$7b5Ojq.Ff2f*-#?9#e1c)WY.UR[@cpk9W"iAs9=)R/,<kjY4`o"W0if(
@h#]A"j8kkSD*J]AZK_nhZN%P3^+B\ua2]ANOa]AG78?;@bB/gMHQW2*@.(K/.m=ZEF"V(9f^^pT
CD]A1/gZG>!]A5gHIjC@o3g8B$_a>nA_G!#as-uSIM6UX[9(g6m51T[>"T%cYNdWaC6ETD=0<c
8%aE/7Kh+1-/)0#U=WTUa5*\%[al;[#SW[4NXteV&UR5a^Z[HaHDXE0<*eCRQX4#03,-lY?a
K@T\+J1"F'"S1K&EX]A2n;s(WF5fZ#ats1gUMeMc9#XJB1ui'3mf/6'_G0&TIP;L,I?4MR5ss
44FR)msZDRgflCB;^4g**Qt.,>Zaj3E:VJ+]AXj.C1"?_#I6?W.iVQT$Na?IA$\hn9mZquD%W
]A\Lp?KBFsof#aVnF_M#m@jWMG"4aKLHh/rtP*%"3F5D\ACg"H;,:JkK?0*"qM`$?RY(a<sZn
Z_]AAM?Th/6RB'/Hcu'sB3+`[900.Lb?N*YJ=jlo]A'EGp,;@Y"_foD?'iDR+<a6cKCjS:>*[W
E:8;`.r4dp'm"\jAFLX'9VhZDTTs`cBh8[\Q)=b^iIK[\>BshgMh\]AE_V0(W,'9cEWX!fY:W
Qq<g-CY3qHJ1;m;XT-dL]A;;m?([8YjIp-it)L&;kTj9]ADJebA^TGdn(PQD3L(V?\1BX'E,:V
\*83<W=G:LHmcS17GtW<9!Br-_YoceebmOZY(Y\QnG@O!XD[=YObi6hK#XSFmn@tTmdT\C!A
HtLk8R>.H-ahZ$AnAPC=Nqo$4j;JX\'k`.JWR+Z!;+J%Z8[.O>0Wh3`nEV'GtcPGe8NI'X,u
`"ZEg%7k4g2mm*JoP5Fh7pc76]A@eZarCJkB4%6FHRPFmlL(mi&k[gO&9E6[Kh/5$ZZDENTWJ
7j7PpdH`J4F%'ko-eWV7"&9]A#B2SM!OjA#KAIu`q+%'YZIJ'GMe1iD<%3qj5accPQP<9d;RO
u#cS:rU<Jq!lF3&?6VFG'`bN!tb!]Ah4c1rq1WSk8WN6J=Q\(Y,>DHpSj6HiH@G'8!RDXu-Mf
-jWY7ZW(Rl="X!6=W[K2BRb/s.+Q;C&U_A/nt^ejN.VIER3!8@S/,iTNiKJ:ZKE!OE=uO0Jr
dHU%M1ki<mFhRr%N#YEgH]AEr>TURMg[p^1@2fQ@c2."ONd$_'T#_Nkl<m[A]AuCZHNZn;ngFE
Fh:jXp(;Nn5>C,4a/(gH@[JP\3!7kt,<)X98U[p/W)rH:?=678=l.U+5m.YKgYGLj6>!)U1,
.tkB'40Q5OBjoAal*NI:CgmA[AU#3:5C#96/rg93`4fVaT=A',K(BSROfBnoZQgkE;=aU'e4
uU]A\UCDu!F<$Ie6Ujq#rYDF/%:h+@q_jdknqja+00r[DN`W?'N%-tM73MoS-ZV:?9[:=lK-U
jCiGDp_0rH]A3H+>T"3Q=uu,r#5:4"l'O:6(p*?!acMd(iAq!FUr\Mo1\dAOIYEjrZ!#m>]AYa
%"FA%SCcgk443GW2rmN9sk2U=Kg_YklL/F4V*-E8OH4%p(PB&5`@Z`,8MDp-RWUroMZco\t[
mHZVOeF(bu1%Z4g8&7(aK#$.5_#)ZZU,F';>+DOK[Ia*uINBReB*>8OZ\#-;e31fkal.3<9[
=ujV3UQ"JDs#Zm@gfS]AWk+C84\Fi4_rV6id*2kOMAu/J-?MCKr.]A+F(8,Qn]A5j2L*W]A>@SI]A
Cc5lQ@amq+6aK"qN;I8taDJF)eUbb?k!O,p"YZ1o&Z1#Yn2i:@Ya54VJoA]Ao&,18RH`74%EI
`X"XRd'/j0,8-NO@0Lj25293]AJ99b3==E-0qhRF:hg4(*584GP0IUhk0'@Z)$/6rD;QrWUBI
``?jA2FWQNj1YAlSli/8K)kq;8"&nM;\:[)(N@OUEQ[1#jg]Af"BY@?;a)h68DR@#J#/^E)mc
WNl5Ad5-N&5B)RiSS)<Wg3(>&EH\m`TOJ]A$(CGl(OV\eH<2[M*"uV4Dfd4c^8?EJr,`MPBAM
cccLjUF3j,4rJJZ<5Xo(<o+q+*TH;PjO*/pUXehlo+HRRW?`%n:PhH_)n4Kr$*'/W!bU^,cC
C7*@"o8VS(^V.5@_7_?/&JDQ)tbF7rSDWC[)[AA&GRJCI!9nh8Gc*Q;?ju&]AMgf"<RrH_bfg
C\trZ`h!l%EoqP0TDaaK*I^3+[YC<h8j[3s(Q$an`b'qjc(Ei,U,\ug?n^YgG\;PW3FE,3V2
XBegO8FJH;E^b6"'-D!n6nH#^g"N]A?ei?opVDD2^4O^$P0-(q'A;&m3e>!I[bUL?'&tdqp6e
Zd!JQL<^nkS"e7Amh0U)P,*_LhsU850]A4`2m;2ktR):i+]A_t5iOkk4!hib_-AG8&=ccMCEe^
V6#(%E2j%k,3'RoT7i]A,3MS;-#t^2^"82+poHC1T%m*217KrPu"2V)?q6D?oGd,Uj<KE7/3/
-KbJ.D"XDE$X[1S,@nK7JfH:cm4O9-Jo31NATq&+T33]AAPIAqJA!(j/G'-CF[<7Qiqs!J.)C
dH[DXY_2)C7:N"C(J_X+0MPSWomK'6SZCo24cg2N2h%g'STor0l6]A)(TUi4fQtHCI%kp[e&h
,j*OXJElH*V-m%klJQ#H3'eM0XqUW$A"lYYNq3[W)Iq0I,/>$-60N't:FM[@MC/pSJi3E^_"
+MG'u`BHi*<JPAA<`I_.jc1B09fW3O;htX81"VX2lO]AWuk,MIIf\a7<5A?DhWG4C_ksuF2E,
gu?E%Z5m@27p=Hkub$3mE5T_2"t*[/&d%q#,1l'O,PEErLjn)To(Q83LWD$dcY`KLEkM]A(Tp
Rq3I=Q)!JA`1sdfo]Ap(=g^<TY`gO_tkIHh&e9Ai4;a$[@]A9LK8'#+rMoP>-hG.r*LLBX(9Pj
#JEmL\;&q2+FCa0Z7YJ4%C;`<MLFMQp11KK$C)T.-^8RC6"t/o@`PM3[o.g%dsC<N?.h#.GI
qel)FA%Z*VPSd(Upnm\eL"Sj$M8$"P,f]Ao\W?rFSemDC"21Se,-ARH:b[EiBWq;T5*ngQ?/S
+Uc7s^;!c*]A?[Z41ksmn;,!5;0AR"NXl(eIk_&-(CThJ%F#\TCB[gN7N]AXVln)dW6pNNQ1Wo
OYL]AWkScb6gaA$7P-R%.=tO#IG@mCHp2tENbEnk:D'OVo'#X,7n^sD6ikC2nU0(Z;cu'dkYE
+S(S[AX6u_B.U<oH&n-]Ad0-:dmA3ptces]AalHnc1aQA74?p7&0*.>Td:g7<`M[hnT8f-tdq2
OVCal^gfUK%&dqH[LbQL[$p90jTTTWCfjfnZn':<]AFC.R=E$DSh'W\8>I6QWEf"qa%D1mGQ'
WS'9sqk.ERL+kLl-#UL$p=f+'sF?04M4kN8iM,g9u)5sNh5=4#9``PIW"CHp:!:&^8foH[L[
U>N:@]AFK?]A50mWlWGDTFCF(\DHq'Vk/8<dYqC2<LW,uK^(U_OX3=;MGQ"iVk5Fp?Kqg.t=\h
UTSc?dkV>#KH/l$[9n4mu0ADQ+-3mMp*4FY3`$U)Zd<aR1K(.+Y7Bje3RJ#KQqUC_II+j4bp
%j'^-\dA3E=.>Ip&-3'%4A0?Z@@ATf,+V@/rOS7]A>QW)E?,AaB6#]A]A7X4K'(=ClXH3/D/@jR
lhi@Qm_*iE]AZV0nbY`N6n^><aYmue5FJ*iOWP,dHIViQ^q):I8Fp%Pf?Dh#mVHrbKS>?A;FH
i^$,I(EZ4>Eud-<[Ji\`?]Ah#OII4Sh]AE^T%eTHM(_9ASYF7<Z?:<9['?shD]An&4=Y;uI<-Z?
&++&sck'LeI9#OKDcaL3Z$#d4W98PLVbPLqgBjA]A^]ACo;!A"FQX\QIGr5e,K1,k1@HquBXO_
j]Ar&*#B,CbU1`)BqU2/[9)ePu'^aD>Nsfj;\832:jE:nlbH)XG;9'0cZ+(CEEJ.KKr;k^Bj7
&1Y)g3PUc$d?D#tRM`47ZHm";Tpja6c7O4S6F_db'2p+nB.tA--WTd2l@'^AsNkDuDWm#$eb
rkh0@H;tqpl!C]Ail5nf!pJTDs4QQKc*?'2J;9uTFObioJq""EfgjMr(VTB,'Fo[eCjsBA%7<
10M^_QZjGs%pCcg<7S.rFiY;3WRiHB`:HiVT+.O>=Y??Ku'?ODV[=u#T(G5h2-X:`?.>W]AM)
Zo_*qrUEeGSIHEjG&*HB0pH!t6lmJtQp4$3ENbE<E3hOnIVIZp7<*/h4HJ+RYee8u?=(Hr=:
fWIlXT,C\]AG/>qfQ-3=0&N#FUfur_Hj<+h:A3UcBS(mU%#AK/$!>@YX%X((H1=$.[5g,'Ynr
7,=M]AP]A53[KPs/KCDL>-!?SS`hSAWGi1cN)BD3O.-33+tV<F<#@-=T6(mC&IdgP]AA/7&X)E4
4[VSOqTKQi.PRbYO$_=NZU&hc!TTU5pfbg-Nk[h+*2>\0dHUUSWAN+%3Lf#20sJ&We+JWQp!
8dAup9#Lampe]Al_n2;)e+_g'ZelU.3rF?TA,H2p^5O!O'M)js?HSZS/ib-2$+dG'+4=?Z_$m
:_(@eZ?f0H$DBsnVlj/"q!_:-?lYS',#BJdd%Vf.(4Bs>lY'9_4GaSS/h#PJX:[2pDfWWNX0
"Hi$!=o(B;!muiN?kfGn"Rl^4+fAKqW69-08dGMn9C!Q0rIaFO`nPB"OD%_07)9WpE10gZj/
t`sGXQgWlJDK)'"r.a6/'qbqc\@q,)"IK]A:^EjPs/If,VW.F_:i#X>Y1eFn*,*VsL#:k$0GE
`P[,l_eVTGYc54efL6i=>j2?1G=C?Kg/6dGmI/I\,NIgafrIS5BrAYYqO8IFQ%K;Ys$OgFL0
PZ6%"sG]AK4'&j?+3Ha:5@80cJD`_C=rsjKsKFliH[^(KAbp.1S9!"Q>1CT#Z\p&$I()Vd/]A'
^j36+>qOUFjij.TRFbWC$dk.T_MX%DgB,kLiqrmr#+*UfG28Co$SOG"_rOc-Q9T*sh=iHbCf
o6h0OdTa[]A(>Bq3!Z0:m$&e9r[@Iqc7RPbEXbNoq>2pUT9";>lA,QM+B?%c&0fDi2*8'!oU'
!Ps"YQFD\47Nj_`35(]A,N1dHQAT7>'*1P&aXlr8e=go5'AO#X"Z)BTlQp9/MX2(YTs$2mgbY
'MbH>'O`j5DA_j'[;ZoeRuDq*?>a3RjT@Y#E+I',a9.@#DqjIX8!L0;jY-,_>9qP8@PfUfSr
g#Z.KTG)@foP!-[N>iJEh82:<&l]A9d.3G[XB$X3epolRI+dnrH*A?aY:o/pDW5;S@L&IaMZI
JQHJa`ciH5Q/MYGO;R#nj:L$QGp'KpccKf?Sb^uf-U!(FgZR@Mb/c;aI4"T\7/L8;LuV(5f-
*g[6[^FAWS6AV$C9IgDBUl%rF1]ABXY]AjaVf1'o%U^9eBr75,26\r?.N;:7S*1irB^K)Zr@ek
(:#eiE8jSn4($[cp..]A20<qqf,`G6X=p`bX*<Rl):ajZ;#'@YDKGCG:0@-2\.m)HK(/:s1G1
OF/AWD$7EKq"+4mP.@n\=_H9!8n53,<V)[Sa[q"W$4[HMEJ-H)ga7dN/"JF?.*U-!PYf0^Vu
ssT'5ZfpG5bB0[Df0CPZ-+jqrXIOcQebK(WPXpF<L1W5.3^*)hhOcLA1BlqERkcd@8<3mnR5
RGE*E"9l^J`b+(ur8%5Y5O;Z"IrA>9[dOW=8:+aOmH1O(Ju=rulFZ-/b9d3[o2X-tFE7C^DJ
fopKP#V_FV"@SW<\R`gH8pr<u8$O2p:R=4TWRpR`m*Jin`6d3,t>1><e8&`e!Y=8Vh`aE48P
H=JJN;Cq5IpKO+&rAM6R8oO4K%!73ES&8/XrL'P[1S3#s"hA`-q2mF%c?j4SB9XM5S_-.gK&
h--c5>022^.gWu3ipt=b*:D0TfV=cG<2.s.\oggQ3gOc_I3L&i1-34EIXH6)DH'f'R[ro8jB
oYXc9mD"4+I/8rKe!Y/_l2Pa#/9g1mBH3[5Y*$5X]ATV\QR_Cc$\bS[nXZ7_JNd)3l12M4k\>
H^"+@2hTsB:40ip'XoBb_ZX:9lEp"@%i8NI\j';k,?OM[fcdVA7&kU%`j?OHO]A(MT\k@g+J\
p]A>+O!0NGS&upo^:or8W^PF=(G5S09^`m$lkT;8h/R.6Zn!#\3AQ2'C3!HketS5lt.=`3\cZ
cU6Si_T]AAuCTMM=llK"?L5DJj/2S)$q5+2]A!<OK#RdUb`u[mg:^8[T&q=aka,Ec'd\PscKeV
25JWMUV['mI<";9&;&&iLje%YC'Dd\c;3URHJ9W(c@NBc,$TqTK=Gp-U#d>\k_jBSc9a$2Ag
R:0@'cuT6rR2*I1d[/$B:4rPeh)&\G'M\V(=@>MWas/+caX(nA,QbLeY__W`,*Bj?8$Kb?)-
]AGt0/3cuUQb7GN'"Vaa(P4pbPS*nF#<j2CD"eF:\.:)Ml0KI(o*?OdS<)i6IQJ.a(Y]AB]AS3`
+_0em[rF1"\Mb-gIqjJ@b!=>K1bE#G5kA>8saaGgr1`5"HBNj#uMf+]A86h'hHN.kkN;nLRs<
0@COA?4:87G1i(<A;#Pdklf9[7,l>R[7hr)TM-Xs?$SrLRlUbm!rRJQbW$\+D:"B+1oIGQD&
*qVdpiFJ:mim[Sp'9e"%!>`se]AVag;e5p.&88(dlDb4!F%&7u>mjhTPZ99G<ZlY>lQh\Pkpj
CSViY?M.&M&Go-gET9il]A.>)q8\I+R<Zi?hlWh_0bMoTf!/OB=nnLJJn)P8^98aST)j2boT-
9:>Q5-ui\!,E3W\$\uHhqYL.uhge2b!(bupW[^Nr?`UpWh/BU0hSdnSd.9VJT9cK[nZ%"ldm
T8e,"sqB`N9/5$>i,J3!&K28)\g;ACb$]A'HXr;2Yth6mjKAh;:Vma:h=*K/Z[eW%TS;NokG\
+MPX_h*t+,cD/_Zf+g]AGqQgp:3qSXKrnNt3Lp#$0VEXr5UpO2aL5"ZC.;/Nok?*Y)F",=3W#
OgWB;/i"NHl[.h5ZPtMjFErPkoURDMF1T^=;@J$g41IIW>?8_&U.O/.\.t9_S6!d,$Hddp6<
uQGK=!-2'o?`6/PTbDd=&C&oGFM>,d\t8>HGMd?0LD9sX.dT@Nr,!+HTo=s2!o1TABa-jgk>
H2IQh(Nmgh9R\WW;-Q!V@]AsI)TE]A?"m)@Pu^$b=O7_WZBqE:iaA2F!t#+&'3&Ht5Z$,R>/F/
(,-CeK09QI*WAg9qL%DeNi"\gasQs68/GpPpdp#uBp$DEoTHW1)"Js%d7q0Yb-4LYUkaHXss
1c8g!PP6Y0<1.r`I;*(1p=?%#2[83h%BpYu9U=en)`]ALfNFp>n>jc=tNW/KH^%^V!COI0t42
:2#FXFPsG;VJsp*r<lt<\Sch7"obQT\%QEfH0Z8(q<rUfE%4R5^V:@&A<2Db?lua-H/%qcE+
XJkV"$@HX"-&iBjmAM\YaLk*'b&\]AsD2HDC;?Jo<[f;I*qf/O8=e<p,\A6)p/0rU1tMP:Ik=
(WR$DIVaQLpa_k.BeB6U@<FNmE6)fLc;FLkgIu/,hYdcs*C"F;MWH33L]A>naf(]AOd.bbamc,
")BOA.V(Etd+6@?<D_\sirSAY`Lq+'WtBlYm^L5&2H0())?k.K9(lH>@A/<>X<f@Uc8"'ha*
bhp^qGe]A(4Z,VmjaD:Rip^Hl6Of6_)hQk/qc5`;^;WL(,"P:rDYP;1@F95`g9]A<#@9,,-+OH
r!+;;[p<mrbbOcI(?%?QW)Ik%Ig%QcV5R)EneF<^5T-76Yi,2$)apRFo.Ad4@]AfjHWTJPnrU
/f]A)bIbBpe\HZ:q0'mITi%%(O9M1S$+OIm*+cDG)#APekI(oV@Fo/_gE-33s\"r[c+j$-\f0
$YXk=Z5%b@HS2FT<<g%/(u_I"\hce1ifE!RWO;o20(8Ips*]Ab8;u/m:HNUGnWLlq^cZ5V.Xo
.1s$,#\+*'tkPHNdj8DKj?cKGPU?WhX;tmND<T@fMV*#`!Loo(J*<_W%*S.+bZi1]AU5qm/6h
?Qr&udjm)GE365=:%b.N$'55Ukn@qa@.uODYO2sbR%q5,U(Os]A`kD4;.Ohi;p=H_kk<L0fAQ
0qmV;'mPIm9.GY5(a[^Yak!D!]AX.\&DS8n2lMQSp1@9eBs3P)&MjO]A4A@<gTeFnl?WIY1fZJ
[7AZS'r7RD+VrQ:95j'RjW@SeKEiPi1YPKnMn&@]A:m988gKr)V<d`o`=oBSP\jnqt@r%jqW!
^HFfY"#QbDo%+O_^bFZ=`N?+50/gAj.DO9Kha6Q$jAitU>U4%e/?Y!r3Ui017d#8K*#)<c.m
9"m7(GH>4V7R-lVS^M8YRC-Z@/6RB1o65gS"SA.9Butf8,3hJ0CBGTmp'T=65U?Hn)4$<@6R
?8+.=7ZfBGOejla[?8o27I+lnj[\O2S%TaUZfVckf:o6^ikX7f<ingW9g^E$KHo`#+V*d4-?
bZ%P)G!Mb.Cq-NdVYerd]A$[rVMiL-BSP5!St'Dm=p?ASFe52tf:K)KS\$aBP,@+Nq5Y+BG0a
iLr<,1W#*m8Q9`Gl)H0]AI(!Nm843B2'DQoDsrru5[VpFg0ihaBD<3gs#EG&%'m[Hc%?!RuS'
P%>LXAp%YIFLc#VM9ZmC`Gn,;\E6@7-.f;a'Ss'Y?NQKfm^7F)jXS4C__$[@SFbL(+.)ibcY
2ME)aS@h&cqGm`4%OdcL_Bi&A<\V"97`u_lG#*C]AqYLNonI6>c6q<#5gAqE>c_4NigLuV<l<
*FC*R^hoRk9*)1m(=6G23TUB+(s*A@U*Se1dZ2Ype\nWftmQJ`/r67k0H\_4;"!_Vg.U.r?0
Rf(`_P<iiqt,+@q!2(THEV=B@To5$Q[+gjMkc]AcDaE%%]Ae)FXU2^dMoKCO?9mI4eFtf^1/F)
`G7DH/rmpBLHYEpCt*2ckLV;i$(l'Gk.fiG9GpU]A*47ogV5HX_D1=%.Vh^A.NJ8\DBEI_[_[
5j'd)e-pWj"<!bC_!POOMYuDkh]AhQWoaT/8Z&hcIWVEZaW!nb-n9PF'>GMA@B25Y1e9O&FV1
C)-D"%@gKp=Ck\oT2GSPtK*>LA%JE=r<NrjRje/R-.Kl/^!B^/<`dl+2%j1t>`S:V80hod*&
`!Qpm0cXcP>91QYK.Op5?6=)+DV&e<t14JoNhmsHU-[cpk&RQn4I#jrZN>uACI!.!)MBj-W3
_SYar2r_imU%WTbl3,eUKe@3Pt!3_eH_9%PPh+146CgUb?@dWTjs0d^k4I%R.*3p`K(u7[Xg
52"e^nTp%F]AHYki*bhVNAk&cNBPV84.a.H^BAm#0r94[WbO'\a3<Z[k:S<[%%Vog(h@#oTqg
]AS'"WY%g2t_B'`F8dNL7R#GW[+.%*sEaleGLl%O^Wj\`K!IbD'^ss"H637J+4e3ZWGM2,L.a
g*fM8^sAe/K8'>fl)Y2^qrD\C9:_dn4s+s'^KrPYl/XmG:mO<8`S1YcD)E1(-SA"lIJ*a/9[
>.-AHo;.j1db#?lK#LW#fB"IR>J'3&=*)e?A9c,^.haI//J\V!t,b!?93_RF,pbgW=%9-h)A
6]AbB\gdpm7dqQbF.'*f]A<;WM,.lY"krJ:n<0B4L-9PXq)e0<5D6>%i5Qo;`V+IarZ3t(W%Q;
t@'nI[AYUbuEL"APgoIc[RoZ&h3Zs\&S24G@#?!",l$"6AlOs@g*T\@)KgX(FEm2tc=<LB%p
g?r^?_k15,Ll$u9]AAGjjdD'2.G2c-+\^q1S>5ioFG"uAdeh`!IdpI]A*]ASVa9nmKj+HCdut<7
u(lZ=u(lSS54a-.=oV!4>U'eq?qL?]Am>Ca&s&([Z`iKj'??fFj+Li=pl1sX+I\\VOcGDh?4p
',nGYp'4i010!^VJ#5'?ehi1sB7=Ps6LnbPe8uG5D$g(0]A`!^,#.8-\n117oX("+I?\9lXcj
kZKaHE)JZSG,M=>``1ep.V_LTC2ts-eK`@;f;nM\tHXC@^[C]A\0V<<3Q&,eSDSo>Rp?.TAAT
A1FNG&0%[]A7XQL_1#o%o7,3cA!;Ab71hWS@DY[XgQMjRZG:UepbH#8Q(Y_(-\:[Y1_+8GDu-
ZKSoTV'juN&prb*h/(=bK'o?fW#]AlXjX!W4fh0D3QiWs/^&mKtS@Ys3:11-[\b,g3qoHT5b]A
,kp2PI4D6aOI0,U4%b=pq?N,B3q(<k"RS[L!,,DA"'!CSPUb\fr]A1&M7>$L*4`=2"DjGL@Pb
)TV`r,f@MNG;79l$/\[I(cXAE?!n[2O>VqC<TUDCcDQof!R71lq4s;r@Hq!\A4lSJu1\+@7\
[ilh[-GB)0Hp4bDT^bIogM53kLLgF!"ncN)$e(H4#i0JLZJ38]Au76V]AL#CVnSiY!_\\S8rN]A
k48j/uH[JTSeoi<_caVl"h5=\kCZ!=X.)L&/*FjX;(ql9J.L`r0"#+[4@d^P>;rJML>PYRc/
0kr=5a70hB%APh^1X#kHa-(u(_'XuWfc*J\ZnD`m4mJWjfn,ol*^W"^OA:dMNB'uo!9+spB(
mMu7=L\W[o9hOq[)/b/p9_Z,Vu(:e0eW4e]AOCg'<@HG4WbK.nu[@OkQGurmo3[gSTaeto-.<
^#1pBTlb"Ws#nm09Z7#s:A)u<ECggFT-g-[ra3gVQCp$+`gLHfmb>E;oo<*0(<k1A[*9a,Z_
*L`W(9>YVGPq_:#"]A"9^D9'1!a3(.cN]AoPJl]AR/+M'bl66MTL-<(=oWQnlCR41eGJFV@T:lk
-.BLY]A6iXRc-8PQ8cE.)O^H<+[cMmfM:3#Hb(2XDX2mA2<E3u8>P9Y$*h@oG^!K2:@WR1uZF
?O9rR(oGauQ75)("fcnYN@Bj55Nm"7MY:D,euspb[gMr;H#LXnXGA,Ao1mRb9_9%ZkOpuHT@
k\UjD<S?9mJnLCP[_'jSG&bA^DkhrOY<V23H#2/u"93-`9QABk^lMVu!o\V+!q6Oq1*3;ACS
SBbWn<"3XA;(R`T>ad#g4B1+n5$$f<FfRh#q3L'#/n@S*u9p7/.$2IboM,'#na)fVR%h@)NF
KaT+lZ$9j;!K6WW?mH'%]AZ=%--B\+*dm\R=bREVm^IM%'GW)5NdWP\^asEt&%nJk3i\j3r?.
?I$A6(]A[@7In?h_/JRdX-!:e;>&Ira,dIrq)cJX1=gc\-^n^p:j<,;AJ1CfEn7lWZ9n.=NmU
a)<WVO7np2hTtAW,u$QiYJ',)em!!f1n^J2*Qs$VNd,/Y5A/j2[t6%D-^!!/VZ8;=A*/NJ2B
L,Z;$M@sf!fFd'[#u;_!,mm_;*@<H&i\\"6;Y9q)WSs++MGO0\30t>a(Pa1hQfgnJf3DBp>"
!HT>a8Sj7D$o8KIp*Oe8X[3sf(R/@eb7.DKVlDfZk<gUI5pGb$uHTbXR>1T[[gG]A-U%@,^(?
?KG,6:UDnd9q/:dA021bBk1=<X.]Ab^%I\35`:"^a*![fX3`c_b(-l9SO%CXo+Tpa%ncTUmOX
8L@ni#-ij._fa4nU,6?t9t""c'f@B=RZBfD0MXUh-0#8PiG5o"KmUsnr7f..G/oTcK?gQE>K
0r_WSHjrrHU<p]AaS1GrLO>?LPie6`&AG1<.RS*ZUU,(Sa9's]ADkSW7h0^<#:l0UD8+@[]A.M+
rt_<3N_#IQe>TB<0B,%B*'<EkprXChEXKbdIS9R(Hnn/ZC$-RoM;WPh>C>pQhD5D]A<20]A&(m
lq\`8*'Yj9?B9*P;*:&fh(WM:Z&+/':ZH-?Y7!n'FFt@&<o>>[Wh&XVi/=NfuFq<%U-8$bY,
enT"9'D?cHoo&b%dML$ck^^lOq(OAT1k`2BIDcSe/4h>"chLeJQp%q^DGr0n(bmSYu.CY0_*
Al.VEp!\Or#`:Q8`(RJadEVI]AJD.e/P9R7elYRYf"4&'0q=(a_pUph1?:X&F)c`ba/C,K"?:
MA$o)EQ+2Bs"dPpF'FIXV"U+Wg[b)"BD@^nojq)NJ"Ir&o7%:^iph\>B6B7Kr<5h3`%b=+l"
\VrEj4l4g(l6\<7,dPpY>a[POq9lIso/4\ddAc55g<,20_cpWF2DoThr'Z^abaAI;j8Rq./n
$_uage/VN8^]Alr:Y.kRWK'%GH`Iu*pg*cj7@,Zu_f55MSTZ<YMlGX#&cqDm^X,1+%/;:2)S:
rE>EAD+O&h_!=i@PE+3.F'25*6QeAB)Fu5G%u3(rO.B[WD@JW$@?F2<O5pnZU<7.0Zg&;ZIL
<)aDFa!U:YD1c#c.EmDiU>iUK?N%JlNj%/.!B1fo[s&;"r$r)-G,TB1k^aK@9S\G*sHdORIE
&WW-"@-cXkO`I&6/%2hu(!$WFe^M]AFNM5qtY\hrtmJSp4du!c21bttf?KA72Sui(8?%H%1<b
V,Se8'N!0HUo;4USND+.>Ig"$5oG\C0k.9Qp$q-iCZYV0?4Ob*#dU>tW_5G.7(kf#5D*HDM:
7=cFNNlYiAuqB&Rp\[8Wr%[V5R2ru^fF:#+-=h(#f7L's9*L8NL"A1VmeOtle$"iQ_V0+t8]A
R#ZGKUM^MR5$1NjS5:aNt)m<Si_`R$Pj\92`Bet(60AuEuJY%9Cs;d-D7>?4=sh'57;TPM)`
XXlGkb[K)5!?m?4PIqSg1)m+]AdFNPBi`R?m\7o69+DP:+B6(dC)uV[t#-=XiScQ.A>q:ik^;
32Q$+ip&3l]AWMX#GTZI_#sS6<S+K%&.]A-pgFn-cm*UU4^iTqOP4NVhZc$cleqN8Y2\akVt<i
T73G%NjLn8<9\USeCikT"D(s2s3L^!VF+BN1.,&_HT`K7"?Y\8qiTUN>,X?W.*klq]ALAI_k?
3=M^7WY1m.`6M#ANYF:'!lOfj3YAXandfLTg%/HBWY.>i-K!fLG>&57h1L+k>><b"i<\Vc!,
_h!.i$pVsGGEc]A9IS$!SBiK/g:nB+o1]A"e,tf`1.gqg$e4`P>G.O&>pmkaT4DLmUQm'_u[8C
2-Ub<B\pVh>K36_eh"$>:6V=HLO:QqQP*DKqVHGkIl0`4m-'CW0VXHW+I+qjE6X7;0&oU2>`
7@f8cDT>D"So1-b;Atc>bA%D9:h+Ngc&#0+W=:j?Q<Qj45T_OnSY781\F^+Pght'iQ!M^9$:
)Xgg_MVbk0,U2f'i[Q!'Q_@N;]AC,f7"s',6j\b?(e^m?T(%6;Esp7l.9_)>LGV.I$^KWk\M=
gP'TK&/kX/^^V1\"J)A'iH25rYBL\Iicg<($mlAI\^tDX^'`'KM.eG.67eOAi$+-@3RqJ5PY
-^"sT,HPM-"7S2EOL'XfKh&n<7O+]A^^RdnFri]AT^$]AfQEeLSPSQD>>WW5QN_Tu#7G/4L;O8<
Cr#<"5bQR%@!)/DD[J6sfS?CXK#QCR>?/?"tU,qbN#FuTj<e^Q^TkGP&r+!75/6hTKplOtEr
Jlr;#)u1.YB+<$+Eb1`%cZ/$?C[.7g:'Wnqm^'6SSKg0U/s^U-E4d^<;;.%:LB]ADrC5jn$[c
ZY_MnUrd'^)F2m'JPbe-$o/RjX@/5RQE5ML?l+.4jl::t&j-o;XfkU:\i%_2+Ta2oh8GU?Rj
@Y\.>eF=buAMYB0m(ehtmlmbZ5$fpE=i3=&lZVtDW[0GFr=5(1Obs+;DPr4Z1NH&V"WM`(U&
`.EgN*Q9KXgeU!T39f0TL3DY]A7ukG@Oa!/',S)/r@%j%`Be"rI,eR-5jeii't>W433Ut!c,m
fmBQBH(,bWbmIe"o6Vk*C?+/)k[knfT!B'Vg+CYV#qVQVDr(CjS1agq>N^.&5ZDo8qjCTbbT
msaY+9:A2mK%YoKXf_<^UAf[ZnA4V?K<`0VH%Oo(^5oUg8MN.Za,5_)7Y%["oCI>l`B*k1!G
eRMj\7-*l>E6_'s'_FEUn6E`\3REcf$m6D7IeeW^D(a/R\XK6qCc\?`iL8Gg;(l!<R_R;iGo
YZ&3o*B8bfieIX4(-^OR9qJ$_.'IkLm$FOm?eAI/D7Ra4^9gf).o[:]Ae0-9GtMCh?tbS<q,d
[X%rT,[9F,_em$?-FAkI=cZ?k2P&[M)ll^<_U*F(OLUTYr2j*cGZ@e]Au%IsjN25Up'lWn;0q
FDg\)kP4klk,r0rFj<+`e9.fB0:4E?stUTuVCn2j;-qJiq'Y]A]A$5qG4CIU!0O))@!EN_YnsK
?-i[[bkWQ=VF.]A!86RaH7k1jm/D(O;^Z!O.F[jVJ]AogE+O#**tLo);Fg.3)Gh^I9e7JistMM
XqR5[EEi+(DSuE/F?C[2r\TrV%6D`'9k")ZR-bioZ1!J*?oQW6TmBY[^A%6&cU=(B[K@CE%d
A]AD1W3AVuoXp>6qiC9K&tq\HV^XLKkhV`OMIX"Y!6hXX1WqJQhfIC$>103bf_[-s-)htcFN+
Qjn4's)Eua<Z_<,IJL;_LHHTiJ.<+YdB#kD#5tmH'opC"0um\^d.%1\MnedfGTtJ]AahX!a@Z
tc8qF]Am*f#]A7j7f*+Z?X"jn)f"LIOOejm7._9Zo4IE#Qu"D?T3l=,ob;Dn$1=0fUM._SVtVS
d0kHMRWe$E$iaIJs3D3A$.@/Phtl4C-t10.2t>>:Y5d*aqYSN6Y3HH$!r`*gncTq\i:dfZ^d
HuUNZY&MAm<"/m4iNWjS7)!+8Q&*DuB&OY%-M8H+s<5dsmNnV]AS)4r_LZ?bXs*-nbYogr')U
;s4P'W_tRF.4)WKC+AAEk9+1<_079%fBE.f4c<)Vq/)K<6nA^(+^,4HT0jCD!,eji952uT8*
8R;1pAJ>#l!TZaDuj*PG>8sq>f)46=HT*gWMul'1P*[gb0ZBVB(T`U,)jL*_Cd\S0eC^kqH)
e.D9fpZWaJPeT8o@LMP]A#j\CoHK5!]At7.e!#U<o!h01iX575kX6/f:@?hp`B,1IS/X_8:Q=J
a$iHe:>H-H<sh#m`g_(GW-Rgc$,F3%Je')bT@TQG_ifSgR-.lkG$ViHQJ_Kc*-)Hh=pP=.Wp
,/:J*$c)5_bbfKTgp(-W*1:\lq->B=\2B?^>T4SEie;?.9=0/4iGaH?\6&O-,]Ao"U%,!A"I6
F<8Y.Ie':-Q^;mm]AIGfteC`1mkJ@;o[l.&0k<pF$(?_G5:cjX7&C(lRQCI[kqD!SjVM'Y/fR
l&$"LG4j6@P86es"`WiVMHPKcTe,`N1!:O*q`WE0C7i'dau1q:X*d0*7@o7=qI]AP"8&P5"1A
:Koi[rdkMF(4=aEl5C*L[+He,;'/A[p#@.i:+8Q^k>7i[oIi^ao?/6M3:ph!>Ij;+1k`$-(U
nR!FmVV'/WGF*4"(5Y+]A.K@V=2'#."$$t'O)q8s8^"%]A\g:a:Wo9Nmgl@J?@l+bE:(&K_.Xa
VEK:&b8C\E)&\&WXALlan+@<:b%)Cm^$YAX75nQc%7A^"2r9l+abo"+R%jptJ*Y5^:Ouh@*'
IUilXP9e:iL&5BgFS$p&F-9ZjY3A7m3&UZ`9)6+4p2&X3JH]A`=HRPiug:Un(dYFc[gD1jp`e
E4m-b.;*6G&cJ:=N^LPk.%b4`L*mn%".LCN'$JU'<'*k6Hb8W2<4OGh]AlE\)4]A':r$aGIXg/
n0jg"H.XI@"u:DT:Ea+C-FIC15ha@>k/Wbb_N!;9F3recrsN>'?qiE2H3F6;migM=u(>b=ne
X7iRW"-<o$l.d4[P;>57pr(_2C*>.-\]A]A<F1a_400HcL>o6/a;A*Hd;SR"M=aKDGF.f75uBX
@O5Q2D0RkS/t]AI))cEkBs1Un[ER&Yr!f71`BR?Y2(E9rqTbr'=LL\lG2ZTqbGdc^61KfENg8
C>"-q[Ri6E7>6J_j4`6.FOFSo!l%a^ibR`^7fQLp\[XO%fLPQXFCo)q:ZOE.WlKEWYPrrUOS
7u$Xs7u]A^?%V<1<XtuAs8TQL5)K8<+NX*:Fip<C<_&e)]AK#3ij)K4hKg<$q&$P&2H26pjkFX
?0^Gr.dSE4f7n[IZ;60;r9'K+@g?_;U-\b\fR=<3Gs6Ef1?U^)jq[OOoZUY4]Ad\FFnaIV@r0
RriA!/i/!qiq=Z2'aJ"=4YtDXCLgdnd5_K2APr=;PI/dD^uhoD)#si:2Q&`Hbl0@`KUI;o:p
B\kQ-G)smEb_=s*nBoIHWrflO*uXYEs_:>._gU\tHgphWPW6bmlpAQ(nSO+V%:WIfFEJHD:u
]AXH3ngo(1r@*ckrm+,^]AU$-RV`ZU=,4#>Y#"]AB*oC03cOF(XnDnMec*.W;`YUMbS'iP!2V;a
WE&Tr8Ek:d"A.!rSGBJpXO*oDq#]A"\ups(O0N4aJS^TA=!P?'QO-TNj[`DlO@&LP"ekkjgUD
YSDq9:P57<K@bNF)p5F2Nm=&cWq>`IRbpAN/@a+hus##d:J\+VNIqm+[r0$O7ZS<64;?b9Hf
V0;leRs1S$"5%nuqDlT6kIWtJ7uM(-k4aRRJ1d7JV"\>n\a?`jBF=_!/'d&,CQ4HUd%%dH5P
""0j$)[qJ'Ml@?ShT4C,BqE^!5:BU8CSP"X/3'I/EX+j39gGl-FtDc(4IP>D%o^qBfkCc^H'
WH@M+L)h-u?naF#j]A3C@52%8K=d_?$9s',6`pI)iV#7!na9G`tr82ifWKNerVfK=s[<FiRpZ
Xu5C`2dbI@@lkmWtWrZ%EIr0\Y"g@qjGe/5KGqt3?QJUDcBST8\"/j3*Jp:EPQm@,Q%.fA/8
,i`U!6bhtt_agV#i3*&KV*ft@V02eDUCdV#1JgA\>\X8C4VG4:8tb),C'd)k[HY'r"hS._7j
~
]]></IM>
<ElementCaseMobileAttrProvider horizontal="1" vertical="0" zoom="true" refresh="false" isUseHTML="false" isMobileCanvasSize="false" appearRefresh="false" allowFullScreen="false"/>
</InnerWidget>
<BoundsAttr x="0" y="0" width="685" height="135"/>
</Widget>
<body class="com.fr.form.ui.ElementCaseEditor">
<WidgetName name="report2"/>
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
<BoundsAttr x="0" y="405" width="685" height="135"/>
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
<border style="0" color="-14669005" borderRadius="0" type="0" borderStyle="0"/>
<WidgetTitle>
<O>
<![CDATA[新建标题]]></O>
<FRFont name="宋体" style="0" size="72"/>
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
<![CDATA[1728000,12306300,723900,723900,723900,723900,723900,723900,723900,723900,723900]]></RowHeight>
<ColumnWidth defaultValue="2743200">
<![CDATA[2743200,2743200,2743200,2743200,2743200,4914900,792000,2743200,2743200,2743200,2743200]]></ColumnWidth>
<CellElementList>
<C c="0" r="0" cs="7" s="0">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[='  '+'流量投入與發放情況分析']]></Attributes>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="7" r="0">
<PrivilegeControl/>
<Expand/>
</C>
<C c="0" r="1" cs="8">
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
<Plot class="com.fr.plugin.chart.area.VanChartAreaPlot">
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
<Attr class="com.fr.plugin.chart.base.AttrLabel">
<AttrLabel>
<labelAttr enable="false"/>
<labelDetail class="com.fr.plugin.chart.base.AttrLabelDetail">
<Attr showLine="false" autoAdjust="false" position="1" isCustom="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="宋体" style="0" size="72"/>
</Attr>
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
<Attr enable="false"/>
</AttrTooltipChangedValueFormat>
</changedValue>
<HtmlLabel customText="" useHtml="false" isCustomWidth="false" isCustomHeight="false" width="50" height="50"/>
</AttrToolTipContent>
</labelDetail>
</AttrLabel>
</Attr>
<Attr class="com.fr.plugin.chart.base.AttrTooltip">
<AttrTooltip>
<Attr enable="true" duration="4" followMouse="true" showMutiSeries="true" isCustom="false"/>
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
<HtmlLabel customText="function(){ return this.category+this.seriesName+this.value+&quot;M&quot;;}" useHtml="false" isCustomWidth="false" isCustomHeight="false" width="50" height="50"/>
</AttrToolTipContent>
<GI>
<AttrBackground>
<Background name="ColorBackground" color="-16777216"/>
<Attr shadow="true"/>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
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
<Attr class="com.fr.plugin.chart.base.VanChartAttrLine">
<VanAttrLine>
<Attr lineWidth="2" lineStyle="2" nullValueBreak="true"/>
</VanAttrLine>
</Attr>
<Attr class="com.fr.plugin.chart.base.VanChartAttrMarker">
<VanAttrMarker>
<Attr isCommon="true" markerType="NullMarker" radius="2.0" width="30.0" height="30.0"/>
<Background name="NullBackground"/>
</VanAttrMarker>
</Attr>
<Attr class="com.fr.plugin.chart.base.AttrAreaSeriesFillColorBackground">
<AttrAreaSeriesFillColorBackground>
<Attr alpha="0.15"/>
</AttrAreaSeriesFillColorBackground>
</Attr>
</AttrList>
</ConditionAttr>
</DefaultAttr>
<ConditionAttrList>
<List index="0">
<ConditionAttr name="条件属性1">
<AttrList>
<Attr class="com.fr.plugin.chart.base.AttrLabel">
<AttrLabel>
<labelAttr enable="true"/>
<labelDetail class="com.fr.plugin.chart.base.AttrLabelDetail">
<Attr showLine="false" autoAdjust="false" position="1" isCustom="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="Al Bayan" style="0" size="72"/>
</Attr>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="false"/>
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
<HtmlLabel customText="function(){ return this.value+&quot;M&quot;;}" useHtml="false" isCustomWidth="false" isCustomHeight="false" width="50" height="50"/>
</AttrToolTipContent>
</labelDetail>
</AttrLabel>
</Attr>
<Attr class="com.fr.plugin.chart.base.AttrEffect">
<AttrEffect>
<attr enabled="true" period="3.0"/>
</AttrEffect>
</Attr>
<Attr class="com.fr.plugin.chart.base.VanChartAttrMarker">
<VanAttrMarker>
<Attr isCommon="true" markerType="RoundFilledMarker" radius="7.0" width="30.0" height="30.0" color="-907154"/>
<Background name="NullBackground"/>
</VanAttrMarker>
</Attr>
</AttrList>
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[0]]></CNUMBER>
<CNAME>
<![CDATA[值]]></CNAME>
<Compare op="0">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=max(File1.select("流量"))]]></Attributes>
</O>
</Compare>
</Condition>
</ConditionAttr>
</List>
<List index="1">
<ConditionAttr name="条件属性2">
<AttrList>
<Attr class="com.fr.plugin.chart.base.AttrLabel">
<AttrLabel>
<labelAttr enable="true"/>
<labelDetail class="com.fr.plugin.chart.base.AttrLabelDetail">
<Attr showLine="false" autoAdjust="false" position="1" isCustom="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="Al Bayan" style="0" size="72"/>
</Attr>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="false"/>
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
<HtmlLabel customText="function(){ return this.value+&quot;M&quot;;}" useHtml="false" isCustomWidth="false" isCustomHeight="false" width="50" height="50"/>
</AttrToolTipContent>
</labelDetail>
</AttrLabel>
</Attr>
<Attr class="com.fr.plugin.chart.base.AttrEffect">
<AttrEffect>
<attr enabled="true" period="2.0"/>
</AttrEffect>
</Attr>
<Attr class="com.fr.plugin.chart.base.VanChartAttrMarker">
<VanAttrMarker>
<Attr isCommon="true" markerType="RoundMarker" radius="4.5" width="30.0" height="30.0" color="-16744448"/>
<Background name="NullBackground"/>
</VanAttrMarker>
</Attr>
</AttrList>
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[0]]></CNUMBER>
<CNAME>
<![CDATA[值]]></CNAME>
<Compare op="0">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=min(File1.select("流量"))]]></Attributes>
</O>
</Compare>
</Condition>
</ConditionAttr>
</List>
</ConditionAttrList>
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
<FRFont name="Al Bayan" style="0" size="72" foreground="-10066330"/>
</Legend>
<Attr4VanChart floating="false" x="100.0" y="2.0" limitSize="false" maxHeight="15.0" isHighlight="true"/>
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
<OColor colvalue="-8202753"/>
<OColor colvalue="-907154"/>
<OColor colvalue="-15872"/>
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
<newAxisAttr isShowAxisLabel="false"/>
<AxisLineStyle AxisStyle="0" MainGridStyle="1"/>
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
<newLineColor mainGridColor="-14735033" lineColor="-5197648"/>
<AxisPosition value="2"/>
<TickLine201106 type="2" secType="0"/>
<ArrowShow arrowShow="false"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="Verdana" style="0" size="72" foreground="-9142639"/>
</Attr>
</TextAttr>
<AxisLabelCount value="=1"/>
<AxisRange/>
<AxisUnit201106 isCustomMainUnit="false" isCustomSecUnit="false" mainUnit="=0" secUnit="=0"/>
<ZoomAxisAttr isZoom="false"/>
<axisReversed axisReversed="false"/>
<VanChartAxisAttr mainTickLine="0" secTickLine="0" axisName="Y軸" titleUseHtml="false" autoLabelGap="true" limitSize="false" maxHeight="15.0" commonValueFormat="false" isRotation="false"/>
<HtmlLabel customText="function(){ return this+&quot;M&quot;; }" useHtml="false" isCustomWidth="false" isCustomHeight="false" width="50" height="50"/>
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
</Plot>
<ChartDefinition>
<OneValueCDDefinition seriesName="公司" valueName="流量" function="com.fr.data.util.function.NoneFunction">
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<TableData class="com.fr.data.impl.NameTableData">
<Name>
<![CDATA[File1]]></Name>
</TableData>
<CategoryName value="日期"/>
</OneValueCDDefinition>
</ChartDefinition>
</Chart>
<tools hidden="false" sort="false" export="false" fullScreen="false"/>
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
<FRFont name="SimSun" style="0" size="144" foreground="-1"/>
<Background name="NullBackground"/>
<Border/>
</Style>
</StyleList>
<heightRestrict heightrestrict="false"/>
<heightPercent heightpercent="0.75"/>
<IM>
<![CDATA[m(7I<;fDC`)FQ-LU4OL3U=,l+MBX1]A8de'QUk?#Sd\N3pJg`+CF9nR5<G>&Y#n[ma64o:t#Y
5=T#uVBZ,WPn>n,&\tmlbmWcJ1MUpW&=4As/^ub-TZF5-$em8)H,L3m)`&'*&"Pe^;*@$imL
:!s&5D*]Ah*J;@n#I('&=RXE3RerSYo]AEL.g'K<=T8@E!$SmZKG*::?_qZFX=;@A23c9uTJ*,
d]AdD"0L2$?5F<hgOA^*7e5(KgSC;/;\k3VL\K[G)uGRAQ^2p_r9QJrr(P<:?40R.6m#hSIA^
bTNQj4>r4Xp+ofj"@`jK)W%,#,9''Kr7`1.2U_[I'QUa*"!rl!5u-1>On6(%7K=O*I@q"*=B
q6,W<P_5%b[_s0Gb_AapYCrMf@0kr]A>`D[\"lY-lS`0XL8d7*.::<uAS7jN.GHQO@fYV\On=
o&d-T>C#*h:jrp'!mW#U*`04dai\E/^rU?/?Mh1jAU"U[-(GTYZ4Val#5%AVn"8*J1cR`,5q
VG7+)mo^Q,EKH<nK23(hhp6j@H>=]AHOlDjR7DcB2I(Ptkl&+d*(W]A^jm*J(XiHW%!0E0PeZD
(5bbg6-`i20)7Mi1J2!E.c2,X6:;&DG&751(N?F<lN"nO*m(:N<B,MGFLRV=!naL9cJQTVr;
4qQ[r[$n+EM1p%/U!p):O%?"]AVs=,i%]A3/kheUlV+kN,qcZE_]AQC.j:\1Omc342+DFi05Dt/
#.NeYj>r'8*G!sa>\c9(fJUc[/b_*@qme*RhrH(C[8NN@k<FPOEnV-\csc3V:>;O;DTrnLWm
:Q;(E@)oV\/=44L3q^]A^/A)m)And9nnT]Als]A(KH.)'!nb1ugHT^?NTH6i!3*N5VA7KId)\`$
0P!AQp8p]Ao9eE5`eTf_,J#L_tUANZ@27`,Z3$%,f#4_%Ol0TL`fO?Z^]A@XHtF-sYipU-MA1E
D$UhHAloH%CoeEQGgJ:A/%\mNjd'KBmUcWeJAQONT-3qS</TV)6RQ9a5&S5nt@)2:a?D)]A[K
bF%''(]A4_kqZ_n;3S5Q:?jIejY]A";tg=JQuk@mM$kX5=<eHN+,#k0Ot("oe/\HZqte@U$3Kn
#C'*Y(rEp6*.4A-9Z+cP@+T"jYAktA3k2`i$eAD##g%Ocd7$(oCe'%5C=M@#6E!bK2l7s[NM
GJno,tpC$[LA%Q']A1P+*5GnLXVL@G=-NrK2f+,dekopO_LDopjX0l5n043s-oY\O+I7ZhF/b
AOem2Cr2bkf\G%gN!EluUabYFir77PLch:_ebSWL#RfMtbht_TretXICU;3rH.Q9lQmLA]A!^
,EVGs%''FD@tPJ.JWnpl]AJIXS9]A$aQf-5;q>Y'srrNQSe0K@B>O<NL^?"0]A^V#:=$odR>IUf
_J8?H0@l2NjEL:;`I"d:<W76ln3J#B`I1fdSTErOD\PIm0&TD=m3g!aWRDaf9DSfCGVM^bq2
p?$j%(;"9@Sdo4)>hD=ElTAhJ$E+>DV/SY^.!1Pnji0pjdd7fneu.Q.1L&1_-A`k1Sa4>`H*
=R,m1;G8a3hfQA`r+.)_Gj\*8EVtP4r"crupJ$s7OqtambSmM,B/X"9U#_5=qpLaNfZ$VoQM
@Umd9d.RlRHHNCd6<a/s%>*"C%5@Wno663X%q&_DsA>2:ZAYKo)IM^t(@((1LeL;6//O#Hlg
MM!Iel5A'6X\i5gm1DWe:L`m[\;LQZL+?V%I6]Aen=tM\C:bbu+@7d?Ln;'*7,"7Q3tbRRY"?
AEBe^f=W!1aVJ1A:sEH7B7D"\>K*=46u(4@IYEK9J/B`d_MhBXa9`tc+rl8!$Glk\Vek03</
7cp#rUZh[s/%Dg"Tq=ERW8?o;M2[@(kWs4&:9(Cn(`$&j.*$#F?_/sV=LlQfZ5,c^ao5s)o3
c_DNq<3ZY@^KFZWX&sG_,BK?U"sffdHS<)Q"SiP:B,,^]A+_n4;@#3d\$7DmLl8V9W+0lbaN9
<eT@\**lpBFr[`h)0TL"LV8?KW%4m,^Uk;Z#IUK%iEaiB-P0:gj.:b&]ArBDoZ/0_-hqT/"sX
"fDoE(NGpH3f81m=%!&PrDR'K6]A\Lip+EqgsZ5!0`T[hgA79kUd>A9T)fl<L\L`1/=`rmU3U
#O2Hugmb'9:0Ze3PFfe):;!$=Z>L`*qHQ[nL#$PWR5b&8<]AI\W&4iILVNaHp`OXpdL&qDAcn
6hgbpd"_";H5;^uk.%94$T/$!a8T26c4=daW&DA^0EJZTH^;Il[+9HGF(!<V\N7CST$`"Vmc
:PDiY#jejfRgiH0oF#g8VD$@,*D6]AQ/"@kZ5Se+a1p8fq.\PZgTD>-?uld[1hCQTp)H^SjfD
m;8'tI]AdsBA:"H;W(J@"fII5=a^\!2A",1:MnRAg\2>qM@2L-'`4:UmmorE4sn-QOZO*`l+T
KdRae!BfR]A+E2'lGf_HWt?hCDieVEAW&/n<VlZ7[HV(QW&BDSG%>!t@Y#T%)H10c/O/.-O?<
MH,&auAj#3D(d*Vrc[dV6Pcu3ZuJq-3NrsH`0e0@2)V<CpYr3AMdOi7Ur`PfY]Aj+nlk=Ghok
IFB4#R.kunI85rZQ&Qk]A.-Ds\Y$Z30DQ;Di"Nt5@0uH[gqD#rK/M2-AAiATBeUQRM\Z]A('ec
hUO2:kbD=^7f63'SIWW4R:&gU>jG;aja7d\E?$\u`X-G4k)'f*;[%=)mOE\*1nUC5GW'.!IT
+`Ot_9eK)0*d)[lAW\hAkn)U/VNXDU9n%ho):[VF.nGJok!uU<UP,l?cVXgFGN4?0%V'<aL+
A4YC6ZAQ#i<o!g[pVlj_l=-957:Xu:+uc><SIXW^Ks$5261T-d&]AjCP06sqcB3f?<E3\6e%e
'deqJ;WJRk0If4E^]Ai%A0'Xd&(Fs+t,d=]A&2Z@c=.*<psBCP8[-'Hs!+n6bd:b\p*$X`]Ad%(
^uFHZ;6dC6.@_JXe`fUY_D68*r1PTdYmk#,8Hh!;o"Q*[<((#XbYJ9[L]A"K7.oN[:Shrbs\1
h[QPBdoDi;S31FU>kA!V%Bf8"KA@g_Xn9ZJE:@iU$aeW[Fp"5j.4SD05$(AfO^6#W#?0Qa:5
]Ai?#b3aMlrYX#WgcD&V!IXdLMORk;^e3edeWMoF?784$(6Cp4i+Z!ljRZgQ2_(o=I2XGtq&f
RWZ9m*S1daES87`tYYf+`Y*18Fj:I\[75\8kr!;h;Y5_4T6gq4AXTZ^04/.]A;(KthW/:R)cq
3n<Uq")P)osXJn<i[?`WsCE:)=m^8[cE0bl0`Taf`C[^j?5T@%:$'>Y$HfhXmDj'`-c:goF4
c=/#;2d=iAqtX&9dCa7U>%hK=edhi6AjJ%h3>msYlCi7>.C$8J5;B3+Lqp?d<IT@)esCtg[u
-RUA?p_kd\"C`f8WHHk;a<Ya(d0pLj!OtGGrb-"u7dO%K/Et@`[ad4DR-el6.HM%MR-IBbhU
-2BR?uQpL5(IJ)j+L5A@qRJ:rG;^.?V>W4'<=,kde7&YdmB&C/BA[S`Ffj?JIHH>gSZLu_Ei
nC"HA$MMh23Cib@fjC)XM;<0!sibXlWM79I3DnVX6RO:XrgfNZe2>n9Y$m-@&se!_2@(r0!N
5Rrksio-RgU=pK)DQ!oO!Obr<)!FmYN)`LKY$NHpGijni'\o%STo7C?2:#&\5u!bof#dc9b<
$2)n[+R^[Po-S[/=ncCOQgUu0a"M`/,#n#b=uaj.#,`T6*XRMuo_W_=n(Oc[Cq3Gles=J&1l
nb"[VI!>b<Ts?O_,nfn*h4!UH8i*B=UlKFY=T8rE%,'s*a3_X]AtPW_@r77rQX-]A1%B&qet6L
/BM;OAAkT$nm3QTLTO'?6aj3:/'+CM>-FJ!B<hQ]A>kVddUM=p&.:Kb+I4P&o$"I511*o\+<q
R</%U8LgJ>jgq!,*VKQ$6@A]AfQ[^8@IKD]A<Kep-)kl@(lK/2+]A:C8Hj?uI>4E:DPk#Z!DM"B
15<c/#C.LTgsSBi/V$ZT/@lmWW"&iqe[pr)Mh2$t?`inW4o>ZhY$i`pOtX2Wn):T4kQZWnSg
!oN/GL5n54N]A&I.PO"lB"0c;8<nfN(<?9I*WQ[pSF[jH!cPRe-rkurnASp]A28'pA5R!aDCd-
JCL%tp#S=eePE7>936HI%fl4/Cs(F/eQl-stml]A$D6;7:*"#=Hj5C_mO:QQglm!%A!DFg2)%
NT6e2&Xto'M9hs:-.#dijcYpBfIJPbUKuEV^n%smsK)WjE@5DB>gV%%t!)O<4q>P@,F%5W`c
/fBgY\&?Z#jm#lK3snmeo=K<oGcO@eoRm:f<G=I!e3BMe6/r0n+.p1aKa/e<0`mG`g%Pu&4`
r$0!/6*(\1Tt?BR\!kf;j\nF-n&>Zdl5BX(H@s$gn:UI$kgF`$un_J+qX?]A;#8Tr]AO=eW3"K
@JXm\-EOX,[oU/n)S18o^e@:sb*<t*b`PMP'2-FdIXT4Y+nPOB^&`joRh>gVniSg4`4e.l$q
H?ZMtqRM_^^mOmhEr9c*Wqo&m(YZR]AtXR@V)@G*m;+J5-:Q*:N>gJU$>"EY?2)[O12OuXp#^
Fe_&?G=Z25+1V+8C16gShU:'[kL2GD39Y.E>93%!1+,]AVnb[a<^Ndm#486$?B_.GPT$'SAHB
.LLb]AQMJH^6RS_+U.)qOM<Yj>5L)22Z7f/n<YtWo\-l]A"\Mdm,N%HC(Tn=cMe^ZPjha5ar"t
0Y%@eAd4a=?S/#0uW(#kp%)mEfR;a(((-S&nkQ"+bsb\W"O#3-?IopR\FRr#_NX"+^\J!C>$
=YD[FeGh:-3O=o-ctrtt9F7_s>fd!iH!MKJSV<5X1DanH_V><[Kb9j.Z'5FZ8Y@V`@L-:Ofj
Zh!h/Of/VWg0"[a:S(*,AI!l*++PRDjYGNnJ-b*s>+4fZQgae0g`d:6M+FAoj!<DO^T\=e5H
?+&eUU?;Cc-T50S7bQ;.,6T!(3EUn9!%osNs`^P%N5_IX(g?aPf'e\oY-$3Y5Kqu46_WoS7V
er8hUn"0ZKKCb3^]A[\6YZb#iiId>GQerlJ\L@QI0`]A2<G'DRJm2K**gpV#rSF*!TkrQk;Puu
f$EE4EN<$+/(Fuosc[>G-=YlY*hIQ@UIESkuJ67hnf[Vdf+Fdo_D0nK,jb.<CRanK"E!AECJ
?DjcG'N9cb82WADlg25`pK'!7ed_@qL>E:r(B(840.]AU1CUGufh5QoLfRM!t#.j*6PU>K5T!
VJ(C^QrpltN;OjI]AVEFDL-=OihB(&uj?V:K[^DgkUS`8H5';l+\0k?E\Qt['FqD?@"Db?5VB
F9hl=eXnfI4IE9e)XN'U;Zc25&(:tKZ*ii\:iS)tP.p)]A&Hu2Kg0)Naf0?LX"MGm0d-QXsMP
LQotn]AW]A_(R!cr/H<*n5O7^if[8GUqb0#]A6Sq#XpNk%)EbHj8',9e62!6KBZg]ATde:BP*/7`
-M]ASd3kReW>ea)^eUCnZF'[q5RV]A_3IAi0!0;3M(`:duC;okb,h7?esgIcH=d/^8DJ?%_N>F
OSfnA)ksJdQ,a@eLo"rG*+g?0:iuI.q+>!16KPlq9u83CQ=$u=1o17u;9,<ti(:kJhUWbL%`
nrO@0Nk3K1Ph^Lkc1fLZ"W02ueK*MmnJaQI*>I&GIX>k6dH@UF[rX[&^H\Qc`Ls2-9F?6DqK
Yd_=^<8"G,U(O[abe>[cJ.>7ZZe4dBA[jhf1pAciRa!*Xq<!Co<_TF]A".(ut>b=id6T?EW'>
^+KL1a@H!gr6i&,9tW7*iDClT-P='c9AIRLh2&.`6E$1"lWXU3Ab+?p4Qq&fMD%"SgH01q<"
-W!B+tqNEYf`%A[\=Q^KD4a4Sb+EbSGoJ[oTs99rn"TGngT\boJ9H_`!5>SEa2A27*^GsI7!
RPQag.Z-ekTf[9%"*,>QKegJJX*MSjSS=c!7CFK',d$&&d*fV7GLL1tGBLJGE>(e4]Ah,:)b$
2OfIkFofmg%I*=aOhDq8+csWW_[[k3uNo:a)Pi>-\gs#=G/T+Hu+OjQWJ)03$[C-hpi`r(,O
-30&i-!sE[b%';9s2jUJ!2b]ANU<K'Zlm+UqRYu<Qbhl!#B7EBfkr_%-^r;><HT4V\MlW-0hA
Qi<Ge4V(B?Y=6rleLM&[YMuJdNj?2D_;%J;6EGt8umMrJO&BP:crrbir\]ABc["9bR[&%1)r>
U&2)3h5ZYO,,FbF(c^u<SC?G@&L*]Aff&3ol6&l.cVV"&,_,]AKcI$IlSo)Ds4XNUheP78*i^_
_l$O\R@n#^c1?Yb_N[*>AZna'ctht0+[`AkF.G?.!hJ7a/FlXQ<<VPd]A?*&sX^r%B'DGNO:N
N+SgpX5-fOQ$\!jiT8oqqsbc.X;/9#eTTC%=g<rUu"X-%@r,!s1jr7Itb*-A/;8cDNn;#7aQ
?mfrf)+Xs=\cBAKFOg=!ScJi#F<h--Br#cGGS[:0O]AAu!nc#j"/kdu]Aji\2NoGT>B79'9-so
1-.i]A62-SYo3O)aAh_FH9c.=(@`S79>Y8hCYkaY>rEC7!,`*_#`%gMU_!,U#C5(.qWpPEWcS
iXO,_W>S/!bbrU&MmL3:QjdLrX]A3GW,i;KUMeC]A+m<C!TWeKdC_(mb>Oem_UH/IAaBh9XOfC
XhIJY6p&%/3L*[^"b4VKD(<q.r0s/rB1:QY;/Rk,&JL%^l=^-!`Wl4/U8E\7+fojaM2_3Q\S
q*A3.S28_,ba^!Ksf_gsgV#9MlXA*okM`5W\Wk,/bLDE\&U#!"g_+Wn.i^IA)4ar"eopJG^K
>7Q#)P#*3OcQ!*+0F[MN+A1;H7Gjo_:_H`TU5L66RB%KLd46$hf/WL9ZI`;?J.A9)m2kt9X)
4_3L<0#b9k'n3nIjM=Bor8iA'F-77ChTc0Z#02:>Ot`$FeaFqmG1'#Dl`(JWWPO1rf`o6EL?
ibn?/C$Yc#m)c'S42i^R,k5QngVPTN,p=/G`/6):+E0CCY=2SadDhpKSuOBKt(-DVU_f4X7I
MT?iU(8hn&?VZoOE_ZV_8/<"qNHK,g?sC5\;TCl_2^g3cL^7?AnSWSdgsCP)34J@Jk]A+9:MV
&uPct`TQeQ"NX8/F:eAa=$+WmXEgP&>_>.-;LlNpVS9kIGEqf-rH8Q<ff(J)HM0+&-`8Har<
'^$'PEoNJl^SO8?8gZt7E;J-KW/15ih4e]A>*"["F"j5SAq,jKWHE6$5/[?u7%jR%O5l?s:SC
0MoJ*r1]AeC#ddDH]A?YGCp'5X/^L_G&p$3ihKBn.GY("2Mf=j6T6ou'fagKWh,6-tg#qgk+L:
IZWdR?BZd$jn&&#ZT^.>PE3WWipSNRCJ@0>$8ig1TNb'1rMbC>kIOWl>NEL8n3CHBsDQBg/!
@h;:;J`A'F')]AE**<&d6<am2&.V@Bu^_pFZNLN6A:#;AK-d^kmhtspl4j#9>:DEPO]A3paIA\
q5)G/K;<:s3ElqZCoiQW*AE5(NXeb-;,J99#[.`4UoH+)5kUG*?)HD]Af3V9lO\S/</Bn<]AsN
tL=*KteCY*.+[#JSpgHSeWBEMWZKHm>Rjk1/)CpF@=BIe,'9J_koI'FC_nK+<;,In!RM!aR^
lJs".OS(:4o=a[C?U")jtV55G8n#5-M&(]AY^lc;5`LEY8dE5.<[QWhf+UOQ7#^\?X1NK[SLG
H,d+SrTH;0b32:$bV$%b0Z7>4#%'4Z$IW@f(=M;/ALFktpCY$'#SZO#FdS)C#]A[Ae9hnPb(.
hN6>jU>NM!]A?\P&L,(+O;_sNcX^!/TGG_C9<7u9j]A`*I![-&g^L?8K"bC-D)e@+X:7FF?9#N
UpiV=`cDH",'sbGp*k?.KF>/2\AAHQQ\JbX]A$]A]A3@I#)g`rCL/]A<]AF-cUZY=+-.o-8]A<'^YY
DlHjJMi4APHgBLj]AQ,V7M_XQ>V+,KDL@>]A2;26nB&;eS?:;NFR5S3;"'3gV?-O]Aj:b)Fl&GZ
\fT5)o3=MGNq5Xfc>=sL>RbiDW;`Rh6,$iT-X&`I2]A06-2g;M3'?::_QpIY5;Z'OA%MIsi1h
PS<)3.+`RmWl&HP_.GXT0JX6CWmC(mts2C'+q:l9t"Ing3H]A-l#kOJeOEblN]A[O2@<$&VoGP
(O1]ARh>P-6itg;+)f$O1JU::[ZC2MkhBhcQ$uQLLZ=b/g<&a7S5MK-J,ZCO/5b[mjd(Y=&Bp
.:dS*/u,5<:X+P,g$lIlEKr#ebm3J)NE.:g;p=E(+*/S:$3QV)?tH/st"!49244JZ45on5G.
tk4jR8Ai946h)NNg$cHpajc.dj_-W1Jm&)Z_,DN4s[[$)em1ltNA2D$IJuLZ@C67P7AgPE8q
o$k_MU$*E^5OY3/V!'/Di&X5PU]A$s8WN1V8Ac)X5]A6HV(IFa*k5Do&9N?=Eh#+cf]A71UZg-B
_OlhE3[GK\I2E[&eT$o(`W:_$FQ>etS.Bc[\R2..:)@'Fc?BRg0@Q/W.'e93$;T3Wob46lWB
-d?<Ma9k@?Kq1r45K+2UIXpImr=(JBVK5uV_nRR0#:TFqA6tQI&jPC,hqSq'T`Y7:""Z:IB`
2!h4e*I1ld>@FC[YW@-gI'_]ANITtg,27o:nb'1MVo4#f_#9FYE0D7&kCIr)On@?ScT%a[.AP
B1;Jq-S$RQ/H.$6c.D/k^]ApSCE*)e"-2ei<I=Da@dHc>K3R?=-nP@FU5:H#)(R/+h,Po%f2_
X=Y0S\-<sEQo6%edf_'>8.[ISu>YIF`[.%<QqMXYl*fY:')F0<t)&F;h"sFqCo"uY2sSZ1Yh
Zj>?5I"L?KKSEV8<QhpkX.K$O]ANbU\'MImi_'>&uj[5f2;C"gIp=[URS2-GA>[]A`r/hh9=Tb
94I7e20--Oc)[^%]AR@bO<$T2PFR.N)+M&LdJpO2HT!G9JF1FQ*7VYF!l641Dr96[,Yr0#M3q
';e$W12l)r[[pO\VGVk%"S3E\fW?#@b[?#5cNSWYcbo;'F_OX?;l_O>gP!DME@2fY67RV83>
FH-c'BDgZ^K5)[Ja]AjZe>fo+>PeJPc=Pa+oR]ALs3Irq<"e@\rDs=^'Tu_:kJlmY"R4%Is>/O
iiM<E+A=sq`+%-Z<s[#.Z,#_43"st.,b($H8Zc[ViEsGPAk!V7r?UK"$D%\Lt,u9U;WRolmX
$4Fh7u%[u;NZ=8/=a"ZsL^ptnLb_e/-D]AN8%E%hus_=#GW_5MPfj+0Q_iaIA*]A;%2W[kRLG_
jt2>qD_5`T#hM<fk#ls<(<.FIdZAlGET'oMdosN&g@H[[qAB:tf'82OW=9TAr-K964BVTVQF
Z1/q>'p;6AlLW'1YF\("adm*6K/rRHh^1JBDeRk^D,n*!Oj*T3TkTR4W?PP=O;d?QYrnmtjb
q>e<q&'>tD4>7/6-a)3.l`!bR&QJjKY@2q3o4(lpS`CV@2A/m#V@(D,lE7&PKY"2l;8mB6_/
!*A`@GJ#@#]AU5,Ki_^(GktJCKc1#3boQdo7Uh=Y]AuhZK"]A(!d:`O\UQ#A<lO9bT6q*EWPP).
;(m._[_+DBpdA2@CPpMFMZ@8+:9o5`9]A`G^]AIDSXY)"=-e`*N:#c$fB!Qho+!(-!d7.!smd>
hC?6#1R)X]A\bYE"Ve6%]AcHj<"a&fpm>0)u_O&h5>BrYV=YGh`m\2UJSQ]Albh.g>g!`=9fed`
oqJd:%%6"uAho!R%-gJ6W2k<j8<;)d5bO,Ngl[^jR1hC2ZM2ci=uLR'@Z(Q6FT=\REh;=iV"
c<(k5Jc#jZar]ATR$VY,&<!WuIq[t@/j0_ma-IBKsKq"k9(YL`R9Q1LlYrKdjdDml9egnYf58
diG%Xl@5]AnFo.&X8roU"]AZ,HFEb;g<Y^#Tf\cG2+BC_LdiPKI6-;:4&5ll"f^2@!lu7CXfGq
^aHuf&49:P[>DCWh4k1!n/1dc(SroB>hX)D9h^HrUu4tgLX8-ROJ'e8g!L50`oFUB0/bi&f.
4:cj?"ecY'37@n`RNKokG>9c$Jn<WGMW0]AjG_4\!<5.cGlV`0;[U=B3/cN"uaV_Nl>67>iU8
tCMZ7\`1lMiW]A5K6Q?Zb*j8E/dHl,?Nb]A>]AA&OE^IP<CPWI4.0[\*XIMQ"?]A6jc^n^dm5I^$
H=b&ucWFrD[=)5=T4=V3FDN(*6(#e-uHE;0G%9*!JU]A&$N.#Eg?Ub^At).i*]AQI#HM"m9^]A=
"jq:CK(5(8i2eC%d.gBAsW]AB6h3?;s--5.Z4_(&Z^:B??f&/L)3L:%Y%\Cfb1n*Z!rQ?F_C%
[>JGLiSGC0H]AS.]Ai1?RGj9c2g0l7TJfJRnh1DG=U(C=*nWiX\^9F#beZCks@A_PCnhCRLAI%
qJZdQ2bq*Sq40f&o0WY(L#M.-g'%H\h_7]A>.!VbpmG`A[_KpIG2I?T<$Xc\*VHOYm=sKkqi2
,*I4^Y=/\DCFm"H.;3)s$*(S5U;n.U,VU'3VSM.35i)9<*j\_N.]A@Nh0d?B<h,\L-&D>L'6M
c2a1A8a4Bt_Z\N"beU<m?)d$72;2UkaTWB.6PkRURWZE+?$fO^u2:!6Mjr'h:mS3WaVeAL&$
V-;Y%`M$.k20anA`_VT$-6<kR-UIO'LIZB`Wl(_JOm-28@+iRqo_pq2ZH1j'MmUG^Hd9193Z
6KLqg@jCMW;[5kci&m&\U%FRXBrK?)Yn^PtCE7D#HMLAE[-*E]A$&!>T5[>$C]ACSDB7(feELX
RaQg?rK5(KE>t@U>ar\uZKs-:$DP,^k7L^036;AVTM^HDEe@Jp%WhD*[YQa,TsNkGDTk1/_1
Db'miCet<chDK._N2Ahf]AG,]AG?dOY%U]AY'ne<kJVg]Ar]AB'c>=?1@P=Y&7QV?@OKNU)]A.o[X/
hUo;sC%:"?_LZ]A[F]Am3#X[W`S_&Ie<ML5dh</5e/k9+oF?"Z'WT8r)9Nrkpftg''k-%34Ou=
':eUq?gkYm*piGcG?&d2KLf;/c-AS<\YCL$sm@q<oh,u_CL\@`/=N]A.L=Wmmul;8Uc_C(KA$
<L3pq)_#?e394gpkZ_!YJ`$JXnD"4(F/a(T)[&lPn`hYuoImnh9]A]AYUI/(V3^_W(NR\CgD=2
P0t8lJlY'16=n63B4a$[HdcI;IRMlpQF105#pL^7s39EYn]AS<nRSKZ6Cel@#0osCc`C[&bX'
pL[.;O[`+G+O?p&uii%Jq?pp2Pd:cORg=STeViS:1,RQC2bhm\P]Ao)a\%]A`1I`<qj01gJpgP
/\8chEWp!s%?OC6$DbU[b?HX&$?/aJJ(,sjVkr:^n7FJ0G:71j1c8MA!J`q(Fcp]A58*snO\b
%^0VN,??8ppL"O6Z\n]A\*lkTo_MH=c]Aqddcup_as,h]AD*1e8=d/-A/]A1;3Z;+eiIdW3]A5rZs
FVMCe-;g^8Mu@d^Lk%&i_8$0K<sfn;p!O2UN)ThiaU$eHSfq`4nA>&LNR<#n3>ap-gAZ4X+a
pUl*[37YYWe3_sKC;1FKO]AKZ/h!t6Ib;j;'Dsho5'^qnH[="+cL!V+F>F[[0M9e(Dk@E&+YB
98]AoU%-2$/6h0-$"GI;)D&@Mi6j)nj"nt/?A:[Ec+%EEGrqO_7i5J0*?$^9(l`SCWeB]ABBNM
@N@>[=BpouH=6[ku0.4GsMXID:I\'`VJj<%8)Bim=p37(a`X#)FE1/NLp]A,<@fL_/(<M'E+J
2&*OZAg+*:-[jEo&HEd?RNTPCJ2VRBZacT]AZIpB%:etOPp5$tJTf[rR0I$)m?FFq/L8VuWTN
_#Pts$uSJF2e!Rop2.r"T?+'B[K\Q)u1m>^M`7jMga)D)#ar`r5/W\s-fUA;NH@X""2[7kmL
-ksM.n;IUTVZYE+\<@'oP"?2a&/KJ^;?BKKE>A5R<u1=!OuMW3a4CZ-a!?=/6O2!TLMB6shT
D!!qDd3@\?TRJ;aA=&I+k29H3G<I_E<u9&JZ>JA]AO*9*u/jA?h9JfH?!H^>qL=t.'XZJgs`6
OFuH@arGgo4i?C\).Gen7HKMSSh.>-O\;^(^pAsU6G6f>J?T8.",O?&Wgm+JK2U!cJKl0h[q
rj6Nh/hmTd"ru]A'6Wgp<D<!7Dd0t58-Qt,'-LRq3/O%B,,R?bDMe(V;D1m.!i3s..HGG&Ref
6]A+n^KZcPN1/2cT/QNJG/uid,FB_(i,EIb=cSIeB!XFc:#H+V$hAkO/I&3Xsi0amMIfL.g`l
U1N!;_I`R$8Fm4*U7d<LW#W8KTkL`IL7%S$rQPF?k+3Z7521Kq=q8!YR/&6FG;l:A,>'cpj\
e(f<<a7?b!7WN8]ArOl-u1TN^G9r<FD6Zadl]A:U<%p+c5T_oR+<00b9-jgBkYb_([A3)9":2t
L7Jln>,q-XZ`s(Q59)GnDi>7Q74b#j%YqYOCF>+T?(43CLWPoB`/TG&KUg`R+s0bhDV0)rQ`
PQSdb+n03_]Ab!h7Tf#XI"#Ss*[I+//*D6aor+EuB^UCnTW9EuePb]A=hYYku/bP+iDph5-Bip
6cOplZuH!kGIQD^O#)$`3Bd-Gia!O*eG.[\bO6q?h&1^pgq:3AoPauB_,)s3^K`+]A+!>7[pA
9""@gc#+#uOE#bW_n0+:r\LjenXgalDs(b3R0"`B/X\C"PgS.DSn*rk#f0rG<`7g:]AS+Y%mf
U9/e7,#4C4;!E!^>FGQ%s6*I\9rlS_Pd)k9)]AaC:2!Mb>Ku\`Ac.]AA_ZIS#N)s(Y9$>n_%4p
,mCLR$YSX:I?34l`gV`.)i*Fp/[2$!*o]A^QC8XD]AMNo;,48$,6o0GoV7GXV+G3maGFKb/a,P
DOtn%)+j?)&#AT[&b-o-+Dr2hF6'\12-mJ"Tk`4qq.J`A*%H9dX0mHp<q#(/PQ!hId/F76m<
E-hh'3jQhZjOY7R.hGmHbueDQdp/e9n0I%7!lX#c6q!fi2FS[07VWP\]Ar[("Vg8Z\a3rF58\
'0f>9eG1DC)%AHcD.;bCH.6j^r0gkXqnfHq[VKc2oUGOmc:(+9M&`iq(uDj/rUhuE+,TJUrL
jR5LhYGMYBD7p.T(.EIbVGDb:s4Uq<Y-C%r"&BJBj'QYQ+e<E"mop*D3>bY9"^bIFQ0Nb+!#
p=6^:tdlIHhYI581F!7$'hZ7@PjJ9B7,N-1g/qLdQD`;&2\@*c"IbS4?N`@2c/RJ@G,*Icg_
om3B:.&(2=fI/4`a+eu$Ha#i.T7!Vs3QrA0:#,Q?PIRj,l-p'hY><.=+6,*TJ!nK9Yt/)oJb
Ga8Wiq3]A9?:IJ&c`IK[@F6>Q[>0MWA;a6HFRLUbspDa#iT#,X(*@e(YgnAK_Dp@B)&q+p;th
WK<te\_puXf2%f`[ac\t/`\[/;o)Tpe?AUEBF7PWCDD^Ml:KGfU<:d!-=:&)4e*G]A-TT1qYH
?+,RnK!l''l83AikIX'%.Yd6oOG^rbJ,L0[b/VKX7/'eeW+*?[.'VTnlfQ:uEJh^]AS]ACi;P$
75.7g",'Qjcf&6AGLc4t<DrI9OQ5*nL>G`8&F3XZ(j49Bp/XUcW\\ATOn`Ko:<XiJ%CK&a5l
Kq4o<DoMSl]AcZs!j&e6&+4oJF9)g5`ou!qkYeY[+m`"2E.#0R@hZT7e5`Wc^4q=`'9j)TMlZ
^oDq)u#QA`ZlV5hnO=hA<sXo%GH'\Z?<L(auc(Bg*sSD.dpLp7trUX(6E5A8)g((QFJCBtol
UE,R+Ps^IZlO'l/0ts>cUFqbjpjUa*mA32YN'>Sm<N`^%^t+lR2k;NfG[@<:ed&o#^oJ!)=j
KFj2(Ybi4JtJ^[YqEErm>HYSd@mhmf>iY(hm'8SC1/1>HWLlKlLjum@f0<iEJTs,-;/$3#k_
PM-O^06K4N3[^&VG5?OUk/>*QndJ`.^3so_8Zi7+Joo4^-@0:&5^^n<43j:<E<G;iVc0FAj*
8PKJQ^=/&=5(=4a>S=GlQQ''<qhr$(NX\9D`2XC\//%)kTrU")/<-l[fpPm7>]A"QW56&D?eW
LS!>E^MH.;BZOK'su,q"gnXNDriinC;36lrO'3E)m.mP>>["ae'3W2NHA;<;OO-HE[C)81I@
T*XIMPi.k)$0$jVMYeAQ-XV*Ba9t_7!4BWecRcO^]AThBt1h&k7at23Kic["\;1%MqUA+X>nR
X&heKDl6$CIN76$I%7Y2mQ'=%?&qLa+48XZT[X(tLlbH9c;V\QdBc_,dMY#*CjMJsLqF!3\B
[=oj\;S%M=+:0DE+632Qfr9C)XjZ9B]AVX^aubCb@rPF`UnZ]Arh7ITBT>P"g0lEtYQu+355SS
IsZ;5q<bH#05sDeCIuCJFgTu``(Vn"+4'3dHn05r-$A(gtcLDV<R8&dOE]AC9KJ6tkN@nP:@,
Yh6YMcj/3$Na`_':U<^?]AceG-81Q>YD]AqY07)p5O)DUR-m>;.?Oq@"C^\2*CEmYVB#:f'Y9t
KJ:NLQ4-l[5DZH70=hVnI!HPeUt9E6(TL)3F-;B@.4dABl'PLIaqAd"U_CfA#I5Y!<IS3GCA
,/%+*p"bPehJG!:[^q>ji*k.C6Iqi2Z!`C^6%5[ID84_tT!2Ha8kt2G->ec\-(V]AG)L\<WPH
RA*GjAil@(r;jhgg"nC2/1"&^(eD)"3K[gWPDUTkc,?WBipS='klfFi8*dBj9n'!p'\7&k'r
Gq;aT[dNN[1cpM$&9*>Y/B(rAKZ>j1L&/JM`,Y=j-rRq43?DgH5*1?T'\i1JpF$F&O-7\.;(
Hi$%<@_%jL0A[NG1^1>9!JiSuhZ_6`64^\'87s+e&>RabD$gZl#Z:g3uZ!rui=dH^*Q[9t(9
*Y[8X(`N%E0ggA+Yc0ib)%gEC(!">ZkdWU^q2[7.QP&3O(``3!4pJ1t!;+8a9uM7eN:YpQdn
WFcT,V!VYHU`K5?f`\+9u`cn8_JbhclLJ#o=Oh^9L-&2'ga,DK,\@gIR[25j\HU*gU+sJYcS
0"D'*#f-nP6;UfF_+#45L*9-%d%=^Imo(ZHK'^1eAT*@Hh\eG2GjLIp?F:4R'.cnA$Y!6=m:
Oe^*0#q:;D%Q%N"hd&1q.t8#Q`HY)q(&E(r"[WE1uJT=@"566X\,HeF5"gL6W%!k))Vms+iN
p:lQ,"]As#,*-NVnS("N!nq`NIp]A>qg9X#<O%pg-;f7Dt_c!`%g'`qDJgP=faaHH+7<]Aru/k\
kXk3saT6icgLmDcO*.r7(?c"3DK,XV?6;adkjjs<O8c\L[5o>-!kcS.oa^-uJHBM.gY4;+5[
Ms`9@jS@fA)7_EWs_>7UWq,!TumQ94G)EccH3On]AagjHjZ)ZE%1Ht)K6OXE$4`5Y&[#2J#t4
KNWd[kRP'[^gj&l"e7!H#bBn"rqXh&d2]A`jXpYMT6Zeq2B>mNPJWQL.Q]A%%FW?=c%&Xmd9XS
6j_moA\W2$igi9Q^mSLLOsl)jXLBogHpr>A7f;u_l]A2ZC(9d+jQ>h^lJ'NrC'RmMdJ$J>*A8
AIoiOc^;%MKnWq)N>lIU6m'Y/,YXVgED,EV#W)sfL@GF*HNr=(1mW(O5?L4pLc>-Vo6;d1ro
B=(njRISXsf#1C7G70Y?[_U4[a$s2t"h_?_gtCjef$GC%"%KMh=?_*pJ<;:9TbQJ!;qful'T
b"qqM`35e_Q=sHfG1o5"q\07#B^3ZHR?N>'pf^G8^-ue^\h9fHr??-$]A4j6V$D9rS?#9#At;
)DPD*u6(k_)C3L_iT*5@C%p`qq-P<HpQoL>/`f_<+qNpd%7.W%3s&cjJq/;M:JX3QdH<3Mjf
e4$K!2*YO9B<=-pNSHVj;G'Q+nd;9W:(F%@50;`3I(GUf&8."7JB26E$7nlCWrLt_?Rt;:UP
&YS-8nO.R,4(U2+<D]AQ)&!dEfNmN3hD+'8>VFG!b`.()DM'6oSD2VNAcLL8@\kkO.%gW?\&e
FI)PVd#X21nuK"EL'4*'FGtuLP^e>X=%()W(Z"jIhg0'hQ's2Yoqs\S-\DhUT=iqM*`%Q".u
O@,O>%O6TuF!#!rs[/Q$'&?NTjMk[s-_:*K;mK4?]A3\J+en]AE0.NsA#lS]A^p4q]Ap7UlD<[Y/
WU2>q'.+R'(mL#XJ2KRo+hC?jWY>F]A5m6%HH2VDiA-o>m*Z;(gUqpU=';Vt,Oo(.IqjX/*rS
:D"Kj_:iSjd\$u2p(%<dB07>!BJ@(h7ajj]Ac.-.:O=G"(q'A"l'8Oj.m92,5-k9Mho59sR#o
8:lHiI2WK<<H,m]A.]AIQInh6,SgfE&O(6g&VLtE0d7P'nf9D=jLA'R.(TYDJ85fP]A!po..X)T
5-1;`(IHu!L7eHDcK+u;BCr39+HP,%5sI""U?g;JXNcQVDIOJCO\reM[Jt0o"i!/1g,#FKSV
q:X:NC_(QRi]A_J4Yjm[\]A!XK?FGDEZ8f?6nM>+jf>:NC]A(7tAI$H->BY`:aHc,8G3dkdr:<e
Gli=i]A2SSY"$A6T4rT[*)LQ(Lb)t!e-4LFJhY-I"U_p*GR4J2AiqRO`E$0\08-l\jA_ZsG8-
$gA+)h-O@r%K-79*K6%71S_Zc'$*<r)!Ddi)^o*)Zp(Hk&mLg^(0_TLoce1HK_b-,B\*/nRq
<2#PB?$80n%1^YYlc(VmBCPq'\GD'>CG(]AcJ'=q6L;Y+X>)*[VbP!Kj-eh3k/2abASt'G0de
?-&[ff#qfGMgEC#<6g8r<Q*.?NTVI6o).Ig4nbU:[)#PF]AtM-f1f^Uc)pCq\$LTt=RE-51ot
rUIGLQ*>hDJ%">_.E_GD#8D64IGJ+;u\9"Z>Cp^&S-s8(P&A?8'N8\SI>H/:WW#Ts_s!@-*#
M.QOKcHDP>"fie[5P@epKA_IfdQ),;0%uAqM7al,_h]A#KZCk^_:`9?Md3o6EJCfQeqEaomP8
hjC%'K&/cNbnQODK2q=!2C6XrJ`_5?a;t&?[\mMY<[a&qHEKBj?!tlAeh%D6"3#.?XV7niKe
s6,n`$,F`^nokm\YThaV4k*LQ8(Sd=f5c%G:W2;Wg+AK+T]AB<hn4Y@Ht,.2,MIYE9JgFmO`-
[UODJeQcHRo2Y4\&V7(g5qd+[p<j9f#.rmE6jM(Z3Wp]AknO\pAY[%&pA:\?cfZ%F6F`W;-/M
Vc8,JdVYqIRa3(fl&KqMD;JJql.gE:Sl!0C$&#,Q1EY\;LeH^KA>>f`C8#"=bL76FdNpU/Lt
)Hjf/uamafL2:basQ!$J\q;Uj6d:imof:b"Lo-pDoD2E[1.WsX+i>IL<r9DFE*T9qriFoR*3
4CA^)H\?EIQ)rmb.`du;0k;+.7a,q)?)h[QU:QL!&1%TU/qFLTcL>N,gg?R[T1p^(mlMPV:o
JKH_p+tb_61r]A;.O.IVq1cjkpVO=&lKr**SGg!j0(MbZmp<`V_@"q:PCOGQu+F*0,3)KC!`m
Ke$Td\7g5=pD]A8Ugk`A*NnQd:Vc*7I?IYJ=eJh(YJo?H9Nl$cDPcqmKP<YNh['0'PM&d_s?W
qAtdn@oG"#'?RkeP^j4!l@:PPP_&0-Rbd/JEuhM5R2mdB6;jrhK]AV#>gZVO,0N,R8a_09]AEp
\!!#3o"tE4+B;m=.T!!\$ZB"bCDf!X<CQ\)5WZ^7/*TaZt2:=#@Ma!Ka8%gP-\gg/kHE@UHe
Yfjj2bp$*bPIN5'2O\g),0/gXDt_'$R-I)IkOoO"<KU7WeSoJ8aUt"kJ,/+gdg<4k=*$%"Gr
l[`"6[7J,<Yl=f>DSFuX/m&![J;\[;uqb$25Y<oi(8\XO\#id]Ac%b@p+'Fg7H60R]A4#&>+(;
Y*X$8A,4d'>#G;]A/DiFkm=NE72sFK/8ir2eS^%?*c`6G@5p&]AO03dgIE)HPkFO?oNCXLS#,=
<Yn\V`\=n`p=2`4S!5c'>Z890,!5"Q)m]A=rCNb9MF&4M`*8DGG`n1;EX'dK3.mi/`hm^Gr6@
AG9[qiH',]Aprr9fqC*f0`D[51!eEXm4r,5Al%/r7MH8OMH\=O2kmNE#7bo,gL!"XEWD]A*4H#
!/);%4Q\b4FOPW\T^J#qZ".ilRfn$g7tqi<U$a<^F=8[!/1Bn'B3l"0(CR$&*2m5XSTKlfFM
EqhBfj+]An"8$A6P)p>fX==nfTl(^q$;sr12jSIM?eXW8X3p+,]AX_DTFJBQ]AA<UJ"Tl,%aMW"
Vn:/^P#R&U0[r3V'>6OJL7V#\K`:34SN"<^s-t$@O!4'EYrq.0ZD@Gik.iaB@?KcO9Qppu$_
>6u_HnHp4+T<trPXO4`@=l-77/:!a&#hFIF+V&2uPQSR^1R8E3Ie8CPchV"JYeFWdaJb7FUU
Ql+P7"aV'"6,V#E`b<5b$/B_aOC*sB<3?:@f&Hr=Ho_mjPJR(<Mk=Jsbd(do)`g>*en^.AQ%
0\TW'TJf1O_3`=.2=R#8%j!sp`)<MUddECS`1Vh:XA!/'d<:NmN(>3i-HcI)s.FZ*YJKKL;a
:-l-]Ae0k]AdX/b4's:hs/^aSnQkeTN?DZW\OTX&/ZcuPErL<?XDY4INp@Y'dH'1)>=h@HZ(pt
GpZE)Z<qU;+b\]Aj!dt$+p_H_B$26tT]Aq]Ar9Ue2SFL0Enq`+`jlje]AM(Mh2HU_$h,nHS;P')R
nYYcXnjIWRTN7m=1,g1rh,%=d>(l:?oc_5-U1t-ESRPX6d9K7439&8[Cr<E=NcY.9kWS_.UQ
KRN8+;i[]A:?0jb9Ue+'3nQL.]A6A!1fHcgt1h0BRjZg;`$/]A\Z2*./eQT1%_b1W>EeI6>aHs1
:u@Uf>g$%>*^6B$;\,O7:&c1,'eOie1"&$Dpb<cM&k2,3^t36>E(rIHa[VrK?iOM*MEJ%QaT
6@k9^sjcLuXYILRAA^\P0SEDdRB\86^ETTLP_qC$JPG?Dg1G_S$/+O_,/e^U)s6<+4):5X$0
G38Qk!3pL0J;WrcL8^/uP7*b,%@!&'S,NS@B%A1:1.(<mQ-F#4]AE`gekjf;+/VQN/3dr4[6i
ge2H.RMq_E8L-QcB%"Vi5Jf^QO=X=IKtf)5[=SKc(*-Z#&U:1sMq<At;*d*s;-S@7"m/,We`
`Pnt6u>IB3bbRq*,i>S9,k7/rT0rE]A$+,nQ1l;KN?QQ(Y#I%\:_YmJbN$PSL`1L6p:'s64.K
$=&6TSYBZFbKugW<cENR3DK;49tk&lftqgal!U_?OgI%823^If_!?X3K(AnT58qH=`?P#'ji
Qf?UoJ@beYBhApbo&:lP)J4*I3lb)LoYQ-0PO?7S0.!qj^^&"S0&$nsebe[YZ-lb#[_kWVZN
Y4oiV6;&#I.n/.Op^<J(9<A35KhTK>B+j1=\ZQ,C@4kH">NM!9MY>)-7:qK[9K\(]A9Mf0!<g
'$NHPr"M3.Be$fc"2rQY\?;2o-8Om-EoNm`+7jF"*U>"&>=3[Ng9-lB]A=W0DO%F(>Hp5$1bO
,ViBi`_;KaINt0>s'<]A5N5cS+WL+VRJRIGZ^2<MGo,kG.89UppU*!<>I'1UcQ\pQmRh%OC3]A
4gMrri+UD">I_U(96RL7m^Zr"(ht/4"iWL@oGU9-d3'?AkTs["q=',U!\sB`t>`7n6^4*VJT
OkP4df%dPQY.M5^<D+jZ?%Y9kQkfbT!0YJ?9Z]A=4JnkK2lCbC*(Y;BSAfc,NNWA$[`Er4Bo<
ka#j2??36-chMh).V3<UC5>8:,V*58pZQ9?p+6&5i1RY?5.gdCp>?5d<n2Q&+Yq.$GEZc8;>
86GL!/>CFpk`QDnaJ"."OB.N7Bq=+<b.!ai8:e[J%0/BMYh<*UDk!cb$R)ZX6X%m3lXTY4HZ
cGIeMjXGfGrZbq&m#.)7'3ofS(+TYSc!s<:6Ye&W(>PPN;)u>hL'aiX[4a3]A>7O!B=knYc;?
bs0l#nB;#hH'_.eWUC"5so`EeMD]AY/kqq;V2DD.qL%bM#>eW;p?Oqp'$TM?%U>ifg=L,Zf]A_
isoUiM]AiHB>S1;merJVDhTF5"(q<'Me/>S6j%U$Mm>f'CjVKpCEH;NS(\*3U?sZ7";+-9)Ch
88#rEI?S[?JoknBJ)B5un;<n\Hb:JIZg1>ZP9CKZq"'^H'=(XV>og]AJj__378,fJ?XUs@hON
&%ZjO\>/G<PQ!?>r)0D;<KtrOYFQSt]Aru7!de;jJHM`o7HaQQ&Jqn^Z3=5'ArO26R.XB(9ou
(L2\P*[8.$6CJbl`Rf>Eq6,%6Nb\/#9#Q&qpIabsD@F?-k_/=@9Ve<[aP6i^.qbffHGQTCKn
Z"M_I1224s7.W>H5R_"^,92q6-)5sb(%Uk>7A$]Aj$k>&,XY;'h>FuHL?%uU(Ab"8[m$mpQs'
gF4-6p16:d[#)FOr]AJm=MJFU,Bb:7hQ&&]ANMc1l;3UA;Upbq^6GDM^T+e.PE$9:\X]A?e^Un-
:^`'Kh13OH&'UtXnqIf6IEErKiKu!U]AAnT]ANm0!PODr/3\*OQQH)8>@LDI]AE^R1Y22f9)qIo
1T(p4a+6&7'^;)C"<L!0W9!,3e`1dli`mhXF:=-iA6oTJ@p2i*7`?J+@KD+'qM7>AWK7/6:H
l2mT3NM[S(J84$0^-N!SMO[%CR#!!@!^#a4c&EF_"'R5[$<RfQ@W0chV,673[fA$#_WJQ4oK
9Pt5GE2),1F2#<aG,Q>cEp;N_$9pNV=(JSDdOS$mlLBB41X<"=kbn8kH@1cZ[Sr%QU4Cd6fI
fnNOF7c`D9K_*p*-F:6.#2Y6e^2SDW^<nMVj?;Bo^(P`G"Rft92q:A$6#\[BYBa#VgC^,c(J
MD^ZP4s#]A1p2-j5VVB5'IY($";![J^<p;#fX(DhD5%jLJVQ"*I(Q4l@R$Ka]AGIQIG'']AB66>
gZr<%Il[)LlO\pHi.#oV)YQJ3]A_[+ao0D[/RU>5TT.8J]AuP3e@!#sXaQ8D["$M:?\E!Y[no\
eUD5[tWU7Ot&!B"k>*,%V!u*PapX+Q3ETH>k_o()j`&%qtC&211C!GFXC4CX1E:;]A)Q!oeIM
HMAd6<u.[*<<mngX+(b+;4X*EQ'l"G:+Kn==;Hnin0=G%=[4gDmp:ik?C&iU(;[;`0sX=F90
FRhb4knQc$piMTC7/IQb_pW'4dCh66Fo3GiVoEQ0B_QO:?Ircl;^.<A7[aYWOHYY.tr.K[fO
dqemteFW\&gL[KmTJbo17Gb4Gd^/'))>k(`-NTQ;a/<YC++mCUklIWtTI94!pFLe$"[GNS-@
.SX3]AUF]AH)c2T8ppP%'Pg-\jt_o/@+FmYS6(8>3f=4r5^/6\C[Uh[\^]As?HM6H+#3RtU2:d\
!-c0/D_Z'lL)5JWNi=7bqPg9l^a'ZMu@U`c/mKolsI&qm*r5u2&k@&)V@0Nsma!smh3Up7M:
l<SJY')ofEm!gR`:q!0\<$-O>ZImU6=!t_XYo.]A=s#-'r.3n"rJE(RHKf(Ijrhos/%^<C(\t
q]A^q+8tF7j,EZN#Q@Tg)%(dBu=Uk:e2$I'"J,7s#[^1^D+NWq^kM/ape;Q)c,J)ZQLr%Wj7&
:e?ddSsOE)+P1U]ADCJ)e>%D7KG)1F!>o1UrOr+mf!dYS&T^"iQ,e>s"Il\23@X"FLRBBN#*-
sq>S#f&1-Ma+e^.n;LT3#fU;(oA2jU_^!o5fNc.tfH$%Kc'Gm9=t46CF1,oIBn:&[&Tmo'JX
g]A.9i2VP'#q(&0_[":lF3(9R+RBiSC#o+3*+5V+R/nZ*A*_gh`i[SW,LUcoW,BDKFPFDP=_l
Wk6MYLc!8NpAflfKALao$Z!C6o+22\X\l5EjK6;9l-O&mom(=^t$4RL;U2o5Ys[T3f`EK4p&
>4`b(Kja7"^+]A-h[E8<>$hV1UXg3(k5F/oT.BZJKe'6doV.H32ITkYA8jl^Y1#YChh>YO#!B
`_R0Vmh;=1rg=AZZOqnp\VreTP7e3DRYK5h7r@-(eC=>t]A)WEG"Vm<)8D,mh#be2Q<#)hc?i
ZI0YgBER-,C.E@"F;p8s?E0J4^%K0iSMd#uuj+Kd\2PU]A?NF#j%0+^3e1sZ[Xe*c8d]A<+.68
=H->fFDe8'6Fp/%P1F%2mR0IAV6W=TSi8'aa=b`=4Te3ok\Y`NWd3kCsnduNn"lAp0&L_esF
mR)dMg+ZiPSoZ0UFC=Ke&?n)D!0agi"g$?TRtL7KFB,(N2r_Z,d*SlNjkY7jeEm.:EbQEh:$
f&p$e$eft^A"eD$-h$-m$bco:Z`2jL).W+E5nB==]Aq\E(+Gc!dqj8!K`(m8q!(W'RH1hjut7
V;4;6=8C^Op86iRklF6*+^?TY5(=0PcFd2Y<+T:nU7W1lM]A#!cG.T0Om70:=^qpVp^Tr8m[F
]A^rYHeA?J%U7)/bA['B"8,&ffO5l4mr_iJ3I>'$$?.#O(T)*2=Z9L6pKV[Y7L_Q4rf$ke+\J
AHpkdsShjo3ptASC`m2O"c\ClCdICrM0V9sUAT/eJei-J[J>uP)dZUh5?;7c(fc"$HrL"<>7
Q#YZ)<#qH8>_:77Rs!'?&%SRPd(q5ZDN"9726"Uk4ep2<l<>jPefR6,>#!u^sXmB#P_LRSa7
r_D-FNarhV&2jiGF\<d^@(8Z&@&jt&G8^/-$Ud'h6Gq=H-9ao_gMlq5jX#2]A9pC7-0B==%)c
!&H_7+sMd-1s6N0MiaD9q8=pc%^>*`K;luW9>4S2W4u?,#i^#"^Kd&ObNuXT]A(IOIN3rFB\7
ON.\%)qb&&bd$KCC\9*&PGVS]APW)VBT.m8ct+E`N$+m^'C\>[Wd!)>`IT:"9Gj2LW]AkIfa[%
S-0#='lS@5tq9CQYTJb4gH(mFP>T=`CCu2.qY97X(d2ns`s5blfh'8o/Q]Abq@%JRLuYDdSLM
oib1Elt]A9nX6L#IQ`OA/5@,!VG;5:c+UY)1A5F2H<jJ3?g;Cmq5hXTi8MK/1Gb577D79VlWY
M0gHFS"Ja,8@_e*@gA^hG:7'BKaY/a@5P`>GPj-Q0FlR`r,D$X6iVo_T^hsg"8"-<!feDn\5
3d-:HjffJ/7ii@cZ<`5/@c[E-r?o*ceXW[e[aq+2s4RPB,K\U[g^Ka'H*?N<r=%b6%=CBfMT
Jc4Ilc3'<*ILeE>^OO1c1*A?>tg(n+DJFo=4l#/DjDMh3@^Od]A0@ipH(hXnd`5B.>F3<oAer
iEW!.O<7C"6Bl\PQZ11hRbMp6YnI_9#NGZVFfb+&DRZjJTpc&MsS[Chn-7PF!aKlDi]AmS`%j
rGB?TJ;^O0-HM9`74Di`*DB&Op!hn/ZqK/h6'T9joe_nZPa9=+@QGmO*8/,bRb'Zq'4*k4Oj
`14![>oHqB-OeT1$l?=n7_<oAbY@LaI3Yr`[Xd@`6ei$.OnlXZK,V4'r)aaYqu!TJrL7rD36
pE5CtA+?s)i_R&BE38cOPJ_JQlHtInLd]AWEF5g=*F:qUFo%)fc%FOd^d^nEJ[l/@lB4JhF`G
(5]AfNj-:CQPB."9#o[1N-NIZE@nU"-"&jTdq3[5amE1X1F_,!(Ep&5kF?AIbofri5QhNr^\F
ZGUQ=`0#0ZF,.N6I9LaZ>>2YI%o\RP?T+b6L>8,X$]A:+TBRRl'"PbqY[lounU0]Aec=.,(p[B
9MfF#$jtkh6WGNJM"FX_o#r3_,6,uOWL1$%HcHDX+cmr^/Iu02<QG27k\^:=Z8m95C<$+mSS
f]AhEIG?mdmUccGR'%nOA37HmGqL3=@!`3Tf<Jh-($rpB!F*eKW&5V%tB/`*=gR$M+-JNqEE<
C?Im*e/16PoHNbNTrRTZ8t'5]AQrs"Apl#.IaDCT(2,W\Y\t+>]A9="9re)nXhnpMarY76<)fl
ai@K*TNcc\Q(Z7F\]AOB;8qVWbYIuEs`_I%'@7Y8/F?#"o.N`(#e.9f/_1![b>Zag47Z_Mq4/
hD#e(Od1W&rLo61^QEl%Aa4)[f14SBGBkEqV8DF^A8Gm$UEu1QBQq):$9Adrf:Hb;^?<e!%b
KKQ!>6n(p+c!IWF'[20^m'hEElM2^oXUU0=c=+KE\XJ6kJ@F'CKt;Ormqih3rK3%.S#HNNAO
X:Ph2d=FZ+V`dCI2$'3CT2_Qbt"p.?<[)2]AGS"FQ4/'"U(@pFZ@Lq3;W*EdO!.7:'sfn^"T8
A"K:.*oVF,&i5U4rBk!Rl1fj5Ci/Q3p[M0MNZg`U&#Bo-qGP#=FRB^?-VAb\4+eIO"%)H1*A
Y7rnG3;B)!Fju4'gd38-lO@p2+#$X8U)m'J-cue]A]AWgs%`IBVB9uLGTfubntjG=o3A7S):[?
#82f9s4ktN!!RS]A5Pq/L(:@&jQ,r1k<4l<na.Oj/]AChEspd8ip51q@)K>s-$DGe%F7k;L9HN
H#neku[5!+%m,f^gDV<4&H]A[9EhhVNgL&)C20*s3`u1Hq=N@F/`"D&",ZfU6XbH#^]AQ;6=E1
aq'[o`Np@p;Zs011F:GOqro8NTo5%_`':T#[q2aSOG.K5FhN"-Whn2?^6@,0IkJS&_Z*]A&d&
M6_p,8i,Xf_iRS<O)$k8g6F$979A\"FssFo+_'iTfR!+-YM!H7]AH/]AJF)as8`r9Nb\Bb1<V)
m/*F\-CDO]A+okjYNdbHU@kTm4PSqS=n&%NNga.I]AWRC[Vog@:%S:t0OU>O4Zdt54C.j6TP(U
^D_,7s7)l-`;S"Zp<A5c_WB]A,rc]As]AC9s7W2@.V!:;FXa;2Mf@UY"6-_7`)/'/LcWTj0D3j;
r+Rdf00@lL&.%N6M5RlJt2QY,O%)"a*a`C/Z"(@)Y()8lQ=c.eAs:*4hI*+26>HRglj_V3*p
jF8uQh*L3C]A[&:@Yq2LDQdei:4sKj5-5bu[g\n?_V@8U9REF'(*aRTI>Jb'X%6-?h:p\"?h8
edA6T8a:EkkMPNE,@u&t[6YT_&J^dT]A&O:O.$45#Q(REkm+?jAg%FK*P$OfLH"P\uJdip5VS
_a:);;Ibc(qSjiAgjUA+#WJ&4Gi5>X44);5Ysp@e.!A3LQC,@88lrlKTnO:3i=f9=U`?YplY
h3&;.,(g@`;WI?7pjEhb4/T*AJ<gSEF\"J2!<?EO\r>BHIkSO4d:+G[n)uEF77:jT=QC)5aP
+-nbmT`0Do$Es2gY(mJCZ=ZWHI05=VC#r<'_-(aB!*h9F3\9(2(5YV#-[?$K@R83S&Q[$"P0
usQ62.cbZr<V1+0L.R*G-YTMOk/$q`k1I)*1('p5_McjTJkRm2)DKDR<tqC.HnNGaQ"q/tUj
nYQX1,+s-,4$q0%0fjG&o!;'FMfd!Fn?Rd)@c-cjF4U/mckf@4-_k4N54OsAm+A(G,ncB#BT
pZ6,GusSj!F%2O04Oc1*eM&9B;pY"#I3HJ=:<l8AP/!K"7?+eAC(_P+8.er_$ac=*'Rn?JH.
@<c4juT/Knb/O(gPREK/NE$!!b(K115V/C*C>KV:7Zqj!K=Ki&+ZpcE\7H"n^M2%2th)b=g/
g"urjdLTMhZ?fLH\%huUrGHJPh2eJ%su\a+^k2"K!r^g!TOY1$]ABo\`$5CFG4*]A1OJm8!-sp
9"TX6VH;+a=&q1mWTbW+]A&2">isT7XRFlAlDtAo:mqKVBl5@1Yp<GS<=@`MBsn<37@[f3cnM
*#_Qc0?;k\PdH#fJKKnM.(`p]ANO7E%rJ7;pD)(r).?s*X'(.kH^bA@9P#WK9:lE'+mB`5Jr%
]Acq2(Ld_@*Vj35YaW2K+f5nP@+Srn.[<^1isoN-PO`r!?LHmkUCMX^>)Xj\Aj<)dkZf4-e5O
=pRcU!L]Aq7*a,I-2JB?o))FE?",Jj$[pc@k(N.10"gA/Y0:DSBndpDrT_p4h3l3DuCKg-!Re
3+o\G%'QA-e!#hRW&gGqLPJ.=aKsI]Aogh<[`spk0r^,9*DaJH'?>aGgh%ID5d:XBI(Yjtr)4
i:rYcl5pZM:k"Oa9-9@%m)-4qVR[W60Y!F7H@OT>AJn'/E-+?n"-@MjDd#265CjhhTU2pYc<
VS]A.oT"AM2"qh#=JtR-LY#D=X\*,dA5>tmD'.u'qr,8qTN=-D2L-Y?eQ,??Gf%nY&f(=f+kb
)@MmM;A)KFD52H-b#2Us,/[(+S!7olWhfgaD5V@ebXjJY1N1=RJ?SY5e<&3Qd8[jjeogN#5Z
a1FiIj.TMfc]AE_`39AV5U&9&Pq?Z@=kZR,CUm[u2X5W]A(,:-\'Ld_<c*=Rm%0@;TNYkHW$hX
BSi[Uu#'eOaM*\Ua=4__.!ES4-QNfhbLMD%)Ji"Fd'BldODAYN^,q$#jm>T>[345FgNJ'_j?
PqcBA$bosfEqS^HDD%#kH8$fAnFenfj>TC;":rWA,mPL`nD4Gug88(>rU]AsaemqG)M*Il-`B
Qu:ohhN]A;4(RFC)eVReHc\Z$tQSq'KI'[Ym`$6nhaiO@Hp1n-T@BPj25'2jWicuZmY'SN^RV
8plj#4i!265@'8ILtU8PC;6;I-sdCDL.Hp_*Z`k2iX@:pun"et_%mM&eGiSW`;UMO(0K-ZPT
=@aogl)L22.f$;9('85##VBpTKkuKC$!V4Kki8ju8r4K+Gh"*)D%4047e9;T'*&:PR'D(gL`
XV2'HR<qBCq,7(1<U!'/1,5FWnJY=;?',=/jP;-[L:opCHW\sbp544N[`]A->0:&GdN_EAKa(
gG%-bE+9N:Ise$G9Wh?AAF9Dgs3DG@sX*Y1%L-;fTd3r=%o2gNKHYEZ(q]Ad@VX<Uc-@F8fPM
OLmHf[VD-TV"=Jb(26m9Ohq%,SV<4Z:O1,\3Pc(HDtdf`P#0oD&r"AqQ!Bc?dOC77U_]A(<\G
+H&l.TISVkEHr`7B%B@/WcUZU_:AOb)L><88Xn[^T;F<B'%D>:^n#K?W8lE1G1=,Bn[1MkZd
5BW-B&_2#)[<1^#n@BErSf,jr4:"2Q,n@_Q6-O2tm(G9ha]Alu/fHgQT(e93rF!')bs"f*&75
&U_ZW4g.e/Sl/rY%XOhEp^*3VJQNcMMBLuosBg(Qhp7K/ka:$O5B,;gb!ra/b/ei:G*kFWSo
_$C6#RU!,@Xsb+oH:f['3FiI/7+@%idJ7i&_toEs&UO1CJn<"\86mR@41\Dp%in<qaufgWH;
POk&@]A]AF_oL\Gf&C.hjf!(a0i.T$f[,(nJ/Tk04KBX)F<eJ"`'iGFMa8X0KPYL?WSGHC:\Zc
'R+rgm-SUoZdO_O.b7YWkacJlKsTr$nOOEj/e2-0bt6l5o@3edM*E\pceG:s9'ME6&>41S,D
ENOPc+ZFlWYN@Hl/I.T(rlPXRP]A;<#@=,k,Cq523%6p-2/K[W#[#(qG#0F-Korm,NG\k2J@F
0kklK>2h.eW@@UG+7'3_5(+OXX>_A6eBo]A\@XJa[DNt-&jpY"#4Co?KCPq%jdiW`C`onEpmW
D:aph?P,KG&p:c%nqI>Ud(!bU:g[Wr[[4^qEPbMLoB8CrO@POtTQjpC?+pmi\.RXA5&(Vjol
d"htTB#TQ.O&ejglUQALI"+m`rS5_8,5uOO7#LZ"4Dco6TD\42r<s;dWM:[.8qLuf[<m&:kV
7NKagI9@"nb+e5g4KG(VRpK6*oe^)s2)DrUX72C-K=IQLFQP8YH[,?p>W]ADAO1#P8<0>kuO(
)oZb>m/esK9G,KW=mH.=rb_C$s_[!;V5#AR%3KLr*j94(TbW\rE0Dul%Z6JVe.Y;&E_!@(UT
LF$H+&.D!L2<n/NmFktGC<4%q^DP=_%8[<'$*5#Vr-N?"G1H-!GToI_jQs;Qna0D?\r"6?`B
b\CIHg^/>@F'i\bF9>'L))dpH"4>V$9`)WVW9:MCdT5MV]A%S9-K7RH^5OIAHPEq[fZIWB@G]A
:/Tmnk]AI.DBMf<IOU'o2SQM7m-@D=oA/jbAg3u2ESeh>89V6\DYNY8b2`,%eZ[m+ilU,a%Mt
J66+`CT<FoLd#=6'GMdou-=+P?M&:V(>12N$:*:`7/(g?188"AK*:oeC"RlZlXP-A:NJ7D^d
<hmOJUS;+KH7TE:f=*)-eL!u*:$qlAkGj!g+QD`Q?Y;`%5M%kd3:fels)rjm:Tp&<oB/aOEl
L?R/%FLZ.b1sb=+!g=R#/O6%.I'3+.ar.UV8Cr[[!YSZI1gG[6mn6WQ8(\Z*:<W&#aLKuZI$
$Zgl#AZ33UF`_ANi_XB*i.p9hV2IGnc"d8r<Wg#6\mk03H!.qj07Jo0BKB-]AAm4mon]A&p@kG
Wd.dBl+<KWZN<^S>dl'(jhAhKF?*VG6tc,0J=*O!AlQl6FZ80k`r/I,<kc&9cE$\e412#(n2
he[/?b4uiq\$2rNQfi,q83(=*FuP;6EKM`B.#`0:18EM:"'\M+4-sXJj`XTau(Onecqr05VP
Xb6iRa>#>B:,,b`,80?FHX$f@pMoHk^DN?1p[$9$9m0>`.OO6oKq!?(W2gN"\UPC5SV4,V.G
P%MS?Z3Y[:hcq\`*lU!h!KA`lY/g!;pgl4jcAi"Gqkf]A7cJ-p-u8-`,"TZ%Lk+84oi5X"-Q<
(ncXXUI7:3p\ehrg0j%sX(an6c]AUU>HYN?M]A/EUNp,pUKp&eBuTh^bXot^oB(W1tEKm('Zun
;ql7G17:-s/+;&q`\?]Al9Ya19cgMG,g?lT;pVcp8:YTkb5TL>nH#Dbs@FCFKBii6L=$,r<I%
#*@:i,K7<0"njkioce?u6D$-t!;b?S5qoc+2LI,a;3f$P"H62q3Dqoo`Y\*/d(IIrmRPSaB,
E?g/Z0[YQVc`GXt"p//g5cHM1hA9l'b;e1@HMn8[Crdd<d28Y>EN=$-X`.AKY?PX4C27<`BX
7eQXPuU>B%)I:5+6EZ#a0B8Pb\C-6i2;N)YiF*0a!jpA#/1N77_s<Zo:/%Ld8gm_iBo*oih4
'"1"#Tn[Gt-X@f4p1Y3"b"L_?2MhRX1VG#Hu\;iCKO4Xe8Jf^s3?,B`/L7:D\@&29Bp<7()`
@,seD)%M@qkE>/T0b4AY5fQ%r<HRmVleKS"mlESjH\^=2K<:$Rr*@3SbDA"V>;r.Ogea^ZYQ
,F"JD8V]AC_G,Bk9*]A>JZ:R1F"/;j2'n2^W]AL(u9erLt,$QLpmqGa1YJIFiC8M@3_ICWlnWO8
j=Z+0SOTZ#oK"4SIE0lpP0mt@d9))sS6OsHdMWT^I.Ssh^.%AUOa9p7A66O8lj'bgc3\I_++
,XWDqmeqoMH'<MUQ1[)H&,p2/fGXC@RBRpFfi*K"oB6I@`_V(fO=YP6<iKlG/j&E,0k\V:]Ao
\GA$f+nr3JRABsUgg3_oYLk+mH^r(IAp$oMS,8V?s*3+<=n\!^?a1N`Fe&gq<S8[33@R$t"!
WpPOU88ZS5+EUR1]A26nkenKo'5,]Ar5G0%:[OqO"i_6)f7=dtJT2H*-GZ#i84jun,3SONg15u
,2M6=;0/cA+tZ%iuOd(+02)kOk4DHRQ/'d_U,n_sF1n+4VR=q$9G9CdnO)0L>DMphO0=CpSV
)-Uh4anCr[TdE<1UGihi!L(>)$3SZ%;A.2_%'4i[sqrT0%#g2J%krWbF1uQ0hhr#2sFLn?=3
7qmdP[+[RP/a,'.1WTbT-h<'EQ9`DT(4++n_:Y/]A(!7"<J#1Ld'VjY^ns=aZCR0#E?F*oMCq
b]A@-S;CZ=^5#ipV`fdKs5)),eomJqjJ<PH:rf.k1oE%(/K*\6hp6e?+8//mM/mN_<NS<rh_o
M!0\+/PXp9['hI>JK6?V2#C/F%?^<UU0&!0+lXkY,EOD^>KO*T\D-VEU9"?2X/gPpP0;/FM_
Y^dkV!.VY:n`J0"`RG\kj%pAru5iWs8c'89a.X<JgfBFIXcFK$>UXE.MrD@uq@nd0i!>3Y'_
D=a2ZHeQ/T:22Cf4P5NdMK<Uc2]Ak+qQ*8Eg`+dq=Z&L><^VG>#J1N$9&1uSf3WCBHhr.H-Mm
WQojF#&miib]A5.5N]Ab)APi<oSu!(]A77+"Eck^,PB/C(,/i]AOt*Q2ed`V&oE0#\)VGRrM(7Ga
%RoYpd)[8XjXEq[%kntPWs.MaNmE8$@4c,3Ifl>g8ATuj$1Xu'?oEaicLf?A7i"NUR"*@><3
>]A2"F`8G\67,H_U*Xo_=kjZan=i^r^>pcIcj^u4K[HL9^d8'4MaD2Kq]A1"r4-58DWU,,36"6
WfS7M3LS/<O:n_B-#p*^YjmaYt[qGBb->j#DIEE^K%d$]AuA%j-"EB<=^o7Or&I5o.=&,1K.7
iT+rmf$eaKVD3aHCqO7Xfmf0MAf)<hpb5%M\oRCXkS`72:`!I_qTuPeA3UltQ&,Xf@KWZd;U
F[ZJ]A>+=MXl8)Y4QS74p641kfa_Zd5*jum^E_P.hX8nt]A$m@j$[OZTmI&<(Nr2K>A%,Cbapq
'm"Jbj</u8Mi\Xu\R'nZD#IK]A<]A%JBB5]A6W_3WYl-QF1^J6I_X9q5qlb.CIk@<ZB^DhJ"p4p
?c91Z?:lIhGRH:o@VU]Ar/4n.'Mjr?'@1P!1U`H,B7CRJ`'n>Qe3n@3Q/C4r*$9o5=.l`Q?EW
.4dZ7]AE/osfBS?nGsrXuFe_UrmP]APb4laLP#hqq5dRGjKHmC&U.a[[mdd`a^IXd%>BUA>NW0
FTB.dm.8,:TYT)#$W/V1KNC"jbR>VE)i[>s3)+1Vr?-S>X@uS9l#*N7@NLg`*CCOcBU<AH_0
7+!#&;_p0Uj<HDb:$E(\O'Yp/G6*c8J_u>f!laRe.0mPD3PC$\++05bt39iMUb_Tg,Z&TRW_
:[Xkqk*PU1@Z0T(RfUAdAr5j7S,k8-%YP*`1CjlFpPBMiQT-Ph_IMI?_1mh$Juqa5f,n6>"W
`MXE@qWIO_6EkXZQ9`]AiPXGq5dH1L#YZdeR9i`Pc^Ma3un/k$r;Z$G3Vh$qVrJ3r4(?:h+:E
"lc*bO``mRQoNj7;:W'C1*WPUZPo+Rcb[5d.k*W'A\B)gl:9nfK)JBBA-8Xb5cc\Mai0hGmh
heMiM8HYM`:@unl,5HRZt2Ce$0a[sG\C.J2W.?7=e9,TGgVZ6@;8]A=edMR`WB$aH:@K%Ns[^
$bnu>=K6Qo[;0FNufaa?b$)r@J+0m_K+d1,Q(;]A4<kuf=N,ldKDt&d>[TM`>_0^gQ;NLc-$U
:)4`YITCoR;\CC]AUhS,;!@=XilJ(,e_^X#7F$P+4K"@uHTNjmi7sB$.kQrXZ`IS,/B=0D>:8
G5HbKb3VKi_S/g@a4:N9NYkq!hcMRn%!>Enqk%0#+#3W^s4Ji2b@8hmmPS>aBB[4]AXXqe#PT
IRVo3V~
]]></IM>
<ElementCaseMobileAttrProvider horizontal="1" vertical="0" zoom="true" refresh="false" isUseHTML="false" isMobileCanvasSize="false" appearRefresh="false" allowFullScreen="false"/>
</InnerWidget>
<BoundsAttr x="0" y="0" width="685" height="269"/>
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
<BoundsAttr x="0" y="136" width="685" height="269"/>
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
<border style="0" color="-14669005" borderRadius="0" type="0" borderStyle="0"/>
<WidgetTitle>
<O>
<![CDATA[新建标题]]></O>
<FRFont name="宋体" style="0" size="72"/>
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
<![CDATA[515500,515500,687334,1497406,1219200,515500,723900,723900,723900,723900,723900]]></RowHeight>
<ColumnWidth defaultValue="2743200">
<![CDATA[515500,1914716,2880000,515500,2880000,2880000,515500,2880000,3313932,515500,2880000,3289385,515500,2743200]]></ColumnWidth>
<CellElementList>
<C c="0" r="0" s="0">
<PrivilegeControl/>
<Expand/>
</C>
<C c="1" r="0" s="0">
<PrivilegeControl/>
<Expand/>
</C>
<C c="2" r="0" s="0">
<PrivilegeControl/>
<Expand/>
</C>
<C c="3" r="0" s="0">
<PrivilegeControl/>
<Expand/>
</C>
<C c="4" r="0" s="0">
<PrivilegeControl/>
<Expand/>
</C>
<C c="5" r="0" s="0">
<PrivilegeControl/>
<Expand/>
</C>
<C c="6" r="0" s="0">
<PrivilegeControl/>
<Expand/>
</C>
<C c="7" r="0" s="0">
<PrivilegeControl/>
<Expand/>
</C>
<C c="8" r="0" s="0">
<PrivilegeControl/>
<Expand/>
</C>
<C c="9" r="0" s="0">
<PrivilegeControl/>
<Expand/>
</C>
<C c="10" r="0" s="0">
<PrivilegeControl/>
<Expand/>
</C>
<C c="11" r="0" s="0">
<PrivilegeControl/>
<Expand/>
</C>
<C c="12" r="0" s="0">
<PrivilegeControl/>
<Expand/>
</C>
<C c="0" r="1" s="0">
<PrivilegeControl/>
<Expand/>
</C>
<C c="1" r="1" s="1">
<PrivilegeControl/>
<Expand/>
</C>
<C c="2" r="1" s="1">
<PrivilegeControl/>
<Expand/>
</C>
<C c="3" r="1" s="0">
<PrivilegeControl/>
<Expand/>
</C>
<C c="4" r="1" s="1">
<PrivilegeControl/>
<Expand/>
</C>
<C c="5" r="1" s="1">
<PrivilegeControl/>
<Expand/>
</C>
<C c="6" r="1" s="0">
<PrivilegeControl/>
<Expand/>
</C>
<C c="7" r="1" s="1">
<PrivilegeControl/>
<Expand/>
</C>
<C c="8" r="1" s="1">
<PrivilegeControl/>
<Expand/>
</C>
<C c="9" r="1" s="0">
<PrivilegeControl/>
<Expand/>
</C>
<C c="10" r="1" s="1">
<PrivilegeControl/>
<Expand/>
</C>
<C c="11" r="1" s="1">
<PrivilegeControl/>
<Expand/>
</C>
<C c="12" r="1" s="0">
<PrivilegeControl/>
<Expand/>
</C>
<C c="0" r="2" s="0">
<PrivilegeControl/>
<Expand/>
</C>
<C c="1" r="2" rs="2" s="2">
<O t="Image">
<IM>
<![CDATA[!HeO&qh\-E7h#eD$31&+%7s)Y;?-[s2?3^W49u,k!!"V-8\4s&"?]A7D5u`*!c'q:<PZ\QJh8
KQF;&#@:6^]ArJoV<lb0$H!V/r7#f#7mP8]A\*8Akp-\ELLES>71V!U_2D]Ag;8g?\l9TALr9nb
USM:8+TI,KB_lNh+Cng,X<IYe4U_>fFn%J"<Jg?HGqRVto<WDA^UGU/:)30cUrG@RFM_P_`4
.^3*T9UX#7nc0h9W4laq^k;@#Es9a?2+53Q^[cRq6!OqA"F$(_a;lCi%'EZj2bU[\,Crtab3
St&'gr$h1Ypl<<;jM\mRNW:F(crYRHM;=V=Q6#&s[U=J;7L^D6@[f*Kpi\aLB`eP&f>!^eWA
*@_<@5@tY1>'A31b1:#9Wjf4NL&[&g0J(b^VP3kFKR-G5aZ*7r<#]AX>or0J#ZuIc._<88Cct
f1IVL>m-W.aZ,g4nlol(9X6jp9jU!u(1N+;d6"!i$*jPi6.?@-Sc%a&(e?qic3%0FUH]A3.0Z
fUJ=<@=B/:C-79M,.tU.B_.^i_*f^t1"P^>:Ol4U=`Z'f8_@2e3aU+8L%"9l3L/map*uNKHJ
Vq6^HtNgS$,7D]AUQU[noNUWh=L>)=p1IlC,]A3sLfEY?aNC&aQ_f-$5Jn]A!Dkc&G>Pnk8C,Dg
G8^h50*fQ^VOl4`FabX93@X&/b6;C)a'rCbrV$WmPpq$3YE[72QG^]AhsDEGSI"K#t\=_^8AE
'XZ7OT:72uHH$kQ+-u&d,'$7`orGC(N@Ium3,m=!FU7dJ68m3O3sZ$$>Qeb0]Ag:t#A!=/h+j
fNS3p*qpYW=Cg20:/k)oE!;G)]A$F["acXP8/?o%@[]A)2l/E1SgJ#l(54Rq6u<d$-)5cII]A1l
lE.ZXO6FC4XrC-+Cd=(">WU[QK7#5WCn>6`[hSSgmF7BE_G^GDMd3f`oE62-2Po%jNiCa,OI
8DAB5DDZi(Jl0g]A?02S>1#U"7ugR3\3]A]AKU1u/m7\^<Gnbn7a?s(aSm"h7*7>Isp^UXe,cu\
T>Bin@H=P8Gdd%5$4V`X&N&*9e.gkHRL#D-\WrX`lSV]AsauDBk'o'E7O7?r>rf"pUCO[?#s#
JZ,=lok$pDkb#Dr,udSV(fe0!"FSA624H*Rdi+RWV8ldXIgNS=R_<kj!coZXj>KK2_OKE[U'
m1?`b>%t[qNrro*UU3NG#g<:docOD2<A=d>_/ufP>@l[!R`aF%-t-bJ4r.@/%/?dB71cK]AV&
Tb&3#)`RN$=BW9o*[m=2jE&pS?_;]Ant>#[se:-<d?D-V'e;B;]AK&e4i!+c">+l%t'l8:QE_G
1bLlN^15?gDALN4J5Q0mT<b4%OV_m1n;p5LFtU9Aght)RtaZ02%MV\r.]A-qPH#1C!4th-$/J
O=7fQ,bK<OHq?jA8un8FdH^$L&8['-.MC*[T(rrHQ?!NaA[q\oM8!!#SZ:.26O@"J~
]]></IM>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="2" r="2" rs="2" s="3">
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
<newColor/>
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
<Attr isNullValueBreak="true" autoRefreshPerSecond="5" seriesDragEnable="false" plotStyle="4" combinedSize="50.0"/>
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
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-1"/>
</AttrBorder>
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
<Attr class="com.fr.plugin.chart.base.AttrLabel">
<AttrLabel>
<labelAttr enable="true"/>
<labelDetail class="com.fr.plugin.chart.base.AttrLabelDetail">
<Attr showLine="false" autoAdjust="true" position="0" isCustom="true"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="Al Bayan" style="0" size="200" foreground="-1954"/>
</Attr>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="false"/>
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
<HtmlLabel customText="function(){ return &apos;+&apos;+this.value;}" useHtml="false" isCustomWidth="false" isCustomHeight="false" width="50" height="50"/>
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
<Attr position="4" visible="false"/>
<FRFont name="微软雅黑" style="0" size="88" foreground="-10066330"/>
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
<OColor colvalue="-1"/>
<OColor colvalue="-11184811"/>
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
<FRFont name="Verdana" style="0" size="88" foreground="-10066330"/>
</Attr>
</TextAttr>
<TitleVisible value="true" position="0"/>
</Title>
<newAxisAttr isShowAxisLabel="false"/>
<AxisLineStyle AxisStyle="0" MainGridStyle="1"/>
<newLineColor lineColor=""/>
<AxisPosition value="1"/>
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
<FRFont name="Verdana" style="0" size="88" foreground="-10066330"/>
</Attr>
</TextAttr>
<TitleVisible value="true" position="0"/>
</Title>
<newAxisAttr isShowAxisLabel="false"/>
<AxisLineStyle AxisStyle="0" MainGridStyle="1"/>
<newLineColor lineColor=""/>
<AxisPosition value="5"/>
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
</VanChartAxis>
</YAxisList>
<stackAndAxisCondition>
<ConditionCollection>
<DefaultAttr class="com.fr.chart.chartglyph.ConditionAttr">
<ConditionAttr name=""/>
</DefaultAttr>
</ConditionCollection>
</stackAndAxisCondition>
<VanChartColumnPlotAttr seriesOverlapPercent="0.0" categoryIntervalPercent="0.0" fixedWidth="true" columnWidth="0" filledWithImage="false" isBar="true"/>
</Plot>
<ChartDefinition>
<OneValueCDDefinition seriesName="result1" valueName="result1" function="com.fr.data.util.function.NoneFunction">
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<TableData class="com.fr.data.impl.NameTableData">
<Name>
<![CDATA[ds1]]></Name>
</TableData>
<CategoryName value=""/>
</OneValueCDDefinition>
</ChartDefinition>
</Chart>
<tools hidden="false" sort="false" export="false" fullScreen="false"/>
<VanChartZoom>
<zoomAttr zoomVisible="false" zoomGesture="true" zoomResize="true" zoomType="xy"/>
<from>
<![CDATA[]]></from>
<to>
<![CDATA[]]></to>
</VanChartZoom>
<refreshMoreLabel>
<attr moreLabel="true" autoTooltip="false"/>
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
</O>
<PrivilegeControl/>
<CellGUIAttr showAsHTML="true"/>
<Expand/>
</C>
<C c="3" r="2" s="4">
<PrivilegeControl/>
<Expand/>
</C>
<C c="4" r="2" rs="2" s="2">
<O t="Image">
<IM>
<![CDATA[!J:N&qh\-E7h#eD$31&+%7s)Y;?-[s8cShk6O3kr!!#+<PIUYn"A26R5u`*!m@6a]A'L<FfT0
"Z]A)iFNE@La;>.>iIK<,b,k,C&]A#lG\YmE'_Ep-n7^UTQh$\#`9#L5uA.Jh(pB=/eLId#VJE
;*eINO@PHnNeSQ"4&pq3jlLi)@n2$8>]A&*I0<HTnL6hI"(8C1i)d%Lm,pY<<u.XWWg6hifgD
R#'#W.7_F'efuf!_*2i^ka!ZOet<5TEH`7')/)7Vu]A,l5dbk*5Srt)<'6p!f(+\+.$:7/./5
>#DTnPGG.$</DaST*kJn$(<7*rFFqTM;jo?g!DMediAh6_Q:oHf]A;:*LBJGr<T;7Ntkk<*jO
hhAp79%#I7i/@<)*,<O[rb_`D+"W/?-DS[CZm2b?iMndS++.uM\Mc:^jnT;,Tdr#6o4uk]AH*
PFP:cQ?#X?l\7QO`1#W!"EKK6$0+/fZ*W8i0c?[Y>#Hi"YL=rm[rR)Y1??b,$jO:_)<@SA3#
]AomdL9]AE4sE5fET&JU5?B8iFHK&b@pl8dO^5"9)[3Kpb1O%otqqdVr5XStR`u4BMV1f9j32(
h_<%(!2*I53aA6XX]A?u^GSi%<_t4`(+F`;)k]A1KEAg>t4kFGgAB<k92Gc"HjRsZTr#rp]AL>(
.;Allq<5Gu;!AfCiN9AI7&%b.MM8H,SW:p"DS'=`IG$GWe@DQ.P(j7XE@j=&\JPInWt;bQ%b
mkkC9NgpPtHdig]A[97`YjZ8mc.J/>-\\2\f>e4Rbi"HPo9hpgC\c!?S29&887[U:a!N6%,BO
?kWQ>R@NplM:s0Ra-9?3n(sR0c?c6Iaue]A\G]A3\oQIU6@l21;1LSE9luC8'8^JhbFKGb!(;=
E;^6'WOqn4e9++`aQ_kA#$$6!j)DKZ6R?T3/R+VjQ2f!Z]Ac#UGqWgYPSf["%6nVG3&bW5\53
jSo`&)9snVGQS:E-i*0o#r<Be&'\c,s/KSaC>B4MbX@eEt]A1'Acn8(loHa1K=SO7K^+=*FFk
N,G$$W,=JPGj@/&<)F:G9"kl"Fl+N^mL6eBsV"B.*sS]A([\Y0F(ieY-T7YmkD_%#fsUL6#o<
C'RWo%76c]Am&%\CV4DcpGnX>0_r5C]A-f`)K2<'Yqj8m"83bfFp6O27<l2gS2BO<(PDF'\U92
!MpWhdc'k4Iqt),LXn*<U@Dou7]AEnedbC-b2'D@Md)M,9+'j6/tXhEnQH:Y>tFk.)eJZZQ%A
q&._;1)jG^mRbLqNJ9'iX]A.r,6dR=&,>h[J@9W&l1dLN5YQM3NFr$J2>?9G#Tk!7%8#J<,s?
H']Ar(q&:4++o:dK9QC2mb0_/#J.#)/[r-C(K:lmo=pjVQ<G2i:Wq?f5APe\$FSP0+1b3EOh*
EtgEeJgqj#MHFgFN"egVnYI434`b2[`e>:hcDn9t\dS<(G0:eO*5gJkof6m[Ir:dn%4z8OZB
BY!QNJ~
]]></IM>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="5" r="2" rs="2" s="3">
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
<newColor/>
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
<Attr isNullValueBreak="true" autoRefreshPerSecond="8" seriesDragEnable="false" plotStyle="4" combinedSize="50.0"/>
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
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-1"/>
</AttrBorder>
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
<Attr class="com.fr.plugin.chart.base.AttrLabel">
<AttrLabel>
<labelAttr enable="true"/>
<labelDetail class="com.fr.plugin.chart.base.AttrLabelDetail">
<Attr showLine="false" autoAdjust="true" position="0" isCustom="true"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="Al Bayan" style="0" size="200" foreground="-1954"/>
</Attr>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="false"/>
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
<HtmlLabel customText="function(){ return &apos;+&apos;+this.value;}" useHtml="false" isCustomWidth="false" isCustomHeight="false" width="50" height="50"/>
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
<Attr position="4" visible="false"/>
<FRFont name="微软雅黑" style="0" size="88" foreground="-10066330"/>
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
<OColor colvalue="-1"/>
<OColor colvalue="-11184811"/>
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
<FRFont name="Verdana" style="0" size="88" foreground="-10066330"/>
</Attr>
</TextAttr>
<TitleVisible value="true" position="0"/>
</Title>
<newAxisAttr isShowAxisLabel="false"/>
<AxisLineStyle AxisStyle="0" MainGridStyle="1"/>
<newLineColor lineColor=""/>
<AxisPosition value="1"/>
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
<FRFont name="Verdana" style="0" size="88" foreground="-10066330"/>
</Attr>
</TextAttr>
<TitleVisible value="true" position="0"/>
</Title>
<newAxisAttr isShowAxisLabel="false"/>
<AxisLineStyle AxisStyle="0" MainGridStyle="1"/>
<newLineColor lineColor=""/>
<AxisPosition value="5"/>
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
</VanChartAxis>
</YAxisList>
<stackAndAxisCondition>
<ConditionCollection>
<DefaultAttr class="com.fr.chart.chartglyph.ConditionAttr">
<ConditionAttr name=""/>
</DefaultAttr>
</ConditionCollection>
</stackAndAxisCondition>
<VanChartColumnPlotAttr seriesOverlapPercent="0.0" categoryIntervalPercent="0.0" fixedWidth="true" columnWidth="0" filledWithImage="false" isBar="true"/>
</Plot>
<ChartDefinition>
<OneValueCDDefinition seriesName="result2" valueName="result2" function="com.fr.data.util.function.NoneFunction">
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<TableData class="com.fr.data.impl.NameTableData">
<Name>
<![CDATA[ds1]]></Name>
</TableData>
<CategoryName value=""/>
</OneValueCDDefinition>
</ChartDefinition>
</Chart>
<tools hidden="false" sort="false" export="false" fullScreen="false"/>
<VanChartZoom>
<zoomAttr zoomVisible="false" zoomGesture="true" zoomResize="true" zoomType="xy"/>
<from>
<![CDATA[]]></from>
<to>
<![CDATA[]]></to>
</VanChartZoom>
<refreshMoreLabel>
<attr moreLabel="true" autoTooltip="false"/>
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
</O>
<PrivilegeControl/>
<CellGUIAttr showAsHTML="true"/>
<Expand/>
</C>
<C c="6" r="2" s="4">
<PrivilegeControl/>
<Expand/>
</C>
<C c="7" r="2" rs="2" s="2">
<O t="Image">
<IM>
<![CDATA[!UU.*pPD^A7h#eD$31&+%7s)Y;?-[s5QCca5R7Po!!'$5ES^Zq#dd/k5u`*!j]A_tO'3,mhhL
!<"$^Pc`@,8<6h(]A=i3f7cjT]A1ofF[ee6'mmd*g#UE\$\Ri25o`,n"@Zr;b:!^Xm+^=3*S_c
^<Wl8BIc&m*,e;_V,hZuRhoqRsc+`q%mskB7rj"\5'\QXo,rUVDZBq7hQ^F4a:IMOX$t2kj#
j^f4O:naT%F+0qB_"rHrm_R#.:*hM]A'o1g6i?CQI"!iFgGd,=G,RuSmTSu0J[AQ(Z)K23Vjk
PL&;&0CjB(:t;99;eQ2nGH,/V'gWUI^;JsKQI`qoJ(=N/Zmbt8A6*t5^*d,b)NZEpNI<>RdK
@.0,la#Og4T&:ZY0fKk_4h5=ES)O-6&H(^a"jcUWXf:'Aq_#NbH"$Xc]AYL\=n@)725K6b)9H
gSH>0so)k]A3K6!/0E`TS:T#J3DC`!+$@V>@O6c5muu3Ks\nmmF^)n!2:XK+%ZbCS/o,T=^B<
k$H[o>_t#3_!<C:"EKER4Z&rN,jJ%0YmkTPZU1n:MZZ-FI[fHO,dT6EVBn%LINJ:YujlaR1M
2e9V]AK[_u62aiDI1C%R@sFk"lmoUm3KLEIQZ&5=b,,31>PeYUYl70h!aNF<0"s^<2pu+7Es=
J]A?@XkpHa48P$2=3,I`->gBBXB/.@+h?2()[9J?_.5fB</$$NTK%O0o$&*,C;q;n4K#YNKH[
'Lfl>4ZPX?\Wd#E&k8'3-9_Y.CrGM7nbs+]A:0?1bH.kZ/qh,d^akbb7JX,-?d-P2rP.?*C(P
'_p'%V(a/$obFHL#S/kaPXg>cMpGa?BUq/p`G5oQ\S)0EBo&W\kTnq^,;:.89_AW[kJ#.86q
4BKH2EIRm/b8!@CPFfFmL;j4[U;kDosTj\="Fc.9LAcN+:s6g!XpCr-M#;'??0'"\"$*O?UX
lfa%1/E\MB_E/@]A#,d[5muu*4#oN4!FR_$[U(Q:kIK"`=?LcC6b^BAVVm\a^.G[PiP4kASsg
T6*ba+V4;(/J<?6YPZK-!b*.mnGd5eV,gqn8Dh&<sZ9PP%d0Wcpp*=\&?/%gD6OG(c9@HKJr
E4WnUI="b9L#a(U,dgaKD,2oWqCQ7\Y[7"ar+Oo\KD8`Zs.Z'g6?f*K.pHs9B5rj?ND5Ip:)
HOOV2?O4nf@A+*1Kn1;%hGE\@rtfk;.LW@-I;4/E$>dE;ZqL5^!.KhuQSN_nJ32*Fj6_G[0h
?JGNqHEWZF[pU_u#]AOi>]A_0rIf_YVD@Yg#$#$KmN8i,rgWIU$d;8Ipo_Q?b'1!BNgE%A8jpj
5t7s.VWAjTY*4"*J`+eQ1Q9,J>Vq6a[m%m9m,erf(NU^WgWLl=9-c!#%9^2T5S>YUaVMNBkE
"20E1up[>">,Nbc/TZC'_XWZcG5di:<u^4mDnL5BP#q0K2@K'M`ibS^U;I*TT(Vu8%JJ0MQf
/47%H#;3)J2g+G0IfL&29tW-?Z$\`aclLm"4U1s.4$EZ&gq._M/bhSl-T-FJ/=uphj'd>E3b
Vs6$*RM%k&BW-MCYW->Xe_!;?2fp!Sj_i-nBWDo)!7/ad?t<`b8BCN0^@YQ)Y'[!apanK48P
gf)6KG`qtN^:'+XBLXcmsWiPrW4UPs[e?l>:Ns,#j[tni<!"<fN[b?Nq^E^X,M%+uKWDYdk'
ne/r76!*:/O>Sae="'qnJ(a8kWGljD#g7re)dZ1&cg_]AX>KcKouG6tBMoL`C6%"oS&2mjXtM
/&3[f##bAC4]A6'J&]AY0SD3Uu7@%0dGF".0,ml!0E\7"$m[\`,O2ObLM.2^WTE?-fEQp@u`-n
3jtb@P"IMt7H]AEN'(#u**'t*lK^<cJdps1b/C^p`O'K/@0aFDT=+5oT"n0U._E8cYOX&=RSt
Taj;:T#"BRo9[KSrNaY/#d\QBMX;U(IrJG_IuA;_0,Ne`Gp$XN#pbi@<mu6E84d%A8"gR?XJ
Xnm/D5Wa(RE;I0e\$jn!kWClKDT+l<.5uL$`f!B*behStQ,-2Z^$r<)%Q+1D;4IKSthbN9^n
k*QVCW0sP%<QLgZ9+!RN"e.%qiU.8<#4)d77Fkl"p?KMD:XlUHi[i)To*4(Fte9e!!EHQ!8P
o.:i]AWFrf__NL7E)\qbRBHH3,5UMgA@8+s[6jLCVpJ#p(qsF_?k^is,Q0<TFmR!g=&t/o]Asq
A#lJfHhmaXNRO_[O=m_0ebDSMMg)uSDZqaQGRUY'8[_S44BWH<P*D)o#/F%m7WKMENn_u?!S
!Gj`p*pb=/o/H/-I39WCRc!e*1A#5!VOn+U*B`A5X(SaXi4.lE,h'AMsI(%@(\Wj@m3.9U=l
^c*C,#&X9k=Gh1PBYH9)L?P!51r<e;5F!$WSrf7*2A>T-Sd_fa+K0k%0W%SO^121mZ"+2Ql=
RH@n)\!U$2TR;SHIN=Qo^D?()Bm*.h"$$g&fInrT-+N<RQ@h1*_!8tgQeTqb+Z[,VVHH`Vbb
>,PM<//*DK<#iZkT+jK=M8J-\0=BMqb7J/k\!c@?4)3^Y>r/Z#F]A<u$.h7jNM9JsoXMJBUIb
&f(+#$mm;W4S*5k]ADu=hXi,YB:?O,*N0,IU=5G@,2\S$L.V#K=[%&M%g9N$U2f'$*DN3D)NY
5?X?6Y@;!tY=3-k-HlQOQ3o7SbdQ!=Jr/Xmuo$<F/l36K[U`=Pj,:=mp)MC8=5q^\%r1<NM;
m#;)mTn3X9u9pPV'S77;Caq8gnWqpUm&`/E+*6RY8:(6Iq<<cE*Y#;r*[.I[;q;%"0YBmqFP
hF\D5D(75gL4)#3D.ZhH8al/J3^*dJU3.+K3]A8\?"AU^K:,p@iY3:-:GrAKI="b$2rN4HO6a
\f":\Ba]A.Sk(HS/:D22V*bb\ib'hS2N'@ceEpR)o=.!!#SZ:.26O@"J~
]]></IM>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="8" r="2" rs="2" s="3">
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
<newColor/>
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
<Attr isNullValueBreak="true" autoRefreshPerSecond="11" seriesDragEnable="false" plotStyle="4" combinedSize="50.0"/>
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
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-1"/>
</AttrBorder>
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
<Attr class="com.fr.plugin.chart.base.AttrLabel">
<AttrLabel>
<labelAttr enable="true"/>
<labelDetail class="com.fr.plugin.chart.base.AttrLabelDetail">
<Attr showLine="false" autoAdjust="true" position="0" isCustom="true"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="Al Bayan" style="0" size="200" foreground="-1954"/>
</Attr>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="false"/>
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
<HtmlLabel customText="function(){ return &apos;+&apos;+this.value;}" useHtml="false" isCustomWidth="false" isCustomHeight="false" width="50" height="50"/>
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
<Attr position="4" visible="false"/>
<FRFont name="微软雅黑" style="0" size="88" foreground="-10066330"/>
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
<OColor colvalue="-1"/>
<OColor colvalue="-11184811"/>
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
<FRFont name="Verdana" style="0" size="88" foreground="-10066330"/>
</Attr>
</TextAttr>
<TitleVisible value="true" position="0"/>
</Title>
<newAxisAttr isShowAxisLabel="false"/>
<AxisLineStyle AxisStyle="0" MainGridStyle="1"/>
<newLineColor lineColor=""/>
<AxisPosition value="1"/>
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
<FRFont name="Verdana" style="0" size="88" foreground="-10066330"/>
</Attr>
</TextAttr>
<TitleVisible value="true" position="0"/>
</Title>
<newAxisAttr isShowAxisLabel="false"/>
<AxisLineStyle AxisStyle="0" MainGridStyle="1"/>
<newLineColor lineColor=""/>
<AxisPosition value="5"/>
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
</VanChartAxis>
</YAxisList>
<stackAndAxisCondition>
<ConditionCollection>
<DefaultAttr class="com.fr.chart.chartglyph.ConditionAttr">
<ConditionAttr name=""/>
</DefaultAttr>
</ConditionCollection>
</stackAndAxisCondition>
<VanChartColumnPlotAttr seriesOverlapPercent="0.0" categoryIntervalPercent="0.0" fixedWidth="true" columnWidth="0" filledWithImage="false" isBar="true"/>
</Plot>
<ChartDefinition>
<OneValueCDDefinition seriesName="result3" valueName="result3" function="com.fr.data.util.function.NoneFunction">
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<TableData class="com.fr.data.impl.NameTableData">
<Name>
<![CDATA[ds1]]></Name>
</TableData>
<CategoryName value=""/>
</OneValueCDDefinition>
</ChartDefinition>
</Chart>
<tools hidden="false" sort="false" export="false" fullScreen="false"/>
<VanChartZoom>
<zoomAttr zoomVisible="false" zoomGesture="true" zoomResize="true" zoomType="xy"/>
<from>
<![CDATA[]]></from>
<to>
<![CDATA[]]></to>
</VanChartZoom>
<refreshMoreLabel>
<attr moreLabel="true" autoTooltip="false"/>
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
</O>
<PrivilegeControl/>
<CellGUIAttr showAsHTML="true"/>
<Expand/>
</C>
<C c="9" r="2" s="4">
<PrivilegeControl/>
<Expand/>
</C>
<C c="10" r="2" rs="2" s="2">
<O t="Image">
<IM>
<![CDATA[!RCp'qMA$D7h#eD$31&+%7s)Y;?-[s1&q:S5mRYp!!&4>pYGlM"dV_J5u`*!m@.mM,srAsYL
ctH-%\Oh`/h(h40oS6=_g/I*g%1dOB?EZ&OE?oIHQVrDc[L'"A:$;@t1^n=gIh]A[GhpZ+1i]A
58q[b!_t^LmIIE,Qh&5UM^=03qBC99@Wk1cqP*=#CmTW[ueN'O&SZ5mDBe$8C]AZ=[^<KurW#
+I`u5"g@m>IA_tK*N@uG2Vu<4iUS!K=1Z#[6L_?/.Wi_03rj"noKkKl`bG[3<o4FE=G+jRGn
Esm]Au+tXoVnPcN@VF("FbbjUToN)MYrDlauQ29H^ReorS_@,g'06i"+i2gXtK:Vfbf?@djuP
B`$uJ_<4VP9\k_Y2rakLVS4uMAoUa68;GK&,q]Ajr/3r(;*<bb)434pSlVXJ,\H&<!H7%FG*?
m'6@X^#J]ATK<W_'n$nR@-?/0UHV.Mi9D9Ln0O>Wf]A;0"G?]AG4I9AsidX%E\0*_dYgD*S0!h5
^"s2#0+tR8d=s+[^g0_ko/I]ASlrB4i1;cY>?S5pIp=N8KA$WlAQ#/7NZL8]A?uEXo7hf;+P?<
B7/Err6?fA3iRG(A7Uj["=lf3B<(.+U2!gJg&;rb3ml7LC/[,:rUg!&_#mD&.hg!VmV7-kec
WocHd6B0uY.o+f$fgM(\U_>Tb_&*6na4$s-il0e9/7$c1ch9HbSsrd3H6k@k/,@Od!pR1"[Y
1[*Prcj):)gDaeb\ND#Z(^qh?B'rQPY\NbXkuIpT>[WOuX6l<u-K\eAD\Wcpg't,2m?en^?k
`$%iLNcE)M<1=$>1>**\P%QD.*iTh%Koh?W;,[]A>@\DMN/7-_<U"C.=NeYUYQ*B:0I45:oRK
iqEH,35+Br+E4Q6W\YV=5a^2q#=%rqaE]Ah]A?E38r%NW9u`]AbKf.TZ?N6lWF)%i&JR2'Bs+_s
%M1(Ir1saC8d)MCPr#+\u&@nCHK7KnAjSn:+6@)K->LiI_X;F1]AF@9]A2SOaFYa#*a8mLYDZ@
cYq"YH"#8&gb!eKg*op*@aYn#cLUX+Er;Pd[/$bS=iN`A0F=&nSe1(bK2P&;d;7$YX&1W)Ja
DVE9s&GVg@3nj7#31IS2$=+c+&[s%9Cs8t_Z-Ohfceq0-"%X"ZL*P%.":=G1J8;'n`=QKMAN
tS*4frQVGcdd1KPmPoPBFdW4:d76^aGrrcbK.3ddCW_JSi)j79ajb6'_JKBbp]AD]As]AJ7`_VG
B0\D&R[p>.;abp?PB4Q?\8!$8EosAF/;E&^RmjQK&Y9fVQ72=OE#!af4+g+o5_\XW\d4g.`V
)m0lE^YusQ6[4NQ!.r.D&((6ilL8Vb0fX-^!L9_8Z3A.'PHLO;Ra/,7I$0u=U)]A.q`'LWJl=
=u\LB0CjcOIC,8_JII?bI&<484EMcOt'8DRef$<&A;(5^/:oGF[JNr5V.@%he?b@1enGne)p
(d!#VoP2@9a;-5W;ZZFb7ugXO;9A7$I;F]AhU6F+M$_Fd^g*/?*7T]ALu8Ht+Jc:c9'BFRd8/%
9=*-)^KW%CQl_]A$coFfqu4fN3SP"mUOZ(VR%GtKN_K-lXBn7?Q/6+mW"sf-`jml-+L%rpkr[
I=pKmNpJ+06T$CJIn5IqCW"`G!^5Jh5-?^bRYPkO2fF-gc$uH_a_nNW.LcA't+[nH^;VuU*[
\bC$Wp!D3AMQ=oXa;W@'Bde]AXoO8BE"MKcHFo3M"D&j$Y;L05@?TCr7N<dj"%\_#`G#\+[F^
HGL+DnS#.jSt)8J'ON&Vbf30fY:#k`Y.Hq9ql_.JVA,BQr:+'c-JD?+OiL2->E*_Dp=A_=8W
.AE^25.%F.:aMa1?R1`IA(\Z_>bc1o`H;$[X8RMJ3JgqP<V4iRz8OZBBY!QNJ~
]]></IM>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="11" r="2" rs="2" s="3">
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
<newColor/>
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
<Attr isNullValueBreak="true" autoRefreshPerSecond="14" seriesDragEnable="false" plotStyle="4" combinedSize="50.0"/>
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
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-1"/>
</AttrBorder>
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
<Attr class="com.fr.plugin.chart.base.AttrLabel">
<AttrLabel>
<labelAttr enable="true"/>
<labelDetail class="com.fr.plugin.chart.base.AttrLabelDetail">
<Attr showLine="false" autoAdjust="true" position="0" isCustom="true"/>
<TextAttr>
<Attr alignText="0">
<FRFont name="Al Bayan" style="0" size="200" foreground="-1954"/>
</Attr>
</TextAttr>
<AttrToolTipContent>
<Attr isCommon="false"/>
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
<HtmlLabel customText="function(){ return &apos;+&apos;+this.value;}" useHtml="false" isCustomWidth="false" isCustomHeight="false" width="50" height="50"/>
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
<Attr position="4" visible="false"/>
<FRFont name="微软雅黑" style="0" size="88" foreground="-10066330"/>
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
<OColor colvalue="-1"/>
<OColor colvalue="-11184811"/>
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
<FRFont name="Verdana" style="0" size="88" foreground="-10066330"/>
</Attr>
</TextAttr>
<TitleVisible value="true" position="0"/>
</Title>
<newAxisAttr isShowAxisLabel="false"/>
<AxisLineStyle AxisStyle="0" MainGridStyle="1"/>
<newLineColor lineColor=""/>
<AxisPosition value="1"/>
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
<FRFont name="Verdana" style="0" size="88" foreground="-10066330"/>
</Attr>
</TextAttr>
<TitleVisible value="true" position="0"/>
</Title>
<newAxisAttr isShowAxisLabel="false"/>
<AxisLineStyle AxisStyle="0" MainGridStyle="1"/>
<newLineColor lineColor=""/>
<AxisPosition value="5"/>
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
</VanChartAxis>
</YAxisList>
<stackAndAxisCondition>
<ConditionCollection>
<DefaultAttr class="com.fr.chart.chartglyph.ConditionAttr">
<ConditionAttr name=""/>
</DefaultAttr>
</ConditionCollection>
</stackAndAxisCondition>
<VanChartColumnPlotAttr seriesOverlapPercent="0.0" categoryIntervalPercent="0.0" fixedWidth="true" columnWidth="0" filledWithImage="false" isBar="true"/>
</Plot>
<ChartDefinition>
<OneValueCDDefinition seriesName="result4" valueName="result4" function="com.fr.data.util.function.NoneFunction">
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<TableData class="com.fr.data.impl.NameTableData">
<Name>
<![CDATA[ds1]]></Name>
</TableData>
<CategoryName value=""/>
</OneValueCDDefinition>
</ChartDefinition>
</Chart>
<tools hidden="false" sort="false" export="false" fullScreen="false"/>
<VanChartZoom>
<zoomAttr zoomVisible="false" zoomGesture="true" zoomResize="true" zoomType="xy"/>
<from>
<![CDATA[]]></from>
<to>
<![CDATA[]]></to>
</VanChartZoom>
<refreshMoreLabel>
<attr moreLabel="true" autoTooltip="false"/>
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
</O>
<PrivilegeControl/>
<CellGUIAttr showAsHTML="true"/>
<Expand/>
</C>
<C c="12" r="2" s="0">
<PrivilegeControl/>
<Expand/>
</C>
<C c="0" r="3" s="0">
<PrivilegeControl/>
<Expand/>
</C>
<C c="3" r="3" s="4">
<PrivilegeControl/>
<Expand/>
</C>
<C c="6" r="3" s="4">
<PrivilegeControl/>
<Expand/>
</C>
<C c="9" r="3" s="4">
<PrivilegeControl/>
<Expand/>
</C>
<C c="12" r="3" s="0">
<PrivilegeControl/>
<Expand/>
</C>
<C c="0" r="4" s="0">
<PrivilegeControl/>
<Expand/>
</C>
<C c="1" r="4" s="5">
<PrivilegeControl/>
<Expand/>
</C>
<C c="2" r="4" s="5">
<O>
<![CDATA[參與活動人數]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="3" r="4" s="4">
<PrivilegeControl/>
<Expand/>
</C>
<C c="4" r="4" s="3">
<PrivilegeControl/>
<Expand/>
</C>
<C c="5" r="4" s="5">
<O>
<![CDATA[新客人數]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="6" r="4" s="4">
<PrivilegeControl/>
<Expand/>
</C>
<C c="7" r="4" s="3">
<PrivilegeControl/>
<Expand/>
</C>
<C c="8" r="4" s="5">
<O>
<![CDATA[購買數量]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="9" r="4" s="4">
<PrivilegeControl/>
<Expand/>
</C>
<C c="10" r="4" s="3">
<PrivilegeControl/>
<Expand/>
</C>
<C c="11" r="4" s="5">
<O>
<![CDATA[購買金額]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="12" r="4" s="0">
<PrivilegeControl/>
<Expand/>
</C>
<C c="0" r="5" s="0">
<PrivilegeControl/>
<Expand/>
</C>
<C c="1" r="5" s="0">
<PrivilegeControl/>
<Expand/>
</C>
<C c="2" r="5" s="0">
<PrivilegeControl/>
<Expand/>
</C>
<C c="3" r="5" s="0">
<PrivilegeControl/>
<Expand/>
</C>
<C c="4" r="5" s="0">
<PrivilegeControl/>
<Expand/>
</C>
<C c="5" r="5" s="0">
<PrivilegeControl/>
<Expand/>
</C>
<C c="6" r="5" s="0">
<PrivilegeControl/>
<Expand/>
</C>
<C c="7" r="5" s="0">
<PrivilegeControl/>
<Expand/>
</C>
<C c="8" r="5" s="0">
<PrivilegeControl/>
<Expand/>
</C>
<C c="9" r="5" s="0">
<PrivilegeControl/>
<Expand/>
</C>
<C c="10" r="5" s="0">
<PrivilegeControl/>
<Expand/>
</C>
<C c="11" r="5" s="0">
<PrivilegeControl/>
<Expand/>
</C>
<C c="12" r="5" s="0">
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
<Background name="ColorBackground" color="-15262921"/>
<Border/>
</Style>
<Style imageLayout="1">
<FRFont name="SimSun" style="0" size="72"/>
<Background name="ColorBackground" color="-14012338"/>
<Border/>
</Style>
<Style horizontal_alignment="0" imageLayout="4">
<FRFont name="SimSun" style="0" size="72"/>
<Background name="ColorBackground" color="-14012338"/>
<Border/>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="SimSun" style="0" size="72"/>
<Background name="ColorBackground" color="-14012338"/>
<Border/>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="SimSun" style="0" size="72"/>
<Background name="ColorBackground" color="-15262921"/>
<Border/>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="微软雅黑" style="0" size="80" foreground="-263173"/>
<Background name="ColorBackground" color="-14012338"/>
<Border/>
</Style>
</StyleList>
<heightRestrict heightrestrict="false"/>
<heightPercent heightpercent="0.75"/>
<IM>
<![CDATA[S9ngH)r@o<>7-U(/`,CsgtbVS,!ekAGB\7E8L[t<-uR#[*<Hq!GB]AD3/hd.`hRhA9^CU'ei<
*6)R58Jfce`a*"FlT$7"5YjrTr2nFHG"mcd/1+\3G?6K'3p^r'-V+B[tG#"cJ!sMC?(am5H6
0WMlU4b./s;5F<M_eA.77%d+!TgdWq5,3e@$(jfR]A&+\\TFn;TlqNI&().q(>)L`5pr$:jqP
@E0_Je)EN2Rpoifdcp4ND9/kl5f=4/p_E!)@'n`Nul"BagFM)X"M%34k6]A-\0WAUn`u`HgHk
'P]A$\TI.`1K#2^47OW."&l\LL>unO,=*aG/#_GEji+_,5E3%32^VU]AQPP<2Rluf_<,sqZBM#
n]A(1dL6pp4cr23M]A&[#DKAk_e.%JK@A.Ti<=CoUul+ZroSFcHWC^a=oE3kgX"EScP>FjJIUa
Q6Y4b[g!g#AjcrgA7X>[=>q);(,T5:0Lm;o,=ZfF3D]A*FR54Tp*Q7,C4It%;F%/iPucaYm,L
I!`PD(@u>Y,Ac)F31B(S9p`q&oijl%<&#pPiZ1!o.o9B4%'[0-PA]A>E74$$=k*dH*5kqUl'=
HI+B)IlK7K$k1/5N9_1lgQfFcu%F#[j[ZG?[>s[*48P;7II/oTe@23/CFcq^PCPmlop#eEpA
p'HZ]A!G_YKN-[=Mpq]AB6_fAJ:5OD<d^"aa(eI!HuOc5.\>?MO$<<+[mNY/H0OL3Q=`^&[i\g
jWD/EQR).p_e85)Jt5M*rbYSf/CqL0c['k;9:rXD/PSeiLD805jTQuY_=fks!&(j?0&cSSpt
CL+pMj=5VQ&n_PJ'S8Tdc+A,AG3:d-tc8HkShVIDEhmdp#+Ng*&5%@.R2r?hsM&h!f>bf5_*
\p4,36lRd54D]A<T)o%e9*NK;$jH`/J'2Kg0B;@Dc$UE$$E!8??#c1*&d&H38*5gUt$9h,2S"
C8JW[1h\EHkXR02uh\%BANi#kLPk^?C.*A7]A)9q?%g`k45,NP(;t*"7Lq^tQdV;9FuppGE3(
]A0+&p\q&<n7CK*;ba^O?:XBanf%;*GMU'MeDt^B;@3jj5HU^m:+$WYW4NF(A38UA?@3I.kmW
%<KG^3-FB_F:^F?-gm22DRA(m[$:H&PRRe@Zpa=3fBgI=q0b+E):YU1HjI`I3Ns`gohKmE08
g9Fg5>6.#HbU87J4VBYrK#eFoK/5$/XO^2C&%`+!nbLcBf)W?I(L>lk!W@.-qiO5afN+RJ]AG
=N'Ri7_B-AO(1:$*b(s=8<5nBU8po*\]AEK%C>A`;M#nY%d'JCAG#kBj83Ffl(4#AB5ch=$Um
-kOVI^b9LHC3PT,Y\'lA\_@WGQ%q.R',X'no&I)J(TK;@4@?$bJ;.NiEpN@5AWCpM96#Zqe`
d-F.pV7e<O2B'@nD'PCU*j-[0gM`P(tlK]Af9K*i"=N_$h*?1Zf6pb*:KK:[0lGL]A?Dt$>@$C
4C6^;B*`3]A%^4N(+!0A)4NXOn!agN$G+406*LIVBRBuV,OT+YhDJ>5&WSg$lM9Pn%OC0jA>k
$.tn.Q&@;-JOI_MoH&hlpL#e6;g"-j#^QWdi/uo'FpR@JF:<Lj`delIG:c$Xfb9TX3Y7s)oa
i6-/PZbPucUIP-uYO-PN7*Q@q'haQD)I!'3/2m>X+,6>2*VDc]ABS_l[*2(dkes5(*^J+f6O8
VuG.rC9d9q)nCeLYoe2&Ve_Da"WWGVFg^3(%$.PAL53Z9fDW33+&`in@jH`Ml:]A0htMYtV1;
0MXlc=\mTM("q=1'a9NRtMs,'[F<rbP6c^9CES#u>c:C*Si3oH(;+qL6::I7s`Hc,+I/X(i,
0G*0*pf@S6,p8rJ^=XFD5Yn@(1I$0h'!gXn5i(J'poQRgTZMlpJF]AG4,gKr-E+$FK-R$eD%$
tog=>5.Q$1Lq`^frDQ,j6]AIs7r]A\FHRX8"B9lHLnE^E&fGhg[N)63'ABuH(%?%e5Pp#-T^X$
48jV2/s8#D*^(NuE*uQ,W;S*,N,MME?nP9='4C;TCH"8puofnlo./+[P%0,iZ(,#`p8H5GT'
sO;sBR'>)`,jY&'7\HmY?\9:`8br8pgC=Yr1E`]A&q8@1_/aOD[)EWPY(/f_euks-GEu/.fq4
4V#GAgY(V\u6,BT0Q(cAiOkUk:A?m/'m%(^e8UpXJmQKD[XB'<A\?$iFrVCoe1j/CTVTAl3N
1kj6l0c8d3HG)RdNTft2EJ7(`K3*@UbIEBo]A37(nUfNDe@TTfcGOo*CiMLiqDnT>$r[^kBCj
cc>C3T1W_lg/%7oPK363")uiT29F4([=1g-T<(^>mSl8A.C5WN[9IlmM\>$RaZ=I.=YrlF+,
E;d+D0$hb(;<_:;GY)NSSEsanm/lBfO.NUqD+\?C0RT]A&$Z\koI3^,5OHI?NiLXF]AF&"*)%9
e+u\rsiE"g$mRLVSgqm.V`+mgaecb%:RR)P)4[4,p1uXh'`)iTJ.Pf38LWj!_%8RP-EJCNuB
0I>Ts`3<F"'M<a5"Fbiu_^;t=]AD-QF'[i4dQPO8;tZU?q+ISOY9TIqeHuK:QmIDP.O)2(%W2
EhFlGi/[&t#KV=P`pJUIBU+.QC\@us.aogZOp9-kfBX7ALhlk-`m$5;C+8RC6?:D3o>n)$XC
4Rn\"W9c&?'>B1VRJarQdjfq23*G]Afg8)flDrT&!+(GeYiJD#YhIGrtTLX,j%Vri>COEqu4%
g\b<dR$_<38Xfmot/I#$Qlg*B*o%9MVatmtM&?(iX3n("R\"(Pt]A+C\PcLm)>(O:2Rc9I($f
atU@=j-qtEto=]AP3!=m2,)ZD9oa2p*F1Q[;EmjbJqi!P8BZ.\'qHL:PADhspF]Ao4bXdj0B>\
`Y2*6S$O3%>WBN^"CQOsOX$,\@4[H'g,fs4]A@bFfYN_+WYj_d-Lm4&i_E5Y*UuDlEfR5#\n[
n6?8"+k\jc53n?LQ[NF&3;U;F=:uadb4^>b@TJ!rE3,_dSF&*r"+uj[2Roq-gB5h.k\J.1"Q
*',&3NB_')Rj?4EVuT2*9<)Q<VLR'+O+c.30]A/*KFO6Pnmj_cr4Q73BW1LY$7@GP0lT6ru=c
e8:&Y,O0CV"F;"hM>T[m2</s!Fd2H*&_/[@%T[EjuB:12T*c&s&CbV,&>^DA.D30j$aY.-pS
PjroVmNo/38&;(6aq^\.r3K%7a`1XR^/Akh7'Q)WX,jd$9\%lXQU!#k!K,\Gs!>Z=AB-j+0B
Rpb?)X)K.ltgXpmJelU:2Xbs*DGVc)aC/Js_l=Z#srX.XVEe8U-XBdL3gd<#OY0A8%"Jlm\'
IJ3Di\cV4W',AWE8A2Yua.3u<e+hLJ:@SNAmgUN25@t"jhL24]Ao6D2V*5Am%]AhTXeFR.QF3[
D*SV,%SYKs>\sDk)hl2Oe34C(DBCo(:gKp.7tLc0Di0EX(n"lOfnUSB&:WZf\o.etP@"/#6o
sc-I!:>n+eg-4JDc!n]AAAd?tKk)33n^#6Mm\GHDLqVKAdh\5`)llU.<jU[)8iB!WkOI=?3nS
.-GlS=DEdmN*G-V.Ot?MD*q&dqru>*SiY9X/?:]A5ro(#*T\6=iXnoKX,C;@3f%%lj5WG-F3]A
(Hh(/e1mr-G[qi#b8k3$rZ8A//kgZ:cN6OajYdpO)3@XDn&(_fh\\dbci*EgJcdWc,t\9@JA
:<-XP^5NPP*...p1Bl^`r7Rq*`O=u$PE-U(O5sWFWKCa\]A:HAR#pYWGg)bK@hV(`.51cM:.t
DBni1*5C/b#@nO4=$B??i,eV=TOb*r'!?pj=&HeF8@AS5<6AO(ULO<c'*;3Lu^9Y16<,(*.d
7_p+C?H9\6r%k%%1$)[CZ.<B9X0H3MeAPVgZYKm!!!#2V\itkP2(--1hPB+-=QO+5Sq!.5gq
u:P"X_u6_KZ>CO(p9_>->H_g,]A2P*RBsh&(qlo+"_l,!EOq4oK8,`M=Wd<?hLneK&9dD@afV
Fn&$4p@&9\1Hcr=G5U^hjl)ujo>es4D>AioG1@:+43<3q\G+Y%4HdaA>u014shYjIAG\o\Lr
0HRH!5k?+5X`YN_nQiB9i\-^u-jNKVh+%SSg7L;/@F+aEmLm5-]A?>a60KejlZ@*;>P%`VOVh
TCN;k3uH6YJdu-Npfd!F7E5I1pm?G]ATU[8n:Okpo@\7R/lmKCtLYh?rK5`8j#Vrk3Mm<0(<@
0cESWDpAJH-d4cHK3F19i%"-lsROP9gRoCu""BdnR!J3E]Ad[n-$5Lq*$]A#K`^]AbUd47o@b/I
_$S6e#F0f3h!/LRQ9o;=dUHq8]Aaljq+ej_InNAWYs@Hqj%cf*HWPs3\paT\F(G?0!;7ZDFC<
u%!^2LnL,spTU)d-um+`ZAgC$c/-2uUn"qNh[_mp\aP%Cpd6df$EV.TKg7cu%.jdR_03XZ!k
c"IJb/s8K-.4B.6f`keR##G(Ql>>a;#t)b"EYXCQpuG"Y_[&QH`P^rB6+U&!>;<5I[!4C0.`
_M_g;BRuCV9M*IpAmZkJ]AM0r(RUCRI5?"E",ToY.!FRalU^h$rq88$39qaSY15#bkKJ_<8!q
tjiS56OFXd&jMkUL3t.f&OHLK@:VS]A1G\3@kDe"3L$DL@<07.?*B/qX]A)?-RT#1KCW4spEd*
p(sH+'"9LAm`XP7!%1Af0D6(Cp87n#DT*dag?Q`o`C`IVnA/6:Q:p_IMR+d@Cp5fYc\q_Qp5
*SY.j4sch.=7:O4g-hL@7#CB*ZI@5:K4O*DM:*_Xg%CrHcJ0h3ETa%P&h=E+4&6?"gDkK5Dp
\:[3THG]Ao.\D$XfbOS`a;m-b0R1-):q'eU:&TD!\^o-iWQ`-t^L"lu_o4U)n.r?$.<%rY(Fn
A'NI+-n(Hi7,aFqF=o7gHFHQYigV.Q/KJOZllk]A-69Yo%q%6E-iE[-G0cb6&P/r+lm``iHBG
<0sCscnd;gis'"W/ELFs617ZX6]A18ub)WdJD;Cj()s''<5.RDqh.!J"$MB5OY10f58>=-XF6
WH>/]A+O'Eo=eZ,1eW^N4J$n8TJT*"#YFr%.=cupOCI,/8FdHdh!XJ&DME3><'./gO*-ePX31
`s$p1&RgUKPXW.2(W\4D.%YG(1\Q`\@a@m+@e>#BuPH@>Ato&iP6Q!Ns>8W3M;L-n7sH5T8^
^fu]A0iIn=n77ZUt(?BS?lX4c4^8uKVUF1KaIaVmX87IX@[H%P1<a_=4p\FZ0B%j7:>N%c/"h
i".Wl7nZn#"j:b@:Z/eOO\9k,BV(=YXs01<P:Q*u_Wc0mEYt%4;=f/an4N]Aleq;0(ad1m/bO
TUB*Q7,u+M;hTM0i,d?-_.sZPKbETT8AGq96V.TBJWGa,2@NUf?D_b;t-KriU,0&9e\D1kFn
X24g?Z/53eIbe<GZ\h+Ush0;LI:@!)aqnMk_XHN$/as%FOTV!d\fWM5jj`^$<l0K)t4_$U7'
UgYM)lFAIbC]A9B$`=-Ak/1J%Nmlebp\To8@'hHut%Q`$$0M!n-$UG.d,?'oO1VlG(D.ko1Y)
;7&b*,2]A's9U7CB$4S]AtQ3l6-@V1WZ&ULY@>a^2ZMc]A>$LQ<5BkG'2?Ec6bg&uU+Ds2kP,[&
N>;qPfhZOq4k"nE=Pu),4#"Pu2]A3_/=G(j.*fs!r!NAhKc3nUdh#(#_&ZGDE_8:L%8;G,$>q
9W6-TYKsoG>e.e[N2do_f(lLkM/O\p&QG8FsM;_O=?GT1laTL9>SP@X!IPjCC[dRrn]AGWo`.
&3tfCL\]ArG2B3DebXE5@X3JpAK@#ks7(CqXVm2j<qWkCl5L,\!'-H;Q':1`8)hSnSqfelW\k
PdT>;t1LB(hOg`tnoYWds3b)n`k]A?;]AlE.NB\0a$qq>#YV7KUPX+B?WF/4.k2mfPQmI9P$C:
nr!F`_8$_FH2!IO-Ff'/pMA&p,a`#t1KP?]A)#`<NknAW.ZX+u[0I5c^^1kXka8C(mrmAH,@k
mPgYGXqcD&Nr25[%=h(u)nhN<cNk?!^u=`sajT,SkI2*j^ZW$^4GW,M%%1oqTBrQNfdoi]A<5
cKcf5d$e4i*OdD5S';,qtVk#@Q8efCl?MbVHAf/(>?gZ<AC16+AE'4hYF3N#Q^D']Aim$>7jk
$bA,7DN\E%eD=Ws+^-IN5a,1:F3/d:Vqq^J6ZL(kE72,ekADXP,-"$4K!;H1g=BH&=P0rmLn
13-tXZ-V-7osAg\HoK/&&.=(6_j13)b=V3c$?rMa2[EZZp<r*tlUHHH<uqdN7PHq,%h5Ku)[
m-X><gI2'fcDab:JWlSBr7mjLPIpir(K:;k_[iKn\2gln=@4tSZT-"<gK>`nQh.7'9rJ>.c5
c8<>2RQjmMgW&W!'l*>[)_256e6UpAoVg94SjJP<<DIP0nEU121/?'30T(+gYo_101tG16s@
d4c1>Gc:R:JD%.i3+;/hPFqNGZaJJ>['+<N=rN.V*K<)$=\pR%:\D>mb'kGh-G.E!^A:s[U&
(foRgf>oLOLNI#eE`/sDO&f!fUBA1:c.9I`31!2LZb-LLjWTd@7nRp8#*Tl""mVq1LV!um3t
H^HQVg,4Ms*m:K]AsM+Elf59AAeW[DL(#-5tWU'lqo%Z/2>r>o#Pl[BAg:k9C-IM@?1pnd,GZ
;EA%iH(kI@_RGK^2(nQNp-c#3?D)qemD3Y8bf:,k^;TMBg'Yih+#t8W?SauY#Lb8<;C!YR\$
7;Ym]AVq$fe:=r!b(!P/;JWM+2k+1Q]AaqsN?/&CI3/FJIPU:%?Ks[_l4R#T5'[Z?Ml_*7GJC9
D$@;1""0=0Db"s)qKqf*"B('b1lRbfe0)f=tg7H%\USHF9@A66b\Q6+GAXN_gldmec1R@c5h
SKum>UpUI+IZ@>BT"5R#J__`\qId7TArF]AUTMT;]A'tS9KGVCHGju0!jBSibP^+^i5bqYe]A'?
^^%$NAsc;lp,Y$I$a#EGXnT\LSFIX?XQ:099)f<putGB,WTf72@23!RD*6Rc="@u7bV'ES;d
#h''8G2\JG(0o$uB!mSG;u[UE3dfkIo6YLd(l(89QY="/f!39qkIl*QqOm^3_K-L@Uq+m]AYD
]AXm^0GcJA_.SYa,1H=;ICSd\=dWrEZ`oEGtJ18h]Apn9]A!W/drA.2<UPnYc'#B,fC]A'NoT7Q5
.3>_R_9F7LBr;0>DX(ris#Thmq#B[I(!XMtMEDuuF^i!f6%VZp'Y8It%ZZal)IR,\nCqX/Gh
+MG5ET7D6M+I.[k"[:52(mdiZR91;7,"q^,%0>[C,_D.3l<r6YIc:s,q?'4)rY\\\ie%ITB9
(Z3C%MS0:#or;>D6;[=f)mNHi$l3%i<DJgD@1;C8Y"3.L#@W]A98p1c,eF]ADkaI:`jaW4I-F_
$5Y2nKU5ia$Z0H6,*SDS9eB'A9ns?q!7[u/Ic);fp0A#n,=)scB,ZO]A2A&Y9mu<\\&8(Sp)7
,)^XDuRm\[33+"'lo>r?_i*#)KHXL^5LVH]A.C^*h(+?B/Ir2F)%,64+lBV5J@PfaI:pP3;ns
OgblE#?^[em?(RX&8!dd2jRAE_=A,,uJ#NAs7al!lk[jV@h0$j:GVG8T/N[(?;n0gq)tf\(,
H:+eeL$;7F*7!^9lMS>l98^*&nUPc&-j9R!aH0+XI*R`6-[.^)k8]A#acR"c\1A1PZ3YnVm!<
PITZM%q#q*)p)'aD.1hGE3lSN<JQ)/aR%umJ)QCW&IPe1Bb:-rR2#SCA<D>(<"Le?lhn:YZ)
J5[W)lp((tHk%_M*NU19VXp/8[)6;B71"5h--l<m070&-(N.B1Er)q#CEpjBCS`WoFl0]A[Yo
Dp4/$!E_O5ENk'$b*nBlZ!!V]ANUI>>BqGd5_\2#BJBBo'fUe%Dus"IPM;i:+5QMrc_3&C9c`
&K&<a^Rsc92*&AI^CNrm]A+2bDd]AqZl(la/f(s$3iD8noT,W8*NGfL(q;`%j#Ap%i=V-\ml/V
H%NB9^h%ZXa4hS:_-DDH2UXNW%]A?Aqg,6XltaE\X'ma[JA4,f]ANLVhhZ[j,19FM4=2XI1qZ_
_gTA\*<g$$"'Z#VkfO-/en-BKf$B7<gpEK6qs+TYb6r+pA/6X#[I2H`Dg>fWk")'rFMOJN!i
PWKdh(12uRa[LuC5\iuc&HpmTQ85e8Amco!G1@pg^>]AU#`+5P.I[D["Uo?"%:_T*Pjtc8Ab9
uD#*ogs`A:=Y%-^nprq`7J7\Zl!^c;W7mS0hiq*-sV.BIr7+!*pl^D_BQ1Bnp[iY:EBX*>L,
cBb]AY(5BTm=$TQrUh@u2tb/Ma3Afe=+[35)L8/PcZ[J<q>#p.tKfTfffJ),%9]A#ERNG,@Ij`
%ZQ&[2q=WN+#J)99/O:*XQn+ril2f%k,)?)[Y9;kU4k(A".]AUQRtQ;CRMkV&D\lT\8hck3lB
WnJL*d_GOK/CXI*G$$,&miH2M>-mSMsdB09E-/3ZHFWgW/Vd?:=f&rMk0&`#"m1j&?mqMi5(
Bc6YJH>6?P?jtf>4hi6te.S#2Q',jjY6-_#)]ACSkGrf8O(S?3TEBAcRe7uNS74OAW;-[:LSt
bD:6j`IUo&@-IYc?=?`3:9a,]AaomD.2mQ[-/K#"C2"<-Sk^Qj*(:9G84?3cB6@aU3i4nkJeD
)Abg/]ACNmg?OcGg]ABJKk!4-!%gL%W]AB;_C2&JV$TTZeLI-K\W(Tr$7d#$]AMBrTDYDOjBunPW
Sl%]AVXOHX)H72EA_rs^Ba\8T[o4&)d_.d;@6'\s3UI:I*0[c$jT^t1H)QtZDXrcD360LR!9i
\TNIMKfGm)^\?[)^SR4?jBrD9T%V&Ea9%'ns4OMLWi\T/*[TN"*1C-`%C4<\:GDUR%7M_rpu
mqF)O#Kt(t@g.GRL-e"F-b^gt4<f`DYDWfRblC3gN6<u9Nc>ajH2H8^(9$LY!SAVb`>UuCa0
C?:OrBLb+39t@CftGX9)S'%\egokUM,j91E;2bDoF27TpGeho"O-[NiZ@R7GX:=1o;XiYW>H
B%PToB2Mo5%.pL(pPlaOBAIMhcEg!IAOE4R0^GpNOKIHIp73'tGjEU2Nf11G2]A9I3h+YtA@i
h#g`p4+C@.lJ("Rk9fZAhHL_rnQP4S!2TA=__mtMZjL$Y*"4!FdOmT0>&6PF%#N\1e$eB4H\
B>bTOep2A03.C!nB=5b?"!?jT+f$:PC-!#p9CZ'=fNE+H%J@LGQDN`OHc>\C'qdkW`H90$"!
LSJiD@QU^!2ir?Y]A>WrVSgEP</5iL3:"5Be9m#?kJu2/"&"7hH`VDiZ0j74go`<gLq)MSo0+
h`lJhB*g[3X,e/NKfZq=l?Z``m5Fn1dN5=S[JJ.>\lmqa<@g`j!f!!@&@<@cuMNeL5Eq,!B/
Dj3NqSH?.,\?5:(O6DpD4J2.;hInK!!QHf.4&eW70GYB#d*X<X3X27:r'Xi=*5'rjl:TZ:P.
A"mj;KFsSI<1ph)P.KDi<19!r6*1Mo9!UO?IAUu/@TDS2a#oo+6_Nuf>^JhK09_MjV!`gA8,
?NT_a=n]A1bOe]AmGgA2Z%$tku**9Z'\ZJnn)jH.O@"Q2sTP[h7M>hQM3:'FAI7n7=-n2FL`eR
B#K15-i[[MoLUlR4:+Tb^UWfH.Rr`b_'I+nWp`:JAQ).bhO6*+Xuf4$C>(>s&!1-f<m`g,`d
5OO*2K\`F7J%]AON4><hP&c2NM21!J>XGl#9bs[pOl3',h\eheat7TDW9u<j,*4f:Fen@XW]A*
jA%RgHR4DWk.]ATGR[&C\Q7mmol1MQk#\D!.L0Z21:DqJai\^BQ<=)V!U,*b`+i$AI:?nL#BZ
bSRtU9G!ldP<somO=dI0=lfh6IlaX+@"GFH_2&9qhStPG^\j1Su$<b;j>6BJ7D-NS/^-lA(A
onk7QcU,\Q$!oIe_eB@WGTY]A[IkQd_`B/iFR"JNJ?qBgs6n0,`S3^fEgMBY0I&<tGID<:&Qg
k!-]A=_?/jS3%58fFd6!Q*h;))"iom45pc%c0<P)d$X/]AjUX`DGlAd_SG#!Mq9[#33^.XascK
.q4gK+9WL%inr7XB9ArL!,lL@FNIFf9J@K:lSCi1Z`-cqIGoTRpt-8RHZc.c##4>#@eXV'Vh
\)ak%]A'nO&<*#`g%@LnWBooBf3G5=f^#>Li*?e_#)>]AT&a64LTaFbt=Ek!;1+m?hR!]AZhCRQ
7k+<mI$i%!k==UZ?,R[81Yd.=ta(Vh;-dV"A\1(Fci:q6r&q5Wa.$<cunmU=G<JL=ST29#)B
o4[$,V)l0I-Z\KOuN="G4/0fPuA]AY5NYBu=JSge1XVSA';"2R<HUl?6OT0jl9t[AfGqhbL=J
3n7$1NM291JYtD,0ik%pI:HNA!mrB"38gO8(5Ng/0T'nB*O4fJQi7I1KV-LJ=?'*igLh>!5B
bg0K*U#I@mGE(3?4<7%$PLq015A*!;[ZGs1R7-j+[Jm<_*8nA8osk\pZ`B@:VI3_>UPe?13L
qnSFC<BRU*4SNp'FLjq-!P%h8Lr=Q,s3$gJT/0pZp/tf^Xo/.4:Be+Np&q]A)i3-sSNr_Gr_;
AQ-b1`6cFd1m$M0n\B9g=<N/G.j9R/qlmIY14W`]Al5)0hHaC[5/-_u,%To+>Ab7aXPp7Oc=*
)!*QUS\!C&<[//!K+ccF&1bKfu['l`.Ul9s^7QK.5lB$:r,39=I0ndPFoE]AUYT-95P"*"1+J
B0K[0"j6Oc>ZZj3Nn@3Ebc+FXI_,DA:]ACf*h\ir>`qWh%$cuGbF)5[<%s'%O9?u/<F(=2j3G
EENK76fA'4JeX0([5\9KALsQhtl`r]Akt@UG13n0_fZ86TD(fTOWG#jI(;t9`ARHZcs2<VCP2
Ld?d;`7!2MnCVnHD<>>f3-*2*I=0A8j$_K,qRkrQ%f`fC=H:t4U$`cUNJb$bTpC6^91:Tl2I
8@%^hq79e:r<UlSLnA.8S$A"%V\L0$[T;JNrlST7=X&X2rFL,P=t.sDYsoY.4?I3L3*js'X/
!6c?subM`7^0Gb'J(N7@VFVO@$]Ah!Wo:$.[1j(Lun``1eMmKAS(O!N<W!L/:([nU&rKU;3N0
g!Y`q0;@rj#/oE6i7@BoBVJQ=3U-.t1%,_QVm"4HV]A,ro=?<JK$N>bI@_K`]AT_-bQK@!^aQ&
&iJeuPb/p<PVU#nU>MY7&TQiu(_%KfiM13>*9(O.oR%@@("<%UGa@p4O)nhMD&nc@Fm([KRV
LS$15mJ_V7Wm^)'OpCIH:UIm[.r89K&Y0aY#4Z%cTWo1X:S^bUI<=I>AdJ!]A#'f<2?PsqVJE
&e#dD0q3:"$-gP>2:%0e#f4Jb,Cg2]AKS4@&9Kk&:bS1FhGg1#<eN0`9q=?.?4NLU&djAqlF8
;fpCn9)j?.ROEr+tf(\o_3qB!RpU0T"IC^0nD$TOJLRI!s$'_J!`TW2[$:[iopS+OeA=BS'`
+iP/SeKGtai6&!/N*rkc+"RuLg>=OL7)!fcq==TkNBa:Bktfs;k'S#Ik'j.+(n&kt(K`B1*<
=&WauS#eh@iMa!aoVc/9IER[/oqMjndMkq2r!pHl_1Yre.5O8ZhN6,P:$CF+)1=YISTl(Cq[
h]AURE#@H+W0O`\E6.!@D$>h-`H)>`+24T^)QHu$Rr.DOo2QcJ\lVbSsmSdr_22]AL8^bfgQSE
R04OO%l35MS#Y\4@f%B;^XKnJL37=$\#Z"ioL5J\=ho9lcItiQ8/:@F;!c[]A8E>^$0t_6U#Y
;KaG]AIEY2-SBf&dflYjA+-V;t3<Zu+FrO(]A4[+(<kqG*RV"bO(o"dLa0F>>ZaL]A'eChh&e&S
qnrMU:%-Cno]AQMB'$OPm=Wmg4o^a"/C[O;h5;2ks]ACcHg334T$6jlYcclj0=EJ1[d[,F,WFm
m#4^Q(s;Gh*=b0_V2j\*BQ=9'R@k0X#?%$%'sa^<Y]ARchK+YJEEJeQci+O7D5/1l$i-U1C,k
&-:GejMFq_`ODsL^L@:JK]A3PWq=T,)Yr,bA%0#3'[%_m`Ahr]An>B?b*sfZ`9)"@0#-F+KK!o
>aXFnq76Zb&Y!/-;PBI;;L+*9pp([dH4_Tkr`Z_BY9V!SDmCm^^Ed'I(aaoB/QY7h+H;%XE`
]A&cZ(gcH@g\AiCOYB`1[[7>tH99"/",-%IfL7<%CrnF\6),=o=E&Ee<hRSdVFBYp;d]ApG,mF
3WAkW_`WD6_bF?2EJ+r&X:Sg7&QUkLVtT5d/hQ(*i_\6N_8&U[0\.a$N/uWpJtI-JnnK16Mq
=TTa\@4C1als!ha$d.@nWLWPbD%W<2O*11MMb[,DiDY&jVE=PRP"`hDRq5bIDM:+P'VG%qg(
tBBFGN!<$=7@2M?&5a#'XXo*k<'=XfL+C]AetlPi9cjcIA#hJ$?3a2(q2Z1]AOs8uL\,^mG'25
`@,=l.-`uq]A]A:pGeWRr5%S]A3Bg_PjJBMNHZ9Mb/7NGDr#Uq?(,3f?Y../[P7SqWqZ?o*a0"+
^uFi5U%16i!*CRMnPN*qYj".a_l>4H9U:7,LbqCh;n1:B5Ua197oIJQ("!51?`;FMB8,h\TO
M5`\O%XP\-<MDJX$t6ZJ0?,V7?![HpnX6Y@#[\eb#pXH)Jb9mL'O"-"'CSqd+2S\YHiU?WD*
CkmiZ#PeHImr'e@9#?^5;a.fL!9>bjSg8J/KkYa).(8DseEpF@o->%La!'YhI`7qdTe!NoJ:
:I9r5MW<'#MQmu;9R-KX?pDekuG-pBb1f5-(BV,&6k]At[f'K]A1^nlU+Ncb/<,3LNkLk*^9g+
F;NQ8K(>8(OHE'F"@/*2eO[$>ftBc,^F@+5&50O/q1C_.Sb+@lFNY>_[\C-;)QMU0*u`uDKp
(#%^_%!Y"qY_T9&4b+(kPPVM0-?=H/?[AU.uQ8^MP>oY#?tYIJq?WS/mC03,(6=toa$UYrp.
P]AJd$SbV.c>oY,m5);62ruR5_.`9*HDnq<2%Z<e9T&@,%gA;n:[sH*:G"27AH?"]A%+tSTIHf
q7Ec'e^aj%2o"gIi6KVb)\U!1a&b$nijN/W86(00!n;s7p%P'RfV)$]AnJlrT<+hnDK_/^+qD
KGFj_"[[:;\o@W*#O3MVg^YaY9VJ&:ZX[NH]AIib_sS$)SZqM;=Ge*1Io/gX+pidUQX6a$D2%
rL"sD@\R6PfdUqgU1uYR*&"A7/+`<MLDAH)?S1\T>CJ2mUS2c"kngS8/Jg]A;;YkM!b*,\$;?
G3EFYRfnPk!G2iu2:Sh!]A=L=9V?M/dbYgeGbq:&u4Zk((nu(k`GZg(]AEheN.^GA8S`tic]A.B
>+Gl*g2ebkm(hB?2oPP!k.W%VIuUEA)+P=<1c9.*`Cpj%=L%^eb9*e!ZEdYki?_JSl1.^kDk
b9NLAg+2Su95Xetnm'oWLekP/P1*qrJ6Q+e'rJ1QFjpVn99PF;CC$2tl`+8Dh8Iq<iUKHu[F
m>muBW>TBF6pg-3KfMPS$kTZ5.0=f&5)f:_F,3Kuj.Vb$N:"c$h[&75&eOQ;UQ.22^^6^XOc
]A"l4;Q?HK/#DXd@r=$uV=>Ri)O%*lG&_Jnc1$q!*_:_lf2:iMo;'En!K@LR518XN'B>0hg#)
gmYm)JcO$;<V`7#!=L0>nJfOpJanP)ctjGK?!kA77SlKf4&8n%8-.5;Y6kZ6jWjHM[\\ld=;
)4sik2LHZo>Gk^a;$2Nq@dG4?/pG5DSITXKJ`%654eN=,8bCIPik,!f9sjJ.ZN[.1&+N;)r"
.@@Ah9!7LG);tN4<huZtu&e+Lba/Je`=GU.+_nog\'k>Ii0:-X5'"D%@n#CYe9B5mS4*W>52
+^L2q8jE7!HIHL>_K,0oI`QG)BF7`@51HU]A!0;aLeY':o95q#HHW3iOM<sn&LB)Mu"d(2j4i
g9*:">hF)nk4*iJ,6I2[NI1UJf2f#A/S-)q=4c-Z\GnXUYb:TrF_<=6_13aET5@_iN`m2?'`
mm@:$4H$EFH@U22&po_SG3%L96d/H`3F2ntuC;29$p%cIqtL[-sus)tne(d#r$,N*Y?iG=Gf
YCEpiKlPO*:\R5?g.m*Y$mbj,_dsqW+Tu%k6<;DbO6E_jknA*T+?oH,#qVDG]ApE.ZPNGlI,#
!ML')jJ6Y^XbAE\hRu+2+!6$H;oT&;!5>;m=5qel:r)e_OCZW]ArF=(T4-oe9sL.FJQup>64k
-#hr%#(Dg^KV]AKlWV"Vt5d]A@04h7d1@%1_32SfY3k1b9Nuq[ZIRDr>:bdha]A.8t]Al+<@,8hh
ChkH2mtgB$Nj8+-$UqXBcobgp[Q_H#JrcS7^&e#>n:XrHWb=J"TtJ]A:\BZQ_jOnNC!3-cHm'
V_Sk#5VCD0'%JP,bLcJW,3kXV7\)[MrEL1]Al]A)4$]AGrL'TNc?fI!j[FB3YXLrr9Rh0P>GujI
&uUU@j\qN-qlc/2D8fZ<j>"$(2"U:^i`_K7m[^G#88mf"HQUdj^ZAd-6FoO1ENY*^@iVP1OE
@SRG:caPXbt=1%hKs3`"sQ;ZTp_',)43<`<h?2_F'[3A<gCeMml_i6P%136LSa__Q+YNe]AMi
uP.utR#&>^./.`##[#T4_Emq`46b=hJP9%+`Zo7(bFTNd<Wt(Bah2Atebf7_Ch=\2FFXuccG
Fd<5md<FT@5aCWr[@:qSg'hiE7;D`r_b*`Y;C0$5?HU@eNL4OgV(IlBnH`3<4&;\J)loEm7%
bfQcQOURnY=an0bio2m`b-+"?46nlb15E<U8jKX[ph$q:jC%kf8/'a\hW36WBO0ZDqWEWLFO
Ck(fjKp89PCj6(tM;_R0i[-mL).fae+98(Mra]AUdfV)@JG("8_b%.FOE[/JX/p:RE:/WWh.<
COj)m@>knWEf'Wsogl)BJ7Jh7\>kl&Ys#Dg#9F.*)!5@(Q9S06H9H!B?Y,@b6@T17n7H:tdf
iqP$P!8/KV;W$@9L7?>#]AoR6^b*N9OR;*<#I=9%B'8@Eug`cCkr:b(FXOfB%l.[Fq-WM$]ARm
14?YbCl3l["JU#Tnj?hTM:]A(T3?pH"hp_mV4OsSq(n8Sq0Z]AsX)Z.G$`@LX*^p-d&ifcTaVp
LJic%))L>6O->:9JIT9MO&6nE;;Hh5'H2SkjEGrq>&Mn4r7"X'\n-M,=WU#F.LakC*G9=ZMe
Q."UCDftPVK<)h).P@Ub^ar@9i%K*bCfCN#q^hhD9;Q?F'=Y%DkWAM4Gi+=l0dDtE<e`et0a
ZFgOA[r_S.(D1m`o1q*N)LOWh7,[6)_)r7rqK;S"nc-nPqP:'q$%:cD'Rk\N$pGSo09/)d,O
iq/I-g2oI/IXk"q/EWKDt9(\oW1(sQ.%WVg8H@Tu-=R`jdnErqAjIJljakL`DUp[,>rCJrq-
qLS;]A)EQ&YO0hcr9eB%L"ehiPg\GrhRKupV/k&<:&S4,4fs_[qZ3\r%0ip%K6+a0:`Teqq)E
!;1QjrGDf]A5;dh.!FX`e)0D:a$mSTU[e#OnM`h:<c!k`4Ctro'kAU8-'%hCUo%gUOY4qhZJW
bq'*QrLR\5^s;b]A\LTL_AcSJJ:iZgecua-[eoM;H<7mU@%=q@I<FM*ao[JVg2^MKCs7nOTbR
'rd![2dFm++is-V:RrY)4-.a".UlU^#I!mT7<mQMLrP"D(hEb-,P0$(3A@4f-0-#)A"KlY*p
dCT!7>c?/p`Z"Mi?+`!9hf-X"u'E):#=Fs$G=QFRt89SXp4%so8A\l/VY-j0nVpg=-XRaAd:
?pjC[B6DAmt[I#:KOe2)j$gWUB<1$[$nD"gI+MOcHm4"+'.R2(*$O#KeDcam(CX2Nca-frjS
'T6\E:&\tTDTY_q?/7-nME?2r&M@#A%2"02r>dR2Gf*5&pRmC0TNfs'?nc+Tderd/TVPlhm(
7H8E4h2`'fmu4VjgQiaB\fg(\@b*(m&F!12%/a,9o'rg!C^\"([c41PTFnY/HXgNbqN+;p"7
J/AMWpDA.q*O_MmBnAX!OF1mA%mgS2R;6oHiU=?f7^AkkIrBSELo]A<@Bra:s0n"0L!X.FC72
DA]A>U*<Jcs-Zbs%!$<G[pK,.`&hi$Ut9aW_Ck+5Z]A,Mr=/Ka;Z_Ja/!5E<IDoF@jofakk4".
UVtol%PF-I.i6)`t4Uj+ms[tQW7TDF0jQ_XXGDP8i-G6cL%3u@[Ae1J$Waf`Ha_7c$_:=6ij
/VX#*4aIM9I1p6m/\*KVPC\/4abnqS!ND_5eT&1!CoZ+G5'f%D)gY4dn__\Ma:iJ,5:i!V8g
&,"jPX-6e[8$;3V]A@)7B&ULfT+&YCC<Juu8CdktsT_-0mgQ'k@Kr56MMt##F+(FUeC+M??O,
f5(o'"eo$L^JuIIC7?\!"Drlej0f9c0DR*3<[SP8)u?.atZ:1Eq\9%)bU[RI'Ju33"lnLsc2
Z-%iPlL4+K`@,i67B7"#tk>X;4He>Z=3rP".j]A\Ur2+_?/V_>1bp9d?I-WfI]AY[gTh*WZ%j!
':#;0YGH^A+/XXH^Y_;6ZKDVbjI%b`<$ZFF)Aa>ILk=N,0`KU>?_LSn"Y\8!L7S4Sb#e/pLu
g(Yg?;d@L74!NB0gC,)d?gS>@kko'1:#_aBOil$TL/)XY&Ni:T_i%%i8La'5bJ7bEdN7]AsW*
cF0QidAm6!gbWTt`2`5nXj\b"!Z3,gZMXO_&fR.UcD;k%b9f7T%_`0Pp=2>kY<-=47V3+FmQ
;sLXOo26-++JL2k<(+BZNr>"+D_EH?r!8:;Ie'0bfSqHeGiI!)a^j-#<0"gV&o6rF'OT7,9e
"@p597TnY2758L@XhW>$G"`W<^olQ5t7T*'-3mW!Id"eDi5<mJ41]AUAFM#6HUaRGcI@:N?m\
.IIC';KLBmITHiBlHfs4<r,Ri*,",X_KorIF2A1Q*%_MN+:4o]A_8%%g_3uF[0>/Y\bS)i<rS
B/0Q]A<;>W?nS6>*tT/Tg9MZ,j<_.Lmr/h*n<UQF?.f2?mBejH(A.$0k6h_$3\s#oAN,1Rm"G
6mH8Kr<3p?oa/W/PC*.!'GG)Upo##9U[n2\VFSs))U7FiJ8k+Hr.NrPCNiGk-&+BE"_E]AX%;
@6o:atV,CZ4uj,oJ\2VX2'O-m*n,[^Eu%<49$lErY=:4f]APcYMZ6$eM]AEo8uUl[,WfW'P*@!
:6ormiU!s%k.;G&G^eWtQ$M6Xa?93)n5-fRF%AooA.;aTlg*9#.K@P(6b1uBfKk5^&O4lU2,
$L_E<)q.VDA5i[$LZ'!_Sa<rc1-]As:SVg+)39+qc4HS+,t9h>:J1pm`VP2lX096]ALQJ4h\Sb
RG"W++dC7G.200R.ld'/-@A[%ua*#eRnUL\drQI=.XqV8r>F-biGGs^ghf"9N%-C!nNHa:Y7
[SeS+nVr9ild+N*hoEe^3HFam#1)d804co5e2tkGR%$:0U<_U?W37GIhDfo\(_m#rS.!C%Rm
hfWj#"in@.pQ1+E1Wl5/!*8>fXX#@bTVQpr-p_UFqob,`u%D[KOJ6?Wp6O5"d#3WM4$S`(<^
5^c-E9X\X+gIJN2>&)P%pYm+=dLeAcgH]ARC"JWtd>Yr3R5=V@`SZMl'2pZ@Uq5'LSk5IXT"/
^JNFY'e=W>:+jSo8PkJ[CnV$qMs<02[rYY<-R"8Z5>ZGD7dF&p,'oGS2R,@Bisb]A8]Ar5?W=b
%W@XK7(;a42eW$ZSLO"Ju<-F<s3;okJ91MBTtr-<q+n'uc*4_.P%,\rs)Oj$+%R%DUbG@QO3
<6*gSb2,B5KO32*e55FlPOqD%/_,BFlc.Z#j6m6NN*\S+R>_aR_YC0[1dWgtF:!i.MU/_kS*
p"=BKPPp`(:rOf%$MK&MQ6B,4BUV#WY<Oi5fZ9*Od;+Mj+hige'[.*?JVF=qo@+hs%mkDR8S
j_%Oo<1ZaeRchQp$poi;*OmL*JFrXF*ZtsUK[&Q,R@s-gF]A[W,6n%E,7DRa/`Fkuh1`"TbqK
.2'B>61!Hk2Z8CV=%>[f.Sh8=31F47".m]A`DJjh]A*[);#:(hTn_=",;n<p:M'!&A01MIfL5L
\'(Ni%I%L!$s"I.2@/`?0EdC$&XO9bd^;IR;JgQI\KX=hkuF^;m-!o-Xm0kEltV^-'G4:AKr
=+FQe"?F5LQA<P'po$?uKT_tO`H_m%2*Aqq`_WNKF1h->CiC_O"/2d%"_Xm@$ZcYr9BV%u.a
1L0C9soD6->9PB@d0\TB(DpY5[mV@m#l^)s*i;OG>BANp[R_O('%p=E3F@.W^<1[^#cW^=%t
NMfb$ZFXdHH>GTn]A$oLqRC=\Z.c&:qK<l!?i7\$KG1.HQkZEHFg.cngYq=P*VoDEK1Qge1h-
(t]AEW1,e2c8[)H0B38$0mD^cLV;c.!7R@VV`2N(4AbmM4u@6p4\CXb4$L-m8cZ6UT-#"1Gee
@+Gu;"5f8AnA./rn0mt8qpLIWT9LT':L0"q@Q:J<S!S(dFhUkaUPYL9:-AHsYN;i[6o4^g@Z
7>^aOgEAq)l$FjQEYW;(Fi*Q0VD(3,Om7hB(R5Epaa'TX/m-@oUJHPSb!4I2WXeuZiIVkdAT
J-4g[RZ4IVs[e-Sp/X3DsZjFFU"I7r>*OKH-d2%#LR/K%.8,%'Whj\n65#-4Tot-"RXds*Me
D1Ojm]Aa@Y\iH@BaqaigI1e_kPS&`Z%,99alWQOs9f>u&enlI1'0l-\'=LjXu@3,CFp;#<9kM
a4Z=54m'SI:en-\M8N["XoTZ6$X6El[*uJPd)7$fdo3r=g6s*g(I?H8Q-`5fh\Qodpj+9Z9\
Y-:<*`63*5eeI7e?i>-RJCdQf05&[H8dFM]A"Sn/V?+Z42)`qfde:]Ac-O@1T^:E=^$Oq^#g9d
l6kctfP%?dpFJfu$l^q%Ocj7W+KEXRl/j,7PKeR1G_tOuS8?^9L`2K=Gi;k-![c$K'jJ7T<k
Fn9Id#8-HJi2@6o5m_c$s_Z2p0'j3`YA-2O/uaA&\[T1fS?e$g<&%,F,d:eCJ!jbDstF./+J
kXt^_F;RMlFI-V5#FMAlIpmNmm7mK+9:EU951IL\5nZ;g'gT5sJKp`6j%l=>>LVPmoo:JSj-
pKp>JkT96gi^J1FPp[A9<P;)ROWPTdn4i!Bp3=1@Vr1IYBOVO$Kipc]A\IHUSRrW3!;4^/7hc
S6(_cWf,a.W>:g<@Fd`a`4UEhn^Z*C<)h^a?W#IAn5Ue>GfJ)7\$nIaEGIhs6D99\l9A(5a*
oWbF">sB3@d^q"+![jPXs)&eV*@HLYIkL"Y`td4JWCWmhq2rXFgl]AooN#"<hmsVl3+8056<f
9Z3h`On8:<GQdV/`]A&bSg[$#j/[>5>[==E!qlMcVh="BG-=kg'ZD0GV`qiE.6[_JbZJkD=Mt
nj(?2M)(m_sa,g1p>%GZpo,UWUDJ,)Ri=\A?L;j)TP"Yr2`(a:V;6iEtd`5.LRppoDl_D!X:
0J+2#YNXpFFg95p>I@6kLEi&MROb!O_,Xr6tWY]AW'TlAr[\R6mR;^b,Y%U#TNAjcJ@(SeJ";
\W;@F*J@+*[>3YXPa9aGbh1EWPgSP#A,]Ae(iZZbdaC7,GG0-L(g%eZIX!Z\L&ERURr\]Aq^)B
$K%-'JD9gQ>&f;^pqXo2pafNAT*ebVs6=&n+:WT%/*cu!\2'03%q1mV?eFO^*Y'2;Z7L;]AR8
23Ka!h=_hM#MNEY1NiSZC&2YRcfoNrJ^>FYJR%WhS=o:V-$jF8^(FL:]Ag/p%ah"R^T)dUhR)
MVuF)/rC)X.-"\C'7pGFCX0I(m@3rt;^f!$g*fr0,T55QJDnnP.H<jM>gT$.4,]AULVW?hajZ
KQ16r5O*=24`3Cg1r,/rXt!`d)[=-5be-mO7HfP5B$"Zd22O?MS*JK#*c&L*X.b'^U8:qpp"
dDI^NmS6hkb"HZ"o9DPtl![^ntX5k-BGDjqjP36,FQ)i:>TqSliOf`7dZ;Cjunk8#,=Pb@Z]A
:%`T#%3e@FiK^Fk/?ZN)YY"b+'p(i!=fLQLEFr9'0T"b(F[`09UdTfTHfdJTE:CJ9#K9#P.0
S!>Be1VKT8HZ+'!)6sZ$k4REW&2@G)1pCjX7(E!WF,%&pdOR.lWE;%A.d=B\Qq#,D'r`54Nb
8H>\?CX_3b<T#MrgmIFqp$,_fm_>(mfgjm1r'^Eje,%6CsEH.?"QIV]Af%Pd/.C4+R:BN,<Or
4O2rY;<UDS@5GEcN=!YQH</9IUmqsTGk:eo0b]A<ni5Hl;YX0>n6U?GXdD/VaiQOM(\;#E=Ak
9TRIPZp#,?o!g8bGJ?5+cBY?&sqG0IN+Y`CBB/1&U0`l0A427#;=':54Q=U1iI5'PhD)\(EI
aHsL$-'449)/hT`-2@!8LNg>=1qAM:9a+<l"]AG./<_nK(b[e#Lk.:i"qL@&V!N6b)$]A"N4oW
^FM3_:1uNg.5m+Glk5%/'HFGXtr"S1O,M<qL;&!BD=h@d5[RUUX)>@Dnp*.TQ157qpbA(@c^
E4aDdFW]Aj8kB]A6dE't0Yg,mc#LI/EY:[l:"WV;0.;VDN>8PUs+K342m!DQAu"=;[R`jA>HMF
?iaW(HGmagUu6\]A--]AT%?lX<M^5T*e"c3ejXe9HJ>aA0@)3;F'Gp'H_?.G9SqDnFb]A"k3>tC
77O\FbFViTn>DLSrXD`h;#>VS1F2GG#pp>qbH(NJA'+lNb!0Zg;?9;ZUOJ0"h[VPr,Y/ruUr
an^R\I/MW5<\<TdVLq=\$"^AL,&faf5[3Z,%"@'&?&$srXq9f3E>).@I8a(R#CG96L1C:rV1
QU?-=4YER1>r^]AZX0!cc@3_s)T4D9NEA_dMRVj]ASa&+5s:&l*LapC$JD=`f9PaoDE)TrQUSP
B36YA_rU4rgSF42a\7+t_>_!rm-gnIde(ErdJ"FM@<F$!TOH,nbhq\JN);M-X3F:mlToLd]A>
Zf7(1OieZTh/PI,`JDmUlE>miJ*@3#S<9$5]A7\[X1^sFR9,As1\?PCl7D%p?;f875\^\^3?#
8u".GN_"%G2%la&Iket5N_7*NdQ'MRK6PT>'?97KhmF*EiEf43h\'V$#t-Vt-6A&]AS*5&&n!
Hq7MWo^^gVTKDh%\_bB1#Oago&d\FOr@u()lA9o_j<Rk9c;)lI/g\@k2`_C'$+2il`r$^CQL
)j:<YpKrh.YL>H(\dYF6(Pl&R,i/DF!]AIjoAai^pVP<"3]A4\=%XU7H8\-4k98sD<FUYmn-gB
U85RkrZ$[G]Ahp7'&RDHtJAa4mX@s)JF[Ie.-,,)`;ISntP#A1$(JA`en""VNkWj$bZbkimMa
!*_d>FW7Fp8\rBLcdDAB[Vf/*hJh.bB*2>UX'foMY\,bDj9fs7j'S8VP,Rg<Z@POH^064e_0
d;Ci2bB3(K<d5"".I%$Z5$)@3aFg,p5n*J(K7q!GjMNLKWm4A?d$Y64/D?_C,J)M;sgbpR4P
]AOJrnN/\Rh?StPXM[2f;YY8(1;SPkn;]AF=Z78V,-QY!**I/C*kbp1Doj$o=PCaA.5;UkR=WY
S+8.V#[!=p4ij`Hm!BI?M47\^P=0I$9QBVlL#XoAMCE\ZQ^\4k1ss?LJ]A'?,P.1m]AYMGlcn%
$g)F9%l%ie"CmLcl6N0i*2:%T@\J=I>KF4fB^^gI&a`JL[7720>p=_Tkq*QhG"D%)*Qt+.s.
o;.R?KjH!WGVgFNS:dtFsbIFGAm=d[Tj?7_09k,QJVHq^!]A$p>`Vh$;;<@1>GYXDNE1t;Ku?
WcY8AA:4"5:c?1^TW]A#5KinRhnc%GJ5d5@EmQ`?tVa7^hGI8gH4m5OElC<0Q"H\$Q.`7=%lu
&/=@loWC"S'iF3^kTDIAKG#S]A'ELWfWZYT)<#()5U8S3j.5cWtOALR_O;j]AMF(ZM%cHNiV4m
.90*EEr*Y]Aog<[/G?ok'a[s;U^gceS"/*8//gV-G"$!I\fcOg$9]AiXo3QT12Q2Qiq$^G#1]AA
/Et;iteJ^%Pef!1P*VsO#U9M^bTK.&W]AKS*#3m,C=?`m,*!S"\gn3h>FpOnSM'=6D(R[0*kL
8H;dPD[T&SRM*Tg[i[sgCX4if.T$CdI[8&"5JBP0Dq11.#86XWdfFF616WIH0\'!,!7K`rF5
S4XG[]ACl_8b)fbpmA(o4P<2SS]AqAO%e+)!C=0l#D;VU]A9u'VF2)>+m/FX)dHZJm#tVD@%K!6
EQ;BVI'f',X*_YM`,jt[AYgsZT:@5^7]A(2M'0ZT]Aqs?Q@DKP14HGQ\OL#;==[uE\l,0(":fZ
B3P/!1XeareZb#EA>Y<Vha[(t8&t+?(7Y_iupm3Xs^rZ$,JYLtLQB;Dn<>'uY3T7gc9qIaP`
Q$p&0!A%Xq@G)&.J0R2NF1?q#_IrY0K<MVSKCJVt(-8%se9O*4R62JlY90f`EcA#7nagfprb
T=CLqc8dfQdtm5Tlr>poOCoFpfMh1)?2R$q5o7M%+jt9*fU_`i9^grorYdl9M5-c:+YhJjU"
3NGhF1D+7mH@5!,&_$)n%4U:c[c.\8J-1gp/6,Se7jfBPGQ)4k+*JF[@3f%ub&4hC@B`Kulr
%S1h"St8'NLk++6LY"/0,d&u_7^)\@6a*AD@@$6!0D'iql#e\Gd-1eOI'j";2)B'CJjs0ILl
04FDn%[/gus[=p(:`JDaRu<9+'5i/bmGrGGt5gX:X?rf6^e)!AYWKs-XB;Pp$8urAZnY_(W#
qd/tT8s*%1-[*Cg$]AD8Lt0^SHSLPY3/2Tjgg*5&me0Y'p2PR(CVcDeus$=@X!r,U%3A@0g=,
iq/68(R`ipLJ'uE:0sfKk/T.b3=FaJBlQi/uSFG6I/QYV*^cM0.9'i,b;L\DZXit/)2jX@Jb
dH/$gaq"b3-[?Mu9RTZR(WFXF&hAoRBi'>MhQkDc'pm_2"SQ$XaBL(<A\a`"9s5aWYl%=[Q5
&nueq4m&GteoDWK6^6+,eEX.W)_H\;o2l8a;aH'lGK,]APJM2W#A[5I&_8AW0Ri/nV0'0jp2`
Oqr(k3>]A=?s)l\8o5W@_$^9q^Db(jfR>GUmk>=cc0uc^1]A^^IDjn#lXmBopWa^b?*L>"-D6+
>]Ai^hR"n21u+Hd?A0]Aohr,'Ws0lT?3Z5T:`!`'quBGa0;O1f8F-FsWf_=6D$13:!cLU/&jcV
M8#]Af$XsM'&(BHm>k*$'W3X#S3^M8>E#P5[V;98]AQi+*[b?R.Vhd=YIXNT0BB-,"pXOAol0Q
3Ko$6Fimt@uu"e2f(`V6;9MZm#`bE]AeW?%1cfH3Q8,/b[354k-q`lR0NCEBN>t5?m2;<O\Z:
rTi)0K7rLtSp321eG.nO%B$6Aq/d4t3%;nOOOBpS+j!B8F4Op^b=q@5QB:'&J^aR<Gm\(pb?
eL0=sO>o,F]A'doDRpa-#]AW\i,>]AWKK[nF$_'rLVDT37:$F`0hm?S!$WI13)@G*3k+=6HMn=h
DDprX^?\oatYri@D[\R^Kgtd^gD2hA^SQ=rFjR=5JA%OH\AkQbA,ZXlH1Bo5r8#$ND(qpr;R
ZG>g,CYS\$Do,DG9L3N75qC.lsMJ5)U[@<p;Ca_JQeNdJ\;gKbF58`#BgZnaZT(B8,p4%=B+
V@'D\fo?#PU$>nqq,m>c.@TVNtf14"/G7YIS]A:<hZ<<mZ9cPhI&9H!ZO=[L(]AKX2clqMqqkJ
!orjilPm1DqQIg7Z'q#tmZa/Tbo!8o\l(6$+"1?-n2oG9/g*TsQ-/AnWB8Weq=OJ^r2/JIm*
B+@hl#F\ml-foqTSia`k3ed;2HGJp2th"kp-LWIS]Aeg[!gX*ZbOQ$U#B3Yp\W>O6-UJueud[
h\Rod'JQ#OB2o50^olClL7O^Bgo:NjbAPGHpfjO0:=29+EiHs^%Ij_YQ<r`Zd=W`Hp]A!e@B7
8\5YPdDEfDSNW\QL7;%^s,tQ2JliF/D'cLY&s+N+@G@3-+%C]A>J4%ge#F.ofOkC;4DaZSb\Q
?*,k$JeTVl#l>%&8j=k&leIFE^0UU?Z8md>MW`Sh.=qJsMY/tL">Y)cDPI9tZgI#<Z,G?as'
"6Nen7\XpK[9soYl`29IZSMrZKro'&?VVp]ACD\8G6%.kfWC9kWK]ADU^@'R^Z56r>_GJ<I?Ci
+t7J0?jL4?1;C$Feh;0,/5j8&IL8S/'@oCtI\]A`tc/"QbNGDK]A\7)W<*L<drm\_q[hRdV.A!
\=gdkN^'$9%:c!"c_au0nY]A7([Q4eOiCTRcPCU7O]AdCmM;o6q-1Ee?%'!gGmG37)'E2NljhU
urPs`LYu^Grk0+eQ.c=K[Y%8<GG,I2gB^O(e1VBhu8"#mbM\jrl:AmLe9a>41n.iWShAO'6*
Qdg7-=epK7KQ#,CuF4@,.dKW::i'%$/_&'>@jVIZ$3?n35b7->[ShTQgJLrit7^o@TAY>;:B
I-*4^N^tkZj[0r;@e<GmE<;3Kq++_Z!L#)m9!=6BG&LBV3\I1U]A1'`&Q4u/(.nd)CL=;dYYI
(-B@clENj%m?OGb8r<.s>O1%\Xam%alHLjeodufXq"!EfLcH_GQojKob?lFEtXm:YmI@cM:L
VMAJ-_@G'D?C\C@O&OtYA\rHhW@`>i/nrP)J[*(p&,@giiD2Wh(&'gWI097;_E]AJZQlM54ae
iK>YEd=Cg-AR!IlebOU3"nJp8YUt*2Dp^YU8XF=:Jq8X/CtM\!"=Qb_X,a<B..i7`?huH?0a
ZBQ")2=(h8;nZF0:Q1k1HYBoHjCh9t^,b,!V(G3Z6C-Ps)=S+0XZ`ln%#`u>o?>+qlQ#Wm!Y
!R"F#d-ZLcnB^1FJWmJ/W;20A(K\#)VBeWXLONri:m#04Pl$c[bH=oLAl@cXg1K!MG8,IJ<@
)N/Ins`Bm7m)oI]AD?t;J("Ag702c6LeO[WE7"^p)]A^RUIDkF.\KR/*),K4aAW[*^^FI$.Hg5
Qlug]A=R>*%gVO)8fX(%S.b-bk(%-<['QY\h"fOo1;A:!@$jf[5POS!$=/tg%f"p@?Y9/Zdu$
isA_7'!h]AJOfn]Al7t+?kK^J>QEGrHU7el&S$3p9E_RBDd&7GRbK!XNQh=FqU+9.<7>RtLOD9
eKElBYY^-W2Gp+Z9--WbJ-"G_,JCi))e>hl0;\Yk`%o]A58G.p+I-Ht/m?=uh-,\]A>;E[$#*?
1G3;*DK7L`m7&t,fLAa'LBu..J"OGk,97&,GF*JBr&C\Sh%3XmYGdrVUXPOX*SH7,.R4=0)(
M>*8aoRX/OUl+q41`nZQ?C!ElJm[M-i8Tb&m4Lc&/[DEC%L^b=@]AE3e31aSBF)G1J@S#fr:n
:[1r::Obff&dFh\.'AL^_PO`=W.DrNX-.ig%pKu^9/ZiZiR)^$.d+E01UKY,S)s?iHiO84BG
>/uihAH=dMY6f5&Asr\$,4%8grDOI[<reRcS4&C`9OFoe03HJLi/pSdc[jYnL>@*a$q06;$"
_7-&-WKMX=uc8uGrGVW2g?<O4HqPF\nZ*`U59mrSJdP/lcdCl\LN?X+J#]AB,OlJB$Y5G9;KD
nKhr7-#W.0p6H@eU7j5H'"e\0H:I@``Xtq_?4VD<E/l6r+&ngFfA\[rEE!jd0:XA,ZgI#k?"
dbL[nFnn%\]Ae28]AEQ_gb"VeM.:Q^q`s&O64Q!(>t"ZWMR<:ReP^^JL-0D6kt-/p1Op8A;"74
EMLj)B1up^iYrWh*D3#cQI-=g0[iUgX6XqV!02&R8H(XXf%;S-@$P+cY<?n!tLD)0%YeY<R0
R+riRptS!cgqMo3jbsckaP36+pW)OHtU^q2t<(1?+t8BCGSq[hj^s`f390XIgC-PhM%8FU#%
2kNs[HHm?:AjIaMgZlB5d-%"jntZ*QR2R9S%;)i,[\EdfM>.Ln.WO7O@39%9.1pC5"f*WE0Y
4q21.S[P-Vp12PYRNTW*8Q0Dna'-7!>*5,[3deI7JL$U"7n4@e-0sZ%f1OuMDP8*;0g+kr9&
DdsLCO%p/ETVrF`haKL(AgB+41,8q/0\9l;gAh<):ULrDOnWOYg2<_OM/-\DGJ:&C)uqV-3R
;DQmiYH<R/hY1g$#JkH7A6sC1(!'_"'IWi4\?.>q[=O?=44r*&CERp.2A&;T.LI'(cn'e6S?
Ok3/.>;MomWVUA+`BS]A8:r_e8H9V"%5Z&Udr2*^YMTGPDBgrkFcu!Z);=&/$(bgEeW.4*kS2
F86t/Y0'esB-9s]AX^.Ta)hAWmg:h+Y)(@<ZbebLG1(@$KXiZ'XYu3?snpFN`nMYF#S[Q0Weg
QuBu]Ab'PRd+t.5Po6U\G:2cZkO^e;0HM<S^;I+mr$"E$IDk5a5`\dBuBEU8l&"_5=dIm?-$*
a"uW]A2t5=#:6?`@<_=etb7XNqgYU`Do6QFJT;g+;,7uf9bHee?L>F3d*'boB_aoJikmX+*lE
%,-`SY5WDKVp-a3D*5Ke_<bP"Yh3=5UR?6)YRG7Dj?`;1L?G?i8)0qL]ANX]AF'`AA"i)n73ka
[gHN5ER3_,37K8+0"R'BpX[99/P6hMr4@6"i`A5V:5*j=t["ccggd`#I4fr[DAF*=Z@Yo)&>
]A!Zd[Z[n*lL2""BMRSc"r6ltGe)['0V8;`VBd1="=`R`.PS6J6H]A)E`1=_Gj^U!oAat?4Wmk
@q-97DSS_I-Q5b&p<:AUI[#[g;p6s,CJA/!PXs6'[M5nCbhg6@"BHY>.O=HK#D6BX^H#pPOf
MofI-q7Fn0Il8`YtZn*79#2Q18E?q,F@>^q3RaZYgt;S;u3Zm*Y@=`InG9$OniiI'o-B5[]A-
Q`Y7o"B1@f7-A/A'fos]A^bAs2\p[-BHj_Sk`XF&UGn]A^V0[nQU;Q,.JJm2qk)<W(7R^[mn^e
C-#(g,%"1?Z1?qN6Rs(h^R,D&GeiDPhpTd8RhpB@ij]AP06[$PDg.Ll<"%Ig[?S2?;4"P_DT@
iYD`'WPbaF3'L'?a<L2\*<hD_l$URV8OYhEfjPM-&(9,nQt^aM\b<&p\,6b_\:7nOhgmMG1q
lk6hYCuKFc@9]AYH&C`\S)jQeIQemj/MR9bDpdeOr's`3V\!o.(Ph)5i2d.da9'K.7h:V+D6m
W8$&`tKDKI-+o>UO)me5f@*.(c=$p'[0'R)SobGM2(=8re-r1ir6n/?$e6g#XsZ]A8M#f(l+<
\d'&?[;6oN"(5-j%Z'Gl.:"2tZ%Sd#%=@bDC-h=rHJM<3kc>!+VAk5YlV2V29b:l0)p6VU["
e*I]AXY!kTF\J^2ERSd'M=a9['_b_L)[XS:PUSZc5t]AIl+AM[bhQB<+'(WGQ@DiRgeLk$EJIJ
?`\T-3)Au)TRBuKJ^V=;`L:h3)+']ALN16WJg9i`#Kjjm0ZN,jI#A18lM\mM>kX!<-lpi_UTB
/Yk?N)TYRpX4,jrkrYS>d.@I73I:^`VgEK=9ssQ5]A(65c%.P$[QsGjFj8KL?9ho/L='c1P-g
(W8[&flmZ[;gj1=]A/=33gf_giZoRM\OOH*ggGnJRPY2'Jl:X.9R%si*?]AnBBF#"cH_)"@uT(
kg8o`2FN?5sFuOLX^o0dc>k526HYR4kK&WXNmW)gsK$"'nNc"[f6;&PUmi@M$4IsV1S_TQWX
ltTu/]Am#pQ:uUsp:iA\.'rdNX]A19>kMJ.n/l^_ne"`8s3;/MeM9,Nu[2.kl(sC>H!b]A*JgKU
(X7BbfYr@!b9.W'em;k`]A#-shq<0(Z_!9(p->lY.cA<UWDbDpb)^Y8#W7n[V[hq/!)M)8Mmq
rI%aPghEAo2IC_c$k!;EH/J\PCLU?5"XF#H%.-$FcSE`-?&!#5;k/YPeEQ;&4cp?nhJ"D7%0
5t(]AaGf.9g.3;'q#%mdFeN51=WF[l($9a;DH0Vk7GNk.6GmgRmr`o@EM7>VSm#uA[U)'_&\+
J0a7SfK;nA#iXnpWI$P;KL!XjD*!Od"h@B@c$l6CUR.%(CRN^l)5[D;EQ=b&\".\ljG_oh=#
2.3R$;no329peA0>RQaLF8fEeHcA/289i-dsFTWdCkfB7hX&6KTr(Y/!R$s_V-lE%hE=pR>h
Q<,UtmJ*GX1X>bX#sBq4(=fqDG092>]A!&iMW4ffOKm%3`S""W_Lq(D.ji.7He'598^qkIeU]A
b^&%&=g`80;+HT<OSBOte!*HFb*?bUV%nsEFD<[P?F=G?&ua"kh0Z=WA_XYsG5"I`RX*`ud]A
no"<kG)r=6R4&*U0d>1eW"8A'Al8@>ZWLIqM0_08A<.VproR+mn(.DRVr\Q0RW'BO>s//3-5
[*-ENPbRJjMlm!njWVN_L1BG);g?.8M,uT\NGX4o?pKcl"kF,sSBR/3oZM-1ukn;Im[6p1al
%moG`ZO!2a?NqOP6%.S*VGHHI'k(Ob6\;L8k&DtiIZA.7A&.Qch6_O+7UG9"OCr^Q9Dggjb.
?@Yo>qUCkNCC5G=srA1BniEbqMT"SXgK5R6s9a'/nPQWb_&;=g/]A7(06H"k6pA6nNG!j)aX!
bA;ipW`ce.q.#4IUh?o7>_3IMV>6<M]Ar"ES\l)rM*;%EW"mP(uK'GWGhmKQ[/YIi,Cm;!'g9
i2mQFG(7J=4WLPJt5RhN#ZA6;s5JN1cN^N$JT-7Do2AP;]AA)ATl?6>qFGI%2QHqq)7Ak!V_1
>$l\Xn>GXrJ><O4RKbIbHGs&NnbLOj@Q$#CJ5./;09@)>.:^cFCH>?5)>A>sj(L=CS^H*$=d
22qUP$'#UrX(ZR;#Mo&/dg<1aqHE?l[`7!8T_U+9^,e&U`5oV.=kFnDhhKYNeRYq[7F#aRue
<kVfe2B`e07]A]A)!JrbJE,+<1o#TNP)YK?<_UtaJ(XJ:feprcZ5Luj-X\URTn5Q::=A>q/e&*
N'[.\=[N<aRLu_^gEjL4`gTs/XLZ_s:SiI^,S0uPhfmRG2Kq<LZ/SV+2knIN%]A'_oZiPD#V'
/Mm`;%763=6>`(9.a_jKWkccUaN?Cl8\j'!BJK0\s[2<rg7L((856kui>-,Qd4N,EP%qdI^"
h?->j))*.VC:uLITo>kHZB#PNS?f,jIbQC!8h_W<qlPm$I!.E-,+Y+a1Lq,d92NGK8P.BiUR
Ljbt`9JPKF8MZpXJn&#*E+--e(T5g[/Yf6044#h34>#5!`1pAqh/]AKf;.;3SD<@:W0[Y=a!.
Vj\f\;UO`'UN\R:jRT+0@gR+p%CaI1#>R+[$@M:m)f;+)dne=g'+)fh,o5"b!9[^0W)OY"_r
E7tCunW$`qqI<(8;k"OA`Phi/(]A$7dM&DIPTA,kr,4\8KeO1<RO/+g!:k+mo\dFJijPgaD>#
m2a7?Sj:P9:p3T[l(Q%CTN;j<rKI7$A.(.&tnDV@-1h?M`V/3mibt6CIC)qmK4fO2]A$S?*t&
U9iLIo.bu=heBPR,`[<[+/Y8ap!,g7d.-FE0s4g<f:Q6a$@1\D+_oWjq8<7"MX[nQ*D]AH+%M
SS.Y[(ED0k,rb*@tpjegZJ$pb-"&7Y%n;+^G);]AHQ:h#%Z%CR%IH.*G+XMsmNhacqkT1]AC\3
&*bf4oM;I\G;'%TL`+_a#LG+7]AdA&krLHOpsg1$jUH87tW8"/QUMihJj)#gHE!eCT#aXNeSF
nt0WO?95BLkY#,P]AElKk(8!eikR;<'kAF8^;:A0d6^fafcZSEGfOR!,T'l@7b'05[kbs>f79
)=>=t_s0oRq,q]A*m6,mQjhbX_uP^O*;/9&l6nYVltFNSaY_jmONaSf7GW41Vjs!B0R""BgSN
oTa;#n2j]A?_/o<2T1a1L2='\W)ACplk+j!5i#@$'-)*Au2,O'X3j)Ch7OnQq&k$-RZbGuVuh
&1!K*jrt(kVfZb@I26`[<04"$@U,)LN!'d+_`WK3%ra8Vjb9/IIsa"b`UI22sgN8hu:\T`g;
[/g)1jMa%rur8qYm^QJaG\&(d$_>bOsN`n:mKY:\Jt<c>![3+KOTj"h/+*p/O1ng^)P(K.n_
iL&Mf\DoOY-,E^mAKa@%`RZS!C/or5=rA`%;c)Lq#FS<B0MQ:k[i;KNYl%#n(M+&]A>)"YjF?
kcMYP*4i-c'0'>ul,tSiQ/^:@e6>^/=Gb?hI_$$O2WA\b\":<i\67ObcTPH-3&g%&XY-bEac
C3:ir[muM_\-k%.e1WsLTcC:P1H;.VBYf`Go-XRj(Y3M&$M,C)3++/DlegY%nH,N8FXI9mF]A
3*)5aHLGP4>E`"+CFOs(<*lU<9+ocBLqm9?'Hup[X!R#dGmOa4b22ZCrAB0r=McaP9Lu*5DZ
P"]A!j<F:iVY5n?^[<F-;n:K1/qTGOR`'qmGi([:`p+0.R-6?'gFRDCEQs5rLpgW#+s[mmjjB
'7hi'GluP>AK0fs"Tgj;4jG66Y`XQLifUaG.UJ9'P8%kA#J*!rKOC=7jXf4S+W"@TA]A=iG"5
D+&F?%1[=*6$RE#4gB*?kV%on&uH\V8%B#_C/N`lXSK)0X#W38A@^7qG:R1j_/]Arr%\(ndQF
QK07Sg0W&h6'+(rVH(SUjP@Q"brT)k;J\M1q!FRT=0bM^Agu_W^%iH4PIW;I.;IDfDr9N3@e
'rMO-6i;-dr8W?QQR>j,5YQ)9$K(O'l!O+Ea=aTJb(d,>Bgu]AG43P$T%8\e#1d?PV)8l.VPe
j:-o^Q('mSJF0^8pU#Tdc/R%ak-P1_=m41aB'QtD_mO1r(n!Bfr7g'0_!o]A"9'$,/CfcQu)V
'!*&#(KVYo*oiB_O6Fo;R%VG$T=861Y)X#%b2EHYHHp"cN]AX!bdRdu(RBp<ho9V%)qrte2Nh
RGN\M7hb77?KI[^K;3KkkdE83NToXU":/22&]A2hsVm'\8O<U4$dq6FQ19eSCqC"MTBHe?c<6
m;ppP*ZR.WW?7V)'=#SS,Xa59(G<tq)j*p7Uf>F>leJB':Zk<eHHI^!4.9u("\U$slUi?Up7
shMASho*(gjDH'HretInlncSGL`m+[D\#pq[J!;Lld"5ln5%*Q'/olojTVe_MA]A&iAi$DPH'
k^=]A)_/]A4D6Z'_oZ*aDXQtP0_t[Hf"e\rKktIK+d_XERH&s8oYo$n'>UdY[NVn7FmfKZ+M`'
"k,dM@XgXmh?Cp<3H8]AS$3C_imp7`S%r-ORM:lEiI:'RCGL=Pa0>h]AkYnQeY\Y>\qh3X%W&f
*Gd,]A1OV^BCNq+TW\Nj*e`O2;W/GXqIGP"m=J+,JQ;DOt:Y:YC*]A!9E'6^R!P$D^lNp)`Iu<
5e*q+Ae=B&M=n?fTnAjoE_o_db7doPYXsu%M^lc5Y=S(EF)BKi^%-qcs8)JLk-uKScq@rO(K
YmSncEG+O3MrrdG4OcX=$9LLVgFD_06kB!VC$gA"As&.%_$nr7-Ur4fAA6D,_F[$j`f"JIc_
mVI*;"$9=c:n&@>:fm8[Ns&`#ZI)iL(;>o@g&"I'S6-D?"to_\Yqp?Q-lW``WEk?eW1=G=:^
n;<A]A'5=!l\qd2"n)LpV_/!&_X5cVOoK.e;><Ki3BP!6fmsU(/g4,%4M'u]ARI<YKi(UC*Y2J
K*$-kTbS\'FNUTOU4S%7kR_M'7.gY2rOKpu#-aVu>pFEhqdhb6-KDj\GUK>tb0&=Wr?HQ:H+
]AKD,jig/"5Y(Ef#/jFd;0hp9RHV6U[L_e%YYWmtL;kG^5r1a@o4=O^(:=pN!71g@8aQR3KsL
AhgT0duf%D>;pA9CY1/<,.DFY8WK'>8grA&A;lbIpKi!dpe.08sT5C-iX+mPlpLWJ/F3DXRJ
Gq"b:r_g-9T!!F0=<M,I*9%>of,>fbuB0\^N4XmoJ2&ElS2h#25B`Qp"6H2hP6G<?`M^*7gi
L;k[efTb8V'`G$n<>MV,!>Li15KE]A^C7$@6e2atO-SH'p&n_TUGf+FR)Nj>%8:tF;:[(SO=]A
?5Scn'PaYte#%+bh>^8ODB]AVOToBRnNlijJ(dg3u".omM,pJN]AQq':L[B),YZ8%?Ug;/+3o1
m)'9nJ-"ejo5Z-RS5:Pm9r'N_3dku/oDKVE/.&_H%.b?]ACWc/=`ihRHo#<ir3aN1^H!ccm-n
$SUia$.ir7pT2GSjo72I7d<*)8`P97K&TkGPLR'<[JkDJG3oWfiLBN-Rg_UA-CUqL8pfAU=g
0X$#M&s+1*b&rtDK-$:(61WB>r"-3"'.J0bq?9RHS3-5MJpM9H2&59M1LU!bJ\8P=#h)0Yr)
VgUm)9LbY1iWgVPHc-9Qp:kt)Uh"sQ3`Vo:Z5hLppQ$*rHt+!Wp^\bj;j*+&BASPE5Q")J(j
<*4<hfUANMZ>M-tT:TjT:a[>&\p7(G-qKeh7ilrjB-2Z',,7U,SsUHm7l'@&``.N+B6S@AW^
o[XF(6K\iE&.O$)##i>R1+'XUhp`BgZ0GUiF+ute)Sp.]Aiq>Y\h%\e<![m,'CbG1Dudua`M4
UWDA[nUc8'_)>_C"s:9WM32XN[5j:2=Foi[oIG89\pVrS]A(B[mn96XO_N:VUUnR2k&s>+\``
Db74jg4kT__sci`=R[9%MW@XDuT2RKD(\t'Q0bQoj,k.VmR(Midt\*j0XC/E0%6(WuP.P#YF
G?7;?7du<e.[,_8j9Iku<=)oXTn!+-CY)@IIIl=WQ"$,UHsZ7oF1\s=iG8)aP,DT+96T0>Te
?hBnC.:ZZ?ZA,?DWqU+MT:fP5!:#a`A#UD]AlPm>l9e*SF-Rm[Jn?>"UY]A/-9*X4%-%6i'I[G
O?Q;RV4rMc@\0^Ijj8@P+0j2m?m:@pj-R8LDIdE?cVl0LVTD4rJh5M`*=^GD]A1cYcsMm#?Qr
1V<^m*rKt\moB*gJ7c:BQ!o)=I$,Ma:hC1@=%i-FaS+2T`3aSQrcLn@n`O:>M17j>>F[[s-W
uQQOqecZ\uep@h#'/8r3loXSHQ111Z>pmZ#[SPl7\0<QYChhcml$7Vs/Z5T:O6\/GhhdmEZU
g]A(C2:X\-<%LU(TX%qXZpD*u?*=&'qnLZ6mYBu'L)N*G%NGH&4*I70f8ur*Ap`1pXO<rh3pi
ka\mS-;pggH_'&T9a>fL7=WCJaEEX(8=U"a9'_r:[W>14P$,9iV<+_mbEp_L=Q`_]AJE$;?(M
B4.'[9((/54f7]A-U$cnk:jTF2l-'.4Z%CML1s'6Ibi9&d]AfE\i3!YZZ)8,!RR=kF$[*J-TcR
\5iLC>qM#p;5"qj6>YS/Q)O;or(R)lYg]A*^s*<,2mhf*4?un>8/D?\_4^_@+mqS@H>f>Z+dh
2q*^kh^RgfO[+]A65rq6a,^V*McpI1#t*nG-$;@q/>%4IE>iZ;\YgYWPp6_sfr$q"[J9jrg;5
`aK?/%/[UB.s:?[b/T=\hT(J@As]A.1p/(AjW'e5h1WiAmT\T)#J_QE!;K8o=%jngNCNIk<iU
F_iL*f&Urcu;$0BK>O"4?ZEJ)5%C+n2o:N<bp3^KH9js#Eb8d:&=SE4i4VLEWOIK.,gM$@TT
f#X3fhjU`a/J=H6NZSi>#+t"XHbp,uDddm@_A+/Z5KP6.t5Gt#s_NIpFmSX,[cb$7Ra5#T"g
b!4]A0\lcWf<,7!'<`e2EL%X332]A_7W8XLGL[;9i@9A0^@,Cnkb^6[m'7;Lp'J1rr$ZY(o+31
Y<s+7>/#^:-(E-83V(Ti%op(k>RRhs>!*h!VW>(rWh%me#@Z5%l>`h9MRKDp7;^@@d#E_0!3
9o&Mi:;/!4>gnlSa+HYe1+*2Od/:r8r["uWfiX3r%QhUqD);Jd*1Sf=gp3Vl;#XT_@`k(oZY
@R3P&@<^B`,?)msbZ(%T^g2^l@Y&E:_pJ#I>W8(s=T"*<Oq2l2Qrqrj19*j=jACqKNPT+'sf
)qa5#=#?E/#TYLdOBm8%Tmlb)]Ag4ScK$]A;sM>G3sB)^>9WR1RVaDfGr)j"GojFPc&sUfGah+
c/OhnIdeUJ;l7pHQ<['"';%L^Bd"S^)W>OpqIZrNPE<5j,kEbnGIjPTcB]A).Uq[[eQ0X5jSr
97r50)$\5j-KY(Er/D!nc8Cem'"IKddb=+0?uPr4N^')gq.J49qI)]AZEe<t9E%#FF?!aAso6
@fH8$OMDCLMZnm<VudE\<#uJ+s0?+M_1Clj?-!sOrV+;CXhUPJE+Ncb#g=;C_!BShs)7Js#F
d+D+5"IUA5B[c0GK,r)$_8G:D_&UQ]A3Fab+&+]AjrC,qM[U&pGetW70&I.>#Z'mYF7!H^`"*:
p33YMX]A"]Ag-HqkHNNi_$uB0)q>a$T9WOK#ukQ.^Aa+c:?QEX)Uc*#aj.:u+R!X07R*>X9WeD
W\m0J)%fC5ej^s[A)pr?/b,FRh;B6gY\uUFYdgk[oWLAjY\S4'&0e&'%D)<AQP/CUIj^"Xg5
QGX`)'.dPo)b>XdIT_>G#b9-d`@$5m22f\tdrAF1$[O5W4Z/E=@uZ+Z,E`S97:^]AX9WSpViU
cn33'7lUX5:D;Q#j+#kNs3,`X)e%C$Xf[\MSu,Zi_^]Ad?Hr)tTf*I6ub[gH8]AbRUCqCD[kpT
R"<3.\-HMP35*rf-.c?I+[G.Kgfsi;qi4D]AgIRE$%%R_Y0+r6['9&GKDnAp+nG+^$Yq"(cGK
A^eknT'&(*5UuH%'Hm1ph_$6qM#Yb/CG#9F;0]A_H`K/Y0/+lJ5p]A3:e_ob$2E^:'/)R>,kZI
fT~
]]></IM>
<ElementCaseMobileAttrProvider horizontal="1" vertical="0" zoom="true" refresh="false" isUseHTML="false" isMobileCanvasSize="false" appearRefresh="false" allowFullScreen="false"/>
</InnerWidget>
<BoundsAttr x="0" y="0" width="960" height="136"/>
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
<![CDATA[1143000,1714500,723900,723900,723900,723900,723900,723900,723900,723900,723900]]></RowHeight>
<ColumnWidth defaultValue="2743200">
<![CDATA[2743200,8640000,990600,2743200,8640000,1028700,2743200,7920000,2514600,1333500,7920000,2743200]]></ColumnWidth>
<CellElementList>
<C c="0" r="0" rs="2" s="0">
<PrivilegeControl/>
<Expand/>
</C>
<C c="1" r="0" s="1">
<O>
<![CDATA[参与活动人数]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="2" r="0" s="0">
<PrivilegeControl/>
</C>
<C c="3" r="0" rs="2" s="0">
<PrivilegeControl/>
</C>
<C c="4" r="0" s="0">
<O>
<![CDATA[新客人数]]></O>
<PrivilegeControl/>
</C>
<C c="5" r="0" s="0">
<PrivilegeControl/>
</C>
<C c="6" r="0" rs="2" s="0">
<PrivilegeControl/>
</C>
<C c="7" r="0" s="0">
<O>
<![CDATA[购买奶粉罐数]]></O>
<PrivilegeControl/>
</C>
<C c="8" r="0" s="0">
<PrivilegeControl/>
</C>
<C c="9" r="0" rs="2" s="0">
<PrivilegeControl/>
</C>
<C c="10" r="0" s="0">
<O>
<![CDATA[购买奶粉金额]]></O>
<PrivilegeControl/>
</C>
<C c="1" r="1" s="2">
<O>
<![CDATA[Number of participating activities]]></O>
<PrivilegeControl/>
</C>
<C c="2" r="1" s="0">
<PrivilegeControl/>
</C>
<C c="4" r="1" s="2">
<O>
<![CDATA[Number of new customers]]></O>
<PrivilegeControl/>
</C>
<C c="5" r="1" s="0">
<PrivilegeControl/>
</C>
<C c="7" r="1" s="2">
<O>
<![CDATA[Number of powder cans]]></O>
<PrivilegeControl/>
</C>
<C c="8" r="1" s="2">
<PrivilegeControl/>
</C>
<C c="10" r="1" s="2">
<O>
<![CDATA[Purchase amount of milk powder]]></O>
<PrivilegeControl/>
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
<FRFont name="SimSun" style="0" size="72" foreground="-263173"/>
<Background name="ColorBackground" color="-14669005"/>
<Border/>
</Style>
<Style imageLayout="1">
<FRFont name="微软雅黑" style="0" size="72" foreground="-263173"/>
<Background name="ColorBackground" color="-14669005"/>
<Border/>
</Style>
<Style imageLayout="1">
<FRFont name="SimSun" style="0" size="72" foreground="-9470325"/>
<Background name="ColorBackground" color="-14669005"/>
<Border/>
</Style>
</StyleList>
<heightRestrict heightrestrict="false"/>
<heightPercent heightpercent="0.75"/>
<ElementCaseMobileAttrProvider horizontal="1" vertical="0" zoom="true" refresh="false" isUseHTML="false" isMobileCanvasSize="false" appearRefresh="false" allowFullScreen="false"/>
</body>
</InnerWidget>
<BoundsAttr x="0" y="0" width="960" height="136"/>
</Widget>
<Sorted sorted="true"/>
<MobileWidgetList>
<Widget widgetName="report0"/>
<Widget widgetName="report1"/>
<Widget widgetName="report5"/>
<Widget widgetName="report3"/>
<Widget widgetName="report2"/>
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
<TemplateIdAttMark TemplateId="8cf5935c-f059-4005-988c-8b75842ce14f"/>
</TemplateIdAttMark>
</Form>
