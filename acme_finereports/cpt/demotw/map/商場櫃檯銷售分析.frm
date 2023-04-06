<?xml version="1.0" encoding="UTF-8"?>
<Form xmlVersion="20170720" releaseVersion="10.0.0">
<TableDataMap>
<TableData name="ds2" class="com.fr.data.impl.DBTableData">
<Parameters/>
<Attributes maxMemRowCount="-1"/>
<Connection class="com.fr.data.impl.NameDatabaseConnection">
<DatabaseName>
<![CDATA[FRDemoTW]]></DatabaseName>
</Connection>
<Query>
<![CDATA[SELECT * FROM `map_櫃檯資訊` ]]></Query>
<PageQuery>
<![CDATA[]]></PageQuery>
</TableData>
<TableData name="ds1" class="com.fr.data.impl.DBTableData">
<Parameters>
<Parameter>
<Attributes name="p"/>
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
<![CDATA[SELECT * FROM map_櫃檯資訊 where 櫃檯號='${p}']]></Query>
<PageQuery>
<![CDATA[]]></PageQuery>
</TableData>
<TableData name="ds3" class="com.fr.data.impl.DBTableData">
<Parameters>
<Parameter>
<Attributes name="p"/>
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
<![CDATA[SELECT * FROM `櫃檯sale` where 櫃檯號='${p}']]></Query>
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
<![CDATA[新建標題]]></O>
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
<![CDATA[新建標題]]></O>
<FRFont name="SimSun" style="0" size="72"/>
<Position pos="0"/>
</WidgetTitle>
<Alpha alpha="1.0"/>
</Border>
<LCAttr vgap="0" hgap="0" compInterval="0"/>
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
<![CDATA[新增標題]]></O>
<FRFont name="Dialog" style="0" size="72"/>
<Position pos="0"/>
</WidgetTitle>
<Alpha alpha="1.0"/>
</Border>
<LCAttr vgap="0" hgap="0" compInterval="0"/>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.ui.container.WTitleLayout">
<WidgetName name="chart0_c"/>
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
<WidgetName name="chart0_c"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<Margin top="0" left="0" bottom="0" right="0"/>
<Border>
<border style="0" color="-723724" borderRadius="0" type="1" borderStyle="0"/>
<WidgetTitle>
<O>
<![CDATA[人民商場服裝櫃檯分佈]]></O>
<FRFont name=".SF NS Text" style="0" size="96" foreground="-16749643"/>
<Position pos="2"/>
<Background name="ColorBackground" color="-2953990"/>
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
<![CDATA[新建图表标题]]></O>
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
<Attr class="com.fr.chart.base.AttrAlpha">
<AttrAlpha>
<Attr alpha="0.75"/>
</AttrAlpha>
</Attr>
<Attr class="com.fr.plugin.chart.base.AttrEffect">
<AttrEffect>
<attr enabled="false" period="3.2"/>
</AttrEffect>
</Attr>
<Attr class="com.fr.plugin.chart.map.line.condition.AttrCurve">
<AttrCurve>
<attr lineWidth="0.5" bending="30.0" alpha="100.0"/>
</AttrCurve>
</Attr>
<Attr class="com.fr.plugin.chart.map.line.condition.AttrLineEffect">
<AttrEffect>
<attr enabled="true" period="30.0"/>
<lineEffectAttr animationType="default"/>
<marker>
<VanAttrMarker>
<Attr isCommon="true" markerType="NullMarker" radius="4.5" width="30.0" height="30.0"/>
<Background name="NullBackground"/>
</VanAttrMarker>
</marker>
</AttrEffect>
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
<Attr class="com.fr.plugin.chart.base.AttrBorderWithAlpha">
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-1"/>
</AttrBorder>
<AlphaAttr alpha="1.0"/>
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
<Attr shadow="false"/>
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
<Attr4VanChart floating="false" x="0.0" y="0.0" limitSize="false" maxHeight="15.0" isHighlight="true"/>
<Attr4VanChartScatter>
<Type rangeLegendType="2"/>
<SectionLegend>
<MapHotAreaColor>
<MC_Attr minValue="0.0" maxValue="100.0" useType="0" areaNumber="5" mainColor="-14374913"/>
<ColorList>
<AreaColor>
<AC_Attr minValue="=80" maxValue="=100" color="-14374913"/>
</AreaColor>
<AreaColor>
<AC_Attr minValue="=60" maxValue="=80" color="-11486721"/>
</AreaColor>
<AreaColor>
<AC_Attr minValue="=40" maxValue="=60" color="-8598785"/>
</AreaColor>
<AreaColor>
<AC_Attr minValue="=20" maxValue="=40" color="-5776129"/>
</AreaColor>
<AreaColor>
<AC_Attr minValue="=0" maxValue="=20" color="-2888193"/>
</AreaColor>
</ColorList>
</MapHotAreaColor>
<LegendLabelFormat>
<IsCommon commonValueFormat="true"/>
</LegendLabelFormat>
</SectionLegend>
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
<VanChartMapPlotAttr mapType="area" geourl="assets/map/image/自定义商场.json" zoomlevel="0" mapmarkertype="0" nullvaluecolor="-3355444"/>
<areaHotHyperLink>
<NameJavaScriptGroup>
<NameJavaScript name="当前表单对象1">
<JavaScript class="com.fr.form.main.FormHyperlink">
<JavaScript class="com.fr.form.main.FormHyperlink">
<Parameters>
<Parameter>
<Attributes name="p"/>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=AREA_NAME]]></Attributes>
</O>
</Parameter>
</Parameters>
<TargetFrame>
<![CDATA[_blank]]></TargetFrame>
<Features/>
<realateName realateValue="report2" animateType="none"/>
<linkType type="1"/>
</JavaScript>
</JavaScript>
</NameJavaScript>
</NameJavaScriptGroup>
</areaHotHyperLink>
<lineMapDataProcessor>
<DataProcessor class="com.fr.base.chart.chartdata.model.NormalDataModel"/>
</lineMapDataProcessor>
<GisLayer>
<Attr gislayer="null" layerName="無"/>
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
<areaDefinition class="com.fr.plugin.chart.map.data.VanMapMoreNameCDDefinition">
<MoreNameCDDefinition>
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<TableData class="com.fr.data.impl.NameTableData">
<Name>
<![CDATA[ds2]]></Name>
</TableData>
<CategoryName value="櫃檯號"/>
<ChartSummaryColumn name="櫃位面積" function="com.fr.data.util.function.NoneFunction" customName="櫃位面積"/>
</MoreNameCDDefinition>
<attr longitude="" latitude="" endLongitude="" endLatitude="" useAreaName="true" endAreaName=""/>
</areaDefinition>
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
</InnerWidget>
<BoundsAttr x="0" y="36" width="480" height="504"/>
</Widget>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.ui.Label">
<WidgetName name="Title_chart0_c"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<widgetValue>
<O>
<![CDATA[人民商場服裝櫃檯分佈]]></O>
</widgetValue>
<LabelAttr verticalcenter="true" textalign="2" autoline="true"/>
<FRFont name=".SF NS Text" style="0" size="96" foreground="-16749643"/>
<Background name="ColorBackground" color="-2953990"/>
<border style="0" color="-723724"/>
</InnerWidget>
<BoundsAttr x="0" y="0" width="480" height="36"/>
</Widget>
<title class="com.fr.form.ui.Label">
<WidgetName name="Title_chart0"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<widgetValue>
<O>
<![CDATA[人民商场服装柜台分布]]></O>
</widgetValue>
<LabelAttr verticalcenter="true" textalign="2" autoline="true"/>
<FRFont name="微软雅黑" style="0" size="96" foreground="-16749643"/>
<Background name="ColorBackground" color="-2953990"/>
<border style="0" color="-723724"/>
</title>
<body class="com.fr.form.ui.ChartEditor">
<WidgetName name="chart0"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<Margin top="0" left="0" bottom="0" right="0"/>
<Border>
<border style="0" color="-723724" borderRadius="0" type="1" borderStyle="0"/>
<WidgetTitle>
<O>
<![CDATA[人民商场服装柜台分布]]></O>
<FRFont name="微软雅黑" style="0" size="96" foreground="-16749643"/>
<Position pos="2"/>
<Background name="ColorBackground" color="-2953990"/>
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
<![CDATA[新建图表标题]]></O>
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
<Attr class="com.fr.chart.base.AttrAlpha">
<AttrAlpha>
<Attr alpha="0.75"/>
</AttrAlpha>
</Attr>
<Attr class="com.fr.plugin.chart.base.AttrEffect">
<AttrEffect>
<attr enabled="false" period="3.2"/>
</AttrEffect>
</Attr>
<Attr class="com.fr.plugin.chart.map.line.condition.AttrCurve">
<AttrCurve>
<attr lineWidth="0.5" bending="30.0" alpha="100.0"/>
</AttrCurve>
</Attr>
<Attr class="com.fr.plugin.chart.map.line.condition.AttrLineEffect">
<AttrEffect>
<attr enabled="true" period="30.0"/>
<lineEffectAttr animationType="default"/>
<marker>
<VanAttrMarker>
<Attr isCommon="true" markerType="NullMarker" radius="4.5" width="30.0" height="30.0"/>
<Background name="NullBackground"/>
</VanAttrMarker>
</marker>
</AttrEffect>
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
<Attr class="com.fr.plugin.chart.base.AttrBorderWithAlpha">
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor borderColor="-1"/>
</AttrBorder>
<AlphaAttr alpha="1.0"/>
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
<Attr shadow="false"/>
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
<Attr4VanChart floating="false" x="0.0" y="0.0" limitSize="false" maxHeight="15.0" isHighlight="true"/>
<Attr4VanChartScatter>
<Type rangeLegendType="2"/>
<SectionLegend>
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
<LegendLabelFormat>
<IsCommon commonValueFormat="true"/>
</LegendLabelFormat>
</SectionLegend>
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
<VanChartMapPlotAttr mapType="area" geourl="assets/geojson/image/自定义图片地图/自定义商场.json" zoomlevel="19" mapmarkertype="0" nullvaluecolor="-3355444"/>
<areaHotHyperLink>
<NameJavaScriptGroup>
<NameJavaScript name="当前表单对象1">
<JavaScript class="com.fr.form.main.FormHyperlink">
<JavaScript class="com.fr.form.main.FormHyperlink">
<Parameters>
<Parameter>
<Attributes name="p"/>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=AREA_NAME]]></Attributes>
</O>
</Parameter>
</Parameters>
<TargetFrame>
<![CDATA[_blank]]></TargetFrame>
<Features/>
<realateName realateValue="report2" animateType="none"/>
<linkType type="1"/>
</JavaScript>
</JavaScript>
</NameJavaScript>
</NameJavaScriptGroup>
</areaHotHyperLink>
<lineMapDataProcessor>
<DataProcessor class="com.fr.base.chart.chartdata.model.NormalDataModel"/>
</lineMapDataProcessor>
<GisLayer>
<Attr gislayer="null" layerName=""/>
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
<areaDefinition class="com.fr.plugin.chart.map.data.VanMapMoreNameCDDefinition">
<MoreNameCDDefinition>
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<TableData class="com.fr.data.impl.NameTableData">
<Name>
<![CDATA[ds2]]></Name>
</TableData>
<CategoryName value="柜台号"/>
<ChartSummaryColumn name="柜位面积" function="com.fr.data.util.function.NoneFunction" customName="柜位面积"/>
</MoreNameCDDefinition>
<attr longitude="" latitude="" endLongitude="" endLatitude="" useAreaName="true" endAreaName=""/>
</areaDefinition>
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
<BoundsAttr x="1" y="1" width="464" height="538"/>
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
<![CDATA[新建標題]]></O>
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
<Margin top="1" left="1" bottom="1" right="1"/>
<Border>
<border style="0" color="-723724" borderRadius="0" type="0" borderStyle="0"/>
<WidgetTitle>
<O>
<![CDATA[新建標題]]></O>
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
<![CDATA[1485900,761760,761760,761760,761760,761760,190080,0,1141920,777600,777600,777600,777600,777600,1141920,761760,761760,761760,761760,761760,1485900,761760,761760,190080,1514475,761760,761760,190080,1485900,761760,761760,761760,761760,761760,723900]]></RowHeight>
<ColumnWidth defaultValue="2743200">
<![CDATA[3238500,2743200,2743200,2743200,2743200,2743200,2743200,2743200,2743200,2743200,2743200]]></ColumnWidth>
<CellElementList>
<C c="0" r="0" cs="8" s="0">
<O>
<![CDATA[櫃檯資訊]]></O>
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) = 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="0" r="1" s="1">
<O>
<![CDATA[櫃檯號]]></O>
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) = 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="1" r="1" cs="2" s="2">
<O t="DSColumn">
<Attributes dsName="ds1" columnName="櫃檯號"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) = 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand dir="0"/>
</C>
<C c="3" r="1" cs="2" s="1">
<O>
<![CDATA[櫃組編碼]]></O>
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) = 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="5" r="1" cs="3" s="2">
<O t="DSColumn">
<Attributes dsName="ds1" columnName="櫃組編碼"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) = 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand dir="0"/>
</C>
<C c="0" r="2" s="1">
<O>
<![CDATA[品牌編碼]]></O>
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) = 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="1" r="2" cs="2" s="2">
<O t="DSColumn">
<Attributes dsName="ds1" columnName="品牌編碼"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) = 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand dir="0"/>
</C>
<C c="3" r="2" cs="2" s="1">
<O>
<![CDATA[品牌名稱]]></O>
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) = 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="5" r="2" cs="3" s="2">
<O t="DSColumn">
<Attributes dsName="ds1" columnName="品牌名稱"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) = 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand dir="0"/>
</C>
<C c="0" r="3" s="1">
<O>
<![CDATA[所屬業種]]></O>
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) = 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="1" r="3" cs="2" s="2">
<O t="DSColumn">
<Attributes dsName="ds1" columnName="所屬業種"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) = 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand dir="0"/>
</C>
<C c="3" r="3" cs="2" s="1">
<O>
<![CDATA[經營方式]]></O>
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) = 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="5" r="3" cs="3" s="2">
<O t="DSColumn">
<Attributes dsName="ds1" columnName="經營方式"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) = 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand dir="0"/>
</C>
<C c="0" r="4" s="1">
<O>
<![CDATA[櫃檯面積]]></O>
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) = 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="1" r="4" cs="2" s="2">
<O t="DSColumn">
<Attributes dsName="ds1" columnName="櫃位面積"/>
<Condition class="com.fr.data.condition.ListCondition"/>
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
<![CDATA[len($p) = 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Present class="com.fr.base.present.DictPresent">
<Dictionary class="com.fr.data.impl.FormulaDictionary">
<FormulaDict>
<![CDATA[$$$]]></FormulaDict>
<EFormulaDict>
<![CDATA[$$$ + "㎡"]]></EFormulaDict>
</Dictionary>
</Present>
<Expand dir="0"/>
</C>
<C c="3" r="4" cs="2" s="1">
<O>
<![CDATA[合同號]]></O>
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) = 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="5" r="4" cs="3" s="2">
<O t="DSColumn">
<Attributes dsName="ds1" columnName="合同號"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) = 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand dir="0"/>
</C>
<C c="0" r="5" s="1">
<O>
<![CDATA[扣率]]></O>
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) = 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="1" r="5" cs="2" s="2">
<O t="DSColumn">
<Attributes dsName="ds1" columnName="扣拿"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) = 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand dir="0"/>
</C>
<C c="3" r="5" cs="2" s="1">
<O>
<![CDATA[供應商]]></O>
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) = 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="5" r="5" cs="3" s="2">
<O t="DSColumn">
<Attributes dsName="ds1" columnName="供應商"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) = 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand dir="0"/>
</C>
<C c="0" r="6">
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) = 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="1" r="6">
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) = 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="2" r="6">
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) = 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="3" r="6">
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) = 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="4" r="6">
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) = 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="5" r="6">
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) = 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="6" r="6">
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) = 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="7" r="6">
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) = 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="0" r="7" cs="8" s="0">
<O>
<![CDATA[櫃檯銷售資訊]]></O>
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) = 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="0" r="8" s="1">
<O>
<![CDATA[項目]]></O>
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[条件属性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) = 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="1" r="8" s="1">
<O>
<![CDATA[一季度]]></O>
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) = 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="2" r="8" s="1">
<O>
<![CDATA[同期]]></O>
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) = 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="3" r="8" s="1">
<O>
<![CDATA[扣拿]]></O>
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) = 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="4" r="8" cs="2" s="1">
<O>
<![CDATA[二季度]]></O>
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) = 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="6" r="8" s="1">
<O>
<![CDATA[同期]]></O>
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) = 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="7" r="8" s="1">
<O>
<![CDATA[扣拿]]></O>
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) = 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="0" r="9" s="1">
<O>
<![CDATA[銷售額]]></O>
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[条件属性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) = 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="1" r="9" s="3">
<O t="DSColumn">
<Attributes dsName="ds3" columnName="銷售額"/>
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[0]]></CNUMBER>
<CNAME>
<![CDATA[季度]]></CNAME>
<Compare op="0">
<O>
<![CDATA[第一季度]]></O>
</Compare>
</Condition>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Result>
<![CDATA[$$$]]></Result>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand dir="0"/>
</C>
<C c="2" r="9" s="3">
<O t="DSColumn">
<Attributes dsName="ds3" columnName="同期銷售額"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand dir="0"/>
</C>
<C c="3" r="9" s="3">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=B6*B10]]></Attributes>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="4" r="9" cs="2" s="3">
<O t="DSColumn">
<Attributes dsName="ds3" columnName="銷售額"/>
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[0]]></CNUMBER>
<CNAME>
<![CDATA[季度]]></CNAME>
<Compare op="0">
<O>
<![CDATA[第二季度]]></O>
</Compare>
</Condition>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Result>
<![CDATA[$$$]]></Result>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand dir="0" leftParentDefault="false"/>
</C>
<C c="6" r="9" s="3">
<O t="DSColumn">
<Attributes dsName="ds3" columnName="同期銷售額"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand dir="0"/>
</C>
<C c="7" r="9" s="3">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=B6*e10]]></Attributes>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="0" r="10" s="1">
<O>
<![CDATA[利潤額]]></O>
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[条件属性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) = 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="1" r="10" s="3">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=B10-D10-234]]></Attributes>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="2" r="10" s="3">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=C10*(1-B6)-322]]></Attributes>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="3" r="10" s="3">
<O>
<![CDATA[--]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="4" r="10" cs="2" s="3">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=E10-H10-432]]></Attributes>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="6" r="10" s="3">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=G10*(1-B6)-221]]></Attributes>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="7" r="10" s="3">
<O>
<![CDATA[--]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="0" r="11" s="1">
<O>
<![CDATA[利潤率]]></O>
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[条件属性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) = 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="1" r="11" s="3">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=IF(B10==NULL,0,B11/B10)]]></Attributes>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="2" r="11" s="3">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=IF(C10==NULL,0,C11/C10)]]></Attributes>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="3" r="11" s="3">
<O>
<![CDATA[--]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="4" r="11" cs="2" s="3">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=IF(E10==NULL,0,E11/E10)]]></Attributes>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="6" r="11" s="3">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=IF(G10==NULL,0,G11/G10)]]></Attributes>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="7" r="11" s="3">
<O>
<![CDATA[--]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="8" r="11">
<PrivilegeControl/>
<Expand/>
</C>
<C c="0" r="12" s="1">
<O>
<![CDATA[月均銷售坪效]]></O>
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[条件属性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) = 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="1" r="12" s="3">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=IF(B5==NULL,0,B10/B5)]]></Attributes>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="2" r="12" s="3">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=IF(B5==NULL,0,C10/B5)]]></Attributes>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="3" r="12" s="3">
<O>
<![CDATA[--]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="4" r="12" cs="2" s="3">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=IF(B5==NULL,0,E10/B5)]]></Attributes>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="6" r="12" s="3">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=IF(B5==NULL,0,G10/B5)]]></Attributes>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="7" r="12" s="3">
<O>
<![CDATA[--]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="0" r="13" s="1">
<O>
<![CDATA[月均利潤坪效]]></O>
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[条件属性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) = 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="1" r="13" s="3">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=IF(B5==NULL,0,B11/B5)]]></Attributes>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="2" r="13" s="3">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=IF(B5==NULL,0,C11/B5)]]></Attributes>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="3" r="13" s="3">
<O>
<![CDATA[--]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="4" r="13" cs="2" s="3">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=IF(B5==NULL,0,E11/B5)]]></Attributes>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="6" r="13" s="3">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=IF(B5==NULL,0,G11/B5)]]></Attributes>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="7" r="13" s="3">
<O>
<![CDATA[--]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="0" r="14" s="1">
<O>
<![CDATA[項目]]></O>
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) = 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="1" r="14" s="1">
<O>
<![CDATA[三季度]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="2" r="14" s="1">
<O>
<![CDATA[同期]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="3" r="14" s="1">
<O>
<![CDATA[扣拿]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="4" r="14" cs="2" s="1">
<O>
<![CDATA[四季度]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="6" r="14" s="1">
<O>
<![CDATA[同期]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="7" r="14" s="1">
<O>
<![CDATA[扣拿]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="0" r="15" s="1">
<O>
<![CDATA[銷售額]]></O>
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) = 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="1" r="15" s="3">
<O t="DSColumn">
<Attributes dsName="ds3" columnName="銷售額"/>
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[0]]></CNUMBER>
<CNAME>
<![CDATA[季度]]></CNAME>
<Compare op="0">
<O>
<![CDATA[第三季度]]></O>
</Compare>
</Condition>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Result>
<![CDATA[$$$]]></Result>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand dir="0"/>
</C>
<C c="2" r="15" s="3">
<O t="DSColumn">
<Attributes dsName="ds3" columnName="同期銷售額"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand dir="0"/>
</C>
<C c="3" r="15" s="3">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=B6*b16]]></Attributes>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="4" r="15" cs="2" s="3">
<O t="DSColumn">
<Attributes dsName="ds3" columnName="銷售額"/>
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[0]]></CNUMBER>
<CNAME>
<![CDATA[季度]]></CNAME>
<Compare op="0">
<O>
<![CDATA[第四季度]]></O>
</Compare>
</Condition>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Result>
<![CDATA[$$$]]></Result>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand dir="0" leftParentDefault="false"/>
</C>
<C c="6" r="15" s="3">
<O t="DSColumn">
<Attributes dsName="ds3" columnName="同期銷售額"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand dir="0"/>
</C>
<C c="7" r="15" s="3">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=B6*e16]]></Attributes>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="0" r="16" s="1">
<O>
<![CDATA[利潤額]]></O>
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) = 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="1" r="16" s="3">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=B16-D16-126]]></Attributes>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="2" r="16" s="3">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=C16*(1-B6)-174]]></Attributes>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="3" r="16" s="3">
<O>
<![CDATA[--]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="4" r="16" cs="2" s="3">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=E16-H16-382]]></Attributes>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="6" r="16" s="3">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=G16*(1-B6)-313]]></Attributes>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="7" r="16" s="3">
<O>
<![CDATA[--]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="0" r="17" s="1">
<O>
<![CDATA[利潤率]]></O>
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) = 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="1" r="17" s="3">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=IF(B16==NULL,0,B17/B16)]]></Attributes>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="2" r="17" s="3">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=IF(C10==NULL,0,C17/c10)]]></Attributes>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="3" r="17" s="3">
<O>
<![CDATA[--]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="4" r="17" cs="2" s="3">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=IF(E16==NULL,0,E17/E16)]]></Attributes>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="6" r="17" s="3">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=IF(G16==NULL,0,G17/G16)]]></Attributes>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="7" r="17" s="3">
<O>
<![CDATA[--]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="0" r="18" s="1">
<O>
<![CDATA[月均銷售坪效]]></O>
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) = 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="1" r="18" s="3">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=IF(B5==NULL,0,B16/B5)]]></Attributes>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="2" r="18" s="3">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=IF(B5==NULL,0,C16/B5)]]></Attributes>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="3" r="18" s="3">
<O>
<![CDATA[--]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="4" r="18" cs="2" s="3">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=IF(B5==NULL,0,E16/B5)]]></Attributes>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="6" r="18" s="3">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=IF(B5==NULL,0,G16/B5)]]></Attributes>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="7" r="18" s="3">
<O>
<![CDATA[--]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="0" r="19" s="1">
<O>
<![CDATA[月均利潤坪效]]></O>
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) = 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="1" r="19" s="3">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=IF(B5==NULL,0,B17/B5)]]></Attributes>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="2" r="19" s="3">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=IF(B5==NULL,0,C17/B5)]]></Attributes>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="3" r="19" s="3">
<O>
<![CDATA[--]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="4" r="19" cs="2" s="3">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=IF(B5==NULL,0,E17/B5)]]></Attributes>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="6" r="19" s="3">
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=IF(B5==NULL,0,G17/B5)]]></Attributes>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="7" r="19" s="3">
<O>
<![CDATA[--]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="0" r="20" cs="8" s="0">
<O>
<![CDATA[樓層信息]]></O>
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) > 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="0" r="21" cs="2" s="1">
<O>
<![CDATA[樓層建築面積]]></O>
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) > 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="2" r="21" cs="2" s="2">
<O>
<![CDATA[1802㎡]]></O>
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) > 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="4" r="21" cs="2" s="1">
<O>
<![CDATA[樓層櫃檯面積]]></O>
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) > 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="6" r="21" cs="2" s="4">
<O>
<![CDATA[1054㎡]]></O>
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) > 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="0" r="22" cs="2" s="1">
<O>
<![CDATA[樓層經營面積]]></O>
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) > 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="2" r="22" cs="2" s="5">
<O>
<![CDATA[1594㎡]]></O>
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) > 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="4" r="22" cs="2" s="1">
<O>
<![CDATA[樓層品牌總數]]></O>
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) > 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="6" r="22" cs="2" s="6">
<O t="I">
<![CDATA[16]]></O>
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) > 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="0" r="23">
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) > 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="1" r="23">
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) > 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="2" r="23">
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) > 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="3" r="23">
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) > 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="4" r="23">
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) > 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="5" r="23">
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) > 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="6" r="23">
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) > 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="7" r="23">
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) > 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="0" r="24" cs="8" s="0">
<O>
<![CDATA[樓層服裝所屬業種情況]]></O>
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) > 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="0" r="25" cs="2" s="1">
<O>
<![CDATA[編碼]]></O>
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) > 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="2" r="25" s="1">
<O>
<![CDATA[名稱]]></O>
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) > 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="3" r="25" cs="4" s="1">
<O>
<![CDATA[品牌]]></O>
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) > 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="7" r="25" s="1">
<O>
<![CDATA[面積]]></O>
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) > 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="0" r="26" cs="2" s="1">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="業種編號"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) > 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand dir="0"/>
</C>
<C c="2" r="26" s="7">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="所屬業種"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) > 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand dir="0"/>
</C>
<C c="3" r="26" cs="4" s="7">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="品牌名稱"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) > 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="7" r="26" s="7">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="櫃位面積"/>
<Condition class="com.fr.data.condition.ListCondition"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.SummaryGrouper">
<FN>
<![CDATA[com.fr.data.util.function.SumFunction]]></FN>
</RG>
<Result>
<![CDATA[$$$+"㎡"]]></Result>
<Parameters/>
</O>
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) > 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="0" r="27">
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) > 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="1" r="27">
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) > 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="2" r="27">
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) > 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="3" r="27">
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) > 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="4" r="27">
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) > 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="5" r="27">
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) > 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="6" r="27">
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) > 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="7" r="27">
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) > 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="0" r="28" cs="8" s="0">
<O>
<![CDATA[各經營方式查看]]></O>
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) > 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="0" r="29" cs="2" s="1">
<O>
<![CDATA[經銷]]></O>
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) > 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="2" r="29" cs="6" s="8">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="品牌名稱"/>
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[0]]></CNUMBER>
<CNAME>
<![CDATA[經營方式]]></CNAME>
<Compare op="0">
<O>
<![CDATA[經銷]]></O>
</Compare>
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
<![CDATA[len($p) > 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="0" r="30" cs="2" s="1">
<O>
<![CDATA[聯銷]]></O>
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) > 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="2" r="30" cs="6" s="8">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="品牌名稱"/>
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[0]]></CNUMBER>
<CNAME>
<![CDATA[經營方式]]></CNAME>
<Compare op="0">
<O>
<![CDATA[聯銷]]></O>
</Compare>
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
<![CDATA[len($p) > 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="0" r="31" cs="2" s="1">
<O>
<![CDATA[代銷]]></O>
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) > 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="2" r="31" cs="6" s="8">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="品牌名稱"/>
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[0]]></CNUMBER>
<CNAME>
<![CDATA[經營方式]]></CNAME>
<Compare op="0">
<O>
<![CDATA[代銷]]></O>
</Compare>
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
<![CDATA[len($p) > 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="0" r="32" cs="2" s="1">
<O>
<![CDATA[代售]]></O>
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) > 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="2" r="32" cs="6" s="8">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="品牌名稱"/>
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[0]]></CNUMBER>
<CNAME>
<![CDATA[經營方式]]></CNAME>
<Compare op="0">
<O>
<![CDATA[代售]]></O>
</Compare>
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
<![CDATA[len($p) > 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="0" r="33" cs="2" s="1">
<O>
<![CDATA[租賃]]></O>
<PrivilegeControl/>
<HighlightList>
<Highlight class="com.fr.report.cell.cellattr.highlight.DefaultHighlight">
<Name>
<![CDATA[條件屬性1]]></Name>
<Condition class="com.fr.data.condition.FormulaCondition">
<Formula>
<![CDATA[len($p) > 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="2" r="33" cs="6" s="8">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="品牌名稱"/>
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[0]]></CNUMBER>
<CNAME>
<![CDATA[經營方式]]></CNAME>
<Compare op="0">
<O>
<![CDATA[租賃]]></O>
</Compare>
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
<![CDATA[len($p) > 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.RowHeightHighlightAction"/>
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
<Style imageLayout="1">
<FRFont name="Microsoft YaHei" style="0" size="96" foreground="-16749643"/>
<Background name="ColorBackground" color="-2953990"/>
<Border>
<Top color="-1446671"/>
<Bottom style="1" color="-1446671"/>
<Left color="-1446671"/>
<Right color="-1446671"/>
</Border>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="Microsoft YaHei" style="0" size="72" foreground="-13421773"/>
<Background name="ColorBackground" color="-854279"/>
<Border>
<Top style="1" color="-1446671"/>
<Bottom style="1" color="-1446671"/>
<Left style="1" color="-1446671"/>
</Border>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="Microsoft YaHei" style="0" size="72" foreground="-13421773"/>
<Background name="NullBackground"/>
<Border>
<Top style="1" color="-1446671"/>
</Border>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<Format class="com.fr.base.CoreDecimalFormat">
<![CDATA[#0.00]]></Format>
<FRFont name="Microsoft YaHei" style="0" size="72" foreground="-13421773"/>
<Background name="NullBackground"/>
<Border>
<Top style="1" color="-1446671"/>
</Border>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="Microsoft YaHei" style="0" size="72" foreground="-13421773"/>
<Background name="NullBackground"/>
<Border>
<Top style="1" color="-1446671"/>
<Right style="1" color="-1446671"/>
</Border>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="Microsoft YaHei" style="0" size="72" foreground="-13421773"/>
<Background name="NullBackground"/>
<Border>
<Top style="1" color="-1446671"/>
<Bottom style="1" color="-1446671"/>
</Border>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="Microsoft YaHei" style="0" size="72" foreground="-13421773"/>
<Background name="NullBackground"/>
<Border>
<Top style="1" color="-1446671"/>
<Bottom style="1" color="-1446671"/>
<Right style="1" color="-1446671"/>
</Border>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="Microsoft YaHei" style="0" size="72" foreground="-13421773"/>
<Background name="NullBackground"/>
<Border>
<Top style="1" color="-1446671"/>
<Bottom style="1" color="-1446671"/>
<Left style="1" color="-1446671"/>
</Border>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="Microsoft YaHei" style="0" size="72" foreground="-13421773"/>
<Background name="NullBackground"/>
<Border>
<Bottom style="1" color="-1446671"/>
<Right style="1" color="-1446671"/>
</Border>
</Style>
</StyleList>
<heightRestrict heightrestrict="false"/>
<heightPercent heightpercent="0.75"/>
<IM>
<![CDATA[]AXh`@;bbk%Wq7c8V1Wkh3_22/.>f6M5c#]A"H4SF4>mX5%3_0iZV"`_m#sIp6hFXXH!m(c*n*
T_ZkF<XWchW$$BCD6GZ`dN<f!VYDT:Tbt;j&kt?+Y9>;H#q_n(KXHi3d?F/0mWn4#t"h<S+C
SSnP,R]A`=qt1jX]A^]A;tY:'dsJp544mq:kcJK&h?Y@ljKXC>&+935NClRIJbY^Nn*<#m^5,lW
Gr??1@$Kb]A%ikI>%(%nC>>B*5`O*[4HJU14P\bNJ(m+3Q_]AF-=,.R(Cp`nf*'$gj+;VEU!<[
\M"a6Ka?VV8Q?9W5+o7M4`l!ki<8>>@"_SptJ1F#uP7.Wf3ZL+pGEJE#5bI<g`8[_&i?JdR*
77KPLi);U2L+NVZ$$q;RKsf2(YI;!LR&=oCVsplFKpY3NQrZL<!ENZG$aulcW9&2jdNY:<Eo
67+KE'I\C$f.4A1[i1?`Q/i51^DHYJ0"Ka%gjj)nb0]AUm6#!d2^CMfg7_U>Kn]AWJ&^NN`:R^
1lF:.IOH18gH'+UW0]A41NgN5[l]A37j%,3Vr=-LNu]Aj3;/Po6J&Jbi'jJQI,6aXl`RkZ"?:P?
,2UUemnF\=kkNDjD+lE/b&b?hpdjgEmf]ANV',p#$QC9r^bP^+]AuP5%,NePa'h[F)X#-9pEA!
c:qo+tk_/MaDN6kqcE[Ci=-L47bl%$FfX]A%$I>*gAV!c/ABB@ibXf<YnR_Q0rVoPmY2aP_MS
?o8t,q_Bmm=Jc%>%^G7rKmt]ACH*Tj2gJA>fMR1X7e\JK@Cl%&ffeW6\X'CH:`3(.1B]Aram2&
=.K@p?427dU,RM8\W`k15>iF(ZBD64'Fs1CCm<U`;g>O#)gAKt>TQ%M3i#O4f"-E[H4KD#\e
T?Wc2qqdYi]AX8X>R"NG[XLi,87=tOt)[cB@q,'P^.%;]A#T]A6^-Cq;u]A<c-H8fo/G7nS=TO)k
-.`g'4Z'*0i9qCi/=:YAE:[k]AMIq&.WFn='OMhJml/Qog!p$(e%ZgjV;`JH;UDoiBCJ.W:2,
PUItc_)N.geQc[o(e)h90U2j^+G>Q&XW$Kni41>KB'H";#e;dlW=%/g]A?YHY(f-[`=hm?rWs
]AS.3bnqF"2:+c7mm!k\n?kl3lf@e#]AfH-Lf*N+sj$Wgi'BX_DPG#b<9MMV>$b"Ku'Cu#Cn#S
+hVhd5@g&m&D\>Dn>ZSATofWq_XQrB*!Ki=LMAa>!/aMa.48k4mu[<ls)MK(KWVj.q/ErkJ:
>83iY9)Pdmd!m]AgqCa>AleZuB-[Te$"mgmo^E#?RUWHdm7A"ipJAg^c\n[g+,4@Ji!4-BE+D
dkRhoZ-pmIp4K8<cGY.$#e48rpAC(@J_I2^j',Ze)-:pLrMW&O>Q$f:hTfT09IRTegG4*DDR
4)^\:-'CYdTo1]ABI>=..#H1Yf&1C\Je6(`=@`DsPiB`)hdIidW=gfj3![Hi&;^$cqGdi^JJ!
D/M'[=t"uTo\\g0;77XDnpb:^i;*Bi3n=9V[2N+/\*Z(Qs4+^&W?MA7NF0AfDPtjKJP,T;a)
2dpP296o]Am,]ApRWZU]AH_%&;:d1sa)XuIMrg@EK9WA%pBK`52HZ,6)it3X808dr$'qD+F`VlD
RMDSa-Na8cn#Mu4MDtcH_o0k314]A,=N/)T30iX0t5^=ThHUQ2;%[n>uLa9&t^nmYs,7NEGB/
Ph<9Il4cEF0Q]A5*K-kB_X=:n0/7a"Bj]A5s,u/$S3IYJN=*osR"-q+*TN8GB=QebEnN(?]A&`^
Hs+Rp8_Rp,R`eDR(.?0bTKK<OKP7bsF'=D0/@>dqF_kOW?UOAB.a)6P"EFVn]AK09>"W?ab+r
)/>N:_]A&Y8]AS8QXc9orKors]A1TDNfrce4"_?&C#CfULK6=mYE4U=Ui&SrH*$%oRdd&(m*G_G
$8B.oHY@/7D3KZR*R0C$11T;lI/63#?n83a#:^0^*HA0.[',S0&&U&VR1(gk@$Z(_<2%/8MH
VKY8,7@'@M^f:3pW4F$e#hf2&3co0/3>@Dm;+42c^PdsBK@PT2gi8@90/GkEI?QPUHi/*^Y:
IGEZmc]A^RaZ(@O0d$1FpH8;^[8*-@2>uiFM>(u<i^?[k!8-mH<1K"r_dt72qH>PT+4P1H$('
[4+X\$$:BF!^+.m\q3+<QRf`l3C^CQhtSFfUO9_"BhdfICh6X=>f^o"DUKP<po:L&,00&l#f
I?cj<Q^jaV1KG@<r-+HBktW#.puuHbDdk[9]Ao0N;PTQ!M&#q/L+TkhgGudEXepE`1s)Hbbk&
4_*5q!QrJ<n<,b,grDP$m6M3@Z<P8&G4uhNRebiCR52g"ok5lCk!-0g=*13^d$2"#P%c5(Z7
qEr0-iZu-nN<'[P(fT!F[YuLfZ_kYn3Y]AkL=#*oCgZWk;j(LehC2c+C\mA'#ERr?GgNgO);i
7QB]A[')[TD_Hmu6r!'tUS:b_hY$_h`;0!/O#6I%;Ap,@8HW#UN44N<Xd*I4g!M&Wmt-80/Cq
1Jn0adA;mDq3MtTkdeu4*Yh1hf&1/)$,C7\j]A!f\c"]A+IrY"\<kg%j.P?_$:-M4/Eo`):QK[
eFho&24Gln[Wc;i\$Ue\bB2O$#0J$7[=-#Y]A5m=JR]A'O1p!rVQDSU/fY0BmQb/9./P=_\:$6
Z#CZ9's``YGjg;Vi'@[-=S(Hf&/#nih,`[d0nnai>sQA5=:V[]AbIOoh0&EA&!Uk$%)8bYkES
,8lp^kTghe8Ke)OB7;u$R,Sr,fYhJBQ2H7"WpsR3t!pb,p%S#m;A'0!N!d9r&97KH>.$A*&*
idKpKAkVV2lf^FXh98f'H/%a)N@uOPmt";e_Z]AM:-#[%&U&L*(FABeb=FCLk[OO`E%ojH_&8
/4]ANcfMlFKTiM@iAhYKZ$$n*=?,c1pOs_eZ`BpbZgDn_:r2^ea*7d>!i('(opk[!0J2]ADJ-l
m'?`+8#R3l#L[OqReglbLDJptQF-'koL7=]AcP3h`\JB7.Z,?T&<0s1ITgidTS2\T$4oc0=!`
3"-IsS[C5P?!@[Bl7e*3:VjT;//>6@q0`e06"9?J*)T.UT-c4TtALi!PJ_GKh83_q_.TeRpK
?Gf1+T.[n]AQJd=EG+r>Q3ABuh7k(h`52aM^,%jYI0cuJc)=a1G<#MAq`_06Q"EGNJj&o$bAG
UX+W/))%#^#_@>.MkRcCD(/'A(P+.1eLW1rmIFNHWW'[VFN*A1MV^5$f0rO^I8Os'[qY0,d^
H6mI='^=1_H-)u6,5<\0LC`!n(D6g0))\!8[AR@tJZFTG-[R*DfMMpSA=]ARH#X(O;u:ncu,3
T&:HfJ4qo&hl6ImOkYk_Z@VbBD"RE_bK,&YO12#,bOaVi_#f>*.0Og@)R5Zs&l=GY^CsWl8p
EWg#M`JU;>oAsBBcE@fnfSl;Ko[AW>4-f9cu8X(32I/5UbA]A'l`%JT$u+SZHj*?K9SFp9UN?
@Bk>WAOfeP@&AVL?Po4FXEX-akUhG#!Y6`f(X2Gb]A]AVL]A&J8.B#1%+lqBs@""rsm_h4@nkMZ
^8>632h]A8G_co#CWe30N8G]ABjRV2Q'hQPMH'-u<S+R5&nLM""`;r5YHV>gL5?kGV<X:$64X1
<BDZ\`%p?K_ur9;25TD0#&eUA"2ddmN5*&M8;7fI#8k_Q8bcGlt$f,R,]A:^6(FEmhCVkH6Eu
)c-J*gqZn'-Kf\U=L/mj#9J7pVkeSppD.5Hp,K(:QQ;,VQgnf]AFL4Kd'7NTLG=kAJ"DjLZFi
@("d6.%YSeKT:0.%U(WgDCgO^tB1&Hl!W9)p@KaJBpudh;_Gk$#Z=/(E;d48/8%AK-0cBT.;
U^B[$<\"pMS'np^>e1o%aPn?CtL2bgaE8N$WKK$2"Jk+*)`Qa-7>H0jJrV#J\rGTOX#j'pKj
?k]A8[cf%4G/M+D.:"H>a_gR3e"^lB$[7G?N&Q;k$_r0'5?PA\dt.[XU._]Ac(qaJApatmfh'd
nj&Es*q_l]As5BhDO>%)BSl:%5!c2[H5f$;2@7D*20XZSn=>3-Q3Ca*G2$rbjJcP;\daUhY&#
"2E7h\.A.B'QmlIcC4s#$06+,:]A3S]AA:^`agM+OhmdNn8gp=i@YI0:fbCHJ%F=e<^eP38[ju
5EbY4,#pf,VQp&/erUiC?8KpqNS.Jt*#[1)^n;P'+#KJ%'ZHB18+L!?5>:Sc$fl6i@&a[<Z<
R<o`ZBh0=4i?5,/6:=^\lNRB4j7N"Q@9HMef)$tAM]A7#MAZU#B0jSA\<2f-nG$l6'%!fPsf\
aI*V4ub_KD7E1_Y8-NgXg.le>H9ng4N7\NS1u+3W$&?V+1&94!pck[2h-=&edNCDpoEZXe3e
t=o$E?1I;I03B[qT7=QJ08^Du\A,^iA[ofs<^Lgs3jMq.gui$K]AK@kKgi_"D5`f"Q[XAh:QJ
ZGEh)E9:l7FQj*Te<Jk-e9".%F>m(ha%ZZCP6f'9M@o-cO3@oia,0Yj1l)o@q;#r:!d1b7\F
BI@FLSg2P[@AthO/&3-iDi<;BYr:PT,@6iiXI*8'IMnD$4_k?:lqKkdD$>K5jYgbC%X1SO@#
SE=dmJ/qE1qfl1P:ru$WU%OdbrN6II7;\MY6WK`R-2<5!1W*0$DrI&8:7jr'R_t0pS4?f73:
G?$:8Y^*:3aYK-EpYIt[]Agh$Y8@*tbNt/6.;3o(.bB\gI:0N,8Nup+(0Y80k&[h<M`c_0Rs=
b%p*_#/DN=9ej0"2Gke=7p*FVZkPYHZO,gL^W]A/3E0p0"0%9(D"dFF[HFYG`#@HM:Eqj8S9-
hG>GKX#SE_X(<VCjgt@C^JQ)0S'@=A4(D.Nm7G.ZpCk<K16/r&?nc?<.o7kRZ6ZgYoRa9udV
UA>W_i&f9BR\d&oHYIhZl?39:#>8aruoS]A5`+X3aIXrX6J=coVh<C3ib=kJ9"C,_$ls2SZf*
Q]A%LtL<R)hrW1u)<HHZ3^QJUeGB0FuNG49q^.Am@D1g(>jEU+cpj?mZ^P$IU,1nqO0C[4..F
)+=XLB@1dD8?Y^CI[(pHkV"_i4Ab%.WDm68B7W6Eugld>dLEFr-3"OaSTqYm.+sUUOI^'g\M
>27eG;N,>uI^[85WZ:n(sBr@Z9!X777%T5Pb:'tp^bl6iJGl7"mQL=SlA$f<kjG6*iJ>:`id
l5.:r\*mNeHM;#eIY]A-sjkBkkI1NdLicG0i6i&.E?V73LZb3D!ZRE1'BqIRoK6!^3S6H]A$4G
V-+bMP<Z\;CggD>@=)he2<#eT*s0%8-'<409$iGo*Y>![JfLpmWoEoSZ'aM7]Af.kML)3[)F/
$\5A4U^ln)Q8j!#+.Wus`hgA?M0(CWHSgI+WjD)O>B1k'm.ojG7+U:;%o7g[NBs&g::$PUq(
[-G+3b^FU\N:$(5"2ni\M@j!<s(h0kd@lp[9dl[T$+cMmV*'@3t&jA_:14M,eqXuUdLPYl2.
A/*j6Q?d^q3*psP]Add4!tU]A"Yo!U&r:C#G2I#PmW2,/5_Ac>n7GN`*EabZO[TCL$Q;!UK19t
o3SY)8V`]APs3#IVe/;,2=h(upGeS^SdDk0t+)4!iY:15U\8ZW$r[?s4_C6J^g[!;VE,Di:Gk
Tb4q^CL4bB,J^ceG3Z,(/f#$DA3n]A'33)ZW=JGm6i^m4t$'&2KIatnMo=dMOY.+:-OK!`X`S
#p60Ae[dn'Kr.+(oBT@OU#@3\BOGpAhV1=p^LE(6X$9q[tR!Ea%n(XNZK/eu[)>8Q4oXahpf
XF(nH[iao#pupGCG-.WB:l#t@IQfdJ#]Adlo*R'Xd7&%5Iti+^e)O/0NcT?1WOSFq29!%g\--
^ZdL1EgO.$]Ap*'b*6Z,o'p*hq0M>9rA]Am1Of,-hMo4`D^sOY$*OZWd.e2(Eo[[J+0;sn?jJ^
!_jY"LY)]AYIXT"CafH_M7Mb*>(`Dqt?;Qb1_AR'lDtbKjdC\k"@]At&p%CjqL\MJ)>R<%=Bq?
H8cD\"1_B^&4KP"'ohEo\XJm%K&8#Y@DRT)WuamYi:36dJ^<Z#do^mn\(QI=j+Liu^Dr$hKA
T?-JhYT1-LF>TUj=gb*@'GF]Aht<pq<]A:)$RjckEB$>jh=]A4EA$%@$3>([Qa?6c[NF/!sr.Eo
Vjcer6Qsc*e<dP%Xn0DV(7J.JFRE,g%$DlGR#q;Z2%35"Q8Tg/:OCTX?lf6?2fjE81c:KFHM
rt5M2<;_<@%K[,g8@nV9g[BW6^^4uFE.c>W;&6\;^9]Ase]AGA*fNgj:4,N8$tA#![0'L9eBW=
",H$b,?&j@5dAjPjRfjiD-bbn&isIXXc99S2t7Vg:Tl1-++\R$h]A:JB@%Ka*AuiA);+@J*Z[
0st=ZAu0!HfRoZe2m/qdn6#0.<3?HcQ9?:[t0sDpF"qbZ8F!O`3>RIhQo;Hs>^XV$>66*(lE
QG^@a%o`GU&8m9LsGaC50H2]A-FW6-BdbF,K8BdYUs,&%T;e^qf.`!(k*aZl]A#.eV:TPntLjD
=Kp<C_oSeS52D0l)6_5[M_HddG*&IB.Pe[_"FjsC/ku9pIN;E<5]Ae1#\\b,dB@j8)/d-\dQ:
\I%$iU)M>2:kQ8\7NU<G(]AgVOI=c[P-6B\=BKlSPhW=M[EW]A1*m8ketLDn'06%94f1rc\nIU
#SA7`fPs"seIMh)qA#r#5aig$BXGiZnD6cU>j"S2XN/m9qRjFh2X:s#AlCi1fWiqN[0DtrE)
Fi)k^q.r;[[<:[\d.*m+ZJS-9j:@kqH%+*.Xm[-H^KVBrDe7=;rOA<I"dmH'nOJ"%\L6?VPa
23"rT9s#F\fC5gR]AHR>4<#QT!:d.a.Y#b-3'\<GCj>u9=>/[.<8l.16-Os1u),."\e>7J2aG
pAo5+'HLi\.rO;`oa@t[X!`do_J+A*H01P-^QO8#.8Z_AFd#/0=uA.jLFT2?T3hts"5I"oWk
.$F*QH.J>'RkAt%`BrclTNB!M/nTaV?-+69?(,HLlEQt?T*9*P1+!hg6apYO#3Gr9(>J<?<'
G;upel>r>Db(R2BU1>'&'q@1>M#$n#j&`C"Ap8fqD9mZ<\*OA_'Fd7?hY$]Ak$.^Ah+o5e>-%
G!HcX?<rf@PLs]A-&"%UDUKn_:S0X(eOu5'R[7F,sfG;B1&W84a7>?J+]AnB<1g2c$fi@l"KEF
58]Am]A3@8l7ZN]ARQcG1750fOa2JRtS73[6a<.jc3ksO(9"@pu72%dFl[=*_9R(hEfeFP9W(&P
&i9E%8!jS7*)eeOD+`]A5DN*fV!Rg9Vg0^Hd#X,n/m4,0*4mSjChT<:n02aV@gPm?#]AFD^Kl7
t)*km;s3L/5k0e5o<A8&\&MhKOfD3E)s1[O+@70BK>9V41,j.lIgEb;IZH,5(N\9^7&kDRt_
iDcFE-'YqN`a02A9)*=p-P?#0ZUG6f\$_CTa_[IpAd`YQEASu<)H!tLh)+aMQ2288lZf_T93
/sd5EM."*8,V./)OH$hD+eB^;`@u7ZM*948,Mt6g6'boZ=>`D$rd,c@h=@:u_V\,T3S4R/A"
#$:4k;igpQAK*:M8jnT2gON$Z+Z!joIXa(B&CP(kb`tT+/)sOW>=?J:s-2a\6/!uI635`c1d
W_5R;0Lc>mYZOfdLQ1sC)gG@Jnq@^@VL4hYAp6'$b8<0i8OucKb=1$J\XhsHac3?)e9U#TZB
p_4'q&MUh8W#4)*c%1_niPbSIA2fAk=-GuUkdT/)kf.O.ro.jUaf,2TFk+\MQ?9=>F[!T44J
%d.&TQ&iF[l*c"r9N;ED$DD<Jq(8aa%S;.PmVuh$BUtc2(N4K,R>lRQ:KBB?rBN">;C>LSem
Y;>Y68G@S?M3NR1>_[[ZZklFo:#T#0%X4n;$n2YWC7pBmg`<oJN]AMr\U^#msLX9.BXhp0c)E
^a3(Pjjf(pj.,u;p%5qDY7\8i[$ORJ\bY^TO^kI[hr_/l<SLC.@$lX_U(u@0MDbV?jfab<k5
>b;'K%sr3H'\YZecIaa1Ijl*%d%N^VRQ;*[uQXu'`?848M,;>0E(:27CSS$EN>q17i"hL6lY
^WksYBG9$H!pS+&4E1+o<2>B-@21=I,W8%d!eQPpYjc!kcg3>,"0f>2IhV=d\]Ae1M)%G$`o6
n3UB[(1i--<804ZL;%FNG*^ku=$+\[G""+nT8hU7S">URZnI'/o+XCJ?k%8mUCEtKD;n+#Ae
l`<NP2U2H?"+Aq-k1-Nq2$Dk,=7Pq\;M7bp*lIbK'tR\p^6EoId:S8<Vu%_Trn34V88(F-eD
1(RWl8<H%T*JDh"?JjVn7deE#$/3iYj9qXGJGP*YdiQ:i:QBIrrHaI&6q.m]A5[?W:`j]Ai%&h
">2*CS=G$l2gCg207]A>=-V<$<;]Ad5aGN?1U*WRr[T,\a.uRRfRin.&A@D'.,gMakl_D"FF@&
Z[aIS'WO>1)k=))GmY2u;\W<FNsS$9+Fd$ce3O4I7R@r#=W?h/SkL8+p>-Xm@Go.[q%&f*Pl
,kBo_7IIDfB/>sMI*YR]A==YTG.q/C)&`/m9>*5US6+W$3/$['r5r-00E(4t>S[XFHk*MmZmJ
FtD+FKWR=u?##1U]Ak=m$ZFV+Ji&G6W#M96P?HJMG-Aq/Z@/PDaanj([XS<4*l0+K/+k[S\P-
m4VJL@<<f<g7lA67WT9`g=VhB7B#4!hTP>Ip^5:##_34&?N3@2-_<'Lrr_!cRfQE\[Q?QfP-
73[JW]A!#,pZLO3j+cJsrrJZ$jE8#q+M,Q%*E+`dHn=1?^J7$?YpfQ1b'&2EkA2Z:*>SLoQ!K
\aTLu?`UKUJnL]ATb1`o\6ud>F:!c*a/=0gB8AVnm<'A&G;[FWUYq#&8Ln"ac([;l(85Mc6B>
n/k;EY5b;qKp[+0G\m.DLji^)^I\W-icjq[Nab.r*=3j7]AT5]A5T3F=YZZ(UbD`Rc8;V_:=/!
dT+aRlQ*(a3uj3Ch<D"#a^%#.#H?#CQ43\jlEECY2dj=e!2(C1-]AoO&/c-q0cUd4YPb90(N\
CK5;8[d1eF8Z>cnar2E+2SkpGN@7cqjo!ghV-G`3KK/<,R(]A'oCLULNJ[Q+ftk>RjOE']A*`K
0FTf,dls\e+F>UR%A:>[Ds!_=`3,B*pKRbm,>_L^%H2Va/o:#V%S.t9c;K'f$F;Rf8(m&X]AA
%o5VHro>(Se(D;H8/SM$OV$eV'oS8a"ZF+[W>8cb`@58rNceb++CcC*W+dh!GLC6pA*:l,u$
6CeYJptTF6OIEJG1GTr.lr:sK2qW.M5f?7\EZ>GEnWE-1iZ+rsN,(`ar05gCHt'GhAN7,5?Q
mS,gs@$*rq6gD@W+$I[3u;')q7g0P"D""6JH@Jnk4F@[:h^534]AboFON(srJ6(%^%-`HEuG;
MUH-4<;KK\<_0>;hb99C&<d]AXW%B0d?^it`%gGKIPCA(-2n3"fa"n*j:YTJ@%G^0_3-^q-$?
b2-n_MrX&<6:V@^F@CCO+p1Q<,Gmmn/q`4^;!j]A3bUt4(W=9WPhG)X:clm#`DsV@\)>_\K%;
^8bqtb.IY$N#]A,o;VU>?T_9S`:eRb+4*a9MqS]AHG.pJ$C&)k5kua\"bKah3;&UhP>n6oL"?'
s06FVHe_psWL@)N"9Z_b:iODMlElC^(,)ER>F%M+S)Fc?mdhr#nWhf86p+A'SC;:HM#JbnVN
WpZC'H/0eN[7KQB1T2UJmZ;&0N*#kaSe\IFI4Hb5+72T@B[]AY&N43_5[5h#N99B8]Ab:/n+1`
PbB!uu*PKKC7i[ntU2"RXT\A"mJ9Gf?1>Zf[er$qe"LUPt2fiK3>Fl+O8UIqgNd&]AJ/mLVui
.!@bSf`=;TqT-u3eW*WD;LU-55)f6qb:I;Y0Eercfq$mRRT8JqTI1'p+XZHY40DSqbUNlf..
/Gdde7I;ErT0=)o'3IXu@ar(,PgAZPBsdBHlF2d^iT,^o;qnT:#lBu`/gBfL$ST_&Mt]A1V:H
KQ+5kqqT[eFI%T5$]ADccosB@^Pb[CAWLgq5Q@9q$U+8]Ag:IWW#@4ba!@sa]AEh;uc9JtD;.8=
ZLYJiJq0A4tf[LEfr4oU>!:[qNZ`21#DpW%un6BVJ$=\tYb53?;CWc`:s_Ri)HG8E;?3ed7k
"eQ>hY%;p-"X3VVr-1K8&I5$6LH10;j(_gtr#7klT1%&9(JUD%ajhn1=mV,3j0<349Q#K6Qe
LJF+7_Vgb6Jq'>)F%p)>TneCG9@2?q7-obf;n;:3S?7>8ju\[,)Qf'9HT/eIKr/j_>N=/4ed
UELW<hCEi(CtW(\`</t!*mr%(srTZf4^qC3VZfKs/%jNhpG_K(/M_T9[?#f?SE_/mLN<[fj4
>B^`\o&):oEFj6'=_;\mW-m-,)&ZEMY3dethM:UO!c2kP"R*WSDR2162-j$!r.K6qL^WFO$8
48K6d6M"5$`EdQPl-*F"/Qt+)F;;Ua+,#nN2\/rgO`%6XRU.!QiuHD5haXh-O\.0kb%[a:k^
@Uu_Ia?!J+LA7r?^3'Qm[*c#Q-IH"qgpGI>8'I.?Jm\;_5$Jt$Eg4*XPIjsp8A30fr^RXo5e
Q(S:GZj7H^<rp3F$Mug#kpOu%%,EI"KhI@i$upei"nLYa]AtCch@bdfi8=7e$NH7-mr;J\L3p
OgPh2Z&Y8@q@;Cf)8MTbTo/AZul-3o:R@8V^>"!_HNg6Lt]A$.Btd,+s\c\Lpq,6.mh>H(eTY
![0g3^CoK+\u>c0iZ4H]AMF$5?AOACCYIC^&'KfI(E5'H0-2WsYrqK.EpZk%AkNK4hc'3(hCd
d-lhl\]A2D^K:8C$.G,pmTpopdYrFGaY7:1AF-EW9N\lQe9r8mthTQbGcm1'@@cq+J.G36ukf
Lbb&n[guBTC%3,@Q%*97TquV-`pT.u9GBa,#]A5?=e"e1NB,4c<mkZ=fbEq!4k3-bp?77Acu5
HsA78pr36EuCPUZ&dU\HTtXjWu9tDKm)LClVP8nNH/Oq['3`#FI:J>+PGV/m17AMh=_j(15.
Cf>)Ytg:+$D@b81gBaQ$210D07Z[p^*@Bp??&@o!EuH"8=Pd,uKbI/U(T;,?$i-Wo<te39OY
U$#$rFAB!s(<qf]AauNF!=[`JDI:LNL/;qdWD@kY!np5k?-EB#iGp\235D4aeejl7:O1Hld;3
LM*-(pptaojiYQ+D5N:6Y;7KDCgGDUK/Zn2qWg34V4;h]A*2HA_Tmb2!6Rs2km7=C("hr4LVM
Y1.SOc,9BM,eL($9nMt_r]A9<ldSQ]A%u6a`[B=&R1CkigAh&[(QC&[=JF!Ylq.?(Em1jfIW_G
s<ge=<E*%G`N+Yb]AIL';8"YaM:CU'j/ZSZj%a%+?@jN8%)tRcQ40R5HDaOA6Y,"LG4+?RkMV
2o)iZcqFH`"W2/M(.@J6VWB:_)+=$Lp-\E@4GW^fJB6o*.)KYa0u&<WTLYYU>gSdEb'62IAQ
Nsp]A1eUK&9#'!/GkRRWI1Ag0;\`LEpQSe7BUNK,DnfEQH^"7WC5>4VJ%Nb_2\hl"G$n9)VWc
_O.&!*_/Yhk\=s),:hN?&Va0Jq.NNXnl]AGg"/O$7*6Tre//DkXZ_N9\inK4l@AR;]AMJG5q*E
g0!/qio<![?=^':OHh`Qm]A'TCQBjU:plXp;7'Ckb5isRK5Iq#H1Jm-K-N]A;lH#KGj#3/\#<L
f$?$>hI`0(IViQ]A+,3g@<r9eT6=hHe]A>o:?ljhIcHT0XZtm@7##nPA$m'lR+<hQc8BZr)*g6
HiIW/]ADK:R8;/AkZC7gB<,e*Ne#L\FkSei5?/M]AKfq^U\96@U?>"N817/&omlj8A<)._GY$@
$QW&<*2sfHp7%Oe'@od;0"NRLck^\%eL51tJHVG#$$Ssko[tK,7`jkE>npkH+q.Va'YuIm@-
g$mWc=lqO(ej,RYKk]AU9k[VE)e?Cj%=jRP+s90iZQEi"8D\f[VrJLebdlJ6rd<;`(C5;$iD8
F@*GJRQ+2iMGDq()JA73!@4@%4m`'.l1uo;gq@TOX*Ot]AR9>9ZMV"@q#i$DRB.PO_%hRE`Z$
tUE*%'%5Y"_Dl8.&Os%*Di)*^r#2%Hhno8<9*fUBg[>7S=7DmRk#Z]Acg1jTm4(cJDX2]A"eRt
V\<D%(a3(MXmI/D>I'+i[ilojdOBFpd)HPK0[Hmb&G6/Q\.X)ZILs6I3;c:"`N+;n-AbbDt]A
8<+W79[2SZ^E3T]AFF(6II**8%%K>+*?FsKsDpSfEL9'%m1'snjB$@6@=8nN%7d1S7bg('6UV
4?$1uJ?7]An>dL6*N:T^Q(qoDsacO*nuE/(;$g<IsDH>LtjP/><V`HAV!tT-9H9WW[;C5lO5a
1/1K6SBrY=8g7?p9*)*/>ofF7ebQi=G(:<f^8hs9A:fc9"VnNf=d3lPD0L(fLLh09\f"Z?QW
jP5'8+?OK"n!rm,rGT=3H?F%I8gOtGJ3>]AX=S[%CR)=k;P%9W\h%PbJ%)IR>pcQ59*_mc9Jn
ptPh1*Y.p@;d%%P"tWUaloHIGS/>/!1&r+PP<nKY!2+,pPI*KJ7KK&bI-+6II%s,9U5EO-!=
\872rG[6m_B,.0p;6WfYh1`l%["gi/QPYDgDb+NN^mb[[CY7?Kb5?4U$G#J=PsaY>V9?._1f
&mTRSDN3qt<RhqN-Vb=@9clk>'?-[_5_Kp[QhQS*k[(.#7W0b"9ug%N(PPSi@9q$E^[f5.eW
@0J"tnp2@#;m[Gl>5,+hTm_?7#1TpChDo?`Pn("S=H^P`&)^FOKPZ-.Z<)%He,[RS2ih6<Dq
0"mdRrCJ,[rn3&-$>^bO4?<0190Y[=ZDm%S5hG$?&;^@QgYS@&,)'X-M:7jhm%shMo35lh-!
(cWn\Ys))dl[i(5#rms_N2rC<WZ!"n[PG>_HD%!U+_,QN8%/cAA._gQ4m]AKa`-1p9"8TW0A+
)'6mJV=":'iJ1Cl:B;GeRAJ-O$b,S-6!T)4:<a0%Lq>@+:m6R85de!+W,WfqGr._=F`6/WIA
j+%#@[EMq7?$>mB)SK!YrYE?hutgG'^4M>XdafA#eoPIW@uF`PKrh:;<SS5r&^4fG,jI")AC
nKt_s-WpVo3OTtg3nU:A1hl'0*OU*#hh1B%^9667*IPr'FmWIEAcOM`G0";)PT@P0rM,:9sS
6,-lbgT24gHHjs/`828GkArr9gfqBUm?pgd7,aiiGB!;./+/c[i4J0mIj+<SHKBE<*YN(V4T
5"X7%Eb]AfZm^dE;WSGK*f@bO_%DHS^rcNTXLLHFM?jp/c2lhQNE?lqH_&*Nhc&ohA4Qs/bBb
E)EGP9PMT4A>af.c0Gg\C!("tHp'jRn(!NWf$CuDi>Z5/lZ7a?7ba(97TYa,Wo!?JjR)BeS\
J_U-g/.]AA9"mI8d71:.53jJ`sT)oH,^q<%-#^BG`QGVY9a=\X:ViY_UN7^+eC(=C-6]AQC57r
P7]A=#r:B/<.</#k".3UQXV7Bn1dAtEJ_"cRmNtF!OpNWMEWJIEK&_t[?3P6s9V5q\?HEV/af
>OcN7`hA5.g_E>4>`GQAaj0E>OY@@HVbPJ_'@X&kOPYmV9>mjcI"n,/1@I7%cFt9O4#MeqP.
1T&-4tL12/GQ:_9PVRT$<O-sUf%L"V<e)1!<?k_ds<nS1'G=^j.6:3Lr!XiBsT3B[JpY2a:Q
*aHb;#D5uM76akaDsE0c4S1Xjht:1B<q#qBd^-]AtAAiOFeF&gagU/t?p7#f)#2KQ>LOSK=Lr
U$%iFaX6'Jtn7>h*[j5#C,i3KCn^;^q>qMY$pZQAKSH?u,<*D=qe*k8+uCG1f&"heJ+r^/%M
a;/q/gs/7"Tm_l)l:h4M]AbqQEh9ngCh40!E1S/L'kO8=bFI/=c\/cZI]Aj7IFRHF<a?,QTN@4
Ep+*4ADI-A-]Ald*:sV[.cLNarBEcS`8VIkY9I?4W`!-u%+i:`g#AMPeU<[t(q=IgR)Mu^?Y/
:CjjNm4\ncKD$_R]A9&kk6L-'ll5,/utaC'E"uML+pUgB9+TOF:aYl)Pfa93(qa3_qiVllUo2
ZECUs1>ls%KRl_M2j^u4Z9?NpCh]AIoM]Alo9UY?NA$qcecjP2]AP\N1TpZgL5qpmSCKYKU4$J?
IN85kJs%9#&e:!?iDH3)U$fSp&mkZ3;`%cgOF9b86Q$2S=gg.ltm<(ZUI^TjAo+iDA6$\3a$
Y6T"uX<Wm2GI020SV`cjK>X70rR+0buDgn^0nkHp\/io_n=?rMC0la`qkH&VV0,45dL'hP"X
jZL2dPC+OM]A4WsooP7E9C.^NQF)]A%H.aIgj^U7F48*^XH,oQL@)Jk)BJiE'()Up++X60X_!/
3I`%I9l2T2j6L:ebS%Lh4(M<'7Lp^b]A@I:$mZH'@E&V_!th=&l<o9@&>8g0*/5/uj1+P399@
&@"uSYN'08o)=N]A'c_R[;FEM^9--?e6,KE`><TgXlOB^+q0Y!JS<A4R4>l'VFT4^31p2-VRC
br)*Cu@<giZijc,t[+#!&?\9\Ai/AHS&3?^PtgQ[ZR<\=ttkj6QCS\ub-#DmuMY5DDb^(/p]A
+\DDqA>?pbeqGMJT2L_Tp'4s`EMhs/Zi;ckj-E$BH_K[/nC>+i?oJTf*WP/#[/?<Hti2'm5m
.3EWQ)k3Xb'X)Pp4s)anHt4bK;#Ta\#X[bN;C1r%!cT6Z9>K\YBXf/\t10bh(dDu11N6po([
a4e1#h_kDqA0[1^03'&JDS5O@("SJ;YHeF)7G`Kh7V_-V0-U6GJD3"gll*6)O^4PX5:9pV><
>cfg]AX.6*M3ke%h%t\`l-_nljY^NqHXO-=%.Gh0/V=PAm1FCO9AgOqp`;bu[pe-R3+(3o)OS
,JkB[;Kg!b@iR>Y4XOKY+o)p0<1U#Yp@''BN2Yrk:jE9(XFWk@B]At76\ipf(AG[]Aota7G0*Y
TJVDYjq9U7V]A>Vr6C=,kS&h:4?YNImBThiL![#)u0k&V_6p=2nlJDHdp(UV3)(a@TW2s,MI4
W0aJn'=H>8L>>*i_+/*qP6J"DJ3/%G^EH1m@$lE<5X8VRep.k%tGCkeCQi"%jlJ$eR1PEji0
ab"d]ABY(<9Hk2cajX($L+/=CBI$hlbaq`XjhV/%E_5[J1r?Y3Ci0\*W<WZ??"N-X_Hf!^1u"
e)h*Gj-j[D=K.-lO?M7!LcX!?\5u*BB&4cDPI&kY[`S1QZ7#og$0ETcO#W4pO6%PQ2ZhBr^;
H[0RneG5P=Wd>h4p\cM58RgKrHH);"H/Kie,_uW8&4J4)DJqZtU^U1bnSc8+BG2!-TA;Da#b
MO3eRG"-98p^F1&4B#T&<!i7QaKC!SWiW9^`:eZlOPF$?1mejt/U<=A)%1:!D_M2l]AOujjB$
p*s9@^;tGg>F,1E8Y1fM&]AX?Rg^,al3\6\%h,:3+VuS:E81Mo*\B5F7$LHL0CQ%H..\$;"D3
d;[;I`2G"MSL\Y+jokuIlGL)GW&!J"3@ODIkToeH<(Ah7C+\QmK.'m3DB%dTR.Fs%godir!V
>bsBRX<tn_#d.CQqB$9:gAM?T2'kH.hFdXnPsNF_?"?dlF$<Ji8(W3QDJM)e>bd/\%_g1:).
]AZ#2=Y>VCV`S2LVnVu8\0/uSh$2]A/HNgLn"G"eB(^b/?JnQCY4&@bPHuJop0[rj>g4saO6@6
h;J`T5ekY.UJ.+ssaiH8N_)$6@eXc-pJXrU6Q=[Lidud)*Dtg7Io0k7&gVK)pA-Shs<^jf?&
)Wo(/1J'o'YO_+[(%nX6=%Sr,Tf(_X80>L[6J*M=#G^>9O`HHK3+c>3O>X7+jIDI,2H"uZ1H
YbC)K*^&n:j-P2#>PYjI!K%DDP7f_?W>P2Y?\GVd]Als"g6%ph7B_]A,,T`aG+Fir2dMb,7.66
$@oc.a;NTCdmWMA*;@d@]ANmF>4kj=DGQUZ,l=6qSE2U5Vm;OgZ&&USu^%)$?N"(]AADsh#l>j
[`TqeH:@HhErqP$0'2d2D@3JgZU+1t_]A(X2(\Y!Fu,'f)e]AH3]ABk2A5se?aYK]A3CW8<+0JA*
L^2N,IZimOjpr?7*,[!Pe"NJCgIN@Lc)^'N;BX"#1/$]A9p]AROcs[&5hW`R]A%uhXG[&j[#k9_
4n<m(q5G(%N/o'F2lf\Y=7>P!Tj7QHp)\!-7q\)*/f&`#[DM:"aR1%;gamIGuNa@%"d3`bOM
=%DChmLb2O8@<;s*I=)i7EbJsc/"j\1kcg`(L6kFQXnmTL.GKUBm0]AD(O?r0A(!ImV\aSi()
o7ueT7IL3h*KqB=<N0:ah=7A!&+\/0<Z9u>d8L+0,(s(%/_h):,"`c9?D%BB1jC+V]A3Rm$0D
&".P<VgSE3O@O9Q<jl[>[8;GN%6+m;/DIQ/:CMm0q/X31<PcUMT:tk:$3M^6^g=TXe_B%n@4
J/<[0bWTucm]A'#oe+L*,e_.&V^Y.ScBgSSYb:eT"I.e"j"q"NoMAWO)gI'@,'h\BNbG>]A]ALN
*G?0#-LZ3IWG>FG+nfG9sO?T>S)leWZoP-PIb\Nc3)Vc)kPC6Sc?2ZPKUI4Y7/bud$$HuaW'
eF*]Ao"T,;OAB>7nS>3tlZ-TrbXA1M<R?Ga)=,*1%TaM3pbqd[W[9^6!Kb>>gb,@0@]A1)2$=P
,AIFqB5Rcd"aJGL[9h2;U0N'o%]AWoi@QlI@O"o$U6]A"ds#=rb.k9e$aVu.1gN'q*ZgehasVD
EZm9ib+D/.C<[K@Au.FZ"($0a=@*dK,#,ZViLeo`,Sn-IC%S[F5F#Y5&-+1Faq4s3@Qb(pt-
+Y^s?aBT@K4B%C7.mi0BpUA5E5RKgE=ekOP&njVjP8t`DA,]Al^GMq<0H`"1)8R^GC6^\l"b/
/-p5*8'/d.cV-o0hMD?d5"hBjL)+I+%SP^0MS<Z`oHbkX.F=rVnBF-.rc&5'd8WmT#*S406L
e1r#\=4R]Af,U8uj^ej@tIC3!2i1HpR$fA@m)1nRWqi=/!3G]A[U3dFJGGCQ,s2rO(G`WSH8lP
5OkIpT1Z>$aK_q!i=<E'9#$YP)hAmILNSh1.nn*Z,UfMJfQAKS3\HIJlW5U$im0l8'P-c8DV
=nZdKf@_8(8oT)q:/e\kT[;V^t)-MSrboV_?#kLBd,5g]ACC*$42[kL]AML*fLqRC%h$s`#je$
`mL1Ml/jll'-K=@&Ph^7-2Ed\#1_,n7i<O_"PBRd!(1]A&6E4k+$l7[_G\`c>8%ZU9`)7P6qq
Kp;Q3!_=,I5kBT*#Yj3!1POc?EpXs[lG+iEX=".33=S4fNL\i!%Zd>2p)KtW;'9A!-T9)B8`
l.FOQlS4@FEijTsRPAaZ%Y'^Y96;!mJ)i__GnETGqCSi.n\(NKAWDbdU_!t&mC88hgL^0Q'B
r8e,':t/*uJ;q`,Ga4_3`=&=>L\aX5A4:6cr"m_n8t2j%hh,9KF070Aca^?l%D]AEQS%_=RYB
%?2Kn32YnY.u.C>&<]AD"dN[h1*1W<bgipj3s]AY%7;HAOag:pqSeEHO+BhIdPa>>l&I/Vn>+3
URPQS?<!!qbI`J):+t"RUl+p!fLY\"g2D//U?/Ngo/5s!OY6(%&"6lK3+m$jEB7shc#5F@Rk
R3B7Z9!iap%NZV$&AOS;f'XgmpkLI+hhd']AM9aD_GcEG;lQo*f9+eb?ba["!O_>**f!BsbSb
l@aet3]A5)lUI`O9#X>2Htk]AV.&#D#`u\Aq;>+GgSW4SJ+X(nY3'$>C4'Do!IXp2W@Jp&C-44
pLBnGnIkD/M3f=>dC3(pD+.d:H9;Fdc)Wh9Z3<#4Cs^FMHe#VWLDnTFUVFBIWA@<QOZb.;Ua
U^a]Aoll4qXFSW_-'cXQt[ldN&aUj/m/\pTb?0ZgR(1ZMKhBHqbqm,UjR_G;dnj<Hr/[^\ct#
G5.VQF7Y-h!IV<,^\)[<[GCQV-IPbEb@CrDM7"XZ>Psa6-%uD^m^%=MH5XsJ59KRph?*SBZf
m5i<]A=WdLN.o*4+t5c2,O$hW;N@IOa+1,Z(1F*bm4?0`ZmGPM^UK(P-sZ8iTBWU9O:8*t(e@
!]A@Q#9a6>fL39KR#A)"e?4bY9iqj?p/2U7Uo&"C?H&]A")g<lNE:Sk^DC&;_=ci;GekSIC,fG
#0r"j[GkoN"B.'po;@pDWCU:*O[*u8DeCfA:)#TTd)R(QpIVNVXcS;&p91U9mp:YU>uEmu&%
9ph.&`"6iKBF[>?Z%T\N@T4o=>,\/h0b[Idb"7p1DpcjPjA:q[^[.\GZB.aoMjJT=Z/"DptM
Ef[=X</bGaJ>9(FR>%l:X.[]AgQB_a_PbB<>kn!.SDiQ;l1#jiN6'r,;3q/cqs@WIS%D6UQXD
R(Me&YklJ?@;@4PoNjo0_PP3nhp?;:WO62gWh[c5#?26N@U<#NVXMo-?-o0b.@<QGptq)YH<
u?ZL"EX#<Fi"b?Kt,nh8h)e@X9jA<$Dj4IiNKjaA(F1mFiF8";jP"*<EF;0F32/LYFMTXp%g
r.`]A/Gi>-<!&LPgosnu!MKZGqkdU$G;j5:H=>_,6I1TH%J`h^XeEMtIPb?+oItCh_O./ChpT
F!1E?]A#N%Z1C?n9X$T60_n,qim^!doN0*\`8kh_0[Kr8lKVaqg*;$I6%PV4l2>BcNjE3=?^'
4GHdR9"Q+:q3@@d4X\4=A[Zbb0Zn;gZiZ<pI)0r>XOpobN,4QM<mLeD`Bt5a7O+H"W:ut.)S
'$*DDq\G/M\nl,(sF%_[6:44@qOHfjFQRYqt``3o$$U$X%b*d0c=Dt>SSF-an,13r=g%;Xi+
iGJ5V0S+i:1dn*&;F]A$J;0_rEH,2?ICaRAi9D]AA-dKQj[gYPGE,9^&Od=Tg_BsRYiuR@<-PE
fY@EBc]AItZ:0qG['gSnNWeNV3eA7``C.VAMqVT^r:M-0a=PEjjdOr[B^%s8!9i'MNPpOSH91
/.6rS]Ad/(;.)DDV9uHH9o!sa.d=A+B!KC)-`52N]AdWN]ADkBcA>fgGdo6EV6pqiL!I+)6/3/9
LMT"!CA8@0Ldk[U,YN=:@'76?g.59IbNNkBs?Xg?GT<16Y=Z[md(B0YNCBX^c=14"B<e%=u'
0mF]Ao1hbJ`4;,7`4+'V(hSY%IT,$[:gC!EpFZ(F(d*8S`nV'<&t>ZH/FNMhH#.JLA<u;75Nf
FCs52+;O3n&Z83XbN5k`4+KFc_>rVBiAa!oQ_QaI,g(U#P$R'lR<\^LI-c(sQN.DZUbmPjMk
P[7U:#gb5VjWDW1*Tui:JZ=K(7i/47rbhR$L:obeonXqRQp9:J>6-Taq"=^<)FWqJ=D6J_0_
'@t3o`q.`AWhG[Q41O(3+R-21_?qepAP?Dp4daR(se<ZprGKSN67m,=g7Q+:6DhH5nlHSAb>
&Y&Q2l+SC+*U?_&&gCJS.PM`P+c2uU8V12HMdBYO+&fZ^PHAR6upVua.T)in"V5M2ldIY5uB
$>Nd4YBLQk;BY,]A$+g)EOClQ(3=1bIU&K/IcWZ+>4-n%:jui]A_l&^,B'd9Y$ains3,`YCpgp
D!#sW7o=69.gqNuE]Ae[]A01L!,?jZl+%b18X89?^(<M6,2p#4SJEFptj?0FB9OfR>n.%q;$/N
&h-OQ`&@]AUi<Eh#C:WSb3V4`A\kJOgIGRck+[]Apo(HZC(M/]AZU2Z]A+:2)*K3&LHHQXooj?fN
r604Ogfl2L(G;H9iS7T30"q!`PnblEo#NCQl]A=,u<42)1nKH[[b(Yf<<6^^\Vtd86n[b7Ku_
J6GU5XD@?16X1^3FiC=Us2^P*$96ig]AN9Glc?bTd1FI649)GFICn3K2/7M4Ha8Sn%;4abaa?
i83A*AE_O+H2[,a]A>lE6'94=\un4d/O]As>an-qdHU6L?(u5N]A:D;R#Z#BB[oA_eI!U=g<<@"
o8@k':M[t\&(o]A,X56%[opDPZ)Zf%U&iFEsHdZiB+lYPk<CXR3S8-*JWMC-C>%cEOCbAA:,E
IQ6&,)&$$^eR)P>dN0<$/_VN&esHj@mHd:q&:`\&)BV+$ZHTe8WL/)D8D\\noNK!tSiHRH/R
O79hTUZLRIR_Mit*?LFkG>5.]AWgu4oA!>Hc"ZK^@%i4_@/qYkgANphAr-qJDe#L_UYV6F0I%
5B.uoi>OZd'W]A^d7-pEF(Es4AMnbFtD[EESl+Dc2ukOVOodrI?5>dEb;fet-0mJZrIRND6HT
-^V\Oi34e"r!V%%k76%Uci'[58qr<:Lfe,-"p%7Z5S^EQnfX[FNK?^K1u!Md.,\hB*:')P1^
[qhjD"P!^:&tb^D(G05@CJoRL8hjK"bebiodZrSguT]AkW5t]A[)_Pht`*Jq[Ec/<U=okWG:?J
=g^-R]A%?c[apO0d;PP3)pImXX-OG-^qU@L<!p2>/=kj?(c<g/6!3:ufq'1j!_5ZNe3'W:\HD
)OZ(7__]A,5WYQNTrY3S*EQZqD>'&BUW&b4F:W$edio2`Gs4F[:3"-,iCi@(1t:9'R;nkL=j*
t4*3!q<*<t=O7t\?)g$b/5:l@l/0"dHa9,)pS(4:e*07QUo[q2%'-I'M`J7Q>dI8>c2.n:X*
TX*Jni;fp<%Qfl@Mn3pHNEeD*Hu'M,T53tX"*F4rg_\"5OQ:4bcLg;lEI4r^5Z*LUr0mSJg.
IJH[fhao1A3nGd`nqi)2(`&'3psIs$qHH`"DEeg90PjN6h+^SGo2M/Q/ua&;\iE6!seg%D&G
\AM2tBq^A3>isUF8[X0dIJqM*FbeS7^-o;ZS><ZtV>M\UX.LDhF1NEr.SK-a.HT'_s"5p*WF
d.=CL1<Aiq9^`E!%jR'bO&]Ad5(LebbjC?rIcSAJ>CN5CROk!>%)?-&bC:em_2V.80@K,f1P>
/_?J9FVNYPID_0K+!?BIG@ph0s[P(>Af&/kNN%iF8qL4>UFA!1.6''2L&iC7u5)@$l>^D`n.
Yl\.$LU?#>i,F%enbM%K8PhG[\enK"o<$O<ibYY[X:%24jFT<Z1=SUO.(_<m)5$)Aq,E&n!%
-_/uO<G6cBTs9C5[c2jXaLi0W2^Kr_1Z$f9^!R.K\ID:_b%M\*em(4>b>9(!.S^f*>SI@;/%
A*Kb-.!L>JCgE<+q^mT(dpJV/rFq,oZ*U*lX=+8P=sV3*baEqp9_2/Es1E9emK]A:t37n"Uo>
IuaT4:nZSPKm"=WNj@FCK(-K;X>ZiuW%o-Cm"<B,MCg^8)NW-;-A8^3VsCc`ejk$r:/2r5(t
$&(fBX:-_!HWUc)MA!1>qOJM$)q0MCuK=^8"Tq`U"::@&m/R0B0^R&O`'q^XcAY<H9o/]AX3.
*^[!ZcGrpk1^N"H`lSSp->XjG8]A%tEr^0n_+!r=51UVg).*m<^MVNZPe7NU^MSV\(,_uY#gC
D682K$#0_]A8gDap_P<;4pgD\DAc5*%r7N1[7+B=?#bA&$=oChS3+Ya2uEV&k%$fLXS4Fl]A8Y
qAHUr0\lV4BJ^)m\rH"kEi[>pA@0eabY[&]A2>_eUZ]A['c@r,aR(7M%H"d@aG*o+)H-Z!b>jN
ja1L7-)/T1k;BU0k!Y0N8\FMR8nLhZViNM?e.Ul_tbY\%PfA6$?PC*Lhk4'LF.-8XFVZHpU,
n##UJV\;)UjDS2<J(HbW*f%r+r`@CV^iQ'+9U::)CR:S#&`W&W)6W'8t)^:GF(G52g:Vm(jF
Jl,!I%QMf9GV=>FcNVI"7[@_XRk*DHm5%F`f%djagNjM>>6nom(_+b5G)/i,0SO2iFGTCoCE
0cg)dYSF;5Ak;ei*-%%'^X4'X]A51FgE9k5Rln>K91cI=&l[h)0:H.+0,'3i&R/+=S`g4`m$4
G9\9%dL7ENNI]AO*%7<':KD0f>ml^&ardFgoiH+C%m<,PE=7?*Q,FtNtg1DFVcNkYtVJoTJ*S
J_9bo4:i^C=T!JnIfc-gKM\C`d(-;C8s2n0R!Be/9Nn(kk8O//kU%<)38r9YG<s8-jgM9\+4
(K."EMO6+[SOe\ua0nuF;5UNs+;N\,D.]A,^[A+kshUMpa%`;[m]A-]Aa*--r2)K+)elU?V%9L!
9JCls7oI:J3nVA\K2GRTcXLoH42&W-tSfELtSeB%WnQ^YT]A)Xb-gE=TTDX4Y<RVVEp>"0M#0
9eVXQ`I"KN>2V'HGl>nU\iR`e=ELrd-a;qeXcXlT(dD/Yh=Nq-f15,WCbc1D3g.9qP-O[!tB
2BI2R-k:=r$4+$*$8tli6%GjC_W/fO\@B@l,CT.VmBh;,Ln+$AdeM`cJ^ngXNGcISd!'HLHn
bRF4D3mKE:rh6W$N9"nn`.cBS"77_.dOk+"5\?:qk!4L19Qt_UQnqC4=j`,*hneL)3XGU8uW
F:,j7H2!I)O:eZG)Y)GbU%^sH550%5QYif+;a=A(?]AI%,:[)c$O$K?*#1@h<9>fdBhkaElGV
>k#*,Km2%]Am:\qTXQg@r,n%Y!YeA"r'NJDn^#2#/+;_5NhKZ'$dU87C-`1Fg,Rgs>UgmX)[-
!_+geePp3ijhN)00kNb!&uRFhSEekF@!BNHs%EAZ#\UJ@/2cU+3opR$B6?>=UE\M&g5P^N@"
O:iuDGiEj,rSueL_bC([`ss<M\F[hHYZ?s_<YT'WQZHnp@igQp<UAR(kiW;q/5',dqUY`kf^
\\9+40ZRqH0gr6$/B$"mp$Sb0+1i;la[lZr&%S`XjNdrpr]A6eP#sXV9lkRQKJjI!_4fI@^DS
O2=QCdhJ^5t5U=<,1MkPmHYe#fi(qu/S(ZCD;9jWNgg>SMU%HV)T5Q@mL'YTH98b&KhtNbXJ
FUnBfY,@aW(JCE"SI-1IT>ROk5Lb_$g^c;FrTl2WZ\+6L7?`\%Dq3J>JL!(;P\mbYa&bJhJq
&%&nj3I%)_V/1.82P7Mh78*T5e%r)<FdCb@b549P(C[tiaP4]AIr&R*St-B`.[?LNu59G3DZE
/SU[Of.YFTqSli^K>@C\n(7T^+)eC4Ri[<ec/b)VJO@8oq@V>kA!XTZSGjj74AQ#Rj1#b^[\
&i]AZ3%5/;ItF_eJa(6Z<D8YmccpP1)g2jj0p^GTe763=dr#gKNhPfB),Aco*n_j_:[7?Nbp#
NIJjkJl=Qk>Fil(/,#/FhaRf:m2HdRH6pEQ"mn@%JE;6d.Vb"`^bGmQ>Lo:PNXk[jco(l>0=
"23gk:0\3c7-1e-6#+m)DsYGNr/+HR8?9$fh(sje0=gXL1;7up6m>9]AC69gU>@=T"hZaD?E\
=ah<u.L\Z"I6I<.#NPK4]ASAH-Y@$Z<t0GfE8HGC%=IYE_jV7Q;ESkiQOZ#(FDjR>bl8DK+*=
i3V'5W?P\Sm.i^LImcDorp+^!*fR"i@Y@A2a/kiR,i/^R*+2.1NbrFo*FJQYROAc*`J7,#`R
D53T0]Ad:GC)%Yd1q=.Z]AS2@=)8/Pa*7"@V^Jb[MB2:.eCU^>U%f$3@jS`Ukta/`N_8DD',C"
"XeOA5gLb2VYQ6J'q#s-s0uBl9fX+"5n7\!ioIr#X<i.0tdsOVboiVD4O45,!Jk+,#o1!BM^
I;J<ZO6-Pq?eWD%ft'O0QaBYFi/;4R<lqHo$uF_\Hlesq]Auc5L)P01P8Tci^9rl7+2DZuHTi
FL:_\/dMS[*+J3oIg'!YW2XY/(Q&[#4D0a<n`XUuq'6\pNl]A;tH$Ckn+GW^lhY`<o"\!6@g&
PB,lLiSkS]A^7pU9!FpP'_uX.k4_9l*Lc2T[8p:Y%qX9]ABeWFCZnm]A^GnFa0j1f4<R]ANd1sec
#?%WUmt'k#3umd]ARNqO7I/4nD?<o(a0sZ0r0=i6XAnT5DU![g(%5_=S$!0=Ug;tE47O%'3c-
(dFmm,R1b[_[e._kjDdUbA6.A6I1ps1`a8Cl_Hn]AB93%:c&)_h9fnjH`aO<)P1-$6r&neHDJ
NeEJ<b<pJA"Ut0bf*ALd%T_\<kk31J9""l?r6g5`FT_+W+e:CStu(fr[]AhgKN/c&IpriDjsO
_F`<W\RECF)""G>JPC+hpVIa3n[FkD_"4)`T>F-,R7>"Jh\P>lYp/5dnm7BW@hlOJI_@\<b"
3@&4u>[rNDB5R'@ca1jLZ;Oc9*:?^2&`L:GEr4oY98b[4:`D-Yk8H(WLE/[FD4N0GIDI@RRo
u@T_'4nMN$)LE2A;gdN-lY_,t_,ngq`jCg;:-;-Z>LVPc3V>@!1/H<n;R6otQ4#hApK2rb#E
Dc'9'@'Lgq0c9&1Nm13($[AKuj322n4FXj(9Qg9RC@g^tg>sTjf.5hdJcT5D"#1soY'8+-dp
W['MPbHS$SV=STTFoiQW=PqfHZ-Si\L"K&^TP<Hf7$>ia1*]A[pJ=RnWUrGuo,iObQU\`qI0a
rO7oe#cDVs2N*3MAO!$]AnR?@(AWEG$<e9W3#;@!*6FLd,"Mj>8kK+;pkP)a@2_1*copRnUb?
3Nu]AnqEp_b:lIpI3?C%0&gGq>eS*>V-R^Z'pAW7fn-m[AL!hs]A\aG"%G8[n]ALao/Z6sqB2^q
2Is;\B9^K<2_\$@;YsD;<is<b:1U:qqJ'$_cu:DBe?`Sp?Vm#,Cgg&q2LqiTQo*lElq1[*d7
'3XW+E.3YVPhJ_@WXC'BuL8J?Z6;k\Y:[qAUYCpTlW+F!p&UVS9%>":Pld'"^fu"E<l7rpZ/
nCF/GRk$_ciEEkn7Q&S@QSLO,1T^UVH?1'5"^YrmlmE<)hQc1qVlR3:%Rn,<j;7F'u8#cS2Y
?pm?)JZHhd/-'P<`/4<K.aeOYfsMi1JkM#H79qmQ^r@GMd$+7cC\Nsa/,?SY0NZFh-<1L"7:
9*74s&oX[@c1pR-1.K>pKP5Qm3:2[Xbr7A#"h,tb$W&L<qIg]AdB?T5TB/i`scg#J"d&UpY)t
H0kr:R1_Jf!&;&a;TCrlg6`1?A?&Ao$KBLb\X<F.eZ`^O^*"%0)3@Mn@mb+Nn#YleF2u_PeF
eon(TA8[6$kDD^pBr3:lg%rF3f;')&<k.J>$T"oK"A,_YY\YnI9e4j#D#\1N^TgK\pfNjLr:
NaG\ht`"3eQE,Ill$n'7;oTNb(lNP`]A#mdmWCF^Bp(rFCZTF+I;jDeD)-93r26.f$l_:")5[
oH)UKUVlK;,uo8jOI9"#ML_IW'RKsVJVeh_'t+3:H%Zg,^4iF@@7`OCFp&b,`LL1`L3h"f>F
'mY"I30dSB4$9>'$o6f`FF(s)bg4,eQTY;3:gESOJ:Y1'Va0JARS_QI9k]AG^\(jsXqJaejJ=
9Zm0BI;N4uUQYZB6!(T/dHmHcP#nep`jB5,V,ip`3Wfc\N5Pm8.R@CM"E(V)7@b+M-0[+sZA
AGDQ70*08>VJ6sLdSgr*X,9.nJlNH]AIN)j$6%6>sXI6L$sEDs$Ok9#oXBikI9m"DL!E;f<;R
X,3D"/n?#_A$M"KUbM6(cPZO*j1aP"(V/>cPFr!Po&=o'83!K$q!h"Z+74rEH&)FdakE_9iL
B]A'"Q3.F`hNOEcRP=^@h,^F1Wok_T02/k+/`2:0TG;`Xg#^)Me#r:rohHC(Ju+-,&;`_s8;Z
15.W3@8-#-L*/'j'qqIdX!rC2`5),OSlucE0T`Pi'YuJ\6Qlu/o3[ZF[dArfm'o1mAUB:,o*
*oabCmJ?O+[:K9K.5o2.qSCQTWOJ5E"GqOc3`o#5"@g[;)hM>L4L-\t'n6Zisu(@n%Qh`AE+
FB/M@,Tj1NHj&,uOgN*+(aY:J4U!B>i`?7hEV>m"]AkoqA4FI*PDQRWC(dXFhR!Eu88Z5RT&g
)pF/`qD[*H$/bQ*G+`HSJrGlXN<=7Q+>8Q&?#iaC7/;5Au%rkKq+1kPC#a1m4D_H_jY.2l8*
IUArn<Mrt(sYhMb-L&R%kA/P6!,nI$eG?hq9[P1CI763&9'h=Xqeck(3h1R(Ifka3hu/_C-o
LG?#IPN."'AF4l3`!O9HOV#/;14)FpOnHF!?JI-&X>'9t'rjsjaPL:X0iU$b*.8o$GO@iXhe
e:]AGtS7AUoU6s,Xit7]A"L\Neoi>I*/o?h>eX]AM==>OFqD!Og)lG_cj,gZ&PBE^.UaBUP7AcN
TPY`udMO;()Xug$okjhil\5EcM+@7$g`;q[b+\1fVO2-`.B)OD$b,'ngYo<.l5\Pnr*`Gii0
t$[m6Z7T,P<@hX5F-2dqB%f)/)n%He>mBlDMoAWl;Tgf&b5R]Ag-1BVA*TSK6H@M87a]A9Nh"&
[8Qh2H!@WaRT*E#L*J4/ViFP%L6\cuY(MAgR+Yu/cYSlcIgH?5<HPg8Bf8<6E[;jRXOFp!/#
mT;a^M%39)U0#!&6((sNfsl;@p=$83jh6X"!(]A@;gf7r2EQ"t'P#T#U;7m.@r$V+^M!Sq%j3
Yae&*"sl'7a,\J*/]A!\\1q.ba_,aedbF4AVGP0k4*(*Wm;5$f9np++7-n:"?qB$`,bcjFck+
J$<7s.MUMC!#=22![uY"nmrj]ArI+Q75K:_h>`P+D`j'dZ71NpV^L$@q*W:2<ta_801L5TcS`
YDPN<;Ho6-?iorjE\4Z#5]ATBh!GNC;M0rUf8<:SQU6`",":)MOSCgWhT2KP#Hj8U,NCiQ"4S
ld\(k4SP!W9DC7s]A.6/ii"Zg1W'p&aP*9W1b>O*GdJd-n-"?7S91S-XL_B8DW]A,kR3fe^*N`
\'Id1I!SKqS*^Jh`:*"5InoPk[@D>/(E*#1rcabgj5hW4HMA3`Ka(L\iC\jFCW+Ot4k:W0g=
V7`O#*H_m2#=;rFF]A?r\ht'IIG(ufkL.mdFA.\f67)<<WS$(<c$TGjb`Y_+\5IG6Cm'$%i<G
t>l*KljNqejI#f*\]Ace+$R\r5Th.s4S%`ke;LT:&EpnK'cR.`)QmM6f9$1eT.ZUl$>fNDXB8
N^6nk4h8p_GRDloF)ITl)M[7)1%6^nWia@nNX_bpT,b*:\I0^j*GP?8ll`$M\+dpb?.;Ws2e
jF+e]AFdm><9)*alqM'NY>r(LmXd2COuIS3$6##IbN6-tJ$B58LBe[e=n$K.A4#_&jR"piGnU
^ahc*c(IJgdX$GqN3]AA_jJ\^\s%/5qPGnJEc9IK+A&KVSFcce.dOZ6BlM*DGf#bgaRp1,ZfN
raYrH/4CFE'fso?!,]AhD$6=!rrQ86Ck4T9d*%g(;Vl0n45?=TY]AT17-?K$>Db['rd?8Oq6*J
t(M!FJiasOPQK@m<0<mon*&e!S10McR\><P3,:)dI\jn"("OhYQesh_4l1Cer:j?Z.4t%ch2
j,tXq*TUtKYGF_=UiKbJS#WZO5[pQ3k%S^W_@Y-i;-gJg!g"C5,<#/^c*2M!^1D1s)`YPZ0g
p^PRpFhqQQQOcXX>RjE/C(+oW0fU'>`!UHBD8B%UJkWlu,K:l5Va2Q@2U;qE-$ne-ubq[)-B
WRD!c<i;EV4=ZnGe]AUeAlMhAWAiMpUB;BPYH5?H!lnN#f@*8=\?]Ab$t(K^+7iK6oAeV/\%ln
.V*ZA8A0BmUKRLm8(+\Ig%_4Wd?a<M$?5!+A(BX$F=9SSGZtciH5L+)YRW[f4AR8o3#F2?0R
L:GsKrO!/dn5/d]AT^^]A>K!r3r]A#[)YW6Rfd=R!n7L$rhtq[OI-u,r1u_Cpt4f2eP!TImX!?N
r5kBYl8b9+^i:'o071ZN9&p;kBuc-`rBa,SNL2'k_(fWFeR)WoVXs,<u.`"att<gIjUJ-!Z)
ca@-:%"Hb-Um#hJtC#0Y8?\5EKXePQba]AT/8aRZ+Y_X*M0H(R#%6@O_:EIXJC;1o/+3$d7YU
%;Pueem$BMA;PZ[>Q`AmWP3I:5'U>&g3)1hNb""8H!d\,aL,C;)o>O,_p)QQYt;Lu0GOJ=Nd
E+na'?Weih>DYk@>;;k29Iu@9(&b;[NkP(6o;U:uk9OMFOf(Mq<:-1?a3nMZ1'IGb"#,WnB%
hFPPKkhR($4%(KX.2fso6>!("1h/:@`q9?")10^:8<Q3;ANjS9E^0G$l1^B>me9:N:9AH/(M
Lt-uJ*BsmGmPANGat*"cu$=d?AMeW=P.gZXn>p.@p'X)lE8AYj4)No6-@3F@h<Y:>rN_ER"K
_K2EMB3Fa1B4n);$RSt<C(4BuFlmeq+<e[i0<iNrGSViLH$D.>9)6@3bc"jlrG$T*rT\9dsL
[)R._]A?]Ag4nrI<B\:Ym0c%BK-Y"+@K1*)UBf^/dfn6F+Yl5cfl?(>dcO-5Q]A$F$/fs5(M9.L
\A(oNK)]AgW^]A`DkZ6V5G*i&/JrOK:5=K"Hb,J8?=-dK^9ai-R:O%eSpNIcO:U&Kn6*k[I^i=
@m5"=J@drH[kqmQQIGo5q?C^,_s+_@+Rg)$n(46/;L$bB$4Y:,/le.X`n%5X\$IrscFqgbqa
4A/OpLQ'3#a?X;?WR*(_HXZZ\3=V;4u%:X^cLm2P#T8'Ng8NrY&R<nf5rd'H0$?pd]AoZp5sW
`qL&[@t=K7PCnFo[E[`>*29WMBBCL>OZ=0bj-;VD%IIZY<5`TFDrOiq1Qo0/^kGL>0BO-_\!
I1rirl@8XWYPu?>JpunT^,qX-\dEF;bWECb8"8mkU2]AqC!.dK$26ILcCI3=2)+,(Uh9WeT[G
T\u[-,AZ%-t%Y-H*_S3qGj6]A@I]Ar>Uk9LL#^`TPO2h#d)kr]A[OZ_/q`Q^9lkULL:GY-d%pu"
kXE4Ud[LLuB#-(sqgfSH`Zmt`EmcJ9/>KHHQSXC*Sm7ZVgMCB)e+bI1IW56j]A2A;.s]AO&'Eg
@u]AXpeR6/hei2nj]A`F91jsn,eOBrk4a=Qm,.Q]A:qqg^4YMOGb=il2SUALS5nY@[Q9_+9_8EM
bM]A"AM@S`DcbT<$N2M7QjS&YcEDegse/f5#Q8[kmsrB'<jsF;#qu)eMn+I$$c%7]AW%N4S'Lb
ma$BFJ)]Au'a[p5oLq3bUTS9AD@;G)N4o!O@>?N$D%4gg:+mW3H[s05n3<,`PI/.nN/M_PkF3
eKE6b\J]A:Z$Wma,5F^:BXJYku>%Ec^!s72+O,@/[gb2:2L7&glcJ"&tUp,^8Y`t7n\/ZplQW
QW3E"4DaL6PIK4kOW;B^P?j_OB3KtI-=J'")XNF8bEH`%ei!']A_C8,R`OoUrbL=4_pfZ7Up<
StR+fZO&![nOp]AC=I*?ifsKlL7=%%rIBn5*AG=WN.I&HTFTWiNVQ+7XGDti:#18BJ>grj(q]A
9+-Q9+D`#8tt?r[$VKG)W!<_1Y;P">-7l^["H:K5l?QZXldhn*%jd/"WO,@.M>c6b!TbPrBQ
;$0@0f=]ALG[(UtX`?AS!RR4-I'`3Y8ahscBNN-@$%"BKmU&)`f^LI8<*B`bgM)<EuSu(l7Tj
J:KOcnp_/+MQ*r=@Ef>U",4'.co&s)Od=><(rZr)FH.(i]A+WUO8EO2DNfO#jbIkkOLXc=4!g
lR(W8pf\m7s\oABt9oa.c=nJbEjXMg1?!lCI]AYYQ`H]A1W.c$,:E!UHQu>F!n_;GlJka4Y9sl
P5=8frdj>4kQ@PE;4iMG2YNp-4cRu==2BPR:CB;$k&V$/;\u3!Nt!77l4AK,[aFHAuCg-,f<
)PZ7[]A(4lc57f[ZWqp[dk<,0o'pq(1$kGlGd0dm3E1hS*9VnUU#9HenZ:6%.?\YBHI^1g;Of
Z<UlX:=[U36CgYY9WTC'/)nMDd04Xdp&)d-^Z+Q_dqD6FIpc$H-8$T@3f4m([Jf7:#WE'WAM
g13nLWrl5T*0jkdEK3]A$P[q,RYp.)*&-Hc6;Hd+<ZM<@D0pdW,8'CVe,_TcGj;>cE9nmAR>Q
OD_C\H7]A-k9%`&kFP1cUDlV<%Yn1Hn`qPUJ/]A%@._jWAu/5:CgGEZ20r$N3s-0d?*qkON-O4
)0UO''I"85?=oa/-.F9B^(KMBD.e?rUEb004:.@X;Naa.dtrjRqpPOaSc=3cdpP+*)DttMuH
/YmH".n!G_Q0]A>;q<h]Abp-lT-4`SLVEGm*VBWSOI^Nfu`?Mr0Yh.YX"3!qho_/K=bhncK/\3
/ZtUj2X=gXM?7ro<:1d!E9QL)1SWDln_W\TXeIig'#RkPe?3Ak1?>e5KsLnDj$ctL[[@qF@T
c:A"AO#q't:[m`">PhV@2%pmEO6eZ'\?CQ=LqZ*7X<HeU)A6)'*_Dk@TU_NbHN'h0V;h1?H[
FLJoZiVk_iM7ajb*)5s_[M<_.%TXefj?BQl7j0(JQB,pD3^uhCq>I#6""SCd!Ye/)Gd20"lG
Ui[FcG9&H[Hlpk8$aq.C3VkLSGna/R4C^tbesNn^4*rl>fZqT^.2NE2:hA$l8l"CNf%fX?4q
5@7u8$U&a0=%ITo%@4Q$%X$*cL7Z;Tj5c76:Jq>Zc04j\$17a;@Hprroq'=;ne'!tD1i?:f6
McI[TaJZU@`NAeFVadeU8`e^+)IomUAr2aEJ`PQ]AN*>g.'P5Tr6r+G/pk;7&a0RjqqTM18gb
eYFFl,"9X1%%[S:\2a5)bOB*0KfW!0e=Z9cdrrj+ScN=lYkHMnFT?huZ&?!0bfC'1e^iCu%W
4kCV']AIr81*]AauLlLn=4.*:B8>E?McB>Pm?8?qM4L71*ip#,[0,"\G;Q0V"JcWr@DkPnOrX2
^)U%f8?lbm_&:#d-'AjeO5%3=nD=nhiG7l(nW>_;G%lT%t.Er?-)>3Z3krOgZ$^o\fUJ2hol
V>+Iqr8s#m-joWY=p*r>[`GS>:t0u*+$K#DPJ\1#XI%b3c)`X9sOjES31&'CPM72'O_FYS;J
!>_5U@YEEYaCINNL90[pCeYBO?c>IU_EW1@<`'g5m5l@6b^;?gaRRdaX\^`d.TEj>AR2H:%W
X8d$@.iO__3Jc$/"M"4uYg8K0nh_aO'*>=C;I$G7$*n_TAQJ)OUH=kR]ApMYUffa`cG,=Ipdb
<S"6YejNb/?j8b;&1Or]AEB56Ntd[;+oa/UQbdCXV#9256On<b)4\nROf17hp\JhS\Gm64q%@
Ijud$(u&T'/7=UE@@72r*g-u&QLoJD%j2q&VB>g=t$Yd2af:XQO-cc7&HN1)F?8&&]A<Gt4u>
W=I[GW)DCK;Ge*fej6[E%I&X-.ZUShH@G36"B'pB*U&IG2\=A1>UY$X1GN?_FL]AqPGg*M7.u
6^:pY[5j4T?j&cJoK(Mdc-0*FclnSd(+O#4a:gjne.+2C<pA"lRAI=S0\tW<X`U%]A,2MG9r_
mb.4,Rn*14/Mi0b><"l9paDf&(#*J:s`(c&hC[(*Jsi$h!0r#h+_?=AdW<5OL$BlDIK'hX5Z
oO2nb@^-#31%+Ft-8DL\_anR7pX_&)G7US-8M8G``#5AtYYq3Y27%^i:G!+RHWN?aYjl[W@#
?F,h-PpO.LlJ$hQYRS/!73ABgM62*&_9(4<K@$NX,g\o/%:8>r+OK\Y!&H]AEC<5hWfeoL.tT
BT0I&lqV,f(\+u^cl"BrR`]AY0+g"KlRUZ#g"dA"1mC?,GWhXk&e\lq\L?bU&Z$QNOBMQt#5k
W8^82h8oHdZ?=dp(.#pMWJUo,'!CXVOD%5&nn,ABTE3PSZ%4WXq9ll/TMVKT06#<1l@<@J#(
fi+osoO`KCcZ1W@N[3ZpTi/Zgl<(4H`KIG_cd$"QXhIQTOfK##P0CHLDOUOSN;qC(6b\"O8q
h8B'l#7+SC04i]Aj9XkU=?:Y2+9"7`uI>4I\gGk9ggSZ#%EN/==;V\5pbrT$Gp10"Zo2M&a\!
hS_Z";XbRTe]Ai;)Tb7U3J/Il.t(T[$3lJM"i6kh<YPQ?(gjn_[J1W<T8#\MI7s*EKlQlj*7]A
l"$d!k;e"Gpg:Y9b>YsHe[S6WRC>i4[6L8aq,1T\VK+=#A!:Qk=<XeUf*Nr,m-*0a=+(g(51
51n_:Xf8E'Y")."RP**dq%/.7.To9$?W\rFJH5?XpT:1)qQMZm.Sf_EE,bVe;3fRg+R@H:<;
>+A5StgH8?cVl![scW*pT%%^Jde.Nu'k0op]Ap!cY*noY_itb[^5YAWjHPm1]Ab4MotR/;HQqH
P#Se8^,\Yr:1Z3QN[MaKqm%">-MCLtl+n;.H5BQ2*fAgI__>oFj19UCI0464ikmIVXe7/!YB
_bt0[b@#QSD4NmUOcci9[S^4loGloAi6!VckY$HLkH=9+??(&^Q]A_>T+QE\PmtpAn,npP@rg
f(mrHGVZ8C#9=aLbcjZ2&Q:[qotjr)QE\-s/!&4!q(/9J7]AldnrF0O/D-RRsjj]A)LXW6N[H/
T;bFOTk`kd_3I+$<7?6I6o5k29r(>*L:<]AJ30YTQ=MkDN-b-/S/A8EX"'L!K2UdE^NstS6`B
['Kqb'>0]Ah6BZUjd?D/:CqA^3/u32_2j_N@KH`p,_@&A%\_A<GdL_!Z#j*I(7MQXgafY-3+9
s3+OQ?6ZM[1WhLg$:(rVg:Att@IpTCC-193Aj&RbFfJPEY^*3CrI6Fhn.DHr7k;l>5%L+,2k
ca*q=nf@JRZ%fQEREU4@nofS`3KG2-b8*t!MrVY@WK)QduKjr6(u[B]AO-\]A/KYo3@_Q:K(%F
SVN-%mks4L;VZVm-E4A`*2*04J`)(CYPdU=&AabRRW'neHb'b=ZjBPSJr)X!W+Hr$jmU/c6e
'M,^G`d@N1$_UiK]A3V?HcK&3*@`2s9-`"^5/nJ_0h6Oc%a]A%2tZOoq<Q]AU`!_cNU<%V>$`d1
,R-eUFL89f-hRLID"'6D9C;[YEK#3a9i^q`bn6Ve#Acr-<P-ABnN-rIQEfFna@]A;=s,O$M#*
cLs[Th?5%NQSqte4W4uI27]ALQ#lTS+5:ssb9j4%^KVB2)!7NqOs%EWA8>?I#oGa+oPn#>m&!
Nr`H$n?+r:Dr1Ir[hTd2Z&#kAmC:p50\Jn<Ah-<]AAja2IUrP.4\-dW8nq2jA'c$(e\ad25I@
E<T06<BeLU<u!#-D6@:U^E=qE!TfbCjd5i5J/8+/@F:@EJdl]AY:&j<,1jK2Io<EKC!^I89iW
CJ`]A(nG$1N'N-?mOTCe,Hqj!B#6PO5A\#"Z\haaoT=1T3Qd+<W(0c/Hg.F4i8A17Bp:5"P1T
\>#+r#tZp)l=0Y'RU/,pj)4N`)_t&kmkhN/DumZbXGV`FDlAqP'\g]Ae1]Ad>%HRufJ*2!Rp]A"
T>rfe&$QXlXb3I[5(Xc5-`-YXlqh8S/#LQ$uZ`Cp_6_ZEa&i)gGEF)DP6ZnK)U=?9t6Yl]ArJ
f2\GDpejm=kWU?R_aMi.m[Bn$InhhY4$C]A6N&,[0sdP%)84RMiGCtGat!PiRT7ic#+oW;n<c
\O!Qpu<%lUS$eS5LQCLmehSdm%4AAf2T9jiDcJ:T0EMj,2YSDFNK31pP,Z36E%!mtUHN=A&O
T+,57:-Cs%TDeD>)Om9po:b$iltjc$.$D[Q=Z#$04dhWO`l`=9P&(*0[i=5GU7VTEle'4NO7
a8lNH`<O@^"<cB!&&$+;ZW+B<=8EBm`1LB-*?^GsC*BP>QrV%XDO,`1M_PnX)1_Ifsa%T[qi
9?CjM#O\kZD)M&[S4",M[Zh"c[i\,Tf-J0rgJO&Wbp]A?S9BQGNmUOdZi:m;oqk::d_:8jOq(
t&KTDi49qNBDLM)S6e>r:a[5&N>#<(p2&spVqIb>Ygr^SQ>G9`W;eAl"qhnP$HKG2a3<e7R?
^8I=pfS']A2Rt7dIA\7*[P:XLJ]A:-_+W=["f7@nldB4J=i%KB`,I4-qgD9TLN>8d!N:s]Ab8U9
%dP/F<@UDhU?YXp&C9[d%ER-0/t.DHP+k%E,D3#,gs8n6RrcWopD98T+#_St.2Q.bN+)BLX9
9Sa\7*4uO6ba+6*unYE>.UFfWGJPOY+7Rhs(tB"/C/Ji6L\H&=?!Ze(kX3@"p/h+PLMu@GBf
+KSe'"M"*kfd-ES<c5;<>>W4;+Z<E'q<?Ru$h-;^,4j#EC2k9Nj2t:fAEYT$d8r_t#8Y`.2L
/[92jqN*EKkCQ\_!#]A%[,&\0FnCL;gSC7X_>sV>Mt@1ANX(*=me<>GYO6[[9B[/NgTrRWs5s
60g*oG%,8N+7@H</oBGmu;f07:'Z/TB%-L%KrK!lt:nU^-L*ZekQA;Pg9.!#H9g1-61R=+S]A
<D#/4Fp*rf;#r-$n%ZR.8ODs6."CHtp-b-S%@<Fed(^3ea0^<rN&>ND6OB-:c<>^]A"km5Jbu
?<4):Nla@fZ.IOG8Om!8\i=eLWFqGO[!up.l_KK-]A5FSk%4t*c`)ci83ageRZP90.SF!X]AlQ
9Z<W2TkKPu>rn?*;lUnhGge?Bs5iB%u:MC)c]As?AXgL"5jJ`B.SW_5H4hm8&PmF)R5^ik4F%
d[L+MrcFi5jt1X0<$EWR]AWW1C1!3:N)"P,ZVDuIQa.HLhV)Fg!dRqKGTUfLI\S+\!(hA;iKa
+hPrU!74=VMclo!P4ESdU%%4nc3ngc'%L&*jM6YF;d$H4u&$hG/n3E5B$EW<d[5Ic*B]Aj0jL
TUNKXGb"\a.#U<:K#khL8nG"b@d*=1d%<*oM(;Rt+LTf(HduK8!XJDJ%)M_V>%$ZtNXpJ^?&
.UPRjG2%[.9cYe9RcdO'T#Ir6u>K,--isU><;8<I+M%F3JkSkhesn!AfcL\RWs*H60>Qr=us
<8B#0P3PIg:J#.im30+YhP!^\);fQ4^Nl:/=WBefa4JEc`SE!+-^RQp(5;H_),&d]A`&sl!),
jU$k+7*d&3-t"f_-0=`$`AbNp+uniJnI+Z;^;pM(=hVV..Fn1r)'#mN61P2a%oV#F6HtmS5J
Gh6:G6:oFiZ2B[[&2Al'[-rZ`dSq?n8E0R)J+QnB;HOZe<1L*JIXM\KFd(a>N/AJt>8L5nq?
N"217]A%@G.$ehZtYkFf6UL'Ic?H6<rqoXtb=nf/qe)bdK^19A`1DP5)#!Ve,"!at<_rT+D4^
i>uS7+/;Hrt1O!?kCA*I$C&Ad!%Jm_7"Q\94#&Y*s,\B($1/*q#P]A37)![LhWYD=MGNVoibL
+<qn#@p4>olrU'Q'+77<)4OnTnk%Sp#b%e@l"0FYBHX<[_=5o-`h7Pn$RukTINupAt.#EE:X
b>6Y[:X5H)UKg9Q0T?bR0q+`s.JPl1Pn&Thq_$d/N;,C7spJ^Y:RJ%gT_GtL;#V$q9bQp1r$
`L!&QXgbN6bL/Ufmt@cP2$'"Fg(/plKig1u1!0E/Ytr6<9MnrJCqi8`A=8kS/;0'cXm4dV4P
(:a\8"pVHZ7u*!SdnckYgWaj)&NP9FJ0+R]A)k9+WoooM>)^U]A%<ZRJ8UT&jFcL/.H&Sq4R%j
B1MCPC"oO)>Y8ja'@jQcHiOaQMga9O!Z1%jf_3IB;%f1`p_A9eOf.Ve$JFH<na_htXRqoA;G
\X5E9n[Fc8eLC6h:gWgg`-V@]A'l')8#@p=nj-pON%L4WQ-Z\mX1H5j[j#l?U4p\eci6.X'^d
OTUFc]A?qo_?g!5,OQUXj0H*Rj_`Uq*,IW6iIu#"fub4BZNcf]AcpI@=62).q`?8VrG@#emB=]A
ILkZqO0oq_Tmik(Bt:<Sb.iU<X28N.a&BCn@D3,ajLAP2^tD'"a!*qdj'Vj/GT"Z^D3e=_p\
i]A9S?5HA[+gs<aEisf1'"23!)r#E^sUtcd4Fsa-MC<\-$[$r&L\Y&j6SGnd+aS<9`,_`?"5U
G^_Ipo8OE37;47frC0>ZK1^NZPRNngYR*D(H1F"oRq"Rs0^0[]A("ir%"I"Bm^7`Tj8W4=Sh9
IbG/XoIa5R;dnu68qXlHKDjc=^WfID*Y7C+$["=K0Q]AYuA)*YY":Yb=T4FRN(:jqZV9HOb2I
mcPj^'gYeLa>]A>:!<&Re(Esd<<$P-PFe&!OQ@A<r+<.<1l\;Q.aF9e,V?9#A%qG,G-5G5m\:
-oCkn;%pBe[7m;tbg4$8XF6Q&PZ1t\Yjis()-)S\h:XeT9d(0<nErp8]AE5\0Ktc]AP21W&9WJ
mW9=AiP#occU([tR1#_]A:'(0WPopbr4'nOqgk[L(-/s7%i%<u&pK_-Q[N%q>>Dt@Ki[Wr+85
+4%4D+(!.KlHShT^N&Wo-E4h;jeR+4>bpbaqfnHe.LY+,K(7SC?U_\85aWq[uLJV`2f^c^M,
%/%<2AFB^5hgFf0hBh'-1#P/t@%CQL#3aQu#W47^,+/-_>7Lhu60inGaH<H>OYdNR.W\0(fT
JlBNDmE0t=hH$pijX9?0m#e%CHh<t`T:K:YFj,hqr84A*TN1WMiV2>_7J$%Zc`)E\(^Ntn9n
88mdkD\2Z:sN$q&T!RG`p7Kl%KGd8Hh>Tl$EdmL)NlAHral7n308Jm6:F.!:$LG3FRW<oriR
c8t]Acg-Ts1Ik6q4Og06[l;X0aT.Y1-!3(TIeMLV_<;!Tm52j*nWIDr@XCE2*pXAAJMrYlIou
8aB:#7+((\Y[8G5hgo3"r1VH@g6HlNAneSY5Ern%c?IiZj&i<I9.\!o/so#oQI)kWRk9o:#W
(:G(ioi>q7N.6-tNo=3&m=IZLT_Trr4cfgsXaV.58apB[1.o5-;$>(#kK-O^/I3F'#6a=Toi
I)hbESknOYWfoA*AlfN8;M:;26e(WRD>\&LF9W<*N@]AahWG*>4l,`?EOj&&-Vi_]A\el[@B6)
[7qY!/H<^k$g;^Im$/lH*3KgtL:LTACBo5N5`geL,=AX&a6#^S!sJbdQ/IrjJ24S!\mEVC..
[bE*h5>pU>M`Fhcp6]AD47H<+o(Yd]A*SZC)mmjC$g7smpk_;BE[G:@iD?)]AEY$C3!KHo9p./R
Qdl-^Au5?3FhZ/jE96d]AS*5,'V&`':;?7C\$S^[mH,h1qh-7(knZS>VS/m<^ub$*Hd6$2q7B
F/jus-N\gX:FTcfa?D]A(t5Sn++DkA?[;[nF:D"VJlGi/0Bm,#'CT)!ag1tGuKn[eT8rM*1:,
P'5oZI$USqHi.*bPIL&7;)C-F2_D*V-#$9%+t2<Zg]AIs.8bjV28+3f)b/QaBV2aUJs-X&J7]A
Loei__p/o1!G%?GYe0=ic30-@:+ma(#jZKD^J50l1?=CrUaR?8RDG=W^`^9dA=(R9]A/6!gj*
OaplRQ&i]AW";W$mhkY=/rn&60?-Y6+\j)<T,UdqTom90h0p<0;M!H_TJrD&lU]A[((1d`5""(
"Q"k2RW?<Zf8\!\qX<JHuRlVp$+804pF4!5TT;XjtF>]A=rffZ&E^8,[d$Jlu>6UAM>o#""Z)
`QA7`3!Q$oLptB^_Nk_CGd6omHN9`q[RYq.-*US+KrRkcX]APCqT&V&oS^#/8-9[@F_RnW!b1
N>pq$U1I/]A_sj7?Q?F>gaL/!_kKNkQWQJBf_"o^E+4%,26q'LQ%^j9(rZO-^hSOC[rTW<`'%
e?o3U7.2,VB>%bNDho>as2[r;9Y7%ue#OjWe-!2,n&EU/tB]AZ]A8i&p2jj_6kk1MEXU?FT$=n
`D1;pE2ce:R[(RV,p?J^KhpqF65EO(NQr>*-/gGqk^0R!V^^o-+e9qhQUQM]A7ALE35AXdp:*
@">-s$H^_<5L2bmd<>A:fWn0pY.]AGITj-o46h*ZLhX[V*B:,7>A$:<5j"=]A5fdD^>eRMa0BK
I\WP&9c,.>@7d,#=8Ea63k79Cp,LKSqSeCIl$/W2rrfNi?MKOp#+0BGkltHa@D`"/de+hUiA
9MhQ8[e(o^4jEEq"Chc8Tj/-p6Fllka;5[,;l9$SYj:]AlPq6<1>]A`:$4A@hVV/i]A;l$bnEIf
0.'j4m0?35&^=]Al?!@K3?<;Ab+"-cmp)%-J>PraPQrI9`,.qo/QDNq<JN9h,CdU*=<PXM*]At
/)R("k798j]AeqF'$gY5L@Xs3W_eJh>M7=Q;i=)m)PnW(e00pu5c4Dr'7P./cGi?sT<56W[_K
^"`="h40*&,<-hd\2DIKkOaq/b0^7PkKT:9j),%r`=?$d<c:W]A:Oslta=da*Wqh;;"lSo;!?
:<JGrG*T+*g3I%I6<fC2>X6d+cgP50#jZW2*JYE,h/0ua4bh/,#Nn@$)]A$e638OP[,;31c?c
<;dmrAi6jAuA1qc#Ko+'Eq.r'D^46Y1`QBaWf7ZA;bO1311BSCsO1V\KW2UD'U.9cg$G*,e(
<9q-HK+p]AY07>"8L$I(k$C@=mH9M\i8JIeGE]ArRt"Fn?M,@,o4ac1qK>DCY%O2FS$GAOe?$]A
FhrD">uC6OBo(Bk#T[B.:J3"N_o+L18lR;@0=-YiLM,KaKl9o9!<*8s?]AEuUSC#45)hbBQ9^
-MmgO0S-5$'),n:D^0hDG$/SJe^jkq=FITMLMbLG#_Q:>ga%o@:m9@O*d8MtGX+,1MMm8+eo
bLn#(lIXQF##mqFYJoaNEVCBNfdg+?K4/8Cf-RAGSDMKZ7HC)B74l9k/G_*(eD`3V3PCsrnO
D-oA?2^X]AHmGZL!mJnEc]ANm<JL633de=j-f3++-,6/McJ^1O%Ah'\TGcJjY;EmWX?XA^3),$
.#B8a<7kd?#ms,pT^O[\f(gL.=J*g[oBU>>2.R3Kjl2R:f-$X(7DkE?:t6>t+igKJpYH([F+
PeMk.YGE&G(EYuW>:h,Tj!i8#3BMDF%(r,kq,Q<)BLd)cqONaH2M'NORH+&J)EKL;4E@o[r?
,i(EF[-W,J_UpV,0QRls/k7G0WSL\**I:Tt;i0g;`#/l@0E?U@O*'0>)BUB+BV(7>%8u"0]AI
sRTLa;->8#uA&$bF<A%L:p$nCn]AQ3WY7#\9qe#jQX!7Kg%<W<8=.G;,h2c/su-/SgJ[Kfumm
j)O:Uj#iBc@>:2Ee%NSqR.'>n(SWgZtACk%<,%6WZhD.l6XAOKgN+NH]A=c9KqjSqP8N2P'P.
cJGeoZ7aq+nV'MqPUPlAB@FUa&;,T,OlPL`"EqB_-6<4'VA&34PBs.3a&Z,VO[^Am!VJfD#H
mj8U0-A</4g@3<!&un;fQ@p.Ud[*e>=M+!2Vt)K%^Rsn<pnX'dfROs;&$m-_^$&oD2VTg<nP
\gXo/k9(cs2YtZM@&uch-0'Pt]Ar7_3b#=f1kBu_QtdRQ)@G23fBLrpItI'ltUh=ek[X2fmPY
E.Cg-?rC?A^s3%`0/2Mp5o_+DT(KrO6r&;khF5F/#E@jq@kcAXMItdD")"c()V]AMO['cu,@P
B.9!HC-.U+`5pS9U3O\W6i[^n1(4d[!T4E[(/9a,U5->;ODYM#0:67.9uF`PnYlu?"WB^&qQ
r0Q</(b.@OC&\elnLe?k^U,T-aHhO=@'D'_>aN?9k+0H%?B,Bui^I8`m@rbV?0<6i?&eG2e#
(0SS$E\t(^?p_#`X^3Id?-841+c6G.XUO7LP*)sHjdYjE,b2+S*Fq@&2(]AQXLPiGZN'gb.EW
Mg+XGE#,ch\rAT:A"".=+g,:;7gp4G`=^iV)J?(k$5cCr3@Gc]A`OGU<qtrC$Hcgnn>[X_dEg
T"?*c%[u8non!qfeI=M5-qc4<:9mZ/N@aH]A<5"]AtY(7sKLXE>c:"FQ.S`='MUV+7V7L:ND0[
]A6;2jaP$m4%Bo^n:$YHheW#\I'74aSaejkc*iejMs!W<l*k)')//`0Rg8P%*j3+V>]A@B&me)
P<Ib56MO8]AH?!5+p9UES$Dka5iLPVa^oLjsFC@7sNQXnPUi'WFjb;D8B<$,PFX_WL\?\^ZX:
G10Z.5<!U6GT3#@i#gs6OV?,\MNfXWgVEA8KUqWD\gQdIS*U@=4j(L!L-H9u,r1@,6]ADg9%:
_9sG'C^Wl=5cI9?AhN8,RT,]AVP&1AE+JXDbOu#Rd,@hd7g*7iThV).5k.LGao!O@F:lIbE@(
5K18a380-6h]AB!Uq)#hfoC8Rhfs3>D9),O;?8.)N;S`"VYkuT5kU%BhHjp[#IV'-0]A(LEM;M
&f(Ri8WpC-35L+jF8<J2Ssn@a?Tg,DLB&T\l`CfZSMZK;NlmJl^ML.DH(0l(pP6MQk%iq-ct
^]A\iES9Ma/;?5!M0rmP[iOLV0E9&c]AtdEu%1"U9R2gDQOQShq:hJ(Fl)q,JC.cQ0sai+jQ,,
-G69n#dGiEY-_&[rH^]AEIB!_uhrIPP"/[`*MPZfNH1XZ>KX$E]Aai5m&\^OVXomg$L%*o34O&
F`SVZ?60bt.cIEfm,)p)g"HR+V%m$/%m^gDl^WJED*3FoC7_-[B:4hsJ#=55$Ruq'"i&eBE<
`E#+^aQbG:D$D%X5OT"0([:QqP3[51gMIINOG(jc26uMfCQJEkh^b'tmEW[>+Ib#[QOEVb8,
\X-oYTn]A7k'VmRM%!/#i\PTWA-c2$d6E(SW%rM(mE]A-@chUL"%`4SMl:p;dMd$0"$_3ATDeB
b,Di<]A".3*%&&+I6"ktjh@FS:%hi70".iAc0Yp[0DH1U>D=7jmSnj-s2j1p$O!m#R'CM]A=@.
Q??aY=l=;Va]Ad7Yg2n>qn%#L=>\Xu/I!\/sAB+uQ;;$?2"F3b(nE]ABg3b'"`B.a(!&<9r_>C
N@EDZNNe!=p5(YHt`,;>`S:qH/,J$V"iNd[s5HQlpN?5<,F4K-Ys?+3aaEG=<i3\*aip\\Pd
Y7N)a]Aqb8Dt?=U4q@BL@>hW&NZf:/L"#aWJ\.3P2@2M%e:F#3=a=O&Z6V<EhiB@Ur^kQd]AZ7
UI=8\<tA)d`>R$Y*d:dITTBgU=[b9BIJZ@n2P)c'EukpK(;<h!VSYVdBE*_,(>\O7").;]A.>
[2HY-$`Y4[$r<4-R4]AuS;]Ako$CG>%5\ul/e.+;DG-hqU)QL4V,!n(Tplj*?RZ;(T$ke83cqJ
JB^4ci.HNUKkSK!(H`P+?tW+2o)Sg!-"qJt^YX5kHLLf7jKWJgKVVr'rI:e/%=V4L[nmLM+>
l!A@_i"ZY.l8>F>9cFQk_#)aoA%5T2GGe@Pdg,K</e8\SA3Am,qDD3JjY^X&\?3_eLaXY.^e
WKqT)9#5mZGYSCC=NPBtFe35AGIk?%2'E8.jT)c!LV'U,>p#7ahP>?=Vg@eU-LYdg[8M-h6c
mB7*Y3k0WW:"[e*q=+B]AiX0o_)Cbk48?"R9)/OEUY^dAC[Ufp7k]AL<[=->YbLB<O\YBHYn6_
UN%/,LPc;Fe7UKhJ:2d)_tZNg:s]AY+j(fk_Vs?_Ul1o8p<PU`%f0Uu9S44nJ^*o2"l=L^`Vf
%<2065`Pe4T)_W9"eSb3%3##`LR.=ZlkV+MK(Yb&K@%Srk1FWQrfVrL1e.$hfC06c0&#%tp@
heb3Jj6s'&[,FF@O+I$T'FJ&ut@:IJVA7Brul_Ja^"HI:>%!^Q\[nq1M(jOtrrETna#b'$`H
5DW`C6(**WIQ%pZRc5opC#*5r?3;oJpNJb69f^5Q*07Wl$f</%tY]AmDfBCb7W``\ajo0^Wr4
eG0>,TrT!rh1Y+PL"8!dpoE,Hd-?37g"X<ouC;s_cgXlQ.idA#cbgfX^/PjHZ`3r*NH@B]Apm
3s7T@mK*4E2UYMWl3CVFf_q+;gqm8"mA=m'\3br,I;^h:5^P@ZfD2:d%na5-&/Y^i3]AN*nA8
HE!)`+g\j1^"dn:C5EFmWGQN3qk45ZP-r>c?>:FiQMj`n;GQVrNm[J/]A!Y&WL8I`aqf]A='XL
.ci3kOrP"-2.igFhBTDZ2\HoRH3<)UccQCi>j48CP"mi8'67@\4G)0DhiM&?F]A"g0]ADu@[=:
#gB)d8e4!.ZfKtkq$3`u00Fif(:d(t1a'=SE-p1bfo3+1[&8&b7_BSU)^2oS:qgiI'4[T=&$
LuTSRY<%.&*K58:IU>%cg*$X41jV2h/E,5e;"q7S_fp==B2el2DL-X>\*H[A`4iVK]A#8m,aI
]A^(^hYSHlNh6=S'qArKLtRhf(7aP:P[0\F[>FjhV21*'c+8U_^3$27$d/'n;8XJDbhZ%kQZ_
<GpK!U[ZtP0,_fJ1)SDK<57huAGTp1h'3!LGr%S?gJ)aWl/8\RLupk/5:,p@&$q^m0r$N!?W
%/^eFl(k0K"rY,!Qu^qgoCU&C_`r9R!&]Ab&*3Plb0Y\.hk0EWe?dH\TO*ahNE2"osPCt&TGF
<->(dcEbJgYULI%>3UIA97iLhX_BR2o1Q*mZ-&R7Hc$H+aQLrl44U<EZ__mr#/0Bh+MJm8\0
jmf-Bke6HWJb\=l%?L%MCgFce%os9pRXr9?=Z_M[ot3VqXh'UH<(lidpI4?*T-mR9`I::DeH
IOip#&r&J!=h*rWVGJ99YYqY\><_@'4(*WSCSg@F$LSf011jmHrKIW:[7"YgMIDc-)iDu]AIC
c[Sn0=aU%mqq.'=q*9;u2%HtCTl0i)CFFI5LiOka,,EFtZEV!Y1p:Z.JAem?QiD,635feBk]A
OL)B4N_/<ickrBt)amjpuFRE,KHM_0ao,e^>c2SLc.jLq>Di-"0Dcd(2_GV?)'3,)VX^^R8D
sG[ZL7:3lLnj:Q&#3Q.H,1btKU6:^$-"m6Ue<q69UHZg8C-LPk.EO!n!Kr;s;AANA*^m<f7?
0DQ4ac@?Lch\-a1([^\I[8cC5J"uTge40"]AZ+^JP%$`<e:bi=&M?1SX.YZ,mrhOtaQ):S)%e
B'$d?[\26C1pU)0=I-BeLHWKZ_`'$S.;+.+5A8RhB@\&&KKi.bmEY8FDa@^_6B^^jUcm[)r;
0'\7abQ2N(nGcm(9.Mr+UB9]ALA;%_pkgFBq<?cl[.+.5QnMj&3Y5j&;_]AW&li,sN+a7LBLHt
Ja@STW%g\mtEF^#'7&5tKD%O4p2%@.E3Ma#9`>5G+ZeWAOpHH!kJ_CRK>k%Sh#[c$Go4i8:(
r['I?gnoAZS>t/M6QM2Q:0fd?L;`*,c;#Z?qLQHXjrpV\_n.Q^BLOdm\8j7\50$G5CKWIpT!
Uj(gKIKILF%G3`_t9V`=gip-`aHj;,C#1/&^Te9g^TcD,r./p^*0\qhXf@,:1DM<ek:rsjPK
<[r[NkK+6ZnMd6m\jJkq#'Ml4^>'6VMsMuj/B?VJib1qDg%GLt8h:Q-nrh"?!"o?K\FKH2r%
79lMC;/bQ:WM,[.@Kf-mJ4ggMF=$NK?h4>laE4oLZDXRSdg6[S>&lpXl"6oSW9Y3V["prglN
X`$)PLG@Md*F6EaK_H^&*:P'U&Opge>LZY/hZ;=3H>#=i\ID5o)*/T:qbe5d:omXZ+L*h_a:
&mPK;"Si8'CB/T;Jcu4;Cf)'1tUJ6$U6U3f9^QSCGA)n'J+/`sg$Z6OVBe*\7/0B<11_;hGG
R,+\(7e*;:X0ALI,\L"i]Aii4)R%?@O\96t&@u/rLt]A:$!Mi_ODZMsL[oiK2*e)eopsdnngm_
*$(S,M//ALa:HQ:L,0Vo@+!2h#19>(4T>[u$EL>=JAWQ=$pL>I5s9Y2i6SZalZd-Oah_R\bt
R*ZSuXaP4KpR%S=fR34Pbe=*;-c$9YZb"FL#!\JFB8K?OR.(bTGC2I9E6A<epZW518B?_f8V
oRWJ7a!g$73PP-RG=AXj60F!a`^Q9??N>?Kh9!"45o+/Oc]AZGTuPGOM5>dPPsIbJ!md@W:h1
&m?`^FrQ0MdD:LuD;<&o5A8X=pqnMP%Aqal2,3s/Lh"\qfrpmS)<d)Z7NcHZLGT8Q7?<#$'K
S5)Ta>fW253792o(WO]AY'3G&C]AS'`^1n:^(kQQ7>$XLPZVf<=\r2X>"qj63@]A+l+eh-[M$Lp
qWMg#M$bXK!bGFm]Ackrp.Hc7YSBci"s>hE)Y$mqX#*0tJbVH4-J!L`0Rk?4p+%6kI$fl3'Za
6BiU=(X\sIn'Ol%cKLhH7\BM$aQNI!53mKdB>&*Zf),H#2<2F>F3Zsr?e9GohD^fRc'8[IN1
:tJ6lG*AJIk3E=KV:h5M7%F'HBJqa`r;6)15h58AQ$B*KHqkp733k9Kt^YGjh$ZeF_nLjSP=
!JYU2Xe58clL8N?KH9bXV]A>:$`R`FR&N"jXU)^1O62@#35?3=rQ"A27ZA=fo<TM%'Y8.7\j,
uhCL)QkA%JHn8n[M\!tnb>tCMDL[KD"&>ooA]A@kNs9a/gn+0sH9_]A25$,I&rN@Q?0mHmd:\u
ipH&mqBm]A2DQ[3qElE1a&T\qe=Rhe$Cs#\.p6ClI\i/87alf$=G:E&M>CY>PTX/D$_$R:7#o
bjR@U3TGXS>#o0)Pa&a21L>bGoe.Nh[&'c@qpa^m52^,TH0e)rBIrX\98!GPP6.WA<]A7kr&>
Z+"[D?5G$,V)4mQb!iRCi@\Ajpc(cCW4MQ.GXmP\tm?^NlW4PI=t,W78e@]A+c&A;3)UUql?`
6h3B%4@BkT2+tc[1)"ki@D?_CQedRBFX?E1ZMs,OZQ`rYeohE>@J%6L^&U,0Mb3./Dq1[fYH
`J(`I+?[M!$*hk]A#.jm"_$2!8!U4abf6b)hrV*Ehf$L]A#l^%`XM!'D^e0'#J_(9[^P"1F>A;
i_$qFGe18p9"-"mOdZTO.m1gLdX`X\%Fh9&S[k/kBgQDFQ*H3MD*dTSHADXk>Ds,3e>*]AZ@&
bhgiQUD5A"b^kQHaAXZ<5.DU)rJ&4.`nHu'VbLj(MqLpd"HnGJe(DdL5g;lRdp&7=4?9"gNf
A@52Y+8M9D1cZ!A!1_j24n@TEt*@Ho.brk$kSi$0]A&TqWLO)kV[a!m>JrnOZ"l-0VXrjEF94
b/c<o&MX7J=*cn9mld!$%Y*F4k*.,Ob:PuI@oV5`e;:M?(o8nG,dCe\X*m9F@QshO(l/X@Ym
?,hh6edI2Bs9k(6M>_M^e<a,Nl\_lrkpP";1Q5Q\bfCIGt.us09sejDG3sCP"LCjYWBXUhb9
)XZ?X$70N%&O""h"laTq%UI_")7aaeLTc&Xo[8E/H]AVI9C!N@4>4:)/c)cV$WCW(4e(eBD`Y
pEDHT)]AGhCUl3LIY_Wk=?3c780ADiXnWb0;;;#1=)Jh7tqWqD5i`qH@mjP3]ALlS3C=Da6oQQ
#i&i",i0,Oo>Y-ULuY71q$=?g@?m9J(RcVldX!T.Ul?*5ZVjbT_sLm=Ooo8de?.?[.9[OBl.
+Pda>SF*K*R,#R!>Mu+q;Y@#K'jY]A$Xs"?Eq4Y<\)?76R:'D`5X6iC+gTF(@B_e]A_`p3sXtU
uX>fKP=`,7l.X$\e">hg+Pr$'RGR\q7[W.EsLbFgd^TqKrt2c_^$p=*AFHg!RPM#:A8N!%OV
mNED,h`%3H^3mG_/j?5,UC"suSC19[B,XDi*J$qq*kVDWFn;!rJDL\"_RqhZ:lg(c4?"pB]Ao
&YiQLN`Xq"jD1SW0NmATO&mV>/]AaD:$/^rUgN8?]AA<V\ejqlp=9jP(]A$bB;M3'TFuqCkmc%p
jX/Z&t`pj0[08a<9mMim3<COauc0G]A45Tb>AIR-dn+)^BV=Z9Xi>W/hV$A(a,UeO:=/e<qa)
mcq16+*HX&RP>R.]A>:<\n'IU0LNhY-t/2N(V6ns:sFiPjVne4Q"S=;2&I9/UjlH)-T9U'@3N
u)).%=Ag-LUMo,HLJJ`GGhp^,#IKKY/W3XZJQXa4d7FfPF*L6n7/?8Z&""`3.CFKK<:De(uY
_WeQr"L\Nds[e$IDL^'-&D\.@Dr?$n7U/:@6rc7!5*5r2UfE'(0cD>2?_%oI<mi$2u;j&*._
pV%#2o#j?!GhNi"Wld.!$i*dq,"Cg+j/TRkd6dgOC#3@5EU57KaF=,Sn)Ed$h\16/o$^X>-d
D;26t6=^Tfnm-:i4eE]A-WAd5&pB>KSd#UE-6>#(4mDt/D':dMEhgD1n$_Q6WT!la`DYu(X:e
&VLD]Afei5=O<SNP>3RU-WZrR_H&;Y`B%V1u<'R+oA>%9M:AOU=rR#&=ZRAg&e:USfGnY"Lj9
]A8l>B[Pq<mnN>_e.hC#Fi!O>WOSdOislre$6s<tKER.K*&]A5*lGSsX"E^b)i=M(-KLRKA$I@
6;Q&[HipfsS'M2iZ4SOV<?$@"[K38;tB?au483A$^#Qh$Q2GWUW%"3m8p=Bk_W[gMIS:U]AQA
U+%S`e.]A=IdC!Z$QKHHkL%V$!q.K&4R8WiSIq96I8:IJpH')7u[J*$=<@l.J0IYE5GeO+N4V
AeKl`iMrgCnktPk=$G;9*R%/?nU7X=c6A[[)a8$X`L'e\0036$[olqmJT56N)KC7/gs_;n]Am
.[-Z]ANc$(*jT%dbTjr'##20)(3^[e"F[1RUhBLG^h(FnmJq)]A1D5s&)<6dF<Pq+6Yc[*-N7>
3T0-;?3Lr$kH]A]AAH0<*p46Y)7@]A&.;Dpi[`R9EH6()V.ciACSKR173-DM^.Z6MTF)H.UjUG@
E3A*d$f-<V$6Qg7.q6?_*=Y?on1gPO,cj5f>5oGXp&a&dY=_+#9]A1Shg_bZB`el46&(Ah3%$
D=Gt!Ge=*A\QC-cn4/nHLJ.+RY+?Mf"f":5W-%8Y+<&tq9tN2aVEJguPqHd(,G5UL]AePa03`
0?ipLlqZ\O:4HQ6%$$XnDJ:Uqn**5F0n_*6l,j"3Ym-MVjGA/rnL^]A_Er8\]Am%gK5CIo7NTi
2Rh<ZS6Mc2rX:cleXZG"W;(@e<_9P]AP)nJ(DanR@N1oJg\IIOo#GqmGD+XV\u_YO"$L_^<QW
`q)?jB,L$XpJr+5@+1qNl9R&"5af0O4IoZ:RtS2]A3K@IDSBL(#I,[Gl-7h,:@`_5dm:eK=nW
rp0)=!,F&LQ@:R\!#(EMa;gtIS3]A5jmj[pW<<^6>NXAPLOW4"h#n+b#bTn52%b;+Z;@*1nL[
_-#,o07gc$X!AN*q(/@(E6<U63C"RYrbe\cS!0iC(IJlY^<=VNEj_78.5J&IRd@:O*p_b]AK1
6?+WLj]AmZ1Nk=ch$A(i.3MJ?_-W0)J46?<8$!mcdd"j_kn3oC@0#jUn/l$LT&h^"Q@1I0dqr
`?_)-)Y/CMJ1@gKRM._4aHCWe='KkPB#E\""nF@lhNd*tNd)>SJGXVL7V1'1p?K,4t\9OjR@
3*0qMS.Q3T?'.FaKDVo\Wt*r!gpE<$a__bVC9G5TQ*OI)iktWG03u8OB,dhX.W(?O^4jXkf(
Rj^H*^h-ZK+QojZ_#&Ndl-)D$=>2@)[98`JV0.K-OrF(sCp$>U?nCD?e2oH#L::KuhC7SAdK
fS?a_HcXGpWtg$ge&mb%6ZV7Vc"nX3gQX=8_rlF6%V)V#S*0)e[qA<,AgBX2Rt:[<B]A5b6]A\
#&ZSc;lZ5fOX+RN/euO_mFY3aZ]A&Y'-IC`6b\L._W\%_nEP9KkVc?eJCH90h3Kc'jU/`P,mj
u;`!c0!T_"&lSLi3Z"15Q?%DmEHD@ams!cOLo"0(u3tIhthpHZR@g!=H'lmO%!1BUF.,";Y)
up-W=CAb4A%q:""uq@ME.0]A6S>84XJcaJq2&`ZB)\5)Y@im&H0i$TQ^0%rhJK!WW:[nqs*Rj
I\`Mqh1^VfN1CImisf_i$?9397/ja,OK(2&jbDcHK&-GQl1)Q7E"MB[lrs#$Pg[Y:4`(D&ao
aW_[/NbK0$;'r\GBn:;?#[=rA)%EZXe[p*<pTIgF4=O:aQWC]Andu/SbeY%!E*!t%U'cE!\M#
=8hKOs;Oa@af]AhfNFieS3T6r@=7c')^QrJ]A%V\K7K9IJIB.CBu>jUmUO5UBl6KmC`3NS"e+0
,$JeQDoQ)K4-@&se`C\Q%X;,co5RNNMNJ`\KN7*%MTgZ8aMCX,_Tm>Zs<)GJM^[(U!nKlGI6
(G&o1q1R6XY@H^ra;]Ar<t\\6-]AOk(beHQNbbV-`[?c-D53f=E]A=\\Hi&<;HR5gN71,W,GZ)d
\(Oc7sfbEK^A<l(8fe3\JPEr$5GAbKBT\:9/G;-_@TUf6L2-$Aj9I,SogS(]A\A?M*&&H()4!
=p(,1GDgBu>r6rnjH?XJC4U7#I#s_>l:!iF#L+]A@5!p:/Xgtcu$]AX0>mg@X0:n2l>UI5BEAc
)^=Xr?Ug2fGoqbG<lDhAcQq[stu@9M[Ln4!FFDU(iI]A3A(8qFEaUNgSRLbotc-cm;TIA68Bp
Hi)1I9"1+2Lj\gQaB7iAT?Bac/Y[S=FhE%m<"lH;Do]A\.;\8Dc_4^lPj4HM0ORp4+XcA/3EA
HkQ[m!8:ts%mRJd?>2U./5A6$%5/KLpiY]A=t1XBoi<@BGr-2Hmp#8hSI>jEP)hd*YkD,T?<q
2l%2_\r0M7;G:Ratu:4YP8rnrQsl^\a95Wa^MI.WG0jl+747Lt`=+WgI?E$SSC-Y`:'5fN*5
U;jh18NFP]A%AmsH?Zm/9oMB!XYqPlg,"=J6S<[4>9Q>/N0_35Q51`=cr-meD2i7mioDOCG%i
r*^TcOhYSRUa0P8,h-XiD.uSQS(%Y_E*^-fW=/@/>qCXtP:(d43#uSh2=*_]Ao2M7Qe^m&Fsb
RHgP<^8BN!.UdUYe+c51To0n#0&M8-1ngJHG`!jP=G4lsk4\uF/:S8-kAPg#8TZ=n7@"G/C&
O;64KjmqkFq87j+A'FG'[`CG4Wts)lXeSo$baSbEQ[F'j#[nX5R)23>R4(j&#07T+F:!O>3+
+J$C="cN4C^]A[1R*(ON3#iG<+$2EA9[0]A.I)V:29N79$:(&5gK&iMGVR6h,&nu>deAteY>'3
=qT!8)7%h5NcIGArR&="BR/X5M?i*Rq[<4F#9l#?Fq:UqR,a$KFO(^F$2Ka_4!F?<3m.CAqn
jfajoemp&V6I4_ahHP\tc9'rr=T;mV)&\o2!_UfJMJ\>TE_Jc&bW":s7c>)>mStB[K2fU"3j
4'&>0&SB3.l3W':3)L$d"R=5gu*\e;f928Rr27+4WA,9tc11%#&##r1IS]A@&UZTS]A>88]ADFO
:Nn<9AQB#33i,;koFYk)gXdA8KSXTg&5'C/GRDU-N<_g+kbM5IXYU*.ne4<N`_]A/;,C%Xbh-
=?B-Jo%k-0s:3s%\>K[bhE?/'YtnCEW:9o<91N%_&4.UsH/*n0BPD#c`Ml"G\XdoP'm7L]A:#
=77j67:rc\_IFntq?`!B2fgnf0XYt^MG1?t^o2@Jb?Y]A7;[.G?a`._H;/W]A4(sq\eePJ4G$?
S.Po2\eOJ#&2uhVn:W*US1N8`t&;6ie>[?I>-AK8Z[]A%%GO_`#3*tjSb:I:t!N5s*$fli!&@
NTV(-9.h:&So!ZQGP<Ht+W'52DB_Hp*(Q7NbSNBrO@8amNWDLDc!6,(%>V[DD.)1D3&71U[?
nq0&QtBU&h!7?t+ScD,)p!J=Ihgr.Nh:_"9U).X_/5E90n'tD5k;L$lB&aI"3F0B]APkM2il*
a9iT?)VV!H4.JF-e,AD:tDQkbi*gES3Z@d;a^?Q\/t4%8gK'.H#nTY6.JTk53-.BBW.PC0RP
U;@VE0J6Z%Y[(J!o\s%Wl&Mn^X4YcRD?Q4X6u.di202r/r/U\hj_`/["F]AsR[6ra"m+A*sC!
R-UVVusISi(f,6eF0d7k_^\,Q2kU2glSeM5d6`Vj^;BnKj;)+L\5JNn6IY3QERG[9dV!<3J?
(PG@YcU[D@98L#DOeT(+E^GLH33`]A?,h?9/?T04,sruoXRggL[0l&U.<c'h"-Juse(1T;cn\
K==-NS%D.77$ak=]A!>^fefTkqONlsTIT/)+:BP8BXa?Q(9?`n>TNQ+-pU.lU[^[rOaV78Z_u
4PL_'o9%6#ZJa67$#2#KCVmOj&QGD]AuA()B7;r"?`]ApoS;]APtmsC&5cRD$)+J<rj*S[Kaj2t
P)@q9#s$5\]AR10!&.l8^,?Pb"[nX<0gUe,>XSA#:'5pm0/G1BF<[8t;!.tql9OK7s@/&4;bA
a=R6<pZJQ#BYBG+2r#)p@nkG8(m(?^:-N9@gJQF9VP]Ajjls>DA,:I$HW=e"q`e@W(7B!m^@A
aS'a]A#Dao;i4skVp!7ua</V9/(iUnHKHPS>ZG3dXZdec=7E>GrMLOQ8c3D(JoOR+7il(5*3*
Ru0V<<FLcMh&u]AH+gs^Ve*.7*kFqSP(-8kd7Ng1&<.*qL,6bg;36Epr21+mGlO5C>g8:1&[,
u%?D,!g6V:20l1h#m2V-2E.j_Ou!9_$gj"rYo!eq\dZmH@Ik?Ti`cp3E]Ap;o7Ygo_g3mP.&o
4,G[P8d-^<$[onceZAsO1TKDP@t>%UMq9\9l5ut6HAC_;@4A;cHh@8Cak>1AK5<nk@Ys&g!c
=oS7u_bsnqEMSo]ANMU<I9YOV+^=t!3tdM?b$WHNjC/YY=@=s7*IDAn$0]AJ8PhlpCG8e-_]Ai/
o!%=Vq,sJ&89;s*i'A0plXXODk(te.PB:>(YhG5G\oah^h-BA`b$FQbP@3dW:04VKI+Wc0^7
FL.0W+cQ[:$,d<kCU+.>-SpYgR+Cl8@%On)O`')ia`e<28/u=:VD=14+*@M;494g\Z*fWi#J
r^K4"Z^2cJS#e5ZDclkP99+$uj_1Dp_dT`/3FM7(#u;*FSg<Y@gap*al?2nmi5d@h'OKj@O7
Sou<]A,+6MR?Q1n?dCCa-,.mCAC)">f@WR=E,kQte!X5:f*he]AsCo\-2*0t_meBdTtYFnH&`G
(K$7OQ+"WZ4GdI'oikBY.!6R2.!<$8P6dEE!U<"CP3DCOE/*U<2`o'.[7p]Aq5Wu)sYe$.qpp
O_WXo"3#2SEj^Rt?Z[nd1X\/%31[#iEEpGo=39T0&&m3?0'b(d05UJWR$5+Ut_s[q3FZN2tj
InI_G<;JF-gM?t/YQ9NKiB46$.!ae`.5.&4Nc[O6WFXJ;UVe]A,G+.X%"6495.=H`EDNX_g,@
[\4f-k.^07"*V%7)bO/5fQ8-f5a-V.N9a:"uAW$1"@1@H(E@C.S"OS]A`G$N%-C;`)XdSB#Zd
P."RD5UW83'opFW+iOM-5,ItjMu4Jih)L;qdR5BpRY:QZFI"Oh\%hr.V=O>+_$6N6X[t=!rt
EkfcJ42NOmQtUGp/6KK<TFQ*_kII8hft4NV)F8-OCQaPX_0IhIOY?8;i>L+sJ>NIL]AeG1_"i
cVR+%uf<JE-["2?`gSie&c4^+#@SV:%V.):kIA@^KWKQeuQq)f'=(1on@[$m&(F_oJ;5*;tY
d<75J6b6bCd\!_\,oP_T=(WVTjDbBDV71i<ps]ALOQE.pG#=Q%,sH%TK.H3Up)W3KJG;F7cC.
iXcLL=#6#WYdVWeA8cXr3;6>Sk)[V76V]AP4'?N&ud9/B`--`j[+[:f0'\!l%T.J.HTq?lh<,
qGWlp07<Mp=qcg'Cs:oL+@D"11sg'Cn!W#%KVQpB(BQA=5`;T$-)'Hbao_8]AY2nG>7,k@(I*
8%`hX`)q]At6Y+I#]A!9O<Jl%+03V-/EuDdJj%b=$g/UkN:lLK9g1W#_m1kU`3ARtTba3,ea4)
Soce%N]A/EWU0r5hW+9bJn[_665ZN)bN=kW#UQ@#H?7Q(0]A[lJ6<2H!bFU')G[OU;V;A25Za9
1L)HM4g@G"#GnH@L6pSs&8EG/gQ]ArRnDd0Rpe!(Llq.;.F*il/41Fk[57@u;=J\[Q[UjFmn!
;,?B;_LWuCX#[#,aY7"Vd=20H4rL9#6Cqp<KI#g?j-YZX&q<"r8<Wj:r]AZhGH-Sp=[<ph3rK
_;q]AWNdO7'4%dlYD*66/e4#*UD$h.XqR\c%B'9+T'hP+rLc769NWZ8\1q.,#L.#Z$#7%3FdQ
<SU`$i^t78>r8?%jaep!srFD['D24dPY/4/0),n0YWXqYc.?QOTi9HZW<%^;-=Q'bd3B"]A+e
V/%:B0Y23jsng0`i\.\1Y9k\`G&(m9@U8^kij5!@H\&"cV$+lU<[K7PngfI/iRIDqW9_JndP
$g8[D2^;1%]Ac^G6ndmq^,@8jW2o`2IIK8WD/p!e:)UuV>hg6a=<-2fYD['\59UCpQBO`MM.7
.)S]AG1%PSX:f(0jFh2(UNmo*QBS)Z9OT=rW+.2F.=S>&K+3aV4FlQJGqWS*3?(,4Wq@>ra7@
#Ght;>-WC+gR**)(mIT^Jio]A.7aAKt>Xc#_eWYRfrHkk$q(ZT^89d$;@Qm;*U3L,7747b0(D
ia&K[HaBDkPirm?^u8,TAf^[-dF@=!!%1SRd&H`mJ>:V*@jFWJ+Z83&:8qZj^+c-/jHhh?3q
5h.3]AncG:AkPrFRs]AQq.ZWl?su2lDkRZ!&UY=mdk2,4nB.e@e`-9\/hQmh)qB)R0T0ReYRE@
F5U+GE[hM0Cl'MU>K\.MMBJR@0@&c$3!b]AB!;_`9/>`NQksq5qFOH\4)Ls@cgq\+9'Z;5%JP
(=0N$S\l5V\$\UQ&L?rE)6/HBgi:/UCq^$-pG-PQB[b,Q\"n4T%u_MJrO6LrT66tu6UUrRJA
;'\i$:<*[=RgB@JDJ*#6BbbC`&7bNG+f$qAKRp(T8<:'8`;!Nm8nj2c";I>B,_XZ^9t+k@-F
JXhhVX/r,mQ.H!M9u&9D`gc&'!:A%:)ajK5j-R/+L]Atm-3ehMJX<co27,V-r>6\<>WYlVA"O
\a*@)<7\Te[Ds^s*>LN"AFb%5nMsJ"0bbT^kCNN>"%2h+KP^jqc[kYAb+3Tf(jbH^.Q1*N2$
L(]A]A(]A^B."Y#orFM?%+ft2"_KDf=pTm@p?eo7[(k1nX%HeYbn;c]A2(r=^iDn]A=@"6mB.M%\/
kL)D-U:DJ*l`cl=MG7F*U_^:IN=c<#gmag)r87k):;@(A<Hl4MZGO)R>L8Po/OE9)AHSk[,M
!c84nEft;BRo\hKd$N<=6FgtZ5fQE*LWRt$M1A6[iNk-HM\;6-k5gns]AegX451*_#>]AB"VNn
4XPGYP9;<_I0DoJVHPeFuXmBOA;#kn@HfD8?1N1HY*d^m;u3&sG`poICaK*$Oaarr+Z,?UkN
`n=Mut,I+tsqj6O%I_IoN/j_ifgj(RJnjC`<`,Vl(S@_q1n\K?b_`^h``-Ss6[!]A#Q^S'jX<
%'J2BrL"iI"V1bJt(S1+Xp0(8cSCS$sqgBEOBPPk./d,WS2b1Qb+N[*]Al$BQD"KChmoRj)nX
Y=IjOZTs)=F1hc`ue=qeTOrmLbt@dTD>_VPH8rk,j#cASN1&Fmjto.p3p+UYB6A79TuZ3GTO
4t1N(gG9$nja!Y*4HcI"_j8LI`E<WMW!*l'/YK1Q,8+$0iHZ=:A,_hBB*P'meW-t>e[D7!V*
HE0QA]A?L=5Q6]A/SalHB8ENFM0^HC?=)Z^mY5>4_+7_KIkJ"ic1sX]ANU*YdBBfjpo5.A=:N(1
X20dC3h)$pZd/I$LeM(*GLXN#V&e>a^b0[0dAB_a=Y<'_T#?*)up4Vf\2ZG6C/55/&`]A`nig
b4OMVq]AOn[^]AsA!_(IOkiTb\]A_Kh+Dgu?C]AJmZQe*l.-nd=qtBEV\9=T#V/(0#sd.5]AuMbCM
I(n.-'=2Bpd9+uVYkk.<lk)7fk`17u?Fpn^UF4Use^:#^;em\ch=Z3-VH(6m\nML(*<msDX]A
FF.'hno.ET]A_R<5[LgL4HbUE"`s)8+#;=_gcZn12T&U\s/HdMU53m]A)@^$\ooB^'#4+ISreV
HZ`/0]AXH^Y@Mb6_e[3BU$&,5=ZJMQ#a?Wr5m.Y\',iL?B"DB;a95>N*9s);m&OSWHkd1cl9p
R_+\;!rl+C3p!nfObh*UY:hB?u>g]AT&p`;_Lg!;-G1D1.,<@TV&oL,c"R5Xr#Q`[2hKH)gUB
k>qUIFgoSchWU6ljLc<9!alV3FYE[1'QBp1R!##2/m:pr=O#ERZH)NaKTj/ET>nei!P:+.lM
/ucA55gVl_0C(9X=Wg"m[g4pmp!!Oll@<u+2HH.?C!#H$d63f<(_lT@Nhb$[/mDl7-"OZ84<
c_iu:_@^p\ro#`>2dD_0L0aAu4JaB4I96?%qIHQ;(5(]A4QI.gkmHi3t9GYsN9ArQcO]AF&q->
9^#=f.&>cj"0,ZN18khlCep9(B<Ha_C%9I)10j9&H9dX[0h1d^k@;M6Y!c#OHMD^Z!-Pg?Nm
-;J9>*k*+Kp_Ztj;W?V7b\R*p/G?MP/Qtl.mIIIh/,\G;1PM]AoSeFWAl.Gp?6B6hXc5(f)F5
;=k?ag9=t6]A$ECN\9JC:VHDHFEl.;@^<l"Mcr(Dj.6!)niL*F;?Jn0-c=*@ZRAm011>FLi:p
s)>&Q2"5TCFYE4.j!F(S>=;7JkBBOc=-Zt=Nf3P=/]A_r<2Q9R;53:;*`IWj@1c*dMO%C[]AZU
f8uu9]A&+&K4GQ`8,@J^W&p^6P!;Puh3`m(-9d)7]A!2pDfYRYZ9S,;F`Z&n1CoiH^O*rK'70@
O@mWVi/mAa[)4+?D^GH&8f1C;]AMV`huY#AdPB>qs$N3K9T4k?5B,6QiN7OQ*%:[I,I>g>f_b
gR?m*-jT?^@`=7OIS7eD<\!&Mf*p,)=iICKV#i8)g/;#o`8>J(P4`1VWCIL`0K=ID8,@PCi<
IGi$.*OaiIRc#?q7c*&4XCKO:\_6PU\F/n]A-2s-@DfjI(6?[>(Pt59"FYM4HfbOkf(spFA0A
eU+4#*W30sqO<Wr7rLo-4HL/,`.YP4h-G5SJij8_$+DoVFG'ol@I5+!H!a`X<a_D+P'6D`@j
qSo>i]AAk6`.nSqU^?0s,@1C!@)eha32T`_q^YLkE8]A8Ss@8Y!RVdA"[;H-'"4#`]A;LWCTr-V
(-^_d5VbXo5.JXKilP-meb.D(i?)/84R>7JQCp[]ANj2PEa=Sh(Tm!E]AW"/D&.nR)f&.q=roQ
[OQ7"V#,@a.GIB$`q]AK]AV'n$?,%(.ssE@"rO?qS'!Ig8A?c'(ZGP>Jm626XEH2(tP'?,L<G'
l"tTPjr;4ZfXNZViQ;cgW$`3AR*I@l6L^O3mBZa@$Q"[Yji4.Bd=M`97c)XB<6[K9g]AU;>d9
-QCt/qcj3-Us-5lPC^a?G&V]Am'deB/5:P6Q:@*6csD:GalYV0^D;3%F-mC"t;s)HEr\&T4n!
*0jHiaCkG)-OVj_f;R'"pjEFkT5PD'rjqm3WrRU+?$%U9i;Emqe3-oIVlukPM@H[V#0FT2J?
nr+>UlM9'rkur<E*W5NlVuLI*97oeh;<#b:mrbDPPMsnF^L$J'6fq[,,:sgVND%S-X0VX]AqT
Rje@p%dn7mW]Al\'fV'L?i-TXQIp]At0/"Y$oH()a(FGS&rM2QQFqGug76:+$54C-u>GBO]A^"T
sio^M6@QA[41oSOaaG\IjonMR3k4\Aec&loXfZV%'S*uH$qUoOC(V-"e%5,nD&[]AfWTQ/9*;
0!#qP*6<7"D/K@hjQFDV_#I?^m/DU=DLFY]A0PA'LRSWuZ&eS`>O/gqq5+,A/L;4.Vca[bJ;&
\-*gdb[\e!\PK&trQfTpI:I1H0"J++5U_O/C[%9T^T&M]A;C8&R>#\0Ka*uPA&TN%/ksk8D&>
4I-P54*\fKMgPR%2#,(#qNg<0[=CT6ObjORC)8]AuRNUMq$LE:HWg8-Nk:)9a#[LEoP/rB4($
`-#5>bSgeU9HO.M9U5?A.IG]A-ho!tRHrpAH)(bM762`pEBFD?.!hiZF<P<E\]AL*aRN<-RT9m
O#VCn^Q+\Ed0qU1(V%=gY^D,lbYe;7Bm9?pQ6L^FuLECmYg_mOcrleel&sa_8+"GN48Comei
+9A$Pc7A`ki+:FTQQ\5n4cD7@DH.7R.p,rrERW"g"]AVb'"/::><6q=4LnY>K5#Ki\]A7Eq]A;c
E+*[nG.dHY_hjH3aX3uTBCfE7d%;IMKkqJ7(=>mYi/.BXdgE)tG!q6-$.:qd,Ua8F[Y3amEC
k/3eU?G!7n/e(Ye;De(UtRpBcbMgkKWGZTF3B":KG55TC#9sZoi&g\_&lj*7ShU'7qKgpE,f
#[V+fJh\_jd7/O)3IuGA?2@M@Z*Dcu1d>'pVg3q@:QeE9@j$6[o1X]A;IeanVYmIT?DbO2=Ac
U68$gl#7W+!P'72sD+N7``9qH2[6*>`U:jo$MpY@`Qf;TT)jtCm/3Xd8B>uP[&:2aOF"DOCi
=Qa&?Da`*LTW(i3qlHKA@GHmFnW>eiI]AiF;H)i(VFs=%7#eYE?6+m?+%XV/7)eVo6U3g758s
>=dhN%2JrJ3UqE*J)rqM8W:@l[ZMfm\6j^QGId\R:\#'B(jqA!%`)ujHh/U;.SXBQfo[XNp[
NeKke#hIK:qWeCq>F(*EdJ>T#M?T6g>8*-1:aj'%eO-H7;oQBB=\83ai=`\FNj9=MBN%#'n#
PYJY"C0LCt,ViiE#ZdjNnQ>/L?'u."q@op/#:+,MlqNER.Kq);N)6N^<"CQ6TT[E/K-]A9[jd
6:'cD["d-1DV-K1[caR7XX+-XKm&p=\oZ_M77Y;r&'Hr'$s]A;I=<L+f567\)5!&aR\LTI<oj
5.lRJ8?T3@`3kLq9.q:jfFh5scW$6O=P6QFrrn<9I!n;JhL/U'Y9?:FbqO"IH.XM>@DqQk/]A
0^0ZKKdPOV"uu+mGj#Q_6mORI`&UmPR9UC?'V_DZ`<;/Zc3)\Q]A->?Sf9\$MLO>+2h`encfQ
^,KncrnuBb1'\=^c^qWAe1p%6YJZIcX:#Oo%T=dEtrIjCSn^`$BB,F)k^PJ[@7k#Ja*0q3m3
4lHT?G>UoS0?+>l?$^N'Jp"q\LF@?H$OetB!ABKQHX"4]A*>Z0Pue6fCifY1nd$\@Ma5""9HG
neM[Y\P`jXt[bV<)PGm#Mc1%6",i*$i8Oa,b]A=fV-XLDd(LO-7I9B7\<>Js92A18:smp_UJd
jOK+q9=PWGs#+L!/pcQAQ!TNg?-:9Sf4m4s9"grZ3J--=tLV9pif6]AiuiiG"]A*,,\9BQd06c
^=%P;OYa#8,!ho2/G$.:nfrh::3tpW`b&GUm_gS=nq6Bpr`qM1[:NsME8:SM9d?$6phu=!$"
>8-9qW#ohEFl*UCO;@p<%BT-?)$WMm6Ji-5HZO7Jq$<6)uq\$7L!>pZr]AC^=0-$4!TGNc%2^
O%fm5J'[a73AX9BO-?/!`OKTpYBf9)$UE8WQRKR6Eqs$Dl/f?tY3]A:r]A(bes@#C*i0jCS/LA
lNDiZ\Bhd?h)/G&F(*faM9\j`TJjlbo,D5j*U$q-q8Co5&RP_RoJuooB4P56WuCU,`_aQRS=
>U`cf>=D\TSF[Uj%hm.lr>0PlrV#ph)4c$Zjt3=3Ip.g/2W7s%tD,9uK7MSPH(e'#aV)F>KI
SB0GWR>a:X5agtp]A[uu/VoVfuW!n<77%Vdb6Oatibpn`TNCsDG9+]ADG<"I))]AMKk)dTtd[8$
TS9-[u'(@#S3c?D#&(Qt7mof*>"7)qe7;_]A"`R(7k)nQ0peW_*P19h;>N2<Z@<^gQJ/CjIR(
XN9L<06Y@s)\B5C.jS!iGG3r`]A_0foPj%8"+?V$"F(!fXJlUQ)fmQ$Q3Ur%J0(Mek;^2,PV!
EWTE)hT)P:ORsMFqa[i;miLHTgCtuOWeTYV^QHT*J^#5gs]AC/Xk)9b3[\+X]Au:b.mEC#^EU,
>&-!LPEWE2Y$f_'Jdq7g>GFff$%nra=e%63oF#bmVPkEG$r`86:TV%(>*f_]Ajhcd8J'O5$m\
9Hf&Zd?r84`k>;jjnU[&gCu11QjclSr1W72;2q3hfXFik.L1<-E;\>"o9qV-U3j16Io.[uLj
c5i!OFcC/'uS_LKjI3#?/Y0<\09lWE11J^O:`[-0SrF9d%"DaJ/Y3(i1cu_G`$t[oPRXH7"+
aW9aCO=9TH@74oMiiaO.m[/B(O%,r'2r=4+_m2f8GSoqZk?\<tRhaNXh6nLdroEP%2'kH8]AD
?p3VM'0Nr_&Kc\V/>1Y[oHLokCilDW=7RTJn/<L4SrQ!nt8D/q(<@EDNh:D/89gPgVPQWfjT
@?XeXf?Xg`&l^TI.#CqX&t%*XZqDI:\j;:B8?[5p*"'-&%k..X=jIW?u84`Lmh36hd^e*$#_
D6p7,U>M`BTc#Ailo#+TBW;=Y,>s=lQV6-t?s.p\?M)j0e\um06m(0HP]A[_=K5a51D_=gq2/
PlNOn.]AhrB"60K-*"E@V.E\gA?J".6&<B6hK^ep#>&!6\i$(^!\k')gG3?Piq/M<\+=2Y8a<
"VInf]AmRrG9F1NA!--s(jHGLt&S.".3L@X8kgHpB1.5+RX>5`T7BT(nKqZlChWo5Ukp62>A-
+"j+8S6fDJL&ef*RHi^c.^%*N>ZnCr+aEl%%@J/B94B)K`btRdPXKBEb"#HfesIs6SjKQA2:
f8=:petA3^'3P"C?Fno>;Rg3;Bi/LmRAB'TJfO&gUe63rnu]A#*pj?Jh8)l<ajD@Z42^@8M8F
D/aT9aS<S/RLXhr-5."#Y5Y(m5eh1-\Z4[+@^RedRdJY?e.PEel`$*A%g3MR6Fl=3/WV!VFR
+.WT2MG$r8"OZjS/(tj`;l/^ZjV59$f%R^PNK1rlJ%tXoIXpjpbl1hAA:jB<]AMi+Lg^gPD8k
M/*5oV,s:R,l;@T(JO"C-,.!ii?3\SYhr]ALh:"=k>3kDf@[Y0*SX]APu.%_NX^EI9O5YA&"a*
KH$dn2oIP@FGRJWKmrtAj'GpA$N^ibZMhP/,_Mq7`>=@\0!Gr!V^-0VMV87bXq)fHQM1A=#/
UON//tjW"'rT75ICmnsWg(Is8KPpB#>U<N'*/2mZ,uDmfri9G+\CbL?7XVrPcn>+m=*B0o[J
$i__@ls_<4nkKn$,fh9lo,CUOjHf.T<aRB7J"Xr*k#Fh1Sit?_k"5[>ROXAR#\Dd&E`haU6X
,2C:/N?XE=)WmM%'BQR]A8p*BK_`!oeOG4U`#_m(PFnX0=4qOI'.c8>l2J:q(ZGgVR2Ssgd.d
mSqO?"p%r466#0NA&$)Gf5Fbph57lBhdQ#q*$c*p6./##&Xum<8Y*sOk-q%HPs3Pe(8Wu]AC.
J2>`Z2&FaFOXXW)JMFjV$JA)S_E:eA#Jal%T<;M,%<Q^]AE&T_MW+Q6;q0jQFMA3q,T)5G+]Am
M,po_+\M]A,HrB)`5tZa2;b2Rh]A*Z8(>U2,p`boif[o"Y#-+<-5j(]A;"lcU;Fe+YAkK):2&td
UKC".`?GTe9%]AB0YXhSTgN)e""KART.EH'WTu>5gSfu?[eT#Ef[+]A]ASAgfg?hIA57)73+&,C
MZsU1S>HKRPJA3:Y$q_mY>H-7LA$&jElo!j65p0lPG#26D0ZmPGZnr-d5GK19?)r0^i/7C9m
=hm5Yid<s$-ZeZKHe;]AteB4=U6Bl!\mGd'JE#jVHn)f1CJ\98kOCfE#l+2i]AmR<sl@HM&L@f
/94(A`fUZb_+WfPqfge&8)cT&N=ub]AC?tM)9=Nod:64K"I+J"#Wi_8T\`gsJYG7t-<2>B+VL
pNU&[tN>dM/P;Y<iCs!CjdCJR%m3X1F%,67=c([-$7c!Dpr:0:ZnA)\[/o6tU`^Rr4;WKZ:i
Q6%a@pf/=QUEg(c%egku04e&.OpN''j"Z-fM3^.6WdM*.gJ(9q2<8UE]A>[>3d37_k)!Sulm^
1>5dVt6;NalrMq.0napi!$o&9h?nW/W(5&F9o8-@DnAIs8(u!r,BhZq\5Q$"Y%_#GS56$b2?
$hYX/N`*m+#L-^[Do^4@_V`'K[!Y)O/ISZ2rB9`!WXgLtKM.9?*d3fYW#lC0?OJBM-(q@or.
K/eL`2"M,LP`a9a*GCh]A:cRJr;^Q91Z:<J0#Oh7"aODdD*$Y`ZbSI,6E-R=:'1u\j(u0ecPB
!*gg9Ds2!EuP=kFWibQu$=Q[WrQj1a@#&^?&s]Ac)"lQ`EHpD&S'%AR-uuOO\)A$tg]A1g;`l%
^;9]Ar/%+oM3uqr'+2di0pEV:;a2^Cq37kO[)\_Z+;3H[HHH!EE9'I*?-\AZZ!r)2VZoX]AN<]A
K$6N.hr%.Tgfk/HKtBJ-ZKg28NEu&sT*A[&tOcbH=C2[aKSfs#Lfh]AQX<[br#_gYr&0?#O<T
iJmLi"8H!59J^658h!=sk2SW#l;Ulh;j)Q7=H&t*sJ=ZYV89'Z/8KifK#TK`P)4Td[1PS@Vh
4M-*22s9#:IkS-ANQ;QHrgtN6_.;i9ubeB::K!0\Eu+/4bnaA5KSsK`?k9<Fb>O1i^?#V*_L
dbj(Y4FY^p0A3*UH*;`lQRf!>8Fj;FUihkT!.Eik_Dp=T:-99&#r`^8@c1P'(P^VlPq_d&hF
=tGCJQAR*59dWuO`@,LaMde!_PBr3s3gmcQ#1#emW/^9cBqmli7Y&-@#iD*95DrhV.%@c#;A
3>8erX'WE?nWk`(P`_:538ld92i6;HLfk'65QaZls"XF^?`KSW)]ABpc2_8[#Na+If@jdA[>)
sPPpP1[&)E!)2c%4G5nGHH!4To,5`#7njb<jp31^;@mLfA(#p<@pG)#;>^XZEVo?V(1>ot*i
bhj4,P%=FoXh/-5>((#R9p_(HN^UOku-n]ACMcSp3oIUL`GMSqi\!IQ%fm5W,X5<m:sOQj!u7
o#fkDP%p9CR`OqYkk1O,(eS=Fd6'WKR51sKJ`'4u_;MTGSB'>gFGmFl>a6JQ%7BqQ>Vk=[k;
Kf0_.l=6d$L:Of7/&,6Y4X4VZ:3;D+hHQoRAt^q>O3K+ZhQ-*]ARaAE&(L;+ATPdp3&B+!H%B
rfQ9)N&s%e3Tt+M,e#G.k&uLbEH4c_&E"LZoE%4_`LYf\b&M7$Y#a@"U_+NRILcOXVV9XFt4
TcaOlkHq(N^1>?M0&4]A6pV='6f@>25DA;tjZaE@AIZo"g'8`haUn)Gf%'.:diMuH+N'+-V/\
X\(';,j&Xe0F3/R1$ut]AR9K+`]AXG9:!."rI;L2an-<+6chFhij^G0?/G=54A<]AN,rB8MsjI^
,m_ZHcdUd]A%Q'hCKLps33`^.,\Fnc6f@QMI$Nd1[-7V\MKPG.htb2j_I4g@<qc.ma>uGG"BM
:iTls]A'ldSH7V\\0QH6D+5QS3AD#fu`oJQ$0.H_"+#B@(g']A2^#j[s,`e]Ae0#L^2[rGCOO-b
]A?u_XQZmjK(F,hXtGZnfhHI?0PDg9`O06s"%:V^b,YKbo1DbC/bl;j4gX3('2$Gj]A-QOpY;C
gTIaG.BogbT.eJu)M:YkV78F>Mh:_e?7'"&61X:9KF@\$GCA7Zh]A),l__",NQ$/jJmi"^&XT
IKTRIKtrXPLqFc<ImM6$nIFF4>`%R?6\"qA2@i-0<X1]AJ'fr65XR838e>P&j<M?0ho7TG@+]A
8p4K6HHc_r?W:"pj!qCLngpRU(6nD[u?!9F6aq)cXmYob)l/p4gY%!b3tR?CPIEq:KWKYl.0
#h?]A,\R6TkQS03+c,Jqe%eU40^TTKV3\gB"%s\`/"a-=2S+;3%F!Kdlji^sKhT>nU28caM*=
p0p4T``j\W1'W(G4X6`ZZTJ<E.k=TDH[!U#/m)^XuD0K:*g`ng-fjZeB6&XO_RZ[$I.Q:%Ge
t<]Aj5nHjpRZOd+m"PsNg$#>!:*MXQ/6.f[>hEf67OU\U@4Q>nSO/+Fn4h),;MBH1f^]AquN:6
pD=*OrYQm!NiDm^+4HcPEBDZ-6n[:-+H%5-Nj0n-0Y6qIbZd%j:O*TM*>^.+aK(eprjY?]A[H
h>AbgZpj2k^HIKgdb90;a"1d#,Za1VO<,7b+bd>GWfiDLp/$;E!*W]A#<hgSXI[o,uY*"q]ATP
<qmE%jXaMBT]ATkXPQ&oM,pf*-8:Ul45Qgq@,%@%]A)\1C_^-4EN1Zb)@MAO+i&YQud>7<p1Hc
;?,=qE#Ept:)Ins8KOG&nHj<Q-&hNe:D3=)Pipl&j=bd]ATP5W"N,\o#O>O.%a[j`L:q?Z4YW
n;+YXOb(ooaCMM6."]AD[d@9dZaE#V#*nNMBA@4go_+Sg,*!>@K:NquJK.u4mm0#L`WHN8js&
8R:nfFg`@[_+duem[^H^$)Xk99>Zs8!']AHi^LO<*"7`53?Ei0Bu/+d>q9*Qf47KbT0E+Hr*V
*(a\j/*=O`Z.D@1Ecoi,Z1<drl\MibZt%,h+o!T7%)T?%BbEN#m`YTJ,uNbW42<#=jb7*#d5
.1/LiKj1$EM[G80o7s/q*;@=<SD\%(>q9-L;>1V0]AEYbI<.p1]A`+OPWR[%I'ejIY;UVCcK`d
bj/R.E=%Q/usS:AZ;64K^6?.9l<'_JGh*9Q"o)2QJ]A&WtNem?*[_Z0OWN4I'emE:/J+D5-19
5H7,.VV@_R1Tf:L`d`]A'G?id-<2Zpj]AZ,f*X3mFm#%4S)>+4oG<f25ZrA%G<-MNA$>CB)V%1
8:$b]AX>iJs7Sft_5*0E3<^QL8U(LN1%X6s>R:(B3+:2saq:t(Q^!aqT?+C@cH2`&6SH=LrR<
$>p9eq[NK*\K6Aa0#o?3i\@mG)t;XX\W:K,u1?HZ(h4!o9hklT03&<5asQ_jCH8&I*g_'GmL
NT:@hU?+6#L#KNE*(ZO3quk'j)pFs+bO-e5\>"*0JGS,f@'\<Q0<sP@Ya'&W)6uGgZ0.I>Hg
XS+SD>9*]A6K6CSX.IBk]A/1&S<&UeD@<q<PBW;gYKR!TrF4*#^^.XiX>V.fWot\*^N(:m5_U$
uMO\<qe@L&[OCmuYWd%QcMaAi>p@ZBZ>(>%6pm\A%K>IWYpKfg)a]A>-LadC$CR)OH08aW8r`
QYIS,/`;\mc$ctX7o99Pr=>geu3@:`sVJm07ctbr<O=oZCT_,iu(5-#G0M-n^%h&8k\$-m,s
&t=5<Eqnis0tRQp>D1O&=oC<*(;U&:f<.eK\ga+#0/eQ(RVmcV-9B8^0b4j#XMHYYB<`t0,8
o;NKZo!&Tn&+Kh+jPe?ao.<o-%_I.,E91rgS+W)_.trHh*9&%r1IIDW#Z,<P$ORs>fUsZ/qq
KC#?*3k)IQ*li5X13fFm:E#d<`aCs&kD-NKnD=L))Vertdsg%pDK>NP7[Is*TBI8clDP\cik
MX/emaF*LZ96ccD9qECPkMY%/=OX/MWpU`2lnforSOdN.5_874kl`-Y]AbLq?)0.A_soM*Ehd
=ea.o-e?gb!K)G7%I"1?)Q<Gm)OT<gT4nLp4!*M9HiP%Jp&?8QdB-<cOmhBh]A2%_rL'iiX2$
u`TE=.%3SN0c;\DY/qKe3JdTPXX6t4i=i^GP[bS.^\Vm>jY%%:1WKXl!OTH)\\f1T<;B^itU
UYS448>5qR8kK,q^VY/DK=RqA,@'#Pl*[[M=9-!2!jqgt\*nd+diufrAoHcF?6b=qf\@4g*1
VFn5J]A/4k]A:QZkE?$5^&+COiR#A!Ti%*+E3fN:H$.d1[F/Yf&'4dAs26N#?/oN9HJ)Eu4,S3
DQ1T3g-$ti7ip#n+'?Bo.Yd>Rb.J*'js4a:d>VS:c/,5^MI&U1;If*gK,L:ZS!LGHq^o]Ae/@
E2$XJA<Zr>*4>EqO(ct!X*dZZpBS*,KiaLpl+C4fq9:Q7ABRa;4Yo"EhrRtR]A(M>h7SD-c\)
1'r4=DZ6&FC$\9l7Pp18qAa6QcJhXFgG-@[9b?p%XJ,1>*JTFlZdLSbclEGBL`%N3PFEfbBj
5XSVEG)!Bked#7`cl?3_hHZUJFk!<e,>jr(eC8B4VY(3erf[e5mKS-8r-h1*#94D4BXL_65P
\ZN]AWbpTqZP4lM``PF&kB2<\Ib:*XH&?"5J8kAIBPQsRQnIj1@a4$,;Yn)Q%[NWo/$X!!EXt
PBbH+AB?b;T\h>jDBa*>P[jOcdSB?OD5_p/,nLOj6QaE+VIKt-sV(_eelTJ1H4F_[ZXJZ,i<
@e=IVCN>3T=h8_>TBm[$qp;!Y@U`acq5`%pDnM+`7UXIfr^fg.oOac[T".I)1k$TUeCR&\u+
HnN/977(nI??bZNf:<sY=:Yh*6E#f"cIo4gG%_>>AR_>5ntm-V-L23+YIL$SYE&^$jqCVCq/
Sq+)NZ-=*:W4e6I1DH=-n/$8k!?`*%(')'U9iNj%Of\as/t.g=A=sFoaK_e3q790*AWb?ON%
m-6=uhl=8Ip?[SsE/i$cc!P;*d/`aC+mVbV[>kf%b]Au[E`t./X1@V-fjr"2gF^8e.=?*q!o-
+k,c*uPtKggTr"#1FNIHGp[^.?H3e7P#m^;\6]A$]AS%[r<7+%n^(X;oa!).Iq&D*lX`qNd5T:
Kl/:cZtL"T(7ph[UWfpUp1GbG=>?.?\PG4M;a!->;GBYMHYoN.NhW"rGOie&]A:@%(lGVu=:@
(RHi.;h+ZMR(CMKd&H*,l&d[+SOAKM5Xmqp=B9L/T\,Z]AKJ#]A3VU%gis[VIXjf_hf3:K4R3(
]A\/&.:N!8J0HQ"XG;3t_Ld!,oNQr96#n$'&D@"l^T+i+4XfuMQ<2[2;d6IH#om,b^=fmI?k3
j6/X9E]AIU?#@+TZQ=8>!!GgY$*j?Q2.R9QQ_?Q6heM,nD0H2iE>,!lh/0aN59CJ;t)Q&k%QW
pF*16Fb-Rq"=e%:uJTUsP=sXOcfuK7`7,n?CRh<;)H*9LU`MDT.p\YEi&(gXkD6J&><!J8.X
@'5\lCj;!pLPqeRg.d8%a#5?mI>8e*gO4QhcrYZ!f.*0Y'pN2,K3gJJuPQ**S/t1+rt`hUF0
YR(`g&KVZ9#d5t@uhIr6b+:`BU[=CM%p941#4"rG/S\n)L+XQ@,q,'E%c10Y1"nP$Cj&f-he
3a60,hks,dB*=98qN,d@1Smf&&ith!q36okFB>%!+n&)(QLj?R]A_1G_2,!HA8#r0VVh\>A$m
Td-L'Q.n1Ur'A68j*tXd3A0q2/hg4)CXuD"&5XhVrS'=#BM),&mb,OA369DAns&eAfEA-Kjk
^P=:UmZpu+l_hc\]AgYD"'8^FZr/beYL^Ea6+;*TQ(V&L1ME$'t0k[3dZ6;HI;c*=qee>$:cP
5shtoXJPar%'G]A>;=kn)2nh3.!Z8&J'bkYhi'2>T0NO?0Jd%7:IC4C-IA,M4V;g(0;be\CB2
a`X&N0?fVjmGr"WKTrjkQo[fS]Au.'Q#+Ha>Y8Rr`Fsc?sI)LdL#KXUtp!lf]ABh-e(ILk6lbj
Vu[.<9DHPBdMf-8a_;`lOfP;O03PT-o[@s/goS3Fg)d6%s*`%m'keZ);Ai&krK(.,ROmY3>_
._LY*F<IYXlB>1Q\,m9aZJF!5I,7TrToo#$e3d&*\jr7&'5n67>*@d<B=8;P)(Fh\s7_S3G(
jBRXlgM"%7IJ,6Aqk4tYhDPOk)8pF/!@UR@M=ZXZu'+Cc6n*W2[?R4?H3!JX!:f8WpfnW'lR
HrdR$7]A('pGMQZ>).0`:Rh?j[tfAtOf"`&iY=lggd(b9a*;AL_[a"1-!I*t_$Ne&2J6Z-nDl
XDa2^p%LF_1B_^mh3>o&/_T4OCN"3RL^#8tdheP"'IPO+TUeiq7pCY1EGlu-(]A7,>L:]AJj3f
ERXL7rT6_H+D"n1QuV2e/V.0Zq=9,0Zp2((MO`1^Yk`Fp8n4>P[f5=5/h?oYXd7l(FXi58^6
@W@#$]AE_FXVUF[%U]Aj\tWE);#!(n.%QIiKXS2E@[jTDS=^n+N!Xr`@q8bm0t*lp]A7ZODri>5
P"pEpiWZ&pd'sJW5Lk!8<JM)u@6:)*79<JQM,5cZ\X^mNZ_#R"^j7.pMJL'sX5HZ!-Br'jV/
[.WkBFKTp"u26kHn#/eJ/^@lTUGFT)fAu%V/i",r\CbeGt!N-Ho_"q]AOL_t1e;.M5rnk:qcL
B5G7pn9q?nF0HmH[pAsQ>Xf0J#fC=Vf4,!j@BWI-E$f)+tO14Jk:o`6tsK=pr-CX.,oSS1XM
*j3`K-<)t'a>@j3QL4m-X8[L)&MM18#mg/k#1:N%`]A@7^&Y8j)\>cNNdP_/q.4Bkn<*6-?<O
j1`g_IWC-N(cN%_n;p(I5gK<\#_g@*(.JI-/\NA'UUF8Z"Y7D4b_.B,9q`AY9QCZM\--\Q'?
3s(<D,JIFJW"&`6'$nS\!:2RgL[bXMXaLt"eY+Y33Z/]A:Bh\2#b-PVBJr$CG0c^dURiiQ3mk
u;0HSY-3fCa,/kT\-NGreuop-98B`i6s50'LYt_;H>+^0&T_AH7@SW+<Ieu9BpM*f9G,H[+h
4p8gr7SkKERK\9lDt\@Q6g1dRTrcia[/GXCoX(*lG&"A*RA@)8Pa%ZL[Z#YkXHgg(gh#ggr.
#9!kc*Sd+_]A&13YZhJ[h5'MrI`r1&WcXMjP>&-a\XQQQc<V+nkJbd1H_]A5%7jH2RJXGuaC`2
J+$7"92?#=d=H&MsX5Ji5BTo^33SNE:m,/,cbrI#%0))rOmOS>a?E^n[U3_AD!:GO>fG&!+4
5^bJ-46[7U]AG%^HfQ"O!p%ri:8f)6t\14m(`#@!HfFM6PUaN8nibX-[*%_5'ZBJ#>?h:$VjC
Fc<C\:'2>-^"t7%+R^WO9]A%J@$#jEPDn0d>c62>c<PF\$mb%p\p4JR'lAa1=fEo!D:'u"Pg<
hULqE>?F5M::i@k*'NR2.n.o4Sh/g8^lZF@QF^=E^kJ/2UB5V(SGU"F<"m[,V9qId4X3!l?"
-bn,jBYll\(QTp%0pN^2a_[g:4!a^<cc[%H"59q;L?<7Zd:,@S?098kW,<h(kq2NVf3]AtXWI
tKi>J`rrQ+!>e@Q4Z7OF5NfGt?d241:nke]A]AQ5I8@W^DrH+q*.+6cWF*`G/NhVX`]AHQS'd"`
e4KIMr&)rC#h?aD_guUi$5T\AJ7,331Q]A-boY8\]A6[6<05RLf!K*M63S3+Qph$VPR6:?,9s&
fs[=/Mis,7o^Uu+W"a5IZs)4T*_g7bge^5CoG8Z<i++(*;<V&(sGr<=#=F1-O1H2>%6;:"';
e;fQ:6_%RVqcqOda`C`E\/k)LPS9t8aDT_!PJ_&M(.AZfBa<;[-f*)`I+G/N!Y>R\&ia@'FZ
a#FdA@c6F_S`G>\GYFff/7Gg=GH;bOBrKmn(TmL%rL$ne3Cg4Q.,)>-J=!t2=es5U2l'T:hY
M'V?(1M2R9gBu)Q/bl0@,E((d<VIKRlcPF%#)A]A8"lgG@*9ZYe1*mrKViI/0*OqpJ$f=i-A=
\a'*Snd$IE60.jVRB+(gKX[1-b:Y!a=T-uRG&[$f=@#TM$gG&TG+k\f=*4bO'^(^d#C%Hr-S
e""c7K>SNTeMM))!0a7\'r"Ypjq3db%KEo:aLj^c%BCK5]AN+o0I2nWH4D<RBXlH8?@.?Za,Y
Sp3PSsd)K_L3pH?e_NBBil0L'9B#>(s45%i6c;kCCTefK/*U@6k`l<NVM10n43-\P=h5#M7S
/)L;q0:BJ2EZQm`OLNL5LKEPbVtPkUYZoJ;p<+V$#l@;.3d17O(&>L,&>*YVQUOs)p"(R0k2
)FXs)Q"8#,f.QG8]A`-CPoms#085>3rE/9(`qu%nR<mtLm)u('N7L%8MS!^)q<gBo1)>"5lji
P2&Ei#QUbQ+MUmt^qJt@sqFk2_R?=_I(,=9=Z241K(s0#&=*(=HjN#>G7u)D,ak3[9L^+=8C
#r;'1CZ7i4\s@j,G(7^bqDNKobdB5i0WQhOSkMA,>;lG2%bGCoXkCT%VrQ6e7p3e_.e5N3*H
ZhO0JoX?fm%i:<=t;$q8D;)u&]A!f%n3oim=2sRLi0*ZQ_(*l-mPN]A)a7A5I\R&#Z6)H##c"4
'R3[UE1IUE&BjX2Gh_A1r7fRq-?R%T-^Y*,4QPt4_Sb.fnTICj5#*Edqk5bEF#W"3)^dqR5H
U.$R=:Z4^e\DZs*>4,gc"M0[.gG$Th=h1SZfqh_dBo)]A9>`,D[^:>(ib!uOZ7_5fXf/[Z5Z1
j'Aa=?f6;_XNM]AP=Vsfrdre'-L/jF]AR@tZ6r&s,Ik=1lnkQu&H%=An"kE\E)8mQ]A09rN%WO+
"91`aB@_V8@tN$iOTi"^\7\Ldn69(]A)pX[icYGU?Lg[Y(23s>Hq&!`RWDCt8&m%S3nY0P%.E
2elD(RMT3Gf%l1XAu4GKXr>(1J-s7)a<(tEZ;f=7%tXaCQn6N!)mA'KRXYnn#$nA/^a::;N[
eNAVO>/W@%(B$-.A`Oko$dG2REA^pojKt(6]A;_NZ]AUm/>_@aHrl6*(!bN%6Nq,I>P/%tCES=
G):Ll;L#o6-=g@q,8)$>Zpfr8[hg!VY!%Cb@PkQ37fsrA/f;>ZU+-<8EF'P\dfVP3h9%hn2"
Rl+_ZIk6.J7,s2oo^lbFO',O.Xj/4`t*,,gkYZm:a.pRXJ#+hU-?M/nIVuKb_ahW]A)0[OF`(
hl<1C$G,k=ScB%*WKH%(UKdZ[\M0q-0!tX/D0#!ao<ZtKak"_]AC+VMX%8d>M\WeLrP,8?=C>
K'q7jRs$Y^5phpVBsgHWk*[<0@;YRk69/jD;>b$24thj'XXAmn'ArLHXMW.58ma_PKg#ca+!
o58Eh]A3eJ6cpsm7IY)3)Uf?s)inY"@pLB8ERhR&bied]A5j$@Zd-)a0mEg#>B*(;5k[u%t6bk
uNJQP7<:e?Sju3CMg(kO<!JaV@tJf3u"o%qc\jf9`YsX&CjcoAWC[!;jVTD8(f]A_CRIm`L`L
'!G7;=*`&k7EZKVd[SIcJ-=fciA9DHSqftlk;KO^n[X.WIN(0@4"P;?:kmV-ZC#P7_2%`]A*D
Vj[K.+6=#%P&lVAW>;'l&0eh_k'\*Xb8hR(]ATspHd".6e[Y$SS4oDJ6\Zg65Yb6hC?>)N?H$
Nj4&b7GSj4Q7Q7Q8*o4E*((2^KR5iEo#p$NA\GY3+:1q.Y0kHRcD4'fAb3HFrSB_mXaB><@-
[T;,r,oZYc2h0H3WdGlI]A>%f*ij3ULl$!-pM>^f;/n`D6YDY5Y[-Qtq8k6"5Hu!\h0+i>pqa
Qs7D6l<2lH:a<IX"kup4nO+j=Gm^="=OS"a`kpKDudf;<M(je>g&YC04nHrHu\r8q;\OcR@8
u**\Atgo,4[g`oFKJbN+g\SL^6\_<.AN\4rP.F\;9?]A7AM^\M@4]A>KL(),na<'IK>25^sK`D
\q.RMVMZEEc0W$U.?0?'0YGZrbG4,Ok]AHZ#:EqP1_]A]Ah)EKlffcrW.Wb(%I3f8H9WYYqTo^:
aT7upO_eX31,Q(RIrWP5kQCA"qM!A>+(O*f==X>p/[ek<^Oc?s3d\'EY[n;pA`W;8GZG3e>/
EUn"F$\%![mm=8OC,bR3'H_uh^pDdf/7H$+;c\Z!O,PS:Q:@r(=Oh$tXG9t[M_oXD+F+-oCA
tge7V?\EAHSN&FII7981s2".&ckTimiriZ*T/XJ27g()Z('\-TYQK-oJ>.ls-<$cI#<n-/C)
19N2cC.eg(+J8^nRSRO;&kT@&=`7SV%%.-uPP]Ac#Skg&p1TR_Z8'enKi/DBM+6aTML$l`3(b
]AJ*pI=b_dr9XD7Z3(OGE4pPp/Em:c,WA-g]AF++epeq.mK-eD85<J`;8p=".6O$\'\t0enfI$
k8o0o)+b;1q;%81^H]A"RQBZ!+]AL&F=5.XQ=26q:=gqoPO@O?JO@:s4(o>S,lcqV)0g,@"3n(
lbc$/_$7nP$kDBGD;6PJQ1e/hH.dZ#,"lmkUP&bDs#.G#bQ%04/n"uKW8Cp,as<S49\N4aOU
.:tm3m6e-kdN<+;;t&O*C)ukgK</pt^5Z67:EUf;MFZC_mn2Q[sg,8phA#[alnt.rmKhjB&R
5I?GX>TALqbEqLOi`N#M-YK_OZ[MgN,1V9ZNL#DBOr.E>n'6"QIc;J<<")3j$R=,JNZdrT@o
HkPtT*5@e>Ads@o3BGZi?2dAqqdkaP/m/#;/^JdKLYnXXd%$O:OI%=GJ6HtXWT,[5k.q_8^1
oA9ng7c^a'ogoO-DHj&33^!pMKNoagb1ZRU-F/85r-UVirK56e!KrsbRRI?fba&5qT39q9<5
^0jc5@$7KfI,_ConM'1(5DAE$AiAdlcU/[7HmH`JLHQu#auf<Z&<=)f1Ee270h*`':OO<#W6
=%=67APbT(!O\NZRSh6`gdF63ut5dL15;hrC_VJAROm$@NF#,rV"J)+rg$Z3He4RlCt[h`m=
WEi8So&b>p>kaeS$L'%-iX3ju#gri?>*[P6,^R,fsV.rPO2nQXTG@CmeeG=9CZr2aLf<EVNM
oDp%LKHHT6qn7RSCq%->u$_:NV>5j'.1p3D%/Z1lX?i#IrH5hYua=3SGeP*9`p!i`^<<-!u6
qL.F:`DKCKC7C&5G>St[qFq#Q'5L&$Qr!SsA!P)p95Y=(dnR@'N]A^C@(?k(,\pg*_?2B)qI-
)n98D3;F#(L`tgDBn<&_77)RgaOj0HYZX`!qeCe#JmtM:5]Ap-4Kn:S"/@DF4aP+SQB1lQW]AC
m>M9V4OC+oD7(I'h?>7JnRRlBpJ*o3=g#b%?hS06&c%&JSVA`,q.aMg?@X"^n?YNofu7H6/]A
M;mqh1?,&5jgmb?_3tigQi]Ag_S5;,BR,B%(+p3_VmToiM`.*J;:+2WV*`0A83'GIq5[Cot(m
^*h-F>5dePV0:,iP(c,dCOUS>_`cNM^Fc;)W7N!kaP*C5HN0FnE:Mr,=F$D^SoPMFSP6:P$/
4Q_.E!6Ak2PT4-Ed8:CO4/gn6rPZ_7)G*qa=YADn(jT?>%'[B,r/DqsJ3Ck@i"&^JO33;!HX
m:n"H.Z\s0rt*8_"@`Vj^%&2H1rOgrUci!/M(n/?>7f+2NfSJ%/u#.^b[6=$9`*@:b@QMDHQ
!'*$QmL^j>8#[jA4KY6-1j,UhNVW>-W+4h::b]AGE`7k%*r33TO#;M?H*JOQguREAtl'*6=[5
fV_N?W.,,GN"4bI^g%@I4<\Il,bfdKJ*<^0VaIAT.r7;adOlgI%?kGtIlu/XY]A@E='rQ=,#R
DRI-UnXG1!$,bJ9W,be%I4^Ykn-Y\,VG1mNJNXl6IUc`pfr"lT(JTA8ptCb$d/JpqKR;q5SU
rs:<Js2=muEPCkJ1idF&,L("LcTVJcbHr@G+3q\"50\U0uQ_K0!sdA]A3dkjj:(Xl70oJe(0a
0?Z\\:p#qP?Y[*9d:9(/r)E#*T-3g$GtnqJO-*gfp.U>u>MjM'i59o"#cU!32BY*;"$q)6!%
,;?,oKkB2<;G00rQlhfq$D'4FZJB$ARUNs1?ss@4r<UAh)ZR@1^$<']A?;J17OPH6_6L0_HD;
9;Q/U0?RT'WYK_MX%51epb8=t7/hg`M;-(pWR*lk<WUjgl;jQ8qM_X*0f(A,\)^bQ7o'@&^Z
+]A2_\i$Og.&keID,**a(Q(bpj+ed_ptt-/q'Vlg\s@<^gso/e"Du:fb`H\f]A2b!#No;N<rMb
9R)\2<&C=V)2-bjKkhKcg#PT93hq7":83)M3UP_Z1KW5]A?Z8Vr_PWhE\6nE1M6P,l4&4r_CB
Y\FT\h=cs$h1m^Uq&SV@r`F9V(hd=]A_(=BJdmfh2)BhW)HS`pZSW$)P8S491l=JA/(S&O\pB
!oM<@/4o2KaJN>GsR7nnD-FN5maOjbqTnJ9LRep@pTZ2g<'303Rd8Ied$9BhLQs_R8f_8gH0
J`VpeTfEqoKP>R=I$<pf/8p4_\Zht43At/G6L0TLtbb&mCU`:A6^#8q)a9O6sVH`t5n\0Ane
:g,sr*.Mn:IT/-[!OP$,:NpD??VrU>r/DMBSR6jn-Pk-;K.oA/kdMI?]A_j#W'.pE!RZ),?6k
5Hf7Ps^#ba/W)ZC@H:#FW%X)I+njNd,IH*'6bmaq@`>8+h<fikaq*"_%<'N@.DiGs['L)SKQ
d@7.`*'."/fOHrbXKehY?j\0UXD=8jO%ro[4+$H6%qAV&oNGtHB$cm%PK@D14>dJ%(0:k2_F
<FO_I@g'$++e/#f0EnGcD+Y<4`T'e%/dW;)/Z6OB$!P/b-O[ZEb@/e"$k<94D3MVd.N>IL^k
-US>O-oNn2q,(QhHmGNa6dSk@3VIXCK?g0OnIJ^YjjT:0e$3nI`pp!o+Nq17n?%Aig`QG0R]A
t>h/Y*.VSdD_t=3oJc@l0oS!p+g6SiGYNNP#"uCUt(@?0e/pG@o&JDVe:tVBLHi-#`EClN8+
<EVuE?lc:Tt#,]A//><LInociB@#TCR[dB%Eu'+!0^um$#h"57DJU7eX*Ogu6@78>?uDrb5h+
78I=G)b"0@Ns]A9jHO(>brcAt"Be\'1`&u.qElDY'N!!fh*PM>QHQu>F$1mh8Xle/3Y%"#LTu
L'D4=i@,oa$3;:Ai']AQppp_Dd_eF#Hp)8G\\Zog,6J#$/fOe._52tH$W^^4,#%ILI?uu_<!'
V'=ucF1_Co2A'l.X%&[):0CaFG#;9j6#>tg\%P_c&OBajnYQXTgZBMbC<8#0q)>[#,ibSr7f
^c$lgaNc>D^E0;kRYUo[K!Q'X<E?-VBEr\laeA-^"eV)mO^(9n"Z_(mefL()\03EJ/RRq)W;
Yc(sgdc^<g1Z?FZ,97h[.LT`$)i-ImsGP$7$'2"W^e,V@t\(ko>&#Ad.%q#cNmoDY46Rs6t[
+_-,1JC*,MJ.n*b'7*5XZij)*),i`#Cl+MgPc-Q<br8<KSXfN:Z$?X>6j8A.L?j/U'3(9+r?
G(9noQ[3S_'OercS\T8312/i$V<;Q3iu:Zc^O:St%5KhaEuX+GebZcQKQ2g\;6[DHMRVk_5K
!SCb?iP(YQ-4=.W^F;pApI&PEa^1\,6l'(m=s-pXro&p`"bV]A.T-1'H"@AXi^IG[L:FH7H,a
D]AZ:qm"dM[H3=:fe>@SmNnX@G8_t3Tt+f[j:!3=%(/sb-\8SBE7Og+>K5U"Amu=e,[9(AN%[
Ll(=MA!3M>[V`DrDI?r)mBVC1ZbW5bd5h_\oqq:Q6E3:j\:.>\t0l]AO^Jf3ng;hLNa=N8uH,
mVFu!_DLfs7?-9dYn>1[h[k`p7JhkX0.WkAI2spo$iK76+Ic!YPgdk#:>C\I6uVOB+X;^#<+
&g-&o,U0Yl6.\Z#&"?lU(V`DVFgDgR7Pc_,[*UagGpF)hN^sr@>"k^fgejpton\"l2_UGe2=
fVUSU->TY+[c"s^Sr-mp7*m)sc,VHH's4eKSHjbQTU2KI3($DgQ?etFSBh#&/Y/dLlZ'5TO4
l^UcBpW'kcK",B1d`_(1=[a3I_n0nh-k"1gQ^,,kRe/#_D%A[VOM(5cZm%ij'\4:Vk;K+qI,
)Y%9<.L@af)*^/EM@.l(@Grt+ctnN@m9c=VE!!\CUpRR)[a/@N,]Ac7fE411AI6'2"Q`?fFq!
b0CaqMRCVZC`q;X.Nf!!CI;Fd?u,l5P3/:Q!IMec+$Z?_'#6'!`uat2*iAT;a8AK>1$fWB[W
fprfr>t(>ZHbE*?XE.hKi;9=r;85ht8]AW+N6Q4,9\9V@ret1iQ-uRN:B"Pc)u#U'=^,&X_?G
R1ZU-n:"`C!IQi*7pmJl2HT&57>r?ro*W2')_PQk(gAYI`[Z[M]A\M9?=flMZ)H]A1A4H?u*Ji
39lGcBO'!ie'/HN]A?u;'.SA67>qhY'cjSSaAr;Rh&Z!Y`Gjt5re2H1nsGKUV6,g0LT7iP:Np
(Y#M_qW(1*O]A2n!WPe4HgN*Pe=]AiTX-nUk(]A2C@=&BrM,ldB6pDFfad-`?$D<R?C/@dDa2f]A
Xa)cm^JY<^EC%LjKG@e.(rALg/b<14F-Ru.)8k'!^B2+p5ISLoB4j?^@Fem^Ll)!*Vl._t-i
:Q`0*1uCNI%&l=h`L)m6:Go>QRV&kuVgK3=<Z%ff%C;ec#+.;\dNL:9m)^)Y]AgPG(kU\RhFj
G46F;RTlB03]A6T/!LoF@=L5t`2:**!.Zp:C40lsi(N$3@cadrPKF8kt's5AKSr\@<-V@pg\o
)Eq8,Ne,]AV.c=tGk4,]AVQ/)9s8:q`bg!%Xci<U#pm@Q18d#+`8TN%^H;e2cp<6>>r=r!lU!L
;_IXKLgIKp-fI7<c-jWc'$\A"naFKm]AiB$&Iqm+JS&bKIc5WB+=Q9,(P9D>OuV&G34u,3TFI
$*3cqaf#_.S`\J4Pk/,*CmjlC[lT^n4"m0el4;`Rio.R51EEfa)s9;N\G:TKY8gYsNl$06hp
ubLb+r;i:s#ea,`lL`;TSM8@aJCfd:pm&;@o#Cj0l30qNZK+hk8@[-!erq,oo"i0&jVr/eZg
;H8:bQ]A3RXL<B=sM;G:R)P"4oMJp$$-B:8X'GWS^3fX]Aa]A#+TVe!]AD_08&<"&WruU_Dqq[AC
H^r!nBSJ"P;eIeMuA`M094Gf)mH#oTJTHt3crgfC/TP%\+s^1K</KoW,YZ>/r+>V0h'M`"RS
R:%R,65\6a$Dn&`(>ED(Q5=A?nR%g<c<-=cqlV>+-,\2+[5$M>CCLd#mopHIU(@.C2g"NE>n
rdLeMO$F%ciY()g?r5o?GNiJ=?X>1k9\44Q)<)7so-:,u6nc.7Ij3OS3jL[GIg9LI\75;#1b
(d=B)1!7IdGo_!r,sHHZ)NOgr6'%$eNkhY"THf,:7JE2UJB)E.Uc(Q5>E*3N^lh8O^F,ZcZ[
W7>'GRU*b&$CjhPN1F$@gVnUH!8cC?+OHS*@$u+@#,4(Q9a(W*F8;=2Fps&*q&L^dI5h#F;W
Gh<jMPX;.S+A5j(9.N'K3q'42_`iUoK0><lLu`t4%VWb9>W!A>2PDZ_P0HK/p\3)"#FT/@TR
8-C-#E5[3k^uJ&Bk-PoW1n;HkhqiLt!p"BbTCh_@D87hC1)lM$dQh^+U9j!q/E;gTG^m-d)O
3Fpf`l3#MJR/poJnVkDlA<@Dmq"=AY41TFW:0QA,LqXkf[5<*V3ZGt]A`01u*""+%m+Wj0Mhn
a8Xq#Li6?9ST,]A&Oo'L&:I63+qCl3ZQI0Nc3GV?N1,=eE3mmN?O9CT2/`!UtiHt-,&qo6j(1
X?6B'ugC9+&hBPFhT=^%e.$$'?7\fcRS%lA<*C_uTHEO`,k1K=?l2KO[4h\5$F22RQ%jl,1h
7X&20!t&A&[kjg"4N[lla8)n5BW=r57#^Pag+((]ADCJI*;F]Ai_<#fMJs-R15N,Rd000%H_el
a**RPS`g92V<j!<:l.u=`l@?dbB(jn$.VuFWT3&TL$@iJEkW.8,thDoF2Xk=^``+?n_Z&ER>
RC>'@!IP4udob#$)#G=1SZR$NYE3qqN7Z\)c&UAI5Nbj1s+""lBtl\-AEZ2fA^^iU?GAW^B*
bRXRG&neg7<tm\#NI@>L%nS?bl80%&[%Wq&Bpic0H$PN;.u5`Y-'<WIt-%BH?.aZpUPmOdXE
5]A^A5Z>iuOJGGQ"M')9Z^R'(u3i.sj!Uf4^mI]A"nJi;d/%'&7'@e8J4hR!FH7fcJ%gmk`CGc
0@sm?H54WGE/DJ,G/CKp.7;i7ER:=n..H$S=B2t%H*o"#C0TpH+[2m55NJDfh=smqL0.k\jf
c8-5/k%CZIol!f#lVbE_;\6#-kPG4"HPeFq+1_*Yh?<se';h^G=B'V<5l;+OnW6`Z!b(]AeFq
rjoT#Wu4DqnZMt*CMPjlb`h9U]AYE.;c0!e'@jl^k#3d/8B==^0O6Y,SEF\B"oZFhK:-P`79l
4h2UAAK\ps30o/7;!&+Jg/#X*=@Sm@iH,^5=$7Y;\cZlHY(Pa5%,9lV>!-io_X7@A-qT5;(&
G,O]A1!jGTY:@p2LH%LRPHf/]As`=37iDJ%$6#m,%c\%>be5UM9+0U@<hkT+((YD`<nToj[[62
iIh.Qt;Dn)[LfR[0U1<(ic0<3(FF41Kp0t%6+cGnbGSMM>:Q$k%7%[2T=A/#L&9I=e]A?t)]A*
7AC*!_"Z`ec2B6cJJDnk?-PsIIudQfIZm<It$j]AC8c`0W(L5P-`h/h3Wl_#r^,n@@OD+dX:Q
8ai8S:4m[K<0;\NS+??4bQPjp.8%:=]A`]A(&dY^#n_+O!@#gK^)5Yb-l=L&?o)@2e-BTT?b#5
q;:F^5o31`.P"cq.1l6pn(E(qO3^&QJb@_CXfBQB1h1JJ?0*bdfCu#UR^Oa`N]A@j\2TfmH$4
YoJUgkaTKA]AO_2l>.,ct:5\V@kY=PX7+l_C6S_Zc_JY^u[;HG[/ol5'+bJ3of<Asu>;l^otW
u=bl-#BVe(7;WB/u?)-ctYBT#g7JqY.)6eWk!4grcL42T@rPH(c(klj^5p]A8+rlq;I2#6;tD
70LHl#19Fk%JW;V`b523pHnp.E(M$'cPH`p#Cql_n1D=@$8DsGM4B.if'!eec+CGDlGMla9.
&jnPr#3d.WeWhc'Y[5`m6k7WA8#_):*t.BVnMuH4MIib$$ZR&D`=I*L*&cgI\0_LYL=8^>:Y
Vc<qQu,1hZg5iA"2gMY)'/7D[VpFQp!tIq>T&0fW[,F"f5*,/`lhUm6&`(XT+'4ZkUGOTMQ*
;b<P)'m>j.6bLUDX,&`rtDb-s;T]Ae9;Vf(]A`89QMsf=(.mJ@gsuUiNgG`!bI*:Uq?b8(nKCN
Wd_@B?-jII>g\g&om!kp.I73=JF?_]AOe>gaE8$Z(Ne(CIR)?K%g`O8@!%87mCTm_FL.o($@^
>phU[65)jcP/r9;^LW`tQT!C33"HBDGjPAL!N>$Ci&PXlj.A*8Db\!eeO;`B8XAE3[+G^OQ2
,B_1TS>6ki+WI/=`hCWs?9@Z>.Snl@9`c[Og(VjR[,6"TE))ng*)7U!AsnnFXfg;0(LJmA&)
YUqO,?bs!/]Au]AKKa"4:=8i90.ZI6e+`%el"9U'g4idqB%)N8KHYD4[ViuRIo-ti6:SZF=0u$
C&EJP/p5I$B-kS2%pYU[MMSuUQDJr2`C%*n7*>fX]Ai%tU2ob?R8\Jph7ZKjDL>olD7gWlEg5
W2rt<f?*k)\Uh(%cDJ1[_i`$/fGPT=(EP$0rHe57t&!8;2VI'OSVJQgIj_$S'G"gE_`+<eT?
_J@99]A"k\t,eRFf0(V^2E[BoKJuJ<Bq#?rNEqBM+WHc[tp+-4UYt="^u\DF\\<jV+ibV/WGf
mf.*cr)!L$Jt0Kii$C6NZkYV*-p%h)e^k1!]A[@Zr5[r!sn=B('2$k`+@h!"6);HHM3Kur9P\
?I"`:nG0A3kC_T=LZo7*rbG>$BU,9oYS`?A^ACDafZ,>:+VhM""0O^0srsQ-=4jNof=XW)KF
W&?[%$,8tkY2Ji$Qp+s(&Id3-Mc%q^IkFib;h]A`_c^W?dD%N^;T9>NdtO1A:R6cYA0KYj_U'
LnT^TILqp!i4N>j+J;0&U,/]AE\VoR-VBAM&+OFa4Q,"C`;l.bdu:S*s*GpU%/;W3JHZA\Zhr
^(U[1UJ0a$MkCI"Kj/sSc1H%sF:=\o-=9U+II!Pl-V?S,<=']AQ1?a(hbLIZR/oQ::[L.W%Ts
Z&M8aJ4Rr5-MbarB?^>5pY&@L8RiKKEQUIY$;SSR_=Z;g-SW\UKOQnK'aLceq3&=qacQE]ACG
kf^BEdh\rPKn*K7,8Jr`/=#SE3BD.8tc;cMj4Tj[[UA!8WZdrj10"`n$Ve[;#+IIZ6,K]As!k
TJE_27d##a!ZgoV-iKX/aI0J[jmT>Rdo5=SaWZuXN`Q`J%pq;B-Y#"Uh^S@>n_0t=bm'un'!
pMD%a-toGpW-7"R8N4#l!D35IWdW$cMY&l1g6:[V6AW7NJcpLli;pba'+_d(3=7ua;:\d01g
E[?]A&uh*QN7eZBQVeoK1?PS7Hm&o&tHSdc'8$UZ?g,BW`cg7WT#>SOAV6,b#1'T:@_rZ6#rp
mcDT9/Z<SME_'e4EL?k4kLt@/GB]AK?nUeLc:P\qO(VW#;Eu=EK5cI@Zf_`95\A*Vc45m9-1k
,r*;)(!q2!.%cXo*$:!mTbXg*dA"?tHH:Rd8a6o#:</ko66064#4_ZY=m4car]AFs+cYoDRTh
3kp;*@7n3ICV^g?$Pa%7L9d_OM@bKGpGI/u"p-&^S5A(*;'2K.;Ymc,bdhqBsa>q?cKhQDl]A
QBLnj3bEOf.<LSVo[4sI(jBYI*2P;`mYte*!!l]A0=?%uSf1_V\S;*Fj%g;2!_5>KrmUmU\>d
J`%/kRO/%C2cJ\DFM5sRe-4<*2Wdc'<Loc$;CU<h1"+h31lBBNouk]A6%S!rEAM\p?-:+\*I7
Je\]A4hsPng[>hFUr=#h--f8*ZY'eaENb5!O\&\L=[=I)TYKY7RL?K7.:rW<F<>Qi+)nW7s\$
:L>cU=:Q;CL![]APanN:AU?opKfF(i)9Co&b=cpLMLa>k?CA8HIgZulb[oD"eX%]ApcHd',(@*
S[MbOBJ[EgF6'kn%Dami*E[QEN^O.F#<"`s>Rr&D0:Du;l)N8^Q-K#@f]A#/NeUHMlm*3?i<a
$?#eN&nar+HB4,OP@V!EF<3fhR.E<9FA0#;.!*r1%^2<Q1.'"d0j'_^g@2PKt%d50nY#YZ9@
o[U1cqNk<mfX$L*o&)r$]A,4**4JoO<23BgGgu-!9m9=a7%'=Np[:cQn-#B"?hT]AA^sHUW0cG
h?f_iB(ZVNOL?N/F:G.%CT!&sR.n,&^c+d--U6g#2k@1N4D!K+OX]Aq5>>RmI-rl_Df-q&NV0
VM_(s8@#GWK`&jO.ni<9H8:=-u_hiZ6I%HV@T'CSLu3ZK2/6OTo<L)B#el[.U:R2Xc87A*JX
o0_DF&CNDoC0"n3pLmZhTn+SV`0#5;(H/iB+[B-H/.f7[D(8?<E?3I-Pg^OX.hSqh^=)U$e5
OF8$KWjuTjPY-4l=>!D-8"0P_"VY#5)ZrcK1)Y]A/nd$$F>rt_V5=tLi`-nE=L!rV*UAT-DsP
LjpVkF\I#g:MnNYbeXkIpb6l#P?Drt*o3BYR9b`OJAh4;ep+3l>n$T`RpI?%Pb',$(:jFGJf
$udulHXeLrgAPdV4fHH==_m"]A'>dBZeR5&lr@GMi9?XA@98b*E!3JHASJC"Tof1eJrHY%P+7
c/uAlRC#XkXrM<lo".ZFM]A]AL1'47!N0A`%f,JMfi\inq@jbJ4b/l&UaD5cSmZ?:^lTH+2+Bc
rYk#m;Wp!MWm%X"69DCs4r55"Qim5.50fk"elP8h3D)#3H?o^5Qa?.)sX>85nbb/qnfB"G1K
BsnDAR""r]Ai1aJ4H7(><&(\lr/qK,G*KEIb:!VF):%U(1iY,BHB4/F5aD0SpjnDBHS.s&BV8
b=!T5c+knr7gmBr8HL!o.:l,jtf9`Q-.N^e.<i1RbS7JndFa6uf:>eSUnSMDjbAnEc-.Rg3M
7KR>bb71IS>oB4,&3V[l:q.>t#.so.]Ag119$M9KcWJHC.RaH:rUY0_+C?l\PhFE,(KrcMb2o
]A1YV6BY]AT58]A!jpO56Z3-YMHD;mmANSB!dMl?'Msin"kZ8HS9)0/_9il^\!E0%q0sh%]Af0)e
JC,?m"8:]A,9[\[_c?#I"rA"V'M=Nju9CUGgIhd,rth;i$4"h(W#C4CNq3GE;e1U2R;ad@-(o
3Pn@$^5#13EAis&aVM]Af?LYC=,`+<jtcC8fU)BnK\j>OP]Ap<7Yt19<KLBH-O@dAt?(!"+[`H
m^%*n@:gY(A8S/>"AT?Zf8+I(YSJ;dVH(;'"[G^4_ORW,W)6`AZ3Q(5fcROjM_OOh1@e+Y!^
-<@j-B(ZJ'J/oD[hVp.DDWDICr@,#M<`XI!BJXV<at-pr,\ZG9DIKeYXdq$bV!m@Y]A7ICsDC
nDp[s(F="1kMNWKj$Rs)t)m@LI/fm$1A?&<*;(.Na)V?>egsJ0^&#5ZFI4U=>Uu?15hB$AN/
6?QO<`K84%%l3s-:/;N%-=$?mGSci6$#@F,'OXti4Un.D]Aqa;n/p(4T%d!=8ek#-"E0Fp8OY
Xpr^Y9g2KA-i_s8n(`(MuOGuGq3b]A^rZKZ]A8'NlLe8eeBjdOR5k,M,:e54UKdS`%/j*+XOo^
KFU*"V!>ql-/\#).r#QP7c>,OI):$l/1,Z#q^Pn.dtKUL)UV$_Ntl8\`R=??h7p-S!4q/jUL
,a1nr4>;;E@:B]A3!W).n:ouO<G*^Aj%)Z"g_UU!7#(K>"10YJqck11E,MRG:8f\/jUQufopq
pku?S.8JC!Rt<Is!)sM!EVSdsCsI5k;X7i1KKKZ3/Z(8Wg0Jib&Eb'Jq-i!eY4C=F0`*"]AjW
:h^-PtCdp@I6DB!a4\DU7bZo>)jO.,:H.a"pdp8.l2hOMn[spZ`Q_+8YUbS\%98A8R-pRW+b
o9g+]ALYM\%Bj8Z*KM4Js"tum(\S=milBV.@'MLf0'O*&3oJ6'kUDeS6jr7C):;gV#We-]A&3l
#3nb5F4gs,?$h_;]A9^G]A)(QmYlrOd#Jq\;0-<g;qGd,BlUqbiiEeQr8,`=#>N**<*K"AH1D_
^Z#=*gKfh&7Ae8RS\TcR>G_;mKj:;Y1.MI8)'T+ONgCmG#R'2,L-)Ck-ipq+:>cFoqVuhqTn
I<!U:GIEE5H"kO.+tfk6I?6\\epdD8fF+$i,F_&IB\75fH9LZ1Fs5>XLDHA`[$K2%s>@,,Qo
A,X/=rW+%%:RQ.DpLDTXOP99@,k+/eQG^p5ZJ<t*$'^9X&iRgM'16PFQfJE3K6orC[UX0Vc:
t@NJJ9&=Z.q%rt*LESF>[=GM(V8A/$2<m^7QVbIn@Tpo?MO]AB]A"g'gPQt)kP^8LP^[p1>Rt=
^X.+^+,KN&j1!u4aFb'GY^'_8)D0Ylg1b:j5A4=P[=r/q14%.pA4HQ29nke@"Q"=qd1cGSKp
P*]ANQLB1=,fWoGh\&9`1&ip/%m56?t'r;)mbr<5Nk9"FEr==1^%=^ai$<i>fF1t/cY7Sdb/A
UO!SmNo49O36MVZnK=Nm[/$Ejq),<q?,lY588q\!`lOFJ,qQ(REM?$T3!g-icrio6m5P48o)
3S"'AMYP8WbU::=LFOcI(pf`8$Z*fTsRX-EGm]A:._G3bud#HX;W/R2Vt0h/Y!'-^6K@k0<FR
,I=X<&h8/4La;jP*B_*3`Oj3P)NXB;Xdkj#a\Oo#/F4PIRa&?\Htf*2ZkVY&NVWsmQQ3FpBn
L&jFcWh#E.tIX6S!RWH8iZ*_:Rag/.DR>cp8%SJM"sSZ'6Xj29tLk26irZmrZTXj&8<3S\U$
&D4QIIaTOs?I0efe!9W'ih?`(XE@G(Fcf$25j'[cidpn8Wbs!r:gs/%_6"pu$i"IW!k\AJk7
$'a%ZDB-@<Q<[?#o<<8MlkD:@u(P-[heIr7W_b/fSOiGlI]A8(oeE]A,7?GK14]ACjs670R>H>L
k$"1a,7?2-E`$rd%^iQcp_H)3R+Qq-_>=3W9M(R,RN<YTqT@`1Z)*j:0%iN7uDRSjaisJ=nh
<[m_-[t54$!QGdk$_FLL3gFlGAu5e$9b"b^#LI6:ZPRa'B.6DYG7jE'*#WkeZ]A\fh8gi[mBn
3JOuA,D7a[[?<ZCHU%oM$DlUCPFfH#Den&)0<Htm=,WT]A4!W4O_Uf@*Hj#D@&qI,P+BYUB$W
500s7MW_\HFtn3kIDdG6"2W#B@77s6U2J')rUK/>'!P"Y.<@[JL8(qdesg&PbF]A`g=/U<<`c
_qU*6uH-Y@]A%s\R.aE3ZT-WoKB'tLD]A]A`mSQ0/,:$a`)bk*TjLL0XMs*i!AX;k*-&AD*=[An
?mM)$*3t6TnO7iS5<<E)'Tr^#W;lE99DohmH%9gCIj8e0bY:k'T'`uJ$Gd9PKh,iUZWR26l,
NH(A?L9.O^e9R3g9fT`,/E*)/G8*5+i[0BQ0E`9-d_^X)U_,f!*:J6$N!Q!@\lIo1jBU'5Y]A
PXmi?TI)`JsN`sj;Ta%.D92_$:rBk&K[77Zpa8UhEI[+f$%_+c-dOn97e9,"JR+*jX-J?,kr
akm=D^V/FfYo(*r-LNK8"=m0*J&8.;Qh>)5l8mgq+kN,A_l0u#E/9&_V,ktH.)uX6?:SZA08
8foeuH'0fc%e7p;n;cB'2h\mm?X6B"5r3:H+Jo`fM[6?Xs?npj[dZc5>1T2UkE0>Vu(AnLHQ
B'gKKZMY3$0j?&9Y=JRYhV6jccFH1i7OVR`iNW/^tdFHs=XW>6VjbuWa4Kj[5C+Y=8jqS-b,
@FQC'$=7@/E08SBX`?6gl5*lVbNTH5V-!V%I(KhU&7LjUurF%4r(FbRW;!#@FkYE&dnrHq_@
QS)'Ei2bEfN:PpP=V5H(1sQ^6^f,d*^K6PS]A<`.moN;,]A]Abl?Z-F<inoJ;9%&`V"Vka#X7d`
pZ&HQ'cKK3!h;EGg>1s:hh?mE-'2'n4*A2,<V!RCchf8tgt&Yo'/!$VOaYHdNbH_#=f#=i(o
mK^#$NK]A5MPNnFBpH65!1F/qi1,]AO7W@[=/C,8gLUW.6&QV8Fdi"g2fj@`-*Or_2$ft3nbOA
e?<=lIQ96N987rJ48`A*$%kQ`&13[VC@4<SkaR3BTJ59H&4.Gj4N/bN]AqA2/;D"+c7`H*ghl
@]A2d7hY872MQhnn11n8&!c\C:)>\%\ia8heS-$EY2kT9^`4nMr.PO:o/t;7c5pm=T#dT9>=c
Xf`P<WjmM;FLW/'o"R%-pr!ntK9QCJ7&cJAVlQ(pZ)AeusN2#&]AQ+Z'1rp_6)0[_6rne[nX_
]AAFmbcjjVjNKd614p&+RWqT%+W5NIq!U)+]A2k(?YJ9I91)qhL('NOPd?;e5'&cl%fm]AX".X%
WmU)[)*F:9'Dg(,(b*7&:D<q,,3]AMuOWD`;LVr'_gZ=An;qmYrEM#LV`<\PTkm&L,18X1J-U
3_?*5GbB'4D\NQ=cG^:agXM5SP9.(&8M)om$rd_*Tl:nB$`<p@L7U-8u'T4k%nYaR&KMK:La
kWld%c3T:RinSMFJ`U@!AM%mkI7Jl"Rf5\/'<%]AGp`Op=R1/mM)(;=_U7*+%K7EVQ]Apbu-e)
MRB\*MG)XRN_g\#QLlH+.r235)^4[i^7EN13q#S/ho=0'7&UibY?l-s]A:0=*+^L!@'^5H(*h
j%ldQ+Wl,!+W]A;t)tVPEOnri'.3F:.<sGrmhnXu<HQ#gl`WDl_nVi,"g$Spg<0'sNBLnT$P4
H.E#U8<4@XrN]A9mT&'Fq8i.)rIKOf)9Bg5J4T6hH(=ZJK]AF8TPUm\g1T3fX]ANo+aj:uP6&1p
.h.ME$502B5ULDfLR2:mUW3E`*"6p;@Uq1SWknZTQkFFq`<0R4c'K7<o'Gf+3eqp:AW6o/4N
0iHYoV^u-$DYE@gU;sB$-fk/4o'E$L]AiEg9U$3XZ7*/2]A&Gtg?utekM(qBlDSVA#2i\V6%sZ
eW/`fCi0(i@6%+_Gk^+q(aZcNJ'VJGj;"0kMG8HgV4+KEo9GFOYb5[uE:T7t$g%9GN>X`#YH
3mX)9e[^oRQr%M,$kb8hRfSS/Xg]Aj>6FQ)@Jo78,a>iBo;W"\+;NHp!]ARCm)7k<!lI=o+I$!
_'Mcdpr`g0O-[R]AE_nr..rSd,O4eI?/]A;2Zon?Ag#5/>SJEMN<"Q>hi-EPVIXWp!+a9NT9*L
*L5pss=7`YWW)o]A8oAf"C(;D!:nY;-)crF%+r`ZC`9!/J/O#d\:O"jhm_$Yg,OFBlmAQd$rf
t2$`B"NFjCE^kk!j0`ChC@"ckgnG?n3$XDmBaG;A"ZNj:c#(*(T_^SGGu[-YM3.*ZA;aHOJC
Asq4*!V"P^>S#,XIIB$_l%W63=8gO@:$9,8#cs,sl@'!i505R.d\ZT!Wg:\D6A*EoJB]Aq,Oo
?E,kBTM\2,Q4)dS5@\Z-9X'+<R]A,I`CH:(s=Z3IYnW]AcLST4hRB4^X(<o(l8b*MZM2,D[jTA
h=kW/87;[anY.8DE%?PG^QI%OI;Z@4V[P6G$h_\W0d<-(+dH64YFc3iN25_IC1aUo<!h'jAT
D]A0'6)`650F=:+a:]Af&/VG44[OL$uZS<n[=@n[sV\-]A=P\!R4eUScsY$dFp30Sj=RRc`G:.,
<d71EccT%[f'KecA@X_k>gX,.Z%l_*HGkt2c!YMi/t;(BGW?RKa+)KN@S/Z-L*miGA7`tmlJ
*M]A)tjjkj.Q]AS2$OHbJ(Zm;*j!23ru37_$J#\"GKoFAfU.JnI@JR3h:#M%[.^`YA=m_!(lN+
G-k*3e&TiAOYVP%dC5$u&'5ao+FQ0L\qQU5$8NmR4L5>\S,mt:DJu"@TBVZ:&B&F?Vj,@Z+]A
KjHc&_T0/5IE'3u/AmG?1_2XhF9Gms'Wg?GaBY4(6Td`>N0:J?7E5DJl'a?*&(JT:1sHHE%"
),8%K1F-$=jI\1u^N*=tS>_Sk_KM*M//e@!Tq=(N5BT,i>]A.DrnR&r`HS#T:jT21j]AJ0;[[[
CPOflKU/02,+j)FrfM[F#O0Pjcom=BXC5B"L$7bO/AKuQ86VD*gC!L5F/ms8K^a;?8qZT-*2
[]AH>Q]AQ_sW*?Nn.shlaOm97EF.7Nn\<tE`m9YE'^7MCmFH#dWWNT>3?EHl=DU9VYm-m2nI;m
0a?%O@9)0AaOCkLQ3'fWcEjb8Zsr$a6g$]AeiOI-73c.pSZ)ITr*.O6Y'D$uW`7RoY)OHW==i
hCl7g4D\Ku+[liYQ7N:U+f;7qjV6:OcOu*Y.HSf2T,hD:P#]A:4&Xu([]ABd9SsMfp8h[RHj4`
[7qoY!)0-*"=O,!'2OEW![QU:tlq8,\<ZuTedbs)u9u26\qBkp6`s:+KGZq^_6]A(V=(csgT4
SeD5!G5EpNON^Ks&.bB%WJXgbDMs56*le'$K_8J0ISUd`*1Ij)XIFs0Mp7nmG6n;Y6Q1s-79
g9@d3]AZAT(.h2rUCV>Js>fG=<e=9Y[?T6baPpR&p'm#i#9*N!abD93i#>.M'om`Qg#`OmU*S
ZBJW@:7Q1NL8s2\&=MMD,s6U$2sT;+#i7MFJV\JcWb4MN&J0a3:K]A+YV)?NA^DFt"c_Dg0,o
l?%1Y#!r142Z!/,"Ka%%EN4<iIYA,H;U$-=4H)Yn]Am1IN,g:ir8[b=Gb85GQ71NR]A?PL^o:(
LBo5AB\3&;;L24hCL)6mM(%k]A6geM2,8nbZ%TU2?"Uad4jmo+.f@]A1Nbpf(\]A`&j4<N-Vck=
?M\=7Erk>l5Y-t[op>XD0\?B,'(-B$0r6-`^t%?mo`/[V.E-oj3rdJdQg$QAE;Ws]AuJ7o7GN
q^(FKMoXT/!@7`5d<8YVDDRN"R)AThoePl3IP?a8.1:9iEjIsArH9ciE!Ut8$9TJ(9aSeIrM
qN7'B)F*$o8/!If$6[D5"AZa&K_8\j@]AT<4Y=lNZ;rC/6fhOE+XEaX]AInB?@iE!mJ&V#R>?"
u)\4Z2kr`h">(bW@>.rRZ"lp9;U!A4cUb4(JJ]AjJAVb-7eYCEE+4J5(01!7O$n@(D]A]AEL?nf
GjA<lGNm>q2Rn4"!Y`Z0B&APlW]Aqkq_B7BG$3[%r@?i"5bm0YAB67k7@(t,lAOtS81L^f!aa
H@7rqYhjH-=Gj2c`6`0D2%JsO.fjF<PH@DkaOAqbQSo-[_uNf[ZKZ-hsen'1H9).s-%Y05tK
<D$mRO1J,;l:KaYegCF&igD:[ki2fE9tRktEkap),mCKpgpIFpltp9/)AhIE.Do3@'aS;1&#
.FQEYBJIC]ANZ-Y3+K0nUq$6.W'RJa`Ig:ghmg@:c]ADA6[=tV*D]A6.`[]A![e<PULf\*J4(8r8
KN)@DFc-]Ar8O:cBQ>jhRltPkRT]AW2n$SgR*;a'f:6q3hhnsV:]A(,)a#@pC&lV"9dJSEtOYbf
08]AI9+>N3T5A&*_D2Xf@&_Be0VGnA-,-C#krA0e"b%9leh,\7rL0iqk,rmgR3/gm=/[.SQ.n
,BLkYoQtU44qV?0,&VqEMNg@.r8<Zd#L+tmQ5!G%2:ITSH6q*,&2$#3C2arp"q#Lo;_&&EI)
BbI6?ORfbBtN5f0eOEN(24EOqmX`I#L=\3B-I<-OV.,NV8Gk8NfmJ1PN@749teFjD7170I=T
'H?Z#@c$FZ:<B&ph[aimpBU`Ri%G!;PRU_imdU1:.01K,?@6j!0jc_84BE#?[F_o/:1H31#9
XWnY]A3qH&XT:e^C$=3bBWXdZOY%113S9KHsJl6kXgf>9kDo;,R]ABCKAJo#,GLV,N<6;-4b^D
ePo0L;%C`1L,E9C/mL'/"5OC;a!EB`r=uUU_cRZe!\nHOr5d)&X\D,I`3O#UN3=@u`gkUTio
D7sqDsoBE2ZIYkVH^6$*q`j;_)tlh%C+s\S.fs9B^!C9c=Z!f[f\,dIJ#+(Z?eCJ0UK#lC[^
"=/3k`,s0/ZDDJ`Ur&MmlfGck\;6/T=27/r-B>;,*OA0S4of&35VC)m4lE&f)g0'1Tul#)qa
M)Si)dTkGaI8GKuE3\=-\!9[4+N)=p@C[U[`Ubf]AD:$>$M$Oeb#j."-GF*Y#-)NVSk@,7_q.
LQR2;9:!A0XYO'?nrV$r251Y8;4`2]A]AHR6h#'u8g\c\jZnqI:@Ho&)p^':0ct[&53lsWe[KQ
tncNkAUH7L0X\5sUd!;-Y!OqrU*UgA,C$io=7Ts08-7ig(F9KC>pmK&I0l?$@l7Fip]AoP>Sb
]AeQ1hk\h;RW#L^f6&`YcPC`eRQVHC<gY>qQjmXf21MUqQT]ATe1I<<rZCrsFnsGTEf&+Gml=0
'e=RT=OA2lLnOo]A\FAen<X4&>/4Eh2*`XPp;IQuGS!iZqpX4,DtEribr6\I9[WC7UUPG3%+)
k>0@!QF#)TX^0dpr0MU@m(H$+iEo1WD$?[rN9]A7Fh5GAq8M4I@j0Q*SYQr<Z:Mp7a7MKd#([
WJjkj7)+7c)iB'*k`?\BEu>(*8XJRR\cih(W]AB9uMiQ&5f52fgbT+R+"k#7,-(9;f"p4\&;&
4_,:]A0L/c1)UueES-N`p)gEdaY`XBsj0dH@\Wa.]A8[c)QAc-D'\(kbr.nUokH@3!;$`(1*&Q
LWWM^TI(\dLl$EX]Ac6)#7&@V;k3Ii,BAqjNf@]A_B0#N5raJXH@VZ6CGE4MFTo_10XoE<bE%m
g2rEh$f<reGg(IKSN6\6YaAO;mCY&Xa:/n]Ap,OjZh$&#Dn2L^]A<"gQ&1s(hg)9"tV[Bbh(hE
ZCaTtCaiAd&'(OT$*!7qd2p`Hm(7@4Re^lAm/7u'j]ArZ#re2=a0CJO&QJ#omBVP>EY5[jSAa
bD?5Gg0]A34uh_gfGg\;RBt)LMriZKU3&`C?u[sb@^O>E?H5rb"5RVKqbOY+]A'E3-.Kr8SFS"
(4PTntBd\\4o.KQ9Z+/#O6Zga!\&BjY@ko6f44,\EqE!,)bR0f!=[>L/5R"H0&+R_o-4=,A@
qjVtAR060!mDd:KqMlgCEJQQm_C%Y,!g(c3Bcip+G>KC,a9kj!2d[0*3E]Ag_:P2#.L37F-P?
OHR845ApOmOT?T`pDZhmFFH\MJ_IR>Xo5ZsDQD(=Tk+sIXP]A$Hp+1j=^i^SfhCiDs$f43Rp_
2O<7)L0Y=UStqHJEJ(jV3Jot9.CO[r:bd#,>$GB8#3Mf^3"jXj]A*l'rCsF(b[G&1!;ATu@:Z
4PtiPAZQ/@YZ,HX&\=-)]A+sQe-Gu\m`:<XX,HC&^%V/KW<0U0:f9rlh88eQo`VR=!L49B`,t
+pgrP3.$*gGT,M%Qmmgg4=G>/M)k:>H%'<iON_m<q+5ZWc,j<2u^UEq)BF[+:!(!N7)$kM@\
2)VsQF^X4Ds%aaTKp]A2NI6RO1aP@V5*pK*b=$a-lEg5Xq33ID<-7<8l@d\Lh)@tIm@8.@L%f
Iq$pgl"4kdm8hpigh5>"qVI>q6\T$apu8ZX!2`apFPQNq4foSsh;3.t`WcA@c)*]A9bRrB`;<
BW2I$h(!%'Q9k?\LZF1U9/m/V%?]A.YC!0H-SQXnoq59m_pri?]AMQ('W/$T;h7nP5l</3i$d3
onr.bU@f8%_I:hjEiK5=)^FL)[i8b.W&6%a#Id_2\[t)UH"UK+bInZbqc)SK"2AY@@[ld\Wg
!kTG:$ZqkEVPDc]Ak\]A3u-@D%7&OYW,]A'R",V:(-,e!Xn(?-9kU3OghK$%V&E1R_uuZ=f9uN@
%\0m=^Mo)[qJ"e0[028O8+Kl%pV+g=-sJ)]Aam!SHq3-C<GEfCbtWiH?Y([sjQBFe=tP(L7/;
ZYDaI>blfq8]Ah=m=N*Io$J%KK]ADr*u/^:qB3cFHXglQtuPQ@-pIi1Aja+EJG0E%"tn"19@9O
P/-#>c7^OE=:PSA;1q9Z8['kkT]A+*qndGZ*EBcF<BGA's>Pr,XU:JjRV@;ZVOO3kY5^'SVH;
A-Z]Af#-(9gpuBd4XWp@AceMoq:tU[UGiY*g6;HHcQ/cm5q)3lIp)T>*'4d;5tapdZKP47>c[
R'iB9KUe<RC?NLL($(sg:;Pdm!8N.cF&dV%s;3;W?#snpQ"SI,VHd;NEEQ5]APk'rQ-f3[cGc
^]A@-\\qr2W@JJa$hSe;CT6C[(Xan:kdeXuI(fN$V4I?,L'64/oj%(LCMsa`\m`_9R5"8kb8e
14@/0NQC\]A>J6/>7NZEg$!HlZK=T-Bo0oAdft\sp^O<d.IVm;7mopGm&sY0pA"S%t8\J*9OH
Uqr)HjoZuro32Sd`T'u0%Z$*]AGX:4R>l]ALY>TnA.<J$^0)a/bdK-?^V8QgZApLqK"Ai,?4@%
moA>U1h(n_K2m]A&54AmRj*6Z56mfl`nU?h'4]AD/J]Aeu%R0CKNLsshC'pWJNhN$`SZ9SqrX;d
g/)th')SR<j+8_nig)+&&m^J'HCdAY7"*25ZEo@<mHQ$/),ip>>KLn3\)"hUuc;4nk?)C4?-
gksPU5%ti`Led0T/4`CO.l1arOSc;$A2$h,Ft%13>sP#F5:;q^?>XH/P7%nS/j;r:Lb#s<K1
E%k&n\:PY&AjK^VsonCZRZ2i8,]Ah(lt'jr7jG%:u$l[3Ik6hmt:MhF3S%W5@2kMm<"RGYp4h
N`h\mj_:37e`tO&K"+g%L-f/-f9Gf[f4r/ES305F=?@C!np72nL2mP<b:$/$n'?<sAFM>ROn
irCAb^6]AKOeW*<MKpmXLm:MF#aSkY`n78/EZ,A&Z3n.RpPFCCs83(JQJIei,`=VXe?2H1e%\
H-J8.6*KS5a"Mn(04MqOJ:2S]A>.);e$F[#:F6'1t:'gL2M]A`;/MU;jT/gEUh)6Z;;Lg\9EAZ
-o;Z-Z/R*gQjmO(2chp_%L=!(K]AoXm)(nqaK58aKsHtB^.i3MLrK+'U-:Mi@]ASNd@M?9o4g9
YgcAu>=`U>RtZE/2ILH%:dmF^=f:Bdps<2\GqD^bZ6YP)%L$j*?46tIG.^))t]A._Lg4i[SFq
qf1AiQd:\;>U5WPlG%e;\.[+RC.iE\Z\kP#F,`m$*$5*,7ZaB8KJkUAG#TjG9>&+I$=3]AQ=#
a(e3mbJX.>ZkPJ:$61l5kqI62`t1+VB)3,CKP/2@=MtN87hj:XU"mWMlk#kMpE3@HS7IO-PQ
D$$okEG&9#CeTpqAmUCD1*V`2Xf,Y?%YZX`\"]Ake"W.$EYhB%fT%9rE0<as`'KA5ccWiN\u/
.H?0gG@,Rhp#-E=(POs3.I#`5#b=>DEH#hj;6O5">Dou(Vb!^jR0;&Zf1Xdc:L=Vi%]A!&@kb
0S(c?Wug&_eC(Dp6J"!.-JEAogu0WiBoDW5`hb!pr48$iOJ^Vd8n8;KHUgs62tEDuBdX!H7b
Ni)[;Jq<FJ'=*e'Fs;K$ine/ss&%8^W,$.Sgs4RIBU"?VS,I@c,`Em:A$,,+V(>Zu3gL`<Fd
@>\TG26W#I7Z:44i#ehOK$tf?$[p38-BUYfC^'X\m;G)j"*e/H$#a(K@Zn)D0t=j@;l8"GOb
GAD;&J"cX=+L8O<W#ta)j,OMV<Ti8%a3E@5R<_gBZ?FoH&G3tV&MM;OhBpb<E'o@>><?&di%
MCT/08^%]AX*c-1'0f_D-P-S\M)IJX0^^902*S:>af]A1%:"f3Kg"JjbYZ\=mAS4^??fo>PMP&
DCo7C@LRLaS]AU*@%J?efBTBV':.Q'U(l*2!#J&2V$G1E(P?J=%6Cc=r&>PYpV/_CL,D'7qQY
7I<]AKj3f/&;Pq_]A"M55]A@'`O0g3tJ"3+G<-bA1lgQ\8&%(7ZHENK(h18QSaYX%HdqKqCjRg-
^s+GH0LQ9XhjJ*Voh-[dk.>UMnH3GD6!,iGp3L_!TQ&@5fjV"`^WK^'Ua/CS$lQ1'LVQc^um
C4?AdF09[*`hDkg=:Ef_$'.f<O;).&PEB&f,huil's.]AUS`4X<u.$'aU75'<tZ^?aU]Ar.BQW
ZH<ZMrW*1HW3?=55aZ-?h0$+r5-K)Ja`@!FQG'mc8MY^SkOAACJ^sh8#PU2(k/,Fmr'l+*&t
m3%:4CiHt:0Fs*\J#jNuMBhiU`6,-[-WX(rn;eu0DXJk?h#RpjA]AT+VbBZ%34[l9k==ft"F\
f:O6TJeg_#>sg8#Z$epP4FbTpfP"Rb0lm0TXK+VEc]A,.,ri\Fsno?5$J,.*?pU]A.,<7so1]Aa
,K7*;AQUPRko._'be)X-+OCj1o<n+h'ZU*["UQrr+2(O=)[AG1%#,:)^3cq#=-B,e?:K+.tY
U3YHe$>n\Z4/nqmp:Q=XnU<W,]AM,jat]AQJ79'.^/K?cRQ9^U(R.?Fd.`]APh3?,K?VXV$3l_G
SF8*_bj'K79`aVe@TP6,jq$*?QDE!f6(9Qq/d/@QrL;i53-Ap,:3qR%6_N7icm+qd]Ad8p4AF
L<!)ml(V+>4uaS>gMn*4joK2oIX%<pqsTUmLR+J%\:+$3A$fpuD?&sR#Y5F:q]ASU,IC$=OuJ
&s@5`q3K_a?=Ef_g8q<ceQng*hO^;d=Td\bJb$3t]A?;UI[RS1jZ!)qRk1\$;#C<KaLj5"=+K
3sRa0:q-3/8<4+krr9*8CjB'rWI@XdiMh<rZambCXl\6H4H`3f1)OSatYuO^aU9X^TdqVqsq
U(aLXGS+D0crS-M6KY*J?2$*SY,5^,.<U%na"4B29BL_fPWK/+XY9Uap2a3.j_ApL@Rl2^uf
RUJZX-TE8"Hg_^H5:Xp\)(8#rT6dkq&%OdFi7N:_TrGFolh2W1m6TPEsDs-))r#CoplB>(Ak
H2p5)S$Lgub*frToNCE-(EZs8aQbs-8crN8urQOt.BV,R]A-0e,+]AhQZHZ$kuj,l[FRf+^`QK
HFMK4df()9hJP6m;@<30_3o.s^k'R1A=d_aQ.kK6*daska*/;8ee79cBaQj$ZCE)HF-Dg6L'
R(,pV.fg3mABL'F3X^M_,idb9NGS$DY,-8V:-tcb&f'A",#:O#:5Xiu*H(_H]AXn\)51G1m^;
k5P0!B'Z?9>m,0^A@/cr^-W]A_l3ED61>TBUa1e3slN\PiE'u_B(Zf'\,OKB4S]A9.9H35A=77
Uf<U*/KF;+=$AXi9^XCk(hE<Vr(7_<=?2D7t5t_jaBFgeoe8&-)jGUBpUbJnS;L($oV`ne=*
a30DCOZZuNh.gZXC`,R(u"GWF^u%DF(g>5!QCh39u5nX1P-9cQT'+7mL\;#K<cJ!!=YraN52
7"ch\TQ[]AoJ1n>uZ;n=7/=.^OP>k0[4*-F5^"pTO6]A:I&Q`+QJRdg'UZE?R?'mlgkVN5q=n-
2oGoU1M:\Rc,omM9O359"S[%fURT\E@%LICHT@BXS,.o;bK2j*Ru]A*b>e+N68LWUJhWJ`8>.
qJRdciN4q\6nB=\u_sD3P'>3nlAh6=R&;Z.=RDmZ]AVKUg!-#<D=fe\#5Z72cR`%BgO?$,M\X
ht;FoP9Nh[95HdkMtk2=;j>(ZnKaWfK8*&dUgL%2)R3W\MF_F,[5\Q'<3D?U5`5RFU$[PI`6
FT!j_UVN6&uRc($f9k9(?h@o[-Dc4`VbiZ,4aRVF+Q,j/>#>"/#dh2V27=B<1XFH+ISG&71e
Gk<]A3&gu>XfGIT8<";niEe2`kGVl8="c#(*fCJHq!cDg"k^#p\Dr#\;7'[+N'^0*D?rnD[lg
fTWP_Uo%KjD^>f82cDBcuTiJ[EI[:$9C2`CS3['c%5^UKRPUW@EJlgeHX&!qJS5Y,tLMD7da
4/T'2gXE/7*[_@Ju^J9nX`'"l!@1![gNkW9-9G!_1He,&GKb"\@Yo@moSk_D9%)W-Sm5WCB;
)&]A1RR[4u'&qVKi&%[WM^+9LY7k#f8X>2M\)ale-#lmPji_J>/UOKJG%Z)F#fR^>]Acu%n1P%
X.6kHu\,oQMZItRA7&p,U/AKkL3Wo!>2)Bocqdg75[5q*5%p1:sBYHqFupA#t"0hc4I\&AMi
SQ74,)LAE'I?A,eKXi]AN6JkE4JZhCpie%.C.P+_<4;r*NTIA:a.bW6gBh<$8XMWq&P0E_D!=
Qp'm$\pban>+e*HG=n\+l9"(n98BG.9b\-LgIRI%PK:s4-'`:UXBDJbo+Pe3PRkNZW/O^kA(
T!gi3L#:O^JKA4G>!U.tXpaW[ueC]A=@L(qXN?M9>jfJ8?hf`cHZa^>8l:YsNl>%#@:VUCCE<
!YC^G+=fYn$#PQVlNR(-"AK0p/O]A<8uM*WV1VB(YWgD0aF]A)r$OlqcK+pS[P'Vk=K8.h1S+:
'=UilI.`Z)mZ)Pc!40_'9_YUiL+fJ1mVl22j3aBt7`:A<;sG!"Fc*1YDN<sXTYgBWM=(Zfh3
F&pbX`0"C/g;q\nVl-Aj@k[h+ps@;eaqpYdq2Y"pJ?q$&Z1)ScCFMk#b.dd2O/i',k'c0Ol'
&ADqs;]AQrIf1PmI1l-8SA!g5YZ2"kJ3Km@6RT9lf6dbR*>j4;mH!JZctGej;%%VK_<h:c"LG
5UZu.OW4(g]Af*IsZkEP8<Q_IMbiX%r2>G"7'QLX8m$o_PtJ$on+I^#SIW4(l7jq;"bj-N)!@
:)"]AABXg`\SYZl=*h(V(8obrKjP]ABBqS:S@"=XX?P)8Bc:aFOV$tpsZNgoE-!kEP_b4<P6hl
c5>GK3LYF,P;\aQp>6@YX\.(;[/c=;BZkE#9f]A^ALX@]Aj=`4IrEnYL(X"M6X/m__Pgr9YZbc
KZ[\^%Tkr,&J7d"0\/mFmuoU+K#Douf]A&SO@Z`$^HWh"C"SGFRCXV**eI*o$X'%f>a8.4BE\
HpY<H0a[h"7BuUF*lrVu348+O28-Yn:?35h/rtEUgL4J).G1W%!DnaLR2Mp(ls70BKnUb.rX
oY"=,egLaugL&]AF*DsPQb/lOLrqGPa']AF$J)ZZ7&/Lb:Ka$;6]AQfR/tcY(TRqU*q:Oda<,Xh
\"!#Aa,=k35@;=&/6qNj=b.D0]A[9^L&-,7Q(4;tRf>ZYDlU1k!r"lk1c5HEf\4"9k8F(S`m%
i,%^\7'):$]A`*n8@_oOjZ71;FM)VnVHV0#Tth-6r'#nO#8d?1n!YP:QcCCJt(kihag0Ep1j^
-OgM5cd(oXW"X747pIZ&3_!UHcSJG<Gsp,Em!6%/OVpB'PDCN8V"]A/Hq7sRddGH)npE=>Srj
t*JE%@r,\PB-XNc[oXnt)H\+!YEso@_%I7F'5G9rcZV^?`r^:3<-b,@CJ]A,^o0P;44tOp<`W
9*-V)>Cm[jl,H-3C>i=gba3)FqeEDaaUJ\V(ld[Mq[#`4pW4u)kGs<iqC9_/:8Dd.i[gOJt`
J:@9<^'.N7@>\Im0(/[cFbB<a68%.`s*\0'WL^ec8q&rYO9".%[&#^]APp0j/oUS3eU>((fCG
CuX5qsa&T:(]AR'4MW6oG?4l8[`Q"Sd)e<iPo2V0A^bY9E0E:FFkug]At:L*S%`Ij9)nJTB_r@
<i,aQ!Iatk8J&OZ8"@eC:iIGoQQS8A['To*(TkuC"fj/UdLE-(OGc2lm%arh"B2W'6K%h53u
8KP2/u".N8cQ+rb.IB>OVZ'\NK\6"-r/803UC!@ep]A7a$\-S`l(!ZTW[=gUKr]A^$ltD)0oK;
;1saR0NbWmh%_K\bSc)77+oE5Pk_?+*X9DXh#B>_I?SU(940mr&\\]Ag/Z/)*@3h8-q^*"5*c
N1='#CT?9f9eAuibNp']APY\]APJ$6nY$Jg@f_$Kf^hK;7Lej2Q4e&72g%pG[S%rt_QVpg3BPt
h6_db$(]AJ'L$)bS'LFM5/(e^aC+-`s#P]A8^[67YZ!DMnGM:8K@Qi`gChrQRDd7!,cR596N_e
'r0\%0meWoE0sd^AWnM2q:8G^.K6/F/4X?L*$s*;[C,nJ<o?CEg%&k21WD.\<I5O^&r(?67F
F>HrK>I5*)G;O.qQ\00_q3Gn\:iM65^_@cIcB*8P#*jjo*92:QN_*'gk*drCU\lVV74sj#<)
e4WX6B;fu!$\4lfZ2]AJls!?ASO;`Auk&P,m>Z)Q:?OQJh$g/\*2(_6g(.3%V9/NZB\XgFY4(
@s$3o7S%6alQfG*'d37=VDujq`1qrgR"Uq)k3gWDQp5:G,/dXgapYW.EPdUm>-.fQ^X:f^33
TD+Y/$CV8qre9]A=QH^!BoHF0o\Q:]AFa<4B4=T>fPXlRE3D!#ee00OF$SP1<V"5XF-sEVP6l\
6(IZ\FXk:fdV\aRU5u)9M(]A-R-=fqT;V;QZ\kNK?SVMUj)FmDY]A()T]AV^$gf72b16G3\q+oU
:G_p$Lq_"o2Ku%hDu[,e7=U1<5_Gbm5L1Mri%u[W!7Z6;e]Ao!SmD12F"@IhBSRsG:^Zm-jXu
Fk_m*?@`V#S41%d!!EC,I1B%u%g&L`]A"aLERp&X-E`-PdLbP8%-18O*(5;OG=3lIW@-/`e=%
%)oHbe0SJfSG$_>2=F9rE<Z*0TW78*)kUoa!!$Y(mJ5l;0YiKb8pYAQ,iD2]A83I)92#c-&Uf
&+6<=7B\'C7pT"R:qP'=u>r2(4.iClUDo6DK#94%/KJ1d%j4b/!EMSU,gY]Aaj);T"SRrp:A/
j/P;hP(#>'J6Uafd,=(Kr=/8Df)>8tZ[%D,/VVrX\[iBR`1%ik,]AYJSnEX!Ga\@Nt/Bqo;kT
6eS*9Wl$f$/aa:M;7<>b_MkV$POE*Y3\iiH"lWG4[7;R"onm-+>h9ne'V12.@.o$NZ<P1UM>
h?(C4jCoiZ9mZq#n5("pENbHZK8[G[]AGTqAsOV0Uf8YI[5<+Unj5l\?^cgbDHN$*4+JtD;nE
soI@5N9aq:1,FNroh"k=h-bm80ng1&7oOcn%:(mrFFcToE+(SjfaU`3"]AT@GRcmYoQdE]A<IK
Mta/AsQ3ESbYU8FAH,J<$e<P:7Y+'*+(ps14eI`]ABlrocYu:^F#RjR,G1_L>14QE^Nh)>UHc
18<^?+j[Kb1Pp?[n=T5m3$nu_..R/sllI&J$PUI#iLfcGC_3:5j;"fJ4S_b@(5-S`ar]A0g>$
t]Ak>gqQQ)g6:E*4X'=-RYfqXnqLS3:$2X62W7l>$(Z<[,Ji-9"lg1UZE7;^?;cVs"PWDnHoC
EX.Lj(DV:q<X.jcqGF%W5Q_t`MHS!e0pj?R`?e.El9E3dGg.\>UI1s8?6tAR16Qt(Gcp0*#9
F#[Hj2p0UNW`q0T5W%?gjSFG#oL8Detf@ASTr,%ILLKa+Kq2763b5Gd2s`ad]A%e*LNn%BF]Ad
"AYa<>Y/DtRh?1EC+GY?lLCp4Yu$>peH;lWAOIW[>6IWZFu>APutA0U*@4B,:;D*N?eTRq"u
I^[:&.*tm)XSd!)#a=ap;F8Z/i!0#*Mai\iTfdTI-OE0CIg5mX.&P]Aojdp`#f?8LjRO3d8s7
uK'H\8:2'Y1$Rn`@tZk8iAg<Z\Z`V$XA"_u+$&&PNeBOB*2Y,_Y*R0t4L4`B)iP06()NM'&b
jLYa``i*BOJ);98sV)tUu,sL0q;B?R_,u@*lc8/B*3X#2neK(,AMLR-3W(#C>?.Fbc\b^Up*
k,;m4DS_'6RHmT4mC#pCQ8JPnL=]AP't\COCf4eLe!f+gr`0AoBP]AZadM0$.2$3GRF=K+/UP5
!uVcL[d4LRabG?7ibZ54RIcPj*c<Qp:@:VmNpZlA`*f/?iFVbNG(K1_X!2t[b*YMRMi;"kb/
SE8R'(4jUac3.;NI9*)La"7jXdEdo@r.;_'^(Iis\f?+)&"9]AbO9QIQ^k,S#hd#[sipT20(M
J_Qmt$BW(Z%CB/#d27/hhfe?'[,YaC_9]A]A>I![nj_K$J=j[BB>XSu'_E2IfHDB',X.2(Mfr,
%S%&6_Ger7Hd(MX1qJYLI0;o_t$e_T_N-^opnN/-/[!&R2%uie-HV]AL.<R<f#C2Y*Y@c($YI
rOTh,5*\HJL'-En(JJ2):c[g\ZT!j5mD:+!;\@/$Xa:Ms#-5/jg:3QVkCQ<.WY*gr>D]Ai$qW
4F4&$O0VVM6_+[?s5VsIY\^8M^KSQ)3PQan<<:D_,rO$Vdf`[%88?L9f/Xc7)T/XLk#Nd*'V
]A@qO0ARsQ&glaW7<9-HKMLana2W=%Kn]Aj1+l+#?YoGUf78C"b*^[0Y>9T9'mY^T?mCDSS$H8
=SFe:Wg$PO?=Fif3KVb;#\fhlSKaW^GGFGV!i7-'P)KC>@2YDr+]A\5RO_D05K.L:=_DCOX)Y
DG2(Z"83BK`b.Z:ko"56YrV+lt(KPnm!EEC\.l0m/R-MHH2*XoAQ96S-"MIn_6gV)Alm/1ro
?,]A=^?8ai>aGaZWdH%/a4/bbj+b9YDR?g]AGAL0^a7E=nj2<r:PooBmLT;3_k%%k;XGq`KhXK
8;P4kI0-H1<[qCLfDCWlujb@8+#qi.U]A-cN=V?Tn\I=[M1u(.k]A)2aH919fHJ3#Bl#-A<<a&
iA#P_V!du!)WgD`]ATtk3F585ekt<WmC'HOM.Wa&9AiDgt@V"":'Q>!ugJC)kXH.$!K!52`/u
U@kWWGm1rm2G'^u5u]AZ[G%m/KA\U,A^ef:lJoqZHa@rX)e18od<dq4lS'V)B\kt(s%Z7m!?k
s6B`]A:0pe]A@d0_SRhR4SO+.I*$h'K%+\e7Cg,+::Qgu_>t-mV.\;V7#m^[,`?PNaRQN6898*
-ITk^''G6UfQn_PN$ji733a1AJ(H*gh+Y&-7\lfb?u$^g[n1rZ$Z(1c?eCg%(X">ULXT-HD1
=oCaS`G[/XGE.@Sm%lu[0\YNAV?Z)Qgb<m5-6If<^0L9n)l`gRq)i<WBO.emCO#grH5S/jH*
Z$FQQIZF1H%]AbU)[NfInOheO-(/A+s8.Jq'*GG(N9s[5W"p&9$IBT1fi:fp%]AkZ?*bMS51,^
9K1RBn;c?Ke.UPhU!-2`n?[o,n7,VD=:KY%n4]ANdjgA\st7JF3Xt.-@Z%_eb(L25>HFIe3Vo
b,N^1$onJ3qcWY%rZHN[r]A`$,EcXe-u0FaNH0RohAM9(nq;IfF\g"JisL>'6(Ti!AMdbR1'/
T7<N#80N46<cL!mPHs9kDq`90Imf%nCt^fX3Lt%->Y-,E#V2:dLUF8RCq;-(Ga'8UlT7?S/$
t7?>--hmB>*dIOM\;a+SQ&)(,LQiSJ[eSg1N<f3JusF;^"CAOdG+[j2KICTIRs1c@O_R\;16
n-S\%O[K"g="F4Cq@r!QkB$dEGS!bd9fC"4r7Z.\e4hDTM!s,Wct<SjmYEMFHAEUgq1P^&r"
X8m]A5,gn-bd!QYufp(X4F"*;rah<H:?T]Acnc$Yb`-`/Z67ljKNiZW/=FT^d1GXaj2cQW#Z[,
FMeHbgI/ANZ@rt15Te>)>\ek8*^C=^Kr3PkI<=(:?o0Z1!;J-QurU=<R%`apP-)7d;6SPSBX
C9$.q?gtB"@=Ei#.A@$=&&@Kf;+LcN8sR@H_Ptd%S;pl]ADOs6^\]A]AI\sg6a.AuL[pAL-ZkKb
TrHE0krRW,2.J@55]AWYOaNNuf2nAG2h;O,"QRee[L?@m`Ve9h\[l#E@ZGqeQ5%$U$rhNE9&K
=1!+cj$#7L0C*Z:bp_<aQ%;NuBG`:oE)+?-*4l#FcqCT9Mtb5j6j0$(s"mNucYO>,N"tLt`G
'9Q[H3d2.Co=T=Hq9TeWRf#8:7iIq0Fuh<O(b`mh8L&e8N1g]ATQ`KHL;AZYLh="4d(H8KOIf
_/CgD38njfpk]Af;L(9`/2c$5H`ULr]A5f3HsKrT8)7a8.I@-M`aDmX?J9-W:l8a`FP'5sa66\
E*e>IL^U@i=;[A.pu"O*JEr_QX68a.ilkdj\#s-rdP8=7_P-24"gR<p2Y+(nbt)KR2!0OY?=
HP`t^HX!'nUq=OTsc'PKZN+cYm:&[X^/R2\Oe3QWFt+?!Oi\B^.opiTVAdb0-Rdj3.c>HY%K
`a0:)3$MRe7W$efk^Kc?DEmb[?;NDn2,Qd1TJ#:kafc_Z,lue.P7XC?Y!G>Z?nT$^M0luj:R
E@P0-QuoV'@[9O7pPV$f<uN/eB:!?+j</^^-X76/E!aJYulI$,(EM%G$^g&f($`6Gl]Ae;G'=
r2'n'nD/O4%+]AU#,r3Wk[]ATM#=2(Go:YTu;>cPG%j9![!ip]A;t*S*pVECh5gV[OBHoK%1j"@
ZL"\frP=!2HC;cmagZAkeq!F%!CY,o/bG\9OD4qc:/[*#[Trm.7V4=n>H>-FI55QX4!m`="^
@[e.)j.96/,P=]AiVfSK#FhDPWoH[Yrlf!6C%,j>LF0"(8G#Lca`TAX)9:F`9d"[@*7Lf&?!>
9^6AlS!?gaoNJ_;!H<(iq69Gt@!5:M3bU"VhjBXc4AA`,e>iWeomh71DAJlq>+5"Dia?[j*7
^sb)[qb)8#e&BP#p`-hf>9d.XF0'\Y$'m6ILm5)#+>K8l42h#_^g?YWlt-$K.fH]AGq!:NP"@
1i2!0.#KPquNpb_K,=7sn\CRdq=jZ\70!s3L6^[iC3<?A_?ZYT/`c6j0j4/9.@>Hgto8M#Q_
8nT/04Ip#63<<IVDX4kmU'29'bkM5UQ<puh?D/%8j>/I=<f>FQK2IAL6-KjpApRKU\A-pb"<
/%P]A?XT=ihofA#[bb\(+]ANE$NeYBs?OY((gQh7QEQ/+SIW"&9=_.J(WS;o>%IJ!-a[X8N_$D
HY7fcP\#o!UsQ&.6`3rIqnV,j)7*kLm=oK&SO2#a4qcM1ZGFr`dp`jPKqMd+gc-.S@DW%<]Ar
`)r2jC^jH=^oeE>JI@I#9k,@%7jdIHuc:W+V6!qHr5H1[5p:]A;ikY:6/f"R?SqaFg(eW)h4V
ceK;'.]A^+R'3*lok>]A\_01+.,[nSGDp?mJf'CE?j,W:Ac\+A-/@<l_8tJ(W(fXI/u^\@IRPS
I.g/W\jq=CIY7MLu3odBYQf(Vuq^(D['jEh_T^FC:IifC<L:;N+KMkNhAu4/NJmMDoeDFp?J
,&jA<+h(P*]A%h^I:Y-tne[Anh,fV)Pb;Q*AE`H::oYQAD"r9n']A!dbq@Fpr1R\jj_Ms3/!IP
$<Vt;'s.da#eMiuRq,cp2/DXqRhhjkd)0j9HD]Aig<!nc`b^1-fKYnL%!^,tKQ'c:*g\+fEX0
MXXVJe>@(6LPioGf,YGBWUkCIg*%?A1OOQiGO`<:@!e:I6^cs7.s\)(mWIEQtop\&<R0>K?p
k$l^oq\a"7K-6<nb!j:@_L!B<8@M0`VbRK$T4nTO=F_M&jNP4NHau"0PJ'Gp8AUbrsqQY6Rm
rRF`)_m8X>QZEbFl:H)1"&WS,ZriBBi74fnpQR6#4>)Nqj&'fT(=u>(aNp!K_&uBi1OJEBgI
Z?M0hM^Jm'Q;ekGd=@^:o,ZD!T(L5u*J-E4X.H9(9B@hYNZI?S`r+YiJ3W)pY2ZM@XV[.>2G
X'tHDN9@\j`3i6"46@,t$2ig:UVXE_@cSD#fpiW_4<sd-Fm0<0l,o,RP>$Qk@FTc>9a/a98J
nXRLXeWf$CRlCS&X4PN\<Z+?O.+0QZ*"`'Y@UN]A@!U&(30+,K#b2n_t(pWa#,KdbK[V9a)>U
Ba`L%*S(^,\A=69&Lf86i.r;2q"X4e?AO[dH,J!2l]A4[m1SV[.]A-`B8%_Sjb2HJ0Rp8KZM*+
R#?!^G1HL(js5?kOo-b.5NPjku_)Ah))%:gM7$'mu\&+X[aQ@rh?a0n9@m);I,AegY">\mnX
;I-/.(JV.DIp._p=Ei-$hZ*o^,J&]AM!NQX),KX/bYrRPi$,+g8oTmeCY?\Gi3!'Od6WHrPrO
H!`1qOt]AM^$&M=NErJE3&pGfH)Ok'6Bh?<aQFZP_47qOBGU:"'['YF>gFeTR1BXsHYkC[bPA
XlGWss%-@:_r:)h<91ig1=X7H8NcjAThpKG&M>VYIn0,_JR>V:)t<J/\K*#Erfb6Yc=;s6"o
C"gb8T7fTfFjKRjF)4g*%3dTq9G*b'r3RiV)?4YN*j\&pSUWk%EKbb+W72H_Lm7ZV(D4XWlb
5`uE:gUQ]AXi.67Q_GG:goMZm=W'HE%q_'dnl#OSepFO"c-,E6oUhb8h@6*DYIAi\Q&<Q'%T3
-7P*1qe8f,Z7hp]AWg5p$I(Br%P8?5EX[OJ21J>sDpQOY3;Y1G/b5;HF^uLN6Af)!E:OMFL`2
r8f6)J)@%+O1J!&_6Ge;RJI#Z$TaV2FIXC%eCZpX*uY8mQc\fhK-VuIa/`Uq/HG_+94,tCqH
s,>Vp9lT?:r>akm<=">bPK,W-3RO@pRo>&`J#ThSI8*:I51-VOZ[,dYXU>'@kCi,t>uqq#o/
aS5jW\).=3#6dZQ=0VCK&d0*/jjiXa&`ol*JI;j&@Vh=,s$"=n^O`&Y@96A0ALg@XWPi8/(Q
Q>=(Wf_nEPlVNu,1^3Cr+pYW80N+r9`3#kccoFNb=n\JK;NQ'jEZ+iGWf>_;tW?,d_2-Z4dd
u$P$nX"s0e&S7!u(mejm.,6:`B58rIQ`fqs=5bl>RojHcQ8c%#WO>mZqR^EOCBPZZ##XS1]A?
2W2D9;)O<T_kc3>rC<;bR/GE_gg0qK,'+W,:*!&V!`f9E&um:@ULhZ:QlsM&s+)n^_pf!!]As
OiP&Tk6&1d!\)=F]A;Dg'-2h74U`&!K6!o.GQ$kcdgQ6=.kE>Di*Y]AX,r%B]AL[Ta9^;9l,a8P
9^a^a^/i<>?5?n%=]Aut8@6KYhP<at%/rCVAR?!J.-44t#W`dMcsQ$;"`@.b,(,9l&^TDqCV*
!ZkBZ3INQ,2>s+5J">lC6ko)6iIl~
]]></IM>
<ElementCaseMobileAttrProvider horizontal="1" vertical="1" zoom="true" refresh="false" isUseHTML="false" isMobileCanvasSize="false" appearRefresh="false" allowFullScreen="false"/>
</InnerWidget>
<BoundsAttr x="480" y="0" width="480" height="540"/>
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
<![CDATA[新建標題]]></O>
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
<C c="0" r="0" cs="6" s="0">
<O>
<![CDATA[樓層信息]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="0" r="1" s="1">
<O>
<![CDATA[樓層建築面積]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="1" r="1" cs="2" s="2">
<O>
<![CDATA[1802㎡]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="3" r="1" s="1">
<O>
<![CDATA[樓層櫃檯面積]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="4" r="1" cs="2" s="3">
<O>
<![CDATA[1054㎡]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="0" r="2" s="1">
<O>
<![CDATA[樓層經營面積]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="1" r="2" cs="2" s="4">
<O>
<![CDATA[1594㎡]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="3" r="2" s="1">
<O>
<![CDATA[樓層品牌總數]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="4" r="2" cs="2" s="5">
<O t="I">
<![CDATA[16]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="0" r="4" cs="6" s="0">
<O>
<![CDATA[樓層服裝所屬業種情況]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="0" r="5" s="1">
<O>
<![CDATA[編碼]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="1" r="5" s="1">
<O>
<![CDATA[名稱]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="2" r="5" cs="3" s="1">
<O>
<![CDATA[品牌]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="5" r="5" s="1">
<O>
<![CDATA[面積]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="0" r="6" s="1">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="業種編號"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand dir="0"/>
</C>
<C c="1" r="6" s="6">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="所屬業種"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand dir="0"/>
</C>
<C c="2" r="6" cs="3" s="6">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="品牌名稱"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="5" r="6" s="6">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="櫃位面積"/>
<Condition class="com.fr.data.condition.ListCondition"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.SummaryGrouper">
<FN>
<![CDATA[com.fr.data.util.function.SumFunction]]></FN>
</RG>
<Result>
<![CDATA[$$$+"㎡"]]></Result>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="0" r="8" cs="6" s="0">
<O>
<![CDATA[各經營方式查看]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="0" r="9" s="1">
<O>
<![CDATA[經銷]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="1" r="9" cs="5" s="7">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="品牌名稱"/>
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[0]]></CNUMBER>
<CNAME>
<![CDATA[經營方式]]></CNAME>
<Compare op="0">
<O>
<![CDATA[經銷]]></O>
</Compare>
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
<![CDATA[len($$$) = 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.ValueHighlightAction">
<O>
<![CDATA[--]]></O>
</HighlightAction>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="0" r="10" s="1">
<O>
<![CDATA[聯銷]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="1" r="10" cs="5" s="7">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="品牌名稱"/>
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[0]]></CNUMBER>
<CNAME>
<![CDATA[經營方式]]></CNAME>
<Compare op="0">
<O>
<![CDATA[聯銷]]></O>
</Compare>
</Condition>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Result>
<![CDATA[$$$]]></Result>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="0" r="11" s="1">
<O>
<![CDATA[代銷]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="1" r="11" cs="5" s="7">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="品牌名稱"/>
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[0]]></CNUMBER>
<CNAME>
<![CDATA[經營方式]]></CNAME>
<Compare op="0">
<O>
<![CDATA[代銷]]></O>
</Compare>
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
<![CDATA[len($$$) = 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.ValueHighlightAction">
<O>
<![CDATA[--]]></O>
</HighlightAction>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="0" r="12" s="1">
<O>
<![CDATA[代售]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="1" r="12" cs="5" s="7">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="品牌名稱"/>
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[0]]></CNUMBER>
<CNAME>
<![CDATA[經營方式]]></CNAME>
<Compare op="0">
<O>
<![CDATA[代售]]></O>
</Compare>
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
<![CDATA[len($$$) = 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.ValueHighlightAction">
<O>
<![CDATA[--]]></O>
</HighlightAction>
</Highlight>
</HighlightList>
<Expand/>
</C>
<C c="0" r="13" s="1">
<O>
<![CDATA[租賃]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="1" r="13" cs="5" s="7">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="品牌名稱"/>
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[0]]></CNUMBER>
<CNAME>
<![CDATA[經營方式]]></CNAME>
<Compare op="0">
<O>
<![CDATA[租賃]]></O>
</Compare>
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
<![CDATA[len($$$) = 0]]></Formula>
</Condition>
<HighlightAction class="com.fr.report.cell.cellattr.highlight.ValueHighlightAction">
<O>
<![CDATA[--]]></O>
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
<Style imageLayout="1">
<FRFont name="Microsoft YaHei" style="0" size="96" foreground="-16749643"/>
<Background name="ColorBackground" color="-2953990"/>
<Border>
<Top color="-1446671"/>
<Bottom style="1" color="-1446671"/>
<Left color="-1446671"/>
<Right color="-1446671"/>
</Border>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="Microsoft YaHei" style="0" size="72" foreground="-13421773"/>
<Background name="ColorBackground" color="-854279"/>
<Border>
<Top style="1" color="-1446671"/>
<Bottom style="1" color="-1446671"/>
<Left style="1" color="-1446671"/>
</Border>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="Microsoft YaHei" style="0" size="72" foreground="-13421773"/>
<Background name="NullBackground"/>
<Border>
<Top style="1" color="-1446671"/>
</Border>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="Microsoft YaHei" style="0" size="72" foreground="-13421773"/>
<Background name="NullBackground"/>
<Border>
<Top style="1" color="-1446671"/>
<Right style="1" color="-1446671"/>
</Border>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="Microsoft YaHei" style="0" size="72" foreground="-13421773"/>
<Background name="NullBackground"/>
<Border>
<Top style="1" color="-1446671"/>
<Bottom style="1" color="-1446671"/>
</Border>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="Microsoft YaHei" style="0" size="72" foreground="-13421773"/>
<Background name="NullBackground"/>
<Border>
<Top style="1" color="-1446671"/>
<Bottom style="1" color="-1446671"/>
<Right style="1" color="-1446671"/>
</Border>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="Microsoft YaHei" style="0" size="72" foreground="-13421773"/>
<Background name="NullBackground"/>
<Border>
<Top style="1" color="-1446671"/>
<Bottom style="1" color="-1446671"/>
<Left style="1" color="-1446671"/>
</Border>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="Microsoft YaHei" style="0" size="72" foreground="-13421773"/>
<Background name="NullBackground"/>
<Border>
<Bottom style="1" color="-1446671"/>
<Right style="1" color="-1446671"/>
</Border>
</Style>
</StyleList>
<heightRestrict heightrestrict="false"/>
<heightPercent heightpercent="0.75"/>
<IM>
<![CDATA[m<a1^P1eQ51[Sql<msUmPa,!%lr6m'e1"+')Gph\%?I9]A2O.C53dJd\`Ec1bQB7,?R`YaOA-
+he8PPb9@NNTY),F@kU*,UH4<X2X=RV1c?LQ*%I+NRJhokjd+.d+.pUX/8hgM[3p953XXbO:
(Z=V51*]AsFD=gi-,EnRaZqZ",>\<>G>(T1if*$u04p:Hm=&U.<QmI8Bo*P>/ss"`8@j!@FgI
+Aki_"L6Qr4VX$2E2[nEV]AF7#(]A0-%Y-#W&V!G[hZJ3Gi@iiA=naXtGA"ocX'U3Ro]A&\Q8oO
!NZrb9>a$3YHSVo_M9YJ0AMeQt*,XN6pm,I]A\s,!=ca/%4R2.8.bpC+p4M1iq8TX/RW%RBPF
)a$:brd;qE9HctHf.-f*#7Z.UBh?dO@onp/<@@'`K::]AC5>Zr8@k(Ylb2*9F.0s8N!TItCKL
?ue;$<XffX>ql)GU(ZpJP;QNlp27^KER$gfc+XUU\-N1+u!.C%Ge&Rh3UEC.kjhKPe(tJaRm
Qb]AqZP6B<Xn`1Y^4pk!+*T;GlrX.C,X_'HtPba?iRJH9`2P\&?X+XX+$dM]AkM\j<Qt]Ab59b6
,cEG0PNrM3Xso'okdt3-W'O&5RS7HN)t),+_Idi#76$Cn/GUoe,/N+1]AI(-7c9jb%?/?k>nY
O"%[m$.A0XF=ZGslgp4$FgZS0k3TnlBuUV6JO%U6q32D]AQZT<mi>WJ$jj?25i%#PqT/:`]A?Y
%r$^d,hO1oI4!6oU6OW^>%>5=0aF5h5-83H<#7KC:C2mE5$N.&Ls7/f4gBhFCRk*5CgKF2OW
`Ljo1>"P-%,m?pco5NSJ\PBFu%?Qj>copK(BV$Is.LYmH[$"#TgJW$CUmrR=/9gmQb0r>;I]A
^_<]A/a]AM;c(HH<h6*qKg';2;r37,CSfXj$tPY^-J-Ti7HT]At$gYS1WH&f3i1!#0Mq8L[Z.OQ
Z-lNheZhG9.P_S5mAs<AJ/TrXCB52HSsfnCf;b#&s/<Y>G%To-h24(@HDY(3n"^+O3r;g`)`
cN^/*Fkmf;KeS^",DonZmhJ:+_AhWIF9h^<\P!ff6nnaI"WHHL\s,lOZ'n$)N+PIps\@\17b
W?uA*%KLDV:Y/[Zd+%Bsk"WnM2BU*u<DLAY984<u0B$34pCB*\4>=bY9dIu<.:bhn(bG,+`=
uXPYGZ#rc%O-89b-N@C20V,?3oLq?9Rr5=ZI[rU$GC6MK)7?QDS7fZ9IjSR[CKZj[]AE'p%4-
&VGg2&+!_Ja_Z:.neF`SM_:`A^p[7:NQXF6_I#:c=jqlQR>!-6B,d3e%pHVM-]AOnuRNNVNqa
dtG2GgOBN\F8LHl&uT?MD5N%N1Pk4"(p>t@)e?hCokb;8OFbc)*^'W%<4WL%!Cf'nmrB.Sf[
bbE7!/&N7Sd*n>_4c*s2a&IbnhDRqmfo4@>nlZ+)cT`Ns@8[k5bmhun4Xj]A?oe5W:KsM&AJT
de+j4?/+"+T5(5E8!9H\)V)hU7s:a9'&D035oK8W*l[tpQIAs:fEtpcALo+@Vtp*n5V8`GM]A
N[6QflM5m;h>ul6_qA)ktEX'N;`bXLW?O!JFP89%*@+l9Q)!-9XqNAP?(T>iAL;(L>huAP]AY
A)ok?/(ltb9[^Cn\b88HVi7-Rr9+B"eEJ_uUf#X?Q<r?$.;NeHT6A)(bKfdB7DTqh,a8:b-U
I)6=e*F_!1PWC>g='5u4XB8Cmf@<lI4jf1GCu+g%[("5Q.l?EG>^/?a00,+5c%=4+t4LQCX=
$3^+Z0u^#jG1_Y$uB:j%,"jKUCChN)_VPaWj_-@=K@lK"OE^nhsOj1rMM"ZmkbAQGH@mD6m6
$$1Gk91EcRCh>4>KQ$Mo%kWC0`98->A)04bZ'">sY<9G*1D>KPO/iX3WG#]A8fVILae99Dbdj
Y6m4q_L+riN39qW>Bg@3MqdQulMECHQu5E*-a&E,S74!Kq.s/X7[P-iA*aH`QtA$eCs[%f5b
<2?WO`fq!nn"0^!>lC7D28gEc?\qO'`Jr,/XTRZSp%Vr%i?WC*k4MrP;)?E!4.k!3CPZd1If
N(:N[ecP'aj(>cFgk'Nr:\'HKb'73\daN0onis*j);%3CY@9ZUMpX:BXh#r!&E'mY-uN?jE.
5pgg6@;TLO1#SM!-?[Zr%C[`Lt5%:$njIS/V5XEr$bDKf3tWD,m2Bg`tn;c([!"in6/UQX)P
7C0ZOQDp@t<hTBE6Ig:OIEe8nSG_]A4p;mMr5S,=8?-\5,Mm<'&IC#233Y(15GOdO:M[JbkSL
Tli)L/f6[e_dsWhmV-jVm'MQ,!-0,iG`dX^"D.eb&g<h-tADZ*r@BW6*ng7]A3_NKmgFk$-U<
SY*l@NG7Pc8=Jf&*8#N)oi3`-gaLI'=Mhi?J4B"9RUp=lRHYc.Mf8[+l3"6S)i0+09b/Y5[V
f2%d2m//1Z"n8[[MN5[_g\Q?CaP'thWeJ5I4mXa&[UiKPSGN_Rq8<.[m`=5`<E^?p&5hq6#D
)l'No.[++BVHX5.Q9K`!0I-'RfaKs/.ES;nn3Qe9(cS5MJE$=mSqL>/rAQ5`ZD*LKZnktYMs
k1;QRZG=Qi*'"cQS;+j>o(F6XiNh[mXR4!EY+>)8R-s?MW9ZAN:up?>mbu%rCdm)L'Yb?G!p
Z8T(n0`g'_?(BprL_mH6'9Ea'$5WVj&FD"A(%t@geiK!Y^(Ji&87(/%[r#7$7<;FC*]AXQ^,u
O)\sOa\+SXM3@B[,eF=>c:s$9rpK$=_q4h_4nEtbU+bAkP0?bSi>s*(V1O:B?'+;q*gD_PhA
;R;=PNkZi4Gc?l5QAj\D?8g^(l>'sM&m`d-;^2lL$,VnI'V"h$`t1NO*R`L@(Q>ZZ!C\f:,B
,9co[L.U#J`05X:I]A"<Y]A;n&P_&o+<Yi]A>2#SaCD<DY)m%WeblV:arA":2?5K9Z36hW3L#Yt
*b-u/a8nC"_@Q2i=2AYb4`S/q9dp4FWT<RVkrUD^;j?&HO<j3h8>>T,_e97s_jd)h)JoVLS]A
0i4bONV!VOL*Og-CC[">m3$"cdMuM#q\5[@'$Z<)VjN]A<:_F/\Jij90*$)>;C*V=28%gaC&E
]Ai&4Ig-u/O["ZcljB%KB=)[-Vg@PP3I"O!o@M\n+RGa3'Q/8sm'Q9]AX\"!o`bAD:p>4!nGmg
oqO$,>fn_dcg+>]AYGQ.LtHS;8[\%]ApqjCs)?`KSk;4'eA/52eG.90n32m;#gf,RSp#/s[YB`
;@0Ro6IHp"K#@!rEC/jF.<Krl2ab-jSrJ;%]AOd_]A1jA_-JaDjp3/$5O!F&fft589ZFQ&Tr`X
U/"Mm^E4=`V^+Gkm_@f[G&9q9`V.d5_Ku!WC51:%3!@8-c\QPNFPDG4:)3F2QqeGMZn4]Agag
B?)+MM.I6?^'n.P%e$[Fr)BYQe%;S`,]A3Auc(=o#,L76o*P69@%G[7F_Ln;4?#CUkti&)(f7
P/n!WYSXfi7!h[[]A_7IP#Kc]AbM?Y7LQj33S\mQb_\cAT_UfM!F(2Mk9lO3IaHc%&ks2oWkkE
LY74O$"7"M/j589_$nr67i8fCO9Ti`eJZF7$ZLj[2lB=Zm8]A(]AY(\nltQeLO54-qa9qtUJQu
Ij%MG0fAh_?<a`/!-U)XZ[Xh2>j+Y5Wc;W71MO;[SmUq=Cbq1ZpI^N3^:<X=5.[+"#@_TG@\
$-o&=*5`B))-XG=/?_soPtio4[=E4TD:^oh8<P<c<=qd_bfQ,,,dsG>,%XmJ;c]A3llo)&/n=
gJaj#BMTn!ij\eh0)?`qu?.eP10K;m4mk&-p`2_e#Zrgb3jBG.n+'JFCA13nj@#=G]A^PBZJ<
[XV(f'Ko$Hg`LnVgmiC10)?ZU,U5<i/HUh6?j+\)F)H@`8=;)@.6m4OOg(CR)5p]Aa&o'>Y),
QQ&,W)C]A)lZ.DAHEUiBHBh$IEc'uPp)h(sZk3pSSKOCmML4i"<U8"X!,&j^"q0OPhCt=hffF
V!lo6<e%ZhIglS?jd"R#XBl]A5WGK"J&e%k9`Q`q8)2p8ZP(RBQ.(D,M,.ds$N',*!%q#>-Us
6,fH*OC;R+#YrOIUj:\]A[?/._D#asE^'=AOQ0jG"Pe:an%Q;S<rY:>OiFkEVg\C`6'8udFrU
_5@_H5Q.PgFt,d<4?))2hH_.:-FD.&qXCZ$/XS'igJ%/D[kT<u'j'\(^Q`nbXCCU@a.`ZE8<
F-T0^U#7G;p_eO9knU#0!F2`k/5O1',->t'Q\\hg&"+]AMmaF6)js6_2NK5bBFP''bNZNJLY8
/,Gu'pY9`P30@GM@*M$4-u7!X,S,AWTh6P6%-954PLhB[0ccCgtmIrU!8I'HbN#sOGoIUYGj
I$j9Y%m2eUT)VNp[h8#88;]AX$0mZ5>cn^mDnq?BjaI'MZ#,/.AlDX7MNW$e:'%#";)he<]ARH
4\juXC`Xqa+ZC4gQ;;rGGidPNac=M]AZ7!cH#V!!hhd;bMqIi+Gd>bS]AX4Og]AUSr6C:t3]A$>a
M*VU<Ii!qcj`3Z>E(1K%[.X9;&NIDd;K9I?'g!b%U41)7&>K:'(;b"3.5/6:<61"-R732@S2
F;'R$?keu)+QOBTZU<138F"j!1+u]Ar`3ol=O?HX)1a#RVKh29XZRW_"Y9`if[<jB@sF7&X4b
^D)h>fJF-[O2iT)R7AIK6)<3G>aWkOX9U9%LP(5Hf^LPl5'G0kruO\_9[C+1-$5#Jge.$I3p
<5U\1)C=&]AKGBK7JUn-=%Uin8j\ST(-#)``k%fdqt%7(`Y#)g`dWrKMD-9]A.uV?Ceg@?8Du$
LefB8$aZPmUM.FonSA:Q4P>M`78!+O)n)Lh#t:(8(ilS)]ASMrrmcJ$UHK"#Ob;'_rq:X$$lt
K\rV%[K'_-eE:$=5;T*K>*V(=i>iA$W_!%`>RZ<$F`Os&R&fMt"B0MmLf[#++"h?bgMPN6"q
^pPb)9DY&0Vd?!4]A\lb4CBVs2n_LQ,#'n>m:Z5Y)n)g8YHW!q7ENfF!JU>HkpdlbV]A"aZo3N
6F)9&p#Qh;=m"Z":V3fpse(^%-57u$8E&)eCb89W#UeUS.KdrQpG!$k^a(*goPm-\YT/&Qkd
ikfoCUYm9-Z,1+_L.Vr8,-++N5BBenmYWOT!r)(dMV`6a@F;/2hCi9n&K,FLp8D3Z2qoi1F+
fUIPN;b0?Ge*#<.oFg>;O<!(1I>#Q).0<+EMm9_oWaZI<YlAH[%OE3qrC?XIB"@A2J(\+h7=
Y76?YnW1biH:>klKib4a_9g0N:J!/<F7<00^I+eQn\On>sZKVE42r.D`?i7r_[O^K_a-X"?\
>O+(gjS$fB2TD=]A%/8Hm5qu1[(kXOks(15/*CI]Apd'(MW.@([itXk5sEi5*]A0&s()&bAMI`[
,$g#g_assbDT0%h#/FPf<=G71C0U%2+)S[_T).JBb_;hTMMlS9Q+aKon'uO.(@Lpak(M[iHW
8]A9<[sR%]AuRk\+_$hB+Z,anp<'qmnS7Y'u5)W'Em^>_Url#+:e:3E(/Y@k+Te!!H37*/q92g
P4;Jhb+fMYYb5,R2ae3gEK`[%k8&5F!r(i3\Qru#B6ut,kiJmX=7&9!ft;5#OUUUb1`5U-3.
[O[.P68"n-`tXS$Bdh\7`P$`51[YNZ@?9.8G*1iTX;LQ]A%$#Y>9e'Wf$4s-:T<dCK`&>njNs
gRkiZV"rAIinnsCDCf-Fu1Yq#HIQWcjM(Xkb;7A]A^H`K:&'$*$Kd,H/a/ULm/RMmO`6'.>8l
:h'+nYLbLJpX*?nBU;,\smIh:"(nt.ula`)MtP=pY2ZNn]AVuppJ>Bt>P@^0g=_KIaL*!0=b;
8MZeIT4GP#npRm@\ilO6QS+`s)RhAI\DpVW_YS7;FD6#]A14EAjI3ZGr,"C`3(QQK3?i7h"k\
gJ]A#?:RJn`[U/KG)P_n>'b@cIn?rar/-qCqcJ;W5C3HkJ$F;bDpGLNKLS3jh*/ne`h_aI%_"
0m7ilh>(if^)jhX26Za51RqU3c+WP\/-`5U_![Yt<NYE"!Iuq`8ceOrfRASo31>P-DA`,g!:
s-J)6+.cR<R=75_&)eTdqa(jZN&r^[ML4[4\_"\XWioH&$s+EtsG?F5egET42hgkrW#"dO9!
bsUSA%R\>$j@2fB7>2AI>33$0[,X]AO0Ok[Y)1P9?L8J]AO^Zucs4/K;_oA.He@k6ipSHs)ApO
'/Q;3uk\J!3bjmC>nFZ#?(k)7Og[D`gBS=&Y'd^OCFXS<)#<(1/RNNS53YSoqX`m7CNY(8.n
^B_3P4q`n/529Q:@[l077?qOa3^!JK0\hLsG#ufkYIQ9hZc%3!XV*gYiuc$RoT\PM'j0M<%%
6un>+SMNFb`;0>$O'(h_)5m;b2]A'X0fZ.T.K=cU=$7c?+ke7j69%4)$EEpl,mL)'st"I%N=H
Y]A8puLX8E+LR-9u>"S7?,NEaUDGA-Y5!HI7O_>BX_hjgNEHEp-`3=S+^LMBlc":/.o<\rV0;
AMT\5KRV^CB6EYm%mY/1:$8H`Z`4F=WmH3[h2k0Cdm+AAn^1a`tQ*sk%!#4%/^6D@MnA!beY
iULbCEiEMs5"Wpa[QbBbs!;"Id>>gtNg9:(j1jo!LnG?n2DWF-r.$WQEe%E^-c#4UN)Ii*VJ
-#6Oj*dQ(*QEu@g1^mlce?J'CpuT_Ub7?_-PNsIT^)l&'9j0qAohkrX_rM6O8<bM'/X2bEpY
K.dm!t.;HdnfWU&9K,Yb_>I;GogXk3OOu<O]Ac\d;:JGjPm5iNrmQFL>s$9h[csN;2N*d5lid
ppk2kdDCoefPp&)]AT+5`0B?i467?T']AW2%BG!7<gD!h*VLi.+l3h1@NHH119KKVKW,%4Tc*p
VU0724eP<6C*A!:0'k_l/0[r!#PEgR2leNd(6h=\h[_S+b`##C=1hY82EZ"MI4pgW]AJmL%[o
+icccgIfVp"7=p4$Le&(9j1^(i3ik[H>>5Y.(NN"%QgAF>5nCZURr$iKnUDA*6X`q:=`7%K0
p:7;K'7i4,kZ1]A<gISHH.B.!fACQ_V:'M(d^4j:p3t.HNN'M>#`+9i=%2aIR<BDGpE`]ASanF
]AN8k^H[k-O7kO+6/WT.7kW*@c03+[#]AOeNEXo=+9Bp3l<m&YfhD$0`WkjA3PVIkKb4;AN7Pj
!6aV00[q]A_-FSCb9:2X(;dI3-MkncLA&^=j/iY/ZPpYT/Bg&-&8m86*#4.1_3YjaoD/HqG%G
2M2O6uhrm7V.6>S2D=8U>I0'W?q[12nV]A]A"dUtD3D_lulE8URmN`=/?aHSQTu4k>k3WdJYtG
kG1Gf7"r<1DpIGf7V;(<e0Y3SmOXdLt'.CUAAG#@M%hJC9S!s$KH+n^25en+/jbhB2JZ1gH]A
dL]AQu9hFaj_Y>)FbGQib&hhe<e#6P>_<X?igniC1Xh;]AN++X3mUs2-hVKSuu!+p_7l7oK@;M
GH0BOZGfOB$YfL$V9C;A.03++]ADG.+tPeb&)Ci8^`aYIT&5N<WIDYf!K+>.usscnpdjK"?:^
?B4i'E'Y8aMMXJt3/*6j7j>Jl&02[H)onns+dTN-ZGpJan[N\+V@Cc#/lIY9#!LqB/b+>Q2)
X#LJs3JdaDc!9&6W(rc@<pUaNgtC$5="I4K-m*%AitXMOHT6%-P6B3S_1'e23X1=M,Jb(=[*
6fPEOp'<@[nQb1J14YZ;rBDEV_Q5L_2rP@^#gIVQ+t\u)GE"'`]AdUf+0f-r@`)4j$gN)(m^T
'&2(T7.rlk89]APe/S8s<KBBO;SI^M_<6+(rTqA$]A)E7_Y>^jLlpH.MoaIZ9HXSSE?'k75o8\
b&Xq9m<U/!a43>%kQ>*BeHI,b;)G-T'Y_3r9NY$H#=2NQdoZdG?.5ZY*pPlOAKa>jnTD<UA/
acbOa"B,2MoM*7l<l"-O1^T<Ba\b\kfZ&$I9!Kr>+OGPHOa&/)AGrd+LAY"\0_$VXNH4nEmW
[]A'E:7EDL/H_%H]Ac&tEFO7>Ze$a39g$/3Y0#-C^bCY!L0`L)">"d%\PEA'5Jh.5<NHf'?;A!
/5h-bZA=cVYO2WB'?dZ[crMZP#BDAQpk@*CuR-NkC6#Ld+qiJNHMk`jAINF)\:p+ouZl-ZF-
F4g,lY2aGoYoU#H7:AIOkW)KCpq^df6JV\D47MW6f10o=Pe/Bd*Fth_LA]AsqK#,T/gP`7cRp
$#UNV8GqrBtPtBj*HrjEP272f-EAC"'$lDu;X=+QBsX"-^AiEU(R[hG:8j&T<W"?R=oOVMZ0
U5t&TIKK8Un]AOtmCjCPtG!hB^:(kL'G=1GE7\b<DYQ*K!Qs'+GfV(h_pS=$ouFQ@B#[8=EIZ
Cs$W%]AcW"\rsu=mXG[3.c^nW=&/@\MG0[f9:5+$Se_kPhnib^T0eX[<ORbs*)aB\EqL>F4["
P.8o1#rKGf462%XEZ.WLp.P=]A&B\4SR-;dF*\DFBF*mO\PHSU\.6Dhj"nU8;?9+;u+-WG*<8
cW5>jn-+/I"5^(P\`X_@.UscWKb;f$>D*L1Sdl/B<;Odrce1OF$]AamQh(P!mLP[828>p(Fmb
rN)gs>?Ijutc:0Eg]A,V=*RXR6YKI_[Rbc>K#_*@6YmPq>GT#P(Jlq>;Is_@'7^5N!=#SCe`H
<XC*8C@`Nh5(2[8(9JKA0heGTid<$;uMYE@R(;T2D/Lc0hgMY,,cUD(2%+pl[Z&n>f>3[>V-
`\kK(R",k@+?hhd-a6[CM"G$OEX4G%>JD*i3FDlO8XsFXk=;*L``n#l3MF*IGS^0+R"/TOBo
iF7f1F_S\@$m<`1d`F^5bRLUs:Zlebab92U*?C4li*n4NjonM_kWmu35i-]A:X5o]Ag^FZcB]A*
b*U]A,EL)Zg%u..[,6S:_<pC06*?r0F]AD^d-Pj*&@MEtrq3jf+u?P-Bu)^;/DV;s@6kXCB"oZ
q!jq<)udbUt!O#sglmDr7/DhtAY(,45_T-<;tW@#Gtq4Gh>Voe!7>W*n)IGjE`+QA,=/"r;B
H:RZCZ(]Aedk^8:mjE)@.9eWOO%0'm<i$pugt.RG@AC#[>VO6BM7)PT`!D7_e"h+jbIai*!B3
`nr#",m"_\kY99cpIq+p)%72A6L^f^,RSE9t7't7?)"EYOt$P8[qI%HeUPFM;BXRos3r_Aa3
1$=i,!557E&b^#(!3#\Kl<ZP*@$;5L_n!p^RSlF[2'I,^jbH^38O[1b&Y=H:s&M+2btJIrsr
)Dr]AgY-Q4Ma*f`oatmm]AfKJF5nBhIKPC:5/jgZbZ)^?e[JKg68@H)#S&!O0bAH6q%g*"-$Q]A
V!6%KR<q\:IN)IEJT%.!51%L_j3n8j@u*:aH<N`B1QHS(7U["e6m6h8L@.bQ<Jg-MV+,4g73
Ti;lZG8t_c^R?8J,>Bm;[QPV)("tY/T1?Cc(DMTi51`:]A%I\=e25`jU)Vo"jFY0e"$q["JFW
p0V8'Mjm2[-bDnfG0k[8);>&qYUMa_Y!N06341b3-8aJQYr87<`Ms?"A,P<'*+u/@DK"ndIG
2Lm9=7F%At(!p4cq[7/.4!0Z$Wir/HSb;X-<9OmQbB?'uY82+u[iT)Q;jQB]AKC1fQ*`,:$gW
BN8E=C<GE<eGOs(*i'IO%3,=beL2<&F(Y94@C^HFL3lSi_LeJX+la+"Gmb]AlpA,Ji,ko"eL\
T>+\Jp%T!>^.a0*MjQc+W?*IjT')'a+PK?"Z]A!%2q<Lq`nFUq=o^0(.N8@jZC>^.QAW#[MgK
:b<ODQNiHIQZ;o:[h-&hbfHb64<`Op#J(\ciQEI8*s%LP^<;2"A)%^>qjLS*i="W;1BQ@+t<
q&oi!&]A60^._B1mp]AYP`_E)C@"+EAJk-kA+$[K,`4D_4qR5n61]A-c14"EZb.XePX7t8#q?i_
u>0P44uHf!>c9n&eZOXLf4W\3Xoi@WQ/Z#ZHq,bbt?@>*-9m\Wud,q@C%g1[jJ!SDF6J)8I8
*a:pSoM^\d!/?mekWEhZkKt^iJ@LN-[eRX7$ER"_O+<Ge[ob0CfA.aW>e8cMK0s=.1D&&M=_
YJWm4ra-B28tC2`P?&QOf&BF*Rtr?)Y:r3c(:Jo&(;[dODX5;C>$B#Rh#q/F4thT=f:u`?PC
``g$dD]AP<ga-`;O2$d[8>'S<'Lc;t-XXbsI0IK!d,3P1HCN"4n2ZD^==@M"oTmE`SuKR[#(n
*G:YV>j7lDFQoJ2qf?81O]A)i\i%I#6*5RKUMX8.bWtE\a;VQ5B1V5q1Y36]A.Z`P\\WW^S2g6
FU9`PbfF=)0G0Fk,Xq7siGHRBa&%/306FRm@DqNgQU_(m^@e^s[^at]AN28ep#bYoOAYOdV\Y
Vs7A`b<%D8(c7&DpiFV&kZbE/g?$Eei2U@/r4<N2f')FR=Ka38=(PZHjWktnQkQKdjmOk7/[
Z#mSJsE5e'iA5rOnog6/'uTmn&reeh&EJKlRt8a%cRg<k*oBB[USCmD7<>QM/(+KofFuR9c!
t$h;&'O09$PM6A8W9PWM\0e1pW),qrHfbgIL<=4XkF4d$5PcdqW[!'sQdb><Jl46'-P-ru[_
*PQU[>LO??*ot2h/t3C#I'n_rMdl*!g!RH`]APW_W=d2^b:d%GU)]AYXi_]At^Za(n?%5)`UggN
DY8L,fjEd"Hq(JeGF%1]A[,8@T-)QN=2fnk3"O?Ol;h-%;3(g#9b,ZAb!k*L^oSe`eaB5E5jO
osIKJAs1jSq/F>4#0>UZra<gp.KGurFTA`Zl.1"fPR_'h$Rh#.P7rKqFEbU(APGZ-o(<HR/u
jaL@*^hcjs?ZKOUFEXp&A!mj\7urc96F_6nl+7oLIDs=kp5*;J(L<$kgYub^AQqUop6uC`gB
NWa7_sN!<`uc/'M6OH,2fZKFs+5E0Y;Ok:.2-ZUTh0;3MP<oc7Y=5.$X:eh=fQ1D@3EbB&V%
KBagj(e!rlip*_0ShVTqES<NC%KCl4qapD1WV-_kD1+LL7PHoPGko=0`E>VThBB=of(>u)XR
Er\r1tUQis@N2QL/eH%1*JL+<eScA]Ah+)/t&n[fcDYR4Cj#/D&eV:]AQs;O)YKU)VJ]AlY.(<d
P$!fYC-#1(!KXVb&O7nt^.Gpki9?j8Z+!_%&H3pd6*L"b`O%*d+cK-F`c%:bm/geOkoYOZPr
t43BlDc#5DN;H*UO'0h?JDm[]Aq*RdLcK"PLfq[bq>k*1;j&S4\ViO+k#`AS^;'=N5GJ&+t(,
o_%CI'&8codmLoR1.f6l`aLh>ZKokiN5[/##$W&[k?#X!'4@i`?%g[4JRc(_&ph,StncGKLS
p$L6Xi4tW7C)YtduXs$h/*:m[S4l,@gPG!!ed"d%O9C@rWn?[2FrWN$u_<Yj+^>)o6aZ2`GV
a-iKk[.=-g`EW*-$3c>:H1rA-P%%q=!e!7`**ebC+('W-"&(bA@OJ)L^`V7r9<n*[FQGp=#c
_1HY8\[AB4[?).*Y@afaWr8gq7N$oPblWDH0H$hnn5PI[57r'mXgd(K8S(Z#Dtmd'.cUMt27
@Cnm\UZRSAP-V4rT&fbT?$i^u.#ImB$PsZP6QobS[C)UIrl54Ir'::`RNaLk]AEHHR&lWZTUV
niOp2l9XnL[&!9D2\1+,:V=Lu/Ts<"-'!Mc$>_Qm7;dh+*)730)_Sbq_s5.:Ob#9WF1TjO0H
RE5Hb!'=_B556LI:KSHZ[]A88\Q"pHB`:t&AK6epXjk#dnFR8Yrf2S_=K@GHHGa,\%M+[3MRo
MT8.XX'!]AO>&crP:M;@JZhqB>N+AYlTJ)4mZ'j6FoNR4EcK+]A`dqC-KnOmt@iF09FVC[Xeh:
:&8a;?[6\WU"Y]A/p;`@l9q>JC-dH,W3UB%trk:DS:'0]At&,_#"`8C0(F''&?CeA.LNq5;k!R
#+2Ps6Am=:`&VHZE"^6[s!=GfiPLG7bC^hd>5sU)]Aa#aG=nXoCkG[@;>BecArbN1@.-nUKR3
-6iG7UVj7.?S__iD\Y(@A&"f;o%BE%[0qG:iIJ,>N.8b3f.P4$#Ci8&8%ar1,Ik\/W&7nAh<
o)QVm\HAMkUf`24rej%YZu9$n[&1TSNe*(DG'e]A]AV<(<?i]AU5^Yr4Y?=+h3^)FTVK/&GD,C1
`f]Ae`soXkDTgM2R)jp1*=WJ+;[Y%]A.)hV!6-RfGfBfnr]ABK]Ao.&VMUk;3$=*;@Jl4ia0J!1e
c+hea!du?gr!1Zrf-;'6C$AUE6T(S=Z)%o*Je\Qm[Q:H?iHWY>,htk;E6oL\f(a='Vh#6=[R
>Y"1J>5$I@J?46oBo!G?@]A?c+hj^P<069m5fRi/uV`VS[6Wa.FRumQ*A3O]A6ohJKYCp8_lsk
KKe\Qt?;UjK?)Kk9Jo6tq+Lr<=W"6]ADoTnag<U-/k+m;:Tgrk38WMS2(7?V,UF_k1S8p,C^!
1M>BodT+^&/e-rr;4LQg_]AZ<jX8@[-q5kh>AtW1SSJ1.9hn$<IUOo,E(OGsfeou4i6C`FV>X
tMIJ$)+mgTF%FmQO4[+LcF2m=u:SbfDiYZA#bV/i[u=Er/<.G)'mDrg"p>pEXc@tkr&^[gt/
&rG_ArIW_EIK5'$fALCEYM>;eC8\ss=/s_f3&p-IhU]A#@@JCqb1/p81WMcXm44U5&dm/4db"
%[EYE9$Hg8F@M)%\()mf9e*gCfpPjg8q_TC]AJeljUrLFlf-j\[lGR%1Hm+Rt!N]Arr@@A;u&u
o]AL#G5c2#@3nioMZJ@M0-M_Cj;/jWUVJb]A*d^A<Cn;*)*k*T`,,"9j=0?`CH%-ct>q6#;6Yp
&u/[<Q4bf?X<?@k6;WH90b'_.sS$rhjKr8o3J83g-,Y[kfs.IoY3D`/R6a**pp!d1l[T%_o#
,[=Gt_o+H*)5;Z(M8/7j\!SU7CGK$72L(aV\V(%r1;WibECInF!r::J!/]AAX@nPE[.iajVPl
oR%lVs$)`dPV"4=>%V<r8PgM3??B;*(8V+PJPVS^c":tl&h$M1V'MtH9[hO4\70E=>C+[0JH
qS=d!ccDIFSsJ-Op!!C"@4QfG92:gCh<[8IF#Gs-IqV.=!kLSi;5Y9IsW>gl;-:H3>V\O(T2
=RQP]A@AI1UM"rDUH"3,Y_hH1eQ#Dn<N/=A77UE3D#$.Q'G'4>7f&i_!*Zjp3^')pLb\$-nCm
oAK_A`%Fh)'mK[o@]AVjIV]A<U<rOSlHc(=]AnGl.!rn$kN&.7"hRJB[-lE`6tlXo.A>^OpAcS3
.U*=t.qhK-gPq6g\YVB$6FHB=RJX%09Ph2OQn:,ekaBIs<M#OS'ioP]Aarpce~
]]></IM>
<ElementCaseMobileAttrProvider horizontal="1" vertical="1" zoom="true" refresh="false" isUseHTML="false" isMobileCanvasSize="false" appearRefresh="false" allowFullScreen="false"/>
</body>
</InnerWidget>
<BoundsAttr x="465" y="0" width="495" height="540"/>
</Widget>
<Sorted sorted="false"/>
<MobileWidgetList>
<Widget widgetName="report2"/>
<Widget widgetName="chart0_c"/>
</MobileWidgetList>
<WidgetScalingAttr compState="1"/>
<DesignResolution absoluteResolutionScaleW="1440" absoluteResolutionScaleH="900"/>
<AppRelayout appRelayout="true"/>
</InnerWidget>
<BoundsAttr x="0" y="0" width="960" height="540"/>
</Widget>
<Sorted sorted="false"/>
<MobileWidgetList>
<Widget widgetName="body"/>
</MobileWidgetList>
<WidgetZoomAttr compState="0"/>
<AppRelayout appRelayout="true"/>
<Size width="960" height="540"/>
<ResolutionScalingAttr percent="1.0"/>
<BodyLayoutType type="1"/>
</Center>
</Layout>
<DesignerVersion DesignerVersion="KAA"/>
<PreviewType PreviewType="0"/>
<WatermarkAttr class="com.fr.base.iofile.attr.WatermarkAttr">
<WatermarkAttr fontSize="20" color="-6710887" valid="false">
<Text>
<![CDATA[]]></Text>
</WatermarkAttr>
</WatermarkAttr>
<TemplateIdAttMark class="com.fr.base.iofile.attr.TemplateIdAttrMark">
<TemplateIdAttMark TemplateId="840ff794-81cd-482b-a87b-10394a60c1c2"/>
</TemplateIdAttMark>
</Form>
