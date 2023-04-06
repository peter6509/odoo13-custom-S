<?xml version="1.0" encoding="UTF-8"?>
<Form xmlVersion="20211223" releaseVersion="11.0.0">
<TableDataMap>
<TableData name="ds1" class="com.fr.data.impl.DBTableData">
<Parameters/>
<Attributes maxMemRowCount="-1"/>
<Connection class="com.fr.data.impl.NameDatabaseConnection">
<DatabaseName>
<![CDATA[FRDemoTW]]></DatabaseName>
</Connection>
<Query>
<![CDATA[SELECT * FROM 銷量]]></Query>
<PageQuery>
<![CDATA[]]></PageQuery>
</TableData>
</TableDataMap>
<ReportFitAttr fitStateInPC="2" fitFont="false"/>
<FormMobileAttr>
<FormMobileAttr refresh="false" isUseHTML="false" isMobileOnly="false" isAdaptivePropertyAutoMatch="false" appearRefresh="false" promptWhenLeaveWithoutSubmit="false" allowDoubleClickOrZoom="true"/>
</FormMobileAttr>
<Parameters>
<Parameter>
<Attributes name="地區"/>
<O>
<![CDATA[華東]]></O>
</Parameter>
</Parameters>
<Layout class="com.fr.form.ui.container.WBorderLayout">
<WidgetName name="form"/>
<WidgetAttr aspectRatioLocked="false" aspectRatioBackup="-1.0" description="">
<MobileBookMark useBookMark="false" bookMarkName="" frozen="false"/>
<PrivilegeControl/>
</WidgetAttr>
<FollowingTheme borderStyle="false"/>
<Margin top="0" left="0" bottom="0" right="0"/>
<Border>
<border style="0" borderRadius="0" type="0" borderStyle="0">
<color>
<FineColor color="-723724" hor="-1" ver="-1"/>
</color>
</border>
<WidgetTitle>
<O>
<![CDATA[新建標題]]></O>
<FRFont name="SimSun" style="0" size="72"/>
<Position pos="0"/>
</WidgetTitle>
<Alpha alpha="1.0"/>
</Border>
<LCAttr vgap="0" hgap="0" compInterval="0"/>
<ShowBookmarks showBookmarks="false"/>
<NorthAttr/>
<North class="com.fr.form.ui.container.WParameterLayout">
<WidgetName name="para"/>
<WidgetAttr aspectRatioLocked="false" aspectRatioBackup="-1.0" description="">
<MobileBookMark useBookMark="false" bookMarkName="" frozen="false"/>
<PrivilegeControl/>
</WidgetAttr>
<FollowingTheme borderStyle="false"/>
<Margin top="0" left="0" bottom="0" right="0"/>
<Border>
<border style="0" borderRadius="0" type="0" borderStyle="0">
<color>
<FineColor color="-723724" hor="-1" ver="-1"/>
</color>
</border>
<WidgetTitle>
<O>
<![CDATA[新建標題]]></O>
<FRFont name="SimSun" style="0" size="72"/>
<Position pos="0"/>
</WidgetTitle>
<Alpha alpha="1.0"/>
</Border>
<Background name="ColorBackground"/>
<LCAttr vgap="0" hgap="0" compInterval="0"/>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.parameter.FormSubmitButton">
<WidgetName name="Search"/>
<LabelName name="地區:"/>
<WidgetAttr aspectRatioLocked="false" aspectRatioBackup="-1.0" description="">
<MobileBookMark useBookMark="false" bookMarkName="" frozen="false"/>
<PrivilegeControl/>
</WidgetAttr>
<Text>
<![CDATA[查詢]]></Text>
<Hotkeys>
<![CDATA[enter]]></Hotkeys>
</InnerWidget>
<BoundsAttr x="560" y="25" width="80" height="21"/>
</Widget>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.ui.ComboBox">
<WidgetName name="地區"/>
<WidgetAttr aspectRatioLocked="false" aspectRatioBackup="-1.0" description="">
<MobileBookMark useBookMark="false" bookMarkName="地區" frozen="false"/>
<PrivilegeControl/>
</WidgetAttr>
<Dictionary class="com.fr.data.impl.TableDataDictionary">
<FormulaDictAttr kiName="地區" viName="地區"/>
<TableDataDictAttr>
<TableData class="com.fr.data.impl.NameTableData">
<Name>
<![CDATA[ds1]]></Name>
</TableData>
</TableDataDictAttr>
</Dictionary>
<widgetValue>
<O>
<![CDATA[華東]]></O>
</widgetValue>
</InnerWidget>
<BoundsAttr x="370" y="25" width="80" height="21"/>
</Widget>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.ui.Label">
<WidgetName name="Label地區"/>
<WidgetAttr aspectRatioLocked="false" aspectRatioBackup="-1.0" description="">
<MobileBookMark useBookMark="false" bookMarkName="Label地區" frozen="false"/>
<PrivilegeControl/>
</WidgetAttr>
<widgetValue>
<O>
<![CDATA[地區:]]></O>
</widgetValue>
<LabelAttr verticalcenter="true" textalign="0" autoline="true"/>
<FRFont name="SimSun" style="0" size="72"/>
<border style="0">
<color>
<FineColor color="-723724" hor="-1" ver="-1"/>
</color>
</border>
</InnerWidget>
<BoundsAttr x="290" y="25" width="80" height="21"/>
</Widget>
<ShowBookmarks showBookmarks="false"/>
<Sorted sorted="false"/>
<MobileWidgetList>
<Widget widgetName="地區"/>
<Widget widgetName="Search"/>
</MobileWidgetList>
<FrozenWidgets/>
<MobileBookMarkStyle class="com.fr.form.ui.mobile.impl.DefaultMobileBookMarkStyle"/>
<Display display="true"/>
<DelayDisplayContent delay="false"/>
<UseParamsTemplate use="true"/>
<paramFireStopEdit fireEvent="false"/>
<Position position="0"/>
<Design_Width design_width="960"/>
<NameTagModified>
<TagModified tag="Search" modified="true"/>
<TagModified tag="地區" modified="true"/>
</NameTagModified>
<WidgetNameTagMap>
<NameTag name="Search" tag="地區:"/>
<NameTag name="地區" tag="地區:"/>
</WidgetNameTagMap>
<ParamAttr class="com.fr.report.mobile.DefaultMobileParamStyle"/>
<ParamStyle class="com.fr.form.ui.mobile.impl.DefaultMobileParameterStyle"/>
</North>
<Center class="com.fr.form.ui.container.WFitLayout">
<WidgetName name="body"/>
<WidgetAttr aspectRatioLocked="false" aspectRatioBackup="-1.0" description="">
<MobileBookMark useBookMark="false" bookMarkName="" frozen="false"/>
<PrivilegeControl/>
</WidgetAttr>
<FollowingTheme borderStyle="true"/>
<Margin top="20" left="20" bottom="20" right="20"/>
<Border>
<border style="0" borderRadius="0" type="0" borderStyle="0">
<color>
<FineColor color="-723724" hor="-1" ver="-1"/>
</color>
</border>
<WidgetTitle>
<O>
<![CDATA[新建標題]]></O>
<FRFont name="SimSun" style="0" size="72"/>
<Position pos="0"/>
</WidgetTitle>
<Background name="ColorBackground">
<color>
<FineColor color="-1" hor="-1" ver="-1"/>
</color>
</Background>
<Alpha alpha="1.0"/>
</Border>
<LCAttr vgap="0" hgap="0" compInterval="20"/>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.ui.container.WTitleLayout">
<WidgetName name="chart0"/>
<WidgetAttr aspectRatioLocked="false" aspectRatioBackup="-1.0" description="">
<MobileBookMark useBookMark="false" bookMarkName="chart0" frozen="false"/>
<PrivilegeControl/>
</WidgetAttr>
<FollowingTheme borderStyle="false"/>
<Margin top="0" left="0" bottom="0" right="0"/>
<Border>
<border style="0" borderRadius="0" type="0" borderStyle="0">
<color>
<FineColor color="-723724" hor="-1" ver="-1"/>
</color>
</border>
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
<InnerWidget class="com.fr.form.ui.ChartEditor">
<WidgetName name="chart0"/>
<WidgetID widgetID="4b6a42fa-c1fe-413a-9bf8-eecbb5495de2"/>
<WidgetAttr aspectRatioLocked="false" aspectRatioBackup="-1.0" description="">
<MobileBookMark useBookMark="false" bookMarkName="" frozen="false"/>
<PrivilegeControl/>
</WidgetAttr>
<FollowingTheme borderStyle="true"/>
<Margin top="0" left="11" bottom="11" right="11"/>
<Border>
<border style="0" borderRadius="0" type="1" borderStyle="0"/>
<WidgetTitle>
<O>
<![CDATA[銷量概況]]></O>
<FRFont name="simhei" style="1" size="128"/>
<Position pos="2"/>
<Background name="ColorBackground">
<color>
<FineColor color="-10243346" hor="-1" ver="-1"/>
</color>
</Background>
<BackgroundOpacity opacity="0.04"/>
<InsetImage padding="4" insetRelativeTextLeft="true" insetRelativeTextRight="false" name="ImageBackground" layout="3">
<FineImage fm="png" imageId="__ImageCache__9BDAD1A694F2AE09931BEB5B979DA1F5">
<IM>
<![CDATA[lO<9(kN.ld@UNU%p%320!n&&RXMhpZ,a0ckg]Ag[)Sh?$H'm#O$mX9@nDg03/<C4dC'hs7\:U
CrUFIA*cmN+n1!@hUKFS0]AXkEO<r!!~
]]></IM>
</FineImage>
</InsetImage>
</WidgetTitle>
<Background name="ColorBackground">
<color>
<FineColor color="-10243346" hor="-1" ver="-1"/>
</color>
</Background>
<Alpha alpha="0.04"/>
</Border>
<LayoutAttr selectedIndex="0"/>
<ChangeAttr enable="false" changeType="button" timeInterval="5" showArrow="true">
<TextAttr>
<Attr alignText="0" themed="false">
<FRFont name="PingFangSC-Regular" style="0" size="96">
<foreground>
<FineColor color="-1" hor="-1" ver="-1"/>
</foreground>
</FRFont>
</Attr>
</TextAttr>
<buttonColor>
<FineColor color="-6710887" hor="-1" ver="-1"/>
</buttonColor>
<carouselColor>
<FineColor color="-8421505" hor="-1" ver="-1"/>
</carouselColor>
</ChangeAttr>
<Chart name="預設" chartClass="com.fr.plugin.chart.vanchart.VanChart">
<Chart class="com.fr.plugin.chart.vanchart.VanChart">
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr gradientType="normal" shadow="false" autoBackground="false" themed="true">
<gradientStartColor>
<FineColor color="-12146441" hor="-1" ver="-1"/>
</gradientStartColor>
<gradientEndColor>
<FineColor color="-9378161" hor="-1" ver="-1"/>
</gradientEndColor>
</Attr>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor autoColor="false" themed="false">
<borderColor>
<FineColor color="-1118482" hor="-1" ver="-1"/>
</borderColor>
</newColor>
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
<Attr gradientType="normal" shadow="false" autoBackground="false" themed="false">
<gradientStartColor>
<FineColor color="-12146441" hor="-1" ver="-1"/>
</gradientStartColor>
<gradientEndColor>
<FineColor color="-9378161" hor="-1" ver="-1"/>
</gradientEndColor>
</Attr>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor autoColor="false" themed="false">
<borderColor>
<FineColor color="-6908266" hor="-1" ver="-1"/>
</borderColor>
</newColor>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<O>
<![CDATA[新建圖表標題]]></O>
<TextAttr>
<Attr alignText="0" themed="true">
<FRFont name="simhei" style="1" size="120">
<foreground>
<FineColor color="-13945534" hor="-1" ver="-1"/>
</foreground>
</FRFont>
</Attr>
</TextAttr>
<TitleVisible value="false" position="0"/>
</Title>
<Attr4VanChart useHtml="false" floating="false" x="0.0" y="0.0" limitSize="false" maxHeight="15.0"/>
</Title4VanChart>
<SwitchTitle>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr gradientType="normal" shadow="false" autoBackground="false" themed="false">
<gradientStartColor>
<FineColor color="-12146441" hor="-1" ver="-1"/>
</gradientStartColor>
<gradientEndColor>
<FineColor color="-9378161" hor="-1" ver="-1"/>
</gradientEndColor>
</Attr>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor autoColor="false" themed="false">
<borderColor>
<FineColor color="-16777216" hor="-1" ver="-1"/>
</borderColor>
</newColor>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<O>
<![CDATA[新建圖表標題]]></O>
</SwitchTitle>
<Plot class="com.fr.plugin.chart.column.VanChartColumnPlot">
<VanChartPlotVersion version="20170715"/>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr gradientType="normal" shadow="false" autoBackground="false" themed="false">
<gradientStartColor>
<FineColor color="-12146441" hor="-1" ver="-1"/>
</gradientStartColor>
<gradientEndColor>
<FineColor color="-9378161" hor="-1" ver="-1"/>
</gradientEndColor>
</Attr>
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
<Attr alignText="0" themed="false"/>
</TextAttr>
<AttrToolTipContent>
<TextAttr>
<Attr alignText="0" themed="false"/>
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
<Background name="ColorBackground">
<color>
<FineColor color="-16777216" hor="-1" ver="-1"/>
</color>
</Background>
<Attr gradientType="normal" shadow="true" autoBackground="false" themed="false">
<gradientStartColor>
<FineColor color="-12146441" hor="-1" ver="-1"/>
</gradientStartColor>
<gradientEndColor>
<FineColor color="-9378161" hor="-1" ver="-1"/>
</gradientEndColor>
</Attr>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="2"/>
<newColor autoColor="false" themed="false">
<borderColor>
<FineColor color="-16777216" hor="-1" ver="-1"/>
</borderColor>
</newColor>
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
<newColor autoColor="true" themed="false">
<borderColor>
<FineColor color="-1" hor="-1" ver="-1"/>
</borderColor>
</newColor>
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
<Attr gradientType="normal" shadow="false" autoBackground="false" themed="false">
<gradientStartColor>
<FineColor color="-12146441" hor="-1" ver="-1"/>
</gradientStartColor>
<gradientEndColor>
<FineColor color="-9378161" hor="-1" ver="-1"/>
</gradientEndColor>
</Attr>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor autoColor="false" themed="false">
<borderColor>
<FineColor color="-3355444" hor="-1" ver="-1"/>
</borderColor>
</newColor>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<Attr position="4" visible="true" themed="true"/>
<FRFont name="simhei" style="0" size="88">
<foreground>
<FineColor color="-8747891" hor="-1" ver="-1"/>
</foreground>
</FRFont>
</Legend>
<Attr4VanChart floating="false" x="0.0" y="0.0" layout="aligned" customSize="false" maxHeight="30.0" isHighlight="true"/>
</Legend4VanChart>
<DataSheet>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr gradientType="normal" shadow="false" autoBackground="false" themed="false">
<gradientStartColor>
<FineColor color="-12146441" hor="-1" ver="-1"/>
</gradientStartColor>
<gradientEndColor>
<FineColor color="-9378161" hor="-1" ver="-1"/>
</gradientEndColor>
</Attr>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="1" isRoundBorder="false" roundRadius="0"/>
<newColor autoColor="false" themed="true">
<borderColor>
<FineColor color="-1578256" hor="-1" ver="-1"/>
</borderColor>
</newColor>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<Attr isVisible="false" themed="true"/>
<FRFont name="simhei" style="0" size="80">
<foreground>
<FineColor color="-8747891" hor="-1" ver="-1"/>
</foreground>
</FRFont>
<Format class="com.fr.base.CoreDecimalFormat" roundingMode="6">
<![CDATA[#.##]]></Format>
</DataSheet>
<DataProcessor class="com.fr.base.chart.chartdata.model.NormalDataModel"/>
<newPlotFillStyle>
<AttrFillStyle>
<AFStyle colorStyle="1"/>
<FillStyleName fillStyleName=""/>
<isCustomFillStyle isCustomFillStyle="true"/>
<PredefinedStyle themed="true"/>
<ColorList>
<OColor>
<colvalue>
<FineColor color="-12999178" hor="-1" ver="-1"/>
</colvalue>
</OColor>
<OColor>
<colvalue>
<FineColor color="-7287309" hor="-1" ver="-1"/>
</colvalue>
</OColor>
<OColor>
<colvalue>
<FineColor color="-600992" hor="-1" ver="-1"/>
</colvalue>
</OColor>
<OColor>
<colvalue>
<FineColor color="-422004" hor="-1" ver="-1"/>
</colvalue>
</OColor>
<OColor>
<colvalue>
<FineColor color="-8595761" hor="-1" ver="-1"/>
</colvalue>
</OColor>
<OColor>
<colvalue>
<FineColor color="-7236949" hor="-1" ver="-1"/>
</colvalue>
</OColor>
<OColor>
<colvalue>
<FineColor color="-8873759" hor="-1" ver="-1"/>
</colvalue>
</OColor>
<OColor>
<colvalue>
<FineColor color="-8935739" hor="-1" ver="-1"/>
</colvalue>
</OColor>
</ColorList>
</AttrFillStyle>
</newPlotFillStyle>
<VanChartPlotAttr isAxisRotation="false" categoryNum="1"/>
<GradientStyle>
<Attr gradientType="gradual">
<startColor>
<FineColor color="-12146441" hor="-1" ver="-1"/>
</startColor>
<endColor>
<FineColor color="-9378161" hor="-1" ver="-1"/>
</endColor>
</Attr>
</GradientStyle>
<VanChartRectanglePlotAttr vanChartPlotType="normal" isDefaultIntervalBackground="true"/>
<XAxisList>
<VanChartAxis class="com.fr.plugin.chart.attr.axis.VanChartAxis">
<Title>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr gradientType="normal" shadow="false" autoBackground="false" themed="false">
<gradientStartColor>
<FineColor color="-12146441" hor="-1" ver="-1"/>
</gradientStartColor>
<gradientEndColor>
<FineColor color="-9378161" hor="-1" ver="-1"/>
</gradientEndColor>
</Attr>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor autoColor="false" themed="false">
<borderColor>
<FineColor color="-16777216" hor="-1" ver="-1"/>
</borderColor>
</newColor>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<O>
<![CDATA[]]></O>
<TextAttr>
<Attr alignText="0" themed="true">
<FRFont name="simhei" style="0" size="88">
<foreground>
<FineColor color="-8747891" hor="-1" ver="-1"/>
</foreground>
</FRFont>
</Attr>
</TextAttr>
<TitleVisible value="true" position="0"/>
</Title>
<newAxisAttr isShowAxisLabel="true"/>
<AxisLineStyle AxisStyle="1" MainGridStyle="1"/>
<newLineColor themed="true">
<lineColor>
<FineColor color="-2171168" hor="-1" ver="-1"/>
</lineColor>
</newLineColor>
<AxisPosition value="3"/>
<TickLine201106 type="2" secType="0"/>
<ArrowShow arrowShow="false"/>
<TextAttr>
<Attr alignText="0" themed="true">
<FRFont name="simhei" style="0" size="88">
<foreground>
<FineColor color="-8747891" hor="-1" ver="-1"/>
</foreground>
</FRFont>
</Attr>
</TextAttr>
<AxisLabelCount value="=1"/>
<AxisRange/>
<AxisUnit201106 isCustomMainUnit="false" isCustomSecUnit="false" mainUnit="=0" secUnit="=0"/>
<ZoomAxisAttr isZoom="false"/>
<axisReversed axisReversed="false"/>
<VanChartAxisAttr mainTickLine="2" secTickLine="0" axisName="X軸" titleUseHtml="false" labelDisplay="interval" autoLabelGap="true" limitSize="false" maxHeight="15.0" commonValueFormat="true" isRotation="false" isShowAxisTitle="false" displayMode="0" gridLineType="NONE"/>
<HtmlLabel customText="function(){ return this; }" useHtml="false" isCustomWidth="false" isCustomHeight="false" width="50" height="50"/>
<alertList/>
<styleList>
<VanChartAxisLabelStyle class="com.fr.plugin.chart.attr.axis.VanChartAxisLabelStyle">
<VanChartAxisLabelStyleAttr showLabel="true" labelDisplay="interval" autoLabelGap="true"/>
<TextAttr>
<Attr alignText="0" themed="true">
<FRFont name="simhei" style="0" size="88">
<foreground>
<FineColor color="-8747891" hor="-1" ver="-1"/>
</foreground>
</FRFont>
</Attr>
</TextAttr>
<AxisLabelCount value="=0"/>
</VanChartAxisLabelStyle>
</styleList>
<customBackgroundList/>
</VanChartAxis>
</XAxisList>
<YAxisList>
<VanChartAxis class="com.fr.plugin.chart.attr.axis.VanChartValueAxis">
<Title>
<GI>
<AttrBackground>
<Background name="NullBackground"/>
<Attr gradientType="normal" shadow="false" autoBackground="false" themed="false">
<gradientStartColor>
<FineColor color="-12146441" hor="-1" ver="-1"/>
</gradientStartColor>
<gradientEndColor>
<FineColor color="-9378161" hor="-1" ver="-1"/>
</gradientEndColor>
</Attr>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="0" isRoundBorder="false" roundRadius="0"/>
<newColor autoColor="false" themed="false">
<borderColor>
<FineColor color="-16777216" hor="-1" ver="-1"/>
</borderColor>
</newColor>
</AttrBorder>
<AttrAlpha>
<Attr alpha="1.0"/>
</AttrAlpha>
</GI>
<O>
<![CDATA[]]></O>
<TextAttr>
<Attr rotation="-90" alignText="0" themed="true">
<FRFont name="simhei" style="0" size="88">
<foreground>
<FineColor color="-8747891" hor="-1" ver="-1"/>
</foreground>
</FRFont>
</Attr>
</TextAttr>
<TitleVisible value="true" position="0"/>
</Title>
<newAxisAttr isShowAxisLabel="true"/>
<AxisLineStyle AxisStyle="0" MainGridStyle="1"/>
<newLineColor themed="true" mainGridPredefinedStyle="true">
<mainGridColor>
<FineColor color="-1578256" hor="-1" ver="-1"/>
</mainGridColor>
<lineColor>
<FineColor color="-2171168" hor="-1" ver="-1"/>
</lineColor>
</newLineColor>
<AxisPosition value="2"/>
<TickLine201106 type="2" secType="0"/>
<ArrowShow arrowShow="false"/>
<TextAttr>
<Attr alignText="0" themed="true">
<FRFont name="simhei" style="0" size="88">
<foreground>
<FineColor color="-8747891" hor="-1" ver="-1"/>
</foreground>
</FRFont>
</Attr>
</TextAttr>
<AxisLabelCount value="=1"/>
<AxisRange/>
<AxisUnit201106 isCustomMainUnit="false" isCustomSecUnit="false" mainUnit="=0" secUnit="=0"/>
<ZoomAxisAttr isZoom="false"/>
<axisReversed axisReversed="false"/>
<VanChartAxisAttr mainTickLine="0" secTickLine="0" axisName="Y軸" titleUseHtml="false" labelDisplay="interval" autoLabelGap="true" limitSize="false" maxHeight="15.0" commonValueFormat="true" isRotation="false" isShowAxisTitle="false" displayMode="0" gridLineType="dashed"/>
<HtmlLabel customText="function(){ return this; }" useHtml="false" isCustomWidth="false" isCustomHeight="false" width="50" height="50"/>
<alertList/>
<styleList/>
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
<VanChartColumnPlotAttr seriesOverlapPercent="20.0" categoryIntervalPercent="20.0" fixedWidth="false" columnWidth="15" filledWithImage="false" isBar="false"/>
</Plot>
<ChartDefinition>
<NormalReportDataDefinition>
<Series>
<SeriesDefinition>
<SeriesName>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=report0~B2]]></Attributes>
</O>
</SeriesName>
<SeriesValue>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=report0~D2]]></Attributes>
</O>
</SeriesValue>
</SeriesDefinition>
</Series>
<Category>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=report0~A2]]></Attributes>
</O>
</Category>
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
</NormalReportDataDefinition>
</ChartDefinition>
</Chart>
<UUID uuid="1fc66a75-27e3-4095-a607-0f4ae6c36532"/>
<tools hidden="true" sort="true" export="true" fullScreen="true"/>
<VanChartZoom>
<zoomAttr zoomVisible="false" zoomGesture="true" zoomResize="true" zoomType="xy" controlType="zoom" categoryNum="8" scaling="0.3"/>
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
<Attr alignText="0" themed="false"/>
</TextAttr>
<AttrToolTipContent>
<TextAttr>
<Attr alignText="0" themed="false"/>
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
<Attr enable="true"/>
</AttrTooltipChangedValueFormat>
</changedValue>
<HtmlLabel customText="" useHtml="false" isCustomWidth="false" isCustomHeight="false" width="50" height="50"/>
</AttrToolTipContent>
<GI>
<AttrBackground>
<Background name="ColorBackground">
<color>
<FineColor color="-1" hor="-1" ver="-1"/>
</color>
</Background>
<Attr gradientType="normal" shadow="false" autoBackground="false" themed="false">
<gradientStartColor>
<FineColor color="-12146441" hor="-1" ver="-1"/>
</gradientStartColor>
<gradientEndColor>
<FineColor color="-9378161" hor="-1" ver="-1"/>
</gradientEndColor>
</Attr>
</AttrBackground>
<AttrBorder>
<Attr lineStyle="1" isRoundBorder="false" roundRadius="4"/>
<newColor autoColor="false" themed="false">
<borderColor>
<FineColor color="-15395563" hor="-1" ver="-1"/>
</borderColor>
</newColor>
</AttrBorder>
<AttrAlpha>
<Attr alpha="0.8"/>
</AttrAlpha>
</GI>
</AttrTooltip>
</refreshMoreLabel>
<ThemeAttr>
<Attr darkTheme="false"/>
</ThemeAttr>
</Chart>
<ChartMobileAttrProvider zoomOut="0" zoomIn="2" allowFullScreen="true" functionalWhenUnactivated="false"/>
<MobileChartCollapsedStyle class="com.fr.form.ui.mobile.MobileChartCollapsedStyle">
<collapseButton showButton="true" foldedHint="" unfoldedHint="" defaultState="0">
<color>
<FineColor color="-6710887" hor="-1" ver="-1"/>
</color>
</collapseButton>
<collapsedWork value="false"/>
</MobileChartCollapsedStyle>
</InnerWidget>
<BoundsAttr x="0" y="36" width="480" height="504"/>
</Widget>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.ui.Label">
<WidgetName name="Title_chart0"/>
<WidgetAttr aspectRatioLocked="false" aspectRatioBackup="-1.0" description="">
<MobileBookMark useBookMark="false" bookMarkName="" frozen="false"/>
<PrivilegeControl/>
</WidgetAttr>
<widgetValue>
<O>
<![CDATA[銷量概況]]></O>
</widgetValue>
<LabelAttr verticalcenter="true" textalign="2" autoline="true"/>
<FRFont name="simhei" style="1" size="128"/>
<Background name="ColorBackground">
<color>
<FineColor color="-10243346" hor="-1" ver="-1"/>
</color>
</Background>
<BackgroundOpacity opacity="0.04"/>
<InsetImage padding="4" insetRelativeTextLeft="true" insetRelativeTextRight="false" name="ImageBackground" layout="3">
<FineImage fm="png" imageId="__ImageCache__9BDAD1A694F2AE09931BEB5B979DA1F5">
<IM>
<![CDATA[lO<9(kN.ld@UNU%p%320!n&&RXMhpZ,a0ckg]Ag[)Sh?$H'm#O$mX9@nDg03/<C4dC'hs7\:U
CrUFIA*cmN+n1!@hUKFS0]AXkEO<r!!~
]]></IM>
</FineImage>
</InsetImage>
<border style="0">
<color>
<FineColor color="-16777216" hor="-1" ver="-1"/>
</color>
</border>
</InnerWidget>
<BoundsAttr x="0" y="0" width="480" height="36"/>
</Widget>
<ShowBookmarks showBookmarks="false"/>
</InnerWidget>
<BoundsAttr x="480" y="0" width="480" height="540"/>
</Widget>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.ui.container.WTitleLayout">
<WidgetName name="report0"/>
<WidgetAttr aspectRatioLocked="false" aspectRatioBackup="-1.0" description="">
<MobileBookMark useBookMark="false" bookMarkName="report0" frozen="false"/>
<PrivilegeControl/>
</WidgetAttr>
<FollowingTheme borderStyle="false"/>
<Margin top="0" left="0" bottom="0" right="0"/>
<Border>
<border style="0" borderRadius="0" type="0" borderStyle="0">
<color>
<FineColor color="-723724" hor="-1" ver="-1"/>
</color>
</border>
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
<WidgetName name="report0"/>
<WidgetID widgetID="d83ae6f9-1d5a-45c5-97ca-84a40212c3dd"/>
<WidgetAttr aspectRatioLocked="false" aspectRatioBackup="-1.0" description="">
<MobileBookMark useBookMark="false" bookMarkName="" frozen="false"/>
<PrivilegeControl/>
</WidgetAttr>
<FollowingTheme borderStyle="true"/>
<Margin top="0" left="11" bottom="11" right="11"/>
<Border>
<border style="0" borderRadius="0" type="1" borderStyle="0"/>
<WidgetTitle>
<O>
<![CDATA[銷量明細]]></O>
<FRFont name="simhei" style="1" size="128"/>
<Position pos="2"/>
<Background name="ColorBackground">
<color>
<FineColor color="-10243346" hor="-1" ver="-1"/>
</color>
</Background>
<BackgroundOpacity opacity="0.04"/>
<InsetImage padding="4" insetRelativeTextLeft="true" insetRelativeTextRight="false" name="ImageBackground" layout="3">
<FineImage fm="png" imageId="__ImageCache__9BDAD1A694F2AE09931BEB5B979DA1F5">
<IM>
<![CDATA[lO<9(kN.ld@UNU%p%320!n&&RXMhpZ,a0ckg]Ag[)Sh?$H'm#O$mX9@nDg03/<C4dC'hs7\:U
CrUFIA*cmN+n1!@hUKFS0]AXkEO<r!!~
]]></IM>
</FineImage>
</InsetImage>
</WidgetTitle>
<Background name="ColorBackground">
<color>
<FineColor color="-10243346" hor="-1" ver="-1"/>
</color>
</Background>
<Alpha alpha="0.04"/>
</Border>
<Refresh class="com.fr.plugin.reportRefresh.ReportExtraRefreshAttr" pluginID="com.fr.plugin.reportRefresh.v11" plugin-version="1.5.6">
<Refresh state="0" interval="0.0" customClass="false"/>
</Refresh>
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
<C c="0" r="0" s="0">
<O>
<![CDATA[地區]]></O>
<PrivilegeControl/>
<Expand>
<cellSortAttr/>
</Expand>
</C>
<C c="1" r="0" s="0">
<O>
<![CDATA[銷售員]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="2" r="0" s="0">
<O>
<![CDATA[產品類型]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="3" r="0" s="0">
<O>
<![CDATA[銷量]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="0" r="1" s="1">
<O t="DSColumn">
<Attributes dsName="ds1" columnName="地區"/>
<Condition class="com.fr.data.condition.CommonCondition">
<CNUMBER>
<![CDATA[0]]></CNUMBER>
<CNAME>
<![CDATA[地區]]></CNAME>
<Compare op="0">
<Parameter>
<Attributes name="地區"/>
<O>
<![CDATA[華東]]></O>
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
<Expand dir="0"/>
</C>
<C c="1" r="1" s="1">
<O t="DSColumn">
<Attributes dsName="ds1" columnName="銷售員"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand dir="0"/>
</C>
<C c="2" r="1" s="1">
<O t="DSColumn">
<Attributes dsName="ds1" columnName="產品類型"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand dir="0"/>
</C>
<C c="3" r="1" s="1">
<O t="DSColumn">
<Attributes dsName="ds1" columnName="銷量"/>
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
</CellElementList>
<ReportAttrSet>
<ReportSettings headerHeight="0" footerHeight="0">
<PaperSetting/>
<FollowingTheme background="true"/>
<Background name="ColorBackground">
<color>
<FineColor color="-1" hor="-1" ver="-1"/>
</color>
</Background>
</ReportSettings>
</ReportAttrSet>
</FormElementCase>
<StyleList>
<Style style_name="表頭" full="true" border_source="-1" horizontal_alignment="0" imageLayout="1">
<FRFont name="simhei" style="1" size="96">
<foreground>
<FineColor color="-1" hor="-1" ver="-1"/>
</foreground>
</FRFont>
<Background name="ColorBackground">
<color>
<FineColor color="-7880449" hor="0" ver="1"/>
</color>
</Background>
<Border/>
</Style>
<Style style_name="正文" full="true" border_source="-1" horizontal_alignment="0" imageLayout="1">
<FRFont name="simhei" style="0" size="88">
<foreground>
<FineColor color="-9276814" hor="-1" ver="-1"/>
</foreground>
</FRFont>
<Background name="NullBackground"/>
<Border>
<Bottom style="1">
<color>
<FineColor color="-2500135" hor="-1" ver="-1"/>
</color>
</Bottom>
</Border>
</Style>
</StyleList>
<heightRestrict heightrestrict="false"/>
<heightPercent heightpercent="0.75"/>
<IM>
<![CDATA[m@*u<e,00c=6ZYNS<MtW@\#R)ksVITZft#@1b+4#O<PI'k%[spEE);G3L$c/jJ"DoR2Hqm93
5%E-6#Uq0JgU!f[Y2kkOZ64^43rmqcgi%G2)>2]A>+&c5@9K7j8")9hoe1JkIp+adr,6e^a>]A
2%NYiTZqLIMFh9S[UD`%Ar&>/d=@7HG*]AT9_3]Aj)-BAGR)-`OkmUahE"_$\n>U<p^]AhHEhJf
-%mZ.PSAmf^'_0g0YIi1@,QZE]ArX)g4RsB#>U4^OE^Z7@Dag\lW5]Aa(Nap_Z%^r@D)We[h30
6ecUoEP5K,<Kmk2@*I8e:]A%*#r,>OIN9@%r3A$n7X_)k!1D`g?if'Ru3H!<<^Z;OC?h2-6cS
a1-)`:q%:Fo,3`Agbo/*_+cG,rK/T?dc@+V>CbMGs,I?P\"1LTR-<d)"SnC*Af+s3%V;eIhD
uHF@ON%TQqG(\2>J6jV3E+k?Oe=.NV4E$$eYXi^Q[S*SKu:se">$`ADbtKXAI'p,2>KGA=Pl
N\o<hU4B^QtR<sTD;RtnQ0.TqUmTeQ]A65G!$09OtSh@h<S!YG\-E&>+%O5.U=Ch\*@hqH/LU
(C">ELA5([obi<M<6':8f:VH39qk#o<;[l9,%).GKl$BcOu[P/ag.+Xj):MBq.[d>uW/O(&$
&ihr.r9>4JuFf0YST@P2S=b(.YD1DmZjBSM4`hJ_7P&*-9Ji0:ddJFZ\'2EWH!`<iK8DKS/X
-#Lum%L6HM4tii68f'A$M\8m5k0PamjHqLg"+,#o-:J5E5EUI44,99gc>sA^)t710#]AfdGbq
MUo,tBurVphG1+-;)bS7n9dM7Xl<L7k"1e0OJ:W3,8cVRo/Q7E$RKEE8D$1l.#HE0(FuD.g^
g-Scp;8#,u*m0uti?`>sK7:V>",/h;>3fYDF_VsC5bpVLae1mueHX5Welm`lGQ)$,:%Jh'79
B!A/Ks(XU[tOY"QB#MVlNpnQ"6o!IOaScKAaYd+`sdlOs"5kq9.Ct.4=bmbI\A_c,27'bN8%
]A'4^=#i5eZZI?0lCH;?U"8>F*0T0_o'JTfYK.+Fg`PnH>!aGF`t8@>99"+?$?BIrB-*`2Z7l
oKoqrd=$IW$*S`g5)b`1P`0s0:J$sOVMX->;W!rZL>O:*a.0k2.9l8hCM6OcKW(6\Pn+-tpX
PMD[$n?%>YqBpRcCnfU!WU%c2OGV"%.WPCRG!lB!`:e$bQC'"9<CP+NeJ*(LDE\!c#P4V?7X
'$V/@Ym5O9`&&oI1B`m>pCj%*li.h.R7&QT.FWICOg@!?+HqGmVlJ[!boX`36bL>J+VB=E@S
k15^m,9QUe?+l<n-<@u]AFpUPonat(0Slfu`KHjHOI`gS=,omgH+(--j8:")-;<qg9^R=G<tO
fJN^6GpD^EIdGO-O`E+HF`UEr_7is`G.&..N;LM?'__6^A@em[#+^4!Bb\^40Vbf%p-i0jK<
*]A8'_Sf$FVp:>E/(>U:S=IurWXX8'+N#CF4('=2qMp(9-Yeu/6*=Z5,NDIC!9AFql1mU`qYT
eJ=>-%5L!!%r_raabJ4u;i.gL+t[mUH5=Ya$Z]A,IGq%28d]A$bqMjG\4=9TDRQ?m>f?#0Ou[.
Ne8DnRd+>T&@r(EU+6T5I]A"i;Wk3%cdbVC"#G&/)2-8*!`*U[;6bAk7=;u7DO^kB5"JY939.
OGV?lSkE['9+Bkp)TXeQ&m;@qUW;bS"\Fa6Ti,BWA\!QEP`!/BV12Nnd$^/4>*?T^itrQO`k
/.8@7!*RuLAG@EK:im8U<qgV"^9Jn7(>p>C)npuh\4@?jH!2816g`T><='cI\<J_dO7E.r^-
/)*T:6u'/HQSdr"cS/dk,ut*QULd2SR2+j6oFNGihk_ATIiH3[g2*M[EoX=KjYGlc2>>9]AU$
(D-klSKnN_?'2rEo3nR>;ef4]A_`7Lcb%CSoi5Wcl9%KfZ2a[Erfb;6D7>sE)`@X$j&27U\?5
5kU+C<qgP\"Z\5qRZMi@0#N4\RbB<?m]A/C<)^$>)W\\l[T<-$-EU[0s`V8J4UB8j8K?M]A,P#
,CKlZtjojS6kljmMh;-j.DN7em'rnQ]AG03Gms&n.@+,jN1DA"*efOibl`G!!4J#uB3'PWm??
JtT@o=`2o``Chj9]A=A>R9&hM3TJl*r]A,@KuO9`Jo"7@*F&fDAt,KB?<$c`5a]AShGC8'\.U<?
r<)"P?ks1(c*rUX&;%"C@g#HVQh)HIkEg$DM;(^);>'P40hu6TKb"K<+[o8,KILO,*JGA.]AK
J@+]A_5Ifhh:rOb>.&[OPm`hRbS^[$"`KQ*qAr>lJ!%AA]A/BFds12VZQhAPJu_8-IQo=C_rUo
T)<p(7/V9h"+cDH`>1jR'3+?67d8TAQDaA0j!<<p@*BonV`]Aj_<Kg#_rA+&"%DT+6+4V%s)=
4;5f[]A@_UhJ2+s3nJT0qAeden+pCukXF%R]AjIr2RcTkcLYoQf8X0-;'Z8Fr^:3XhVtXXiib^
:U"Go0Obt\;6$7Z'hhs!$n0`r4Ns#0j,kp>\A&j[5TBXE6I[(P2Jq&iHq4L6TGGIh(B&$?MJ
"V$DCL2=Ia/3QZ]Aobsf9lWFEQ=rl?s\,GCaHjQd<!>jZXId%\6[Pbdn-\ENWf.'L;A+U!NC8
A_jX'QR8<i9]A;iR>jqjl,@,-\TfH63g[QR0@-PFJfV\!./DP#s'j?*s$mV=D'L<\^UPu7tO6
%LXY:CI`Z<eo/h9U@t=qSD,T1<KKV\NZYWgP(S!$1:I$Zd/MG05"Zu1Y,!g&>79`jX13+%"F
_#aOTpOf[FR>7tFbHY7#YoP>fD%o->#4bQiSK^q4CSd0p4Z"ZIqCHZ]A(k6<4XJn_I$ZW(Ic'
%6Ro*2LQ&$^)`%ti;JZ?,5iXmQL`m5?7gq_:)MO)$=<#_Yt@JL:JONsd(Cs%62lObNSPFe&<
55cpHr74]A;&tJ_[jkAH]As0o55@tW'RZqFBhRH?$bn(%O?A8$^+Y*!.9Ajpc5E%3[p#JsX0H1
/W.Xu42N7(4b/g_gAaqR_)1c-<`Jj+%#4'XbA`#[_rA\;j/.E#_4lQG.-]A06&F4q5(Esj(Pi
Q<V3u5_]ACkM3[7)*D>Q3PWc3Zj(O%sJOH\[hj\gt9mQ:X-i]AkW$?.FXa#`J-!d*PqH?Y4:YT
f%nti]A6MnYc[?0;bmX@C>@p&=4cNehFIGN^*B69O4/olDd,b#%:UhrNk)-TFq2Vhg$]ANV;)L
A]A4n.S+I0>R(p3.,+]At"p[MPJ+Uqn<96WNFaD+kH\oO+]Aj%m,>o^6%>IZ,^uepm:W8<b+Q6C
8XXTr'?,ami:+TUQ`]AYJ,K*tbU&R2S=H*:9^T.h3^Jl5)IY==l2+PCu03Le]AL_PXXhR>sHq!
a]Ap\E8?pAFhid.!.PcjpIPs=(rlR+a:olX`REI>f`PiTSjZ]ALaVJ5e-V.ElUq5sc&QZ:DenY
6kpI!&.mj.&WM.rml*HcF"W_j[W,\O#YKCd`*W,<8Mu)<p\0GmU]AFXipY5$uiGuNVgiLRT%$
6BVef"=%ESFqONC0"-8-qOXORTE=;WHPY-_uo!H)GUYZ;m\[KNkrVKDu2IpDHj)99\.XfXY%
gp8(Tr1X[.GB4<2K!D7fHchDkG1gYhS1`(+M)Aps7qqcSD-L2F#R?qB['&K(gZfpFU[e2hRO
gYi&u"^>^rj"OG42Ije11@OQ5V<WGcZWS/YOPJMM,C8>%?5C.+l]AOq[g+14ulFM<?KImPJoZ
_pK*B$p`ZPa/RPH(k[glJ#`n$Vk&$M^SM5!4(^SAtmU2poMr*r`$2j"d(I'0Df&me<\6gU")
c4^V4\Etd"S8.duUh_Y`nka9-Aq;XGSA8sdbM4B/3llp\_nW,;uoMAFl+"U@8k9`^rS&2M!O
t2OuT?\2%\0(uFCTB[$lYYBUBjVTn:F<_Z/ht$uXBF*`9;4.Dmi:2n0)QR<5sXk)%49+r4Qs
e\9qc$ACo3++iiJ1K3.@t#>L+:V>OoRPEcY$KbFnl/U'7uS&*)-sD`*-gc<ZnOrEaN3Nk[MP
/%]A>Xl!%Njo5K8`rPj0!+D;,0HK\tN=K^8%?4qCt[[%\Er?YRupMogHihqEn3bip0;0*,KVm
j?VXm!hRmJ5?I&21UIWW/HWL8tIe9cMFYPXB"_/0\U1W,1VHos(&W^a\<;:tHI7(s=IP/;!/
&j^:=HLhK+l]AN+?/FUeR1`]AnHm/i\<<8G%H>2A%!KD/u99dl?EVUKi/kg,q`49aF?bQj&$8K
eS/4HG:\g]A-gDKBjY"Op"+)o8`!-Z'%O]A!_&r]A#eGJ_60DY;cJrf,)h6iMK^\HnZQ!@PNO'r
)WS8B-/:>@CTWaYGi-&m'W^#Cq]ARhfXi&UU:sbEB)3_u,H]A!oFjc`+t-Xb9aXlp4p5,&VJ/Z
?[^/#mJ7-1a/Z%u@"]A%mdJ8H'N>\pc<i=t[g^5JIaHG/DT0")OP40<8eM)"JJ]A>?,B\1F4!r
rJ,ar1$+^7lpqD62%]A[3ssg-hL(jZBtCd=\]A<(j3g@_KI-tRD3kr@r@$&+^@T83i/:>nP_b6
p4iN*5q8Vu.Brc_Io-c-$qR7,&SM,@lZCgqk3jkLj:.ps:]A[$KVCe!"UPH*37FO6%2I-1FG1
8B9^2\)-J?MkObmD\u6\MlG#gEgB28;<N9k2KhK@LB5[n%j0ar"RW0.G]A/Fcuc>LU-=le]AK)
g$i3*kE;:>hKW_:YprXg6X_=rF<6@0L94PH1`W^-M"pY[=f\M<Z8q@';]AGBb42E+j'7QM<;O
-BhXu1p8[i34"kBfQ$MF3#cD]AN,AFd!@9Tk]A@,%&e>pR/mX8Q%"SO$F;TK=:L+3B3\BIlk8Y
%Jgd8=mAnm,=D'&@V6PYo=?IR&R\';HDjo#mS:6i1O_hYt)kY?DH2osI%GJVXG)f8jQnSC&%
04K)-`[hC[2A=U!tIb[><F(Q,bPHMVRVr"(Dk*mc@"CUH#K+tA_\Vl<aOa6;@l3N!0&-0hZ/
ecohhq3QUJ=:!&40@j3>B"cp\QbQ(EMCLG<]AYOmfnD]A>)YN4^Qq7Y&@5$:4S,0a%Us53IM$"
U]ABk*;)k#W_nY9Wf;6Fiin>r[/?>?`o4Q'hK*)P>)`AGh;1b<)qG8M!qt1TrX_O.tJD;jsMN
i_k$B\+('/f44C)BDu>;(S$aaCpdHd2G[mC_Lstf9\,G%[pA)%>j8B'C0/7\gma/Zn"IrX7&
ZH#]Ac#"i+6_[b=,_SlQMV#]AVr0b_(C0@3!rs?WXW203,0+sto/BZ5No6"T?2b3640V(t;H*8
#oJpV7&^DqO=cn^+Z8`,DL`Yt,CX%/XAFb\s/q4/IJ`gi06I%OG]AP<739HUPom>l,?'A\i:h
Q;qK_i8_56TSl3H!\7'N1JaZ-_FTU'fT3MdQ`k>jmp(?KU+9PK4*pWe*hT6nYi%)rc+pjLg%
k2X$/]A855UJ^:1h!D\"Jt,AZ;HJhN^'hD%_h-G57mDk>N)?IBH?Ao#I9&Q]Ar_o*;#X2l77ne
D6T$Q!76g9V+K4#ht"S4_ueXP;)s*.&JBbB#'(#WIN>eNck?r3AOY6^#dLkI\kbjp9.rKd#l
c5V#^M:q@sW;6Q[[<JC^.NHLe?W6$heaFaggt/3+QU#ZJH;?N]Ag#bq(3ZsQD9.):15FYic+-
5[#*9\=r%i4,.JTS/VCpfin-kncub\bK9ena:IWg&d3#Khl;P7\$d&2QUV.d)7bsnuH6u@Z#
UCEDifSKn;F8M@Gn7n(((d=!p11).)7&aH#?)/EKs@U=jBnfTb"IH&C,<qp(5V=?%`@T]A`ll
I;cItP5r2*)V>S9fDO"E5m@S=hsk*LGd.WIB/lp0F"["`qQ=_!a8G`tpGF+)cq<tFPTTVWki
aGN['&D)A`?JWW)"=g=6Q+6Z>RVKA5gRi-S>$[V*VNoC\:EOOp!.0SndoiSXaq/X)QK;hcl<
r[)76cYA[=57@?I6Ufj3A7sL%!fnm)<G,ij1NS3'&HPiMa6-bjG@N2'*Fqk\AlG:d:N%b9Es
_p;6iGdXKpuiT#b6$S,JBJ'RXsqoX+5a-ITI;_Vs_<;gipqd[EHW'OQ#-il>[jN'il8(B(<6
rYdUj%Z^:[0iXOaSW0[/W"q#Z2a`:#HfXgBph5q5gC9_6@T4tHdW?s$P@f9mj`F[m=*t?mLR
)@JO1pZcC^tu"B7B"h;7>!+7,CtZOm5[,W',S?VsqSRk#BAZ-s7cL?q7@?0j4p[^:=b6lFd/
iF43=7C'iC7b:KAkl-s'6BX/T:mcIE-ulE<P9NuPijio'f!_$#RV?U)R(oOZM<%F^O[_,Zd=
T,<4MKHodtT?!Mo.$S;DI`Soq"B=07%s;PbX.!h1Wi905^,_iohVs?%a2\4,)p#:uf[JYNKJ
=XO1XlXXJ?@a"QS^WgA#+n9'^X*=_^%s&t'f-L!)!*^5C;?P7?r[E2U^q33cn+aGn"JrZg;D
Vbmn*;3Ka]Ai*_MR=FBT2pY?D&l$iaV`hX9qG\C+FS&urCdm-U%oE`_7-@i71)]A1]AQ0]A%^Z(1
E;0fR#pd]AhlV`UX)cAK?3TBE(gO[:B32WbjYq<HO>;:AOXN]A09&m7>go7Yb3SR(nc84Np27h
RS(XQXH;]AO2QN_`e3h<[5NRN-lt#G\Ni0(@iDqFfj8<P^fUES'B+iiClRstHglg)<)2?U(@T
>2bIa/V.8fZ$H/N$MEq!kU;fI2F9Eb<Pc&=AGG`R#6(hTJ0gBGSeFAm=cngd1BEB9oBAVu?a
'2251uMJ3Bh>274AXHW\Lp%nuc9aR/aDS_>?Vs%+e/50YfjP[elpX[t"6]AjK%i=^8<3J51Yk
ih%-#"t?H.c2j=1h9(V0t`8K`^W7&1[IP(A:'AbYZBZJ7HWh/G+AJN^tPsDlEZXaU^$SMa0@
%OQn"_L*J9-jLY$<GUj[uTQ`$9D5nPtm!XB)aT^J!1lal(Ln3K\Odl5i'JnH%6#lJSMS`6N(
G[W'"a=YE-KdI%r<pm49UV1QEp--D&._C_#UlFHS6DRbdM.Npi.uHs\:=n;2R[eY=$NF2&Ye
7CP^D(4G2VF%o;/7HN]A&;i^7To`4Knd>,]A4OjehBc7bptYPCXH^#h//a4p)=-/@?t>Gkkjc6
\RqsLS.$;*G=0jMc?5p`)?T.M23omV<r8t<9l=08b+P08jE6Bq7U9Rd$3#$!>5/Z8XD/dF02
=-#GZX(m/Pk8E>D3=F=EF01hDJll/P)LFM@MtT$7->.D!1Jd9GHsBf'';/n09L=Y36]A5RXU%
o^+b9j*$(>fX4k.3+ag'><.;t*0]A[0dAZmF`XXlD2qJ`Nu$n"RS'4+QmrrPi]AKVpfp!.2gtl
9'7<&Z@/,UGkSp?=ithFns6%e3?@2N3"gq5qnl?n9Jlpd9R:\Y+.T3qiX.!"@gr`]A2,T9HUF
iNU;d@3=Q.J25UJ4W.`bt%d"64DjT@d!_'kbd8IK0u_%ReFT[f')t]AjJ#N=qMI!R?Of?Y_Cb
Ict2]A,&=-:nMFs2c3j7psdV/:!"3inHFj1D-j(gPJm(g.`]AM(S!QB*I:Ube%LjZ?8p&a"^#c
";3X\li#_,ook=:'Z%gr8aQaoW4Q/K/U.96GYA2NNOQgV2Up@,;-:YGY8;]A0:R0HfK9\e\J,
`4<(CEu&^M:WotI:Q`I&<e/g+K9mH\s3)4o-GJm^`m-=HQOlo-AtZOt$C\;STKX15_[pd^c5
2?e3BBdB/;"Di_coU9%Aog3h1cE?k5UF4Xb7E((H?GE/6j!\#qWK2oBF/5Dt$I'GMWSD&6DQ
=8J\g24]ALUT2q9\<a>6^+p`:]A9&$ls+B\Qu'Sqmg2XV]AGjepbd6gLiq]AV[5KiB%3&cE4PTKn
BEj"rJb`^YAgP>Eu-=O%lrTTrZ+ik5*n'@AWZYJY`q.iYJ8k07EC3)^688*p3;)if?d#g0$.
up%!:3BDLD?6=j"S)h(PdrrsK'E6ca<7#Dm#&RU1&OT<G0t*/DmBUa_>(;OCfog%&3Fm/rqZ
JEd5S]AH]An#O<jSYU=.jbX+D:65;T/gEl7Qt:J`).V1ms>[:On:#oeea/\m:]A5]AM_m.+Fj[S0
@@O!craX`G&U,q20*]A0V8aK)gG+"I12M91G?0cW]AZ)01f/VUR`+:h0W)K`:IdDALB6OcOR#@
^K2(,m`,^2d0mIguYZ#ZMis']A%,)k0JKqI/l8FJ_MU!;iFhR:smjh_>IS3e[JC)YL0stg+Ek
VQ\5NEa-O:sl#8#6R.+RIQYsX;BBX0^1m\fb<SH,KY'\u6S:QNOITML%Jr+do$sb@!I>DR94
NZlR\^>pf)=OfCH2?!)6(Uc<E9;DWi@TP_CW0=a4A<B`e+kAe/<Rq%N6]Aal1a'H;cUFs!Mn4
UH*HF]AD^^9)%FoT(uS]A#31?U2Z)^W,O>J2=7P_uS[4BQO`oEb@8!!A@J\<WKRZCfeC(XdTgZ
pPg(M"aD$_ML7k,,%$J9aB.FQneLtXHptan?]AhP5=6(n&(&<`77K/>ZKfWf=O4?lE]AkV/._e
,f(*M@nb6N<J6hERApkN_5aXO[-$<rXKJB\9ik6P0O'F8ruV3p,X)(2l=X@ool2Gki@*r#1^
j56~
]]></IM>
<ReportFitAttr fitStateInPC="2" fitFont="false"/>
<ElementCaseMobileAttrProvider horizontal="1" vertical="1" zoom="true" refresh="false" isUseHTML="false" isMobileCanvasSize="false" appearRefresh="false" allowFullScreen="false" allowDoubleClickOrZoom="true" functionalWhenUnactivated="false"/>
<MobileFormCollapsedStyle class="com.fr.form.ui.mobile.MobileFormCollapsedStyle">
<collapseButton showButton="true" foldedHint="" unfoldedHint="" defaultState="0">
<color>
<FineColor color="-6710887" hor="-1" ver="-1"/>
</color>
</collapseButton>
<collapsedWork value="false"/>
<lineAttr number="1"/>
</MobileFormCollapsedStyle>
</InnerWidget>
<BoundsAttr x="0" y="36" width="480" height="504"/>
</Widget>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.ui.Label">
<WidgetName name="Title_report0"/>
<WidgetAttr aspectRatioLocked="false" aspectRatioBackup="-1.0" description="">
<MobileBookMark useBookMark="false" bookMarkName="" frozen="false"/>
<PrivilegeControl/>
</WidgetAttr>
<widgetValue>
<O>
<![CDATA[銷量明細]]></O>
</widgetValue>
<LabelAttr verticalcenter="true" textalign="2" autoline="true"/>
<FRFont name="simhei" style="1" size="128"/>
<Background name="ColorBackground">
<color>
<FineColor color="-10243346" hor="-1" ver="-1"/>
</color>
</Background>
<BackgroundOpacity opacity="0.04"/>
<InsetImage padding="4" insetRelativeTextLeft="true" insetRelativeTextRight="false" name="ImageBackground" layout="3">
<FineImage fm="png" imageId="__ImageCache__9BDAD1A694F2AE09931BEB5B979DA1F5">
<IM>
<![CDATA[lO<9(kN.ld@UNU%p%320!n&&RXMhpZ,a0ckg]Ag[)Sh?$H'm#O$mX9@nDg03/<C4dC'hs7\:U
CrUFIA*cmN+n1!@hUKFS0]AXkEO<r!!~
]]></IM>
</FineImage>
</InsetImage>
<border style="0">
<color>
<FineColor color="-16777216" hor="-1" ver="-1"/>
</color>
</border>
</InnerWidget>
<BoundsAttr x="0" y="0" width="480" height="36"/>
</Widget>
<ShowBookmarks showBookmarks="false"/>
</InnerWidget>
<BoundsAttr x="0" y="0" width="480" height="540"/>
</Widget>
<ShowBookmarks showBookmarks="true"/>
<Sorted sorted="false"/>
<MobileWidgetList>
<Widget widgetName="report0"/>
<Widget widgetName="chart0"/>
</MobileWidgetList>
<FrozenWidgets/>
<MobileBookMarkStyle class="com.fr.form.ui.mobile.impl.DefaultMobileBookMarkStyle"/>
<WidgetZoomAttr compState="0" scaleAttr="2"/>
<AppRelayout appRelayout="true"/>
<Size width="960" height="540"/>
<BodyLayoutType type="0"/>
</Center>
</Layout>
<DesignerVersion DesignerVersion="LAA"/>
<PreviewType PreviewType="6"/>
<TemplateThemeAttrMark class="com.fr.base.iofile.attr.TemplateThemeAttrMark">
<TemplateThemeAttrMark name="經典穩重" dark="false"/>
</TemplateThemeAttrMark>
<WatermarkAttr class="com.fr.base.iofile.attr.WatermarkAttr">
<WatermarkAttr fontSize="20" horizontalGap="200" verticalGap="100" valid="false">
<color>
<FineColor color="-6710887" hor="-1" ver="-1"/>
</color>
<Text>
<![CDATA[]]></Text>
</WatermarkAttr>
</WatermarkAttr>
<TemplateLayoutIdAttrMark class="com.fr.base.iofile.attr.TemplateLayoutIdAttrMark">
<TemplateLayoutIdAttrMark LayoutId="9ebf6aff-ad53-45a9-a175-9633f4162a3a"/>
</TemplateLayoutIdAttrMark>
<StrategyConfigsAttr class="com.fr.esd.core.strategy.persistence.StrategyConfigsAttr">
<StrategyConfigs>
<StrategyConfig dsName="ds1" enabled="false" useGlobal="true" shouldMonitor="true" shouldEvolve="false" scheduleBySchema="false" timeToLive="1500000" timeToIdle="86400000" updateInterval="1500000" terminalTime="" updateSchema="0 0 8 * * ? *" activeInitiation="false"/>
</StrategyConfigs>
</StrategyConfigsAttr>
<NewFormMarkAttr class="com.fr.form.fit.NewFormMarkAttr">
<NewFormMarkAttr type="1" tabPreload="true"/>
</NewFormMarkAttr>
<TemplateCloudInfoAttrMark class="com.fr.plugin.cloud.analytics.attr.TemplateInfoAttrMark" pluginID="com.fr.plugin.cloud.analytics.v11" plugin-version="3.5.0.20220514">
<TemplateCloudInfoAttrMark createTime="1635919082034"/>
</TemplateCloudInfoAttrMark>
<TemplateIdAttMark class="com.fr.base.iofile.attr.TemplateIdAttrMark">
<TemplateIdAttMark TemplateId="5608ea80-5e77-4dc0-8182-ce76b028baac"/>
</TemplateIdAttMark>
</Form>
