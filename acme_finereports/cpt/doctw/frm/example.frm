<?xml version="1.0" encoding="UTF-8"?>
<Form xmlVersion="20170720" releaseVersion="10.0.0">
<TableDataMap>
<TableData name="ds1" class="com.fr.data.impl.DBTableData">
<Parameters>
<Parameter>
<Attributes name="company"/>
<O>
<![CDATA[VINET]]></O>
</Parameter>
</Parameters>
<Attributes maxMemRowCount="-1"/>
<Connection class="com.fr.data.impl.NameDatabaseConnection">
<DatabaseName>
<![CDATA[FRDemoTW]]></DatabaseName>
</Connection>
<Query>
<![CDATA[SELECT 產品名稱,庫存量,產品.成本價 ,產品.單價 FROM 訂單,訂單明細,產品 where 客戶ID='${company}'and 訂單.訂單ID=訂單明細.訂單ID and 訂單明細.產品ID=產品.產品ID]]></Query>
<PageQuery>
<![CDATA[]]></PageQuery>
</TableData>
<TableData name="ds2" class="com.fr.data.impl.DBTableData">
<Parameters>
<Parameter>
<Attributes name="company"/>
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
<![CDATA[select * from 訂單 where 客戶ID='${company}']]></Query>
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
<NorthAttr size="59"/>
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
<BoundsAttr x="567" y="25" width="119" height="21"/>
</Widget>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.ui.Label">
<WidgetName name="Labelcompany"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<widgetValue>
<O>
<![CDATA[公司]]></O>
</widgetValue>
<LabelAttr verticalcenter="true" textalign="0" autoline="true"/>
<FRFont name="SimSun" style="0" size="72"/>
<border style="0" color="-723724"/>
</InnerWidget>
<BoundsAttr x="50" y="25" width="80" height="21"/>
</Widget>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.ui.ComboBox">
<WidgetName name="company"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<Dictionary class="com.fr.data.impl.DatabaseDictionary">
<FormulaDictAttr kiName="客戶ID" viName="公司名稱"/>
<DBDictAttr tableName="客戶" schemaName="" ki="-1" vi="-1" kiName="客戶ID" viName="公司名稱"/>
<Connection class="com.fr.data.impl.NameDatabaseConnection">
<DatabaseName>
<![CDATA[FRDemoTW]]></DatabaseName>
</Connection>
</Dictionary>
<widgetValue>
<O>
<![CDATA[VINET]]></O>
</widgetValue>
</InnerWidget>
<BoundsAttr x="130" y="25" width="80" height="21"/>
</Widget>
<Sorted sorted="false"/>
<MobileWidgetList>
<Widget widgetName="company"/>
<Widget widgetName="Search"/>
</MobileWidgetList>
<Display display="true"/>
<DelayDisplayContent delay="true"/>
<UseParamsTemplate use="false"/>
<Position position="0"/>
<Design_Width design_width="960"/>
<NameTagModified/>
<WidgetNameTagMap>
<NameTag name="company" tag="公司"/>
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
<border style="0" color="-16744448" borderRadius="0" type="0" borderStyle="0"/>
<WidgetTitle>
<O>
<![CDATA[订单明细]]></O>
<FRFont name="宋体" style="0" size="72"/>
<Position pos="0"/>
</WidgetTitle>
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
<![CDATA[1104900,838200,838200,723900,723900,723900,723900,723900,723900,723900,723900]]></RowHeight>
<ColumnWidth defaultValue="2743200">
<![CDATA[2743200,2743200,2743200,2743200,2743200,2743200,2743200,2743200,2743200,2743200,2743200]]></ColumnWidth>
<CellElementList>
<C c="0" r="0" cs="6" s="0">
<O>
<![CDATA[訂單明細]]></O>
<PrivilegeControl/>
<CellGUIAttr/>
<CellPageAttr/>
<Expand/>
</C>
<C c="0" r="1" s="1">
<O>
<![CDATA[訂單ID]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="1" r="1" s="1">
<O>
<![CDATA[僱員]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="2" r="1" s="1">
<O>
<![CDATA[訂購日期]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="3" r="1" s="1">
<O>
<![CDATA[貨主地區]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="4" r="1" s="1">
<O>
<![CDATA[貨主城市]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="5" r="1" s="1">
<O>
<![CDATA[是否已付]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="0" r="2" s="2">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="訂單ID"/>
<Condition class="com.fr.data.condition.ListCondition"/>
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
<Attributes name="ID"/>
<O>
<![CDATA[A3]]></O>
</Parameter>
</Parameters>
<Content>
<![CDATA[location="/WebReport/ReportServer?reportlet=/Details_3.cpt&ID="+ID]]></Content>
</JavaScript>
</NameJavaScript>
</NameJavaScriptGroup>
<Expand dir="0"/>
</C>
<C c="1" r="2" s="2">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="僱員ID"/>
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
<C c="2" r="2" s="2">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="訂購日期"/>
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
<C c="3" r="2" s="2">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="貨主地區"/>
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
<C c="4" r="2" s="2">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="貨主城市"/>
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
<C c="5" r="2" s="2">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="是否已付"/>
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
<FRFont name="SimSun" style="1" size="108" foreground="-16737895"/>
<Background name="NullBackground"/>
<Border/>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="SimSun" style="0" size="72"/>
<Background name="ColorBackground" color="-1577999"/>
<Border>
<Top style="1" color="-6697729"/>
<Bottom style="1" color="-6697729"/>
<Left style="1" color="-6697729"/>
<Right style="1" color="-6697729"/>
</Border>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="SimSun" style="0" size="72"/>
<Background name="NullBackground"/>
<Border>
<Top style="1" color="-6697729"/>
<Bottom style="1" color="-6697729"/>
<Left style="1" color="-6697729"/>
<Right style="1" color="-6697729"/>
</Border>
</Style>
</StyleList>
<heightRestrict heightrestrict="false"/>
<heightPercent heightpercent="0.75"/>
<IM>
<![CDATA[m<j7_P?51OJKgZ)K'2G;(e5]Al:*!,#+Ef/:DM^O5:5:<?9!)R4UpW*1OpL$<)e(B[W(aHjPZ
r72;FF%e8.:T<f2Mit&Wgr<6pZVo6A1HtjZUFQ$T>3Ga7ngWcZ:0'K*S^>GOMrkqQ7/SC[DR
ds13L9RrA6(%2ThI2a@/bFe?1R\7&ZJ>aN1=_"#MXrsc8lb6HuslTY5'X&RnNq!gZO[9IkO]A
=>L,C>V5PVetTm]Ask@Wh;8Y,h)>4IdM^m8aQ\>I;j3'HNkEt9hUoO$2!:F`6RN5&YJK&jQ[P
/Opk8-^<7HW'UVD*7.map.LTZekGPJi99t_k:9K@):G56C+8X$Mm]A2kabQ.\i4$L>8UTLiG3
Q3"*f*ums09\gSq[;37'@m2Ilmp434@YR^XW[Qh4C!5Utb+Xj;;.CNTE>6rFea&nE%<B.KGc
Y=uj`Uqm1&`T,0jqXh?W8t3P3O2a,DVujR)bq&pPW<;qqY")YccFG]AauTKq#^TqhX#<@bK-)
[EQ(bp-:;Wfnm.Sfl>cO%@nkl*.L?uM.3Hf^(c=*3ZXsFg!5%:oQgL*C^"LD\pZa@2]AhqZgc
Ko1\Ij@o/W]Appnmp=rJs"$bj0:+F0_os:R:h[=C3IU2=KUrp>VY+>Qlh%c[@XrolF16$[8[W
j4c!>:5pUeWR<en-p>E$GcL82\:`;I0TW3?ddEV@no1O$Kc6;3&Q(I+0Z]AF'kVRg7Gh0NS\f
95s0-b0PPNY1*-r*=Om0'uOs;2V=.>?.h]A.oC"74:00)D^+S!@-7]A%ol!1iVX60Oj*c$oOo0
#]AT#cpS@_k&'W2s&[hcM`J/AmeDfdBT="KLS^"3I*!RY8mhC?lk'ZGF;.DUh9(Q6KN:&WrFY
LN"^4m]A?#5DA*39tDYbU<Gm/J;C0*DB%^c!`8\UT,Ku2JY%Jh8#4"FH^0Ai6N8\V9Bo1#B.G
-,^WF+:3L:A.A!Fo6ir:iq_)b,<_%ft'[pM1ZcTa91W<S-R!GougIfVS+oY/jJ&=N+>pf[s1
^(NK+_@?K&/47_4<0_mANik,/%=AR1)!H%Xs6;5fA'"Hl.*b6e?rNs$su@>_)fZ'^\>q.552
7i5OC$]A`@?^bYbD,\o,5U%KRAWf>b$@5nku"..m<bDVa&9@gitlT8QlR>N<HXNc`kk1uWiae
.*:m3DSl!3@$XkG3ClFmM<"V[067h(.6JKYjLpVT4GjN!VD4F]AYuurH!p7hW/2:SGW!&R+7=
0?/'#Qc$]ALVcCiaU;0TIPc(SHJUg=u0>"[>q)5JQA7N,p3LN%LXJHCgX;r49/7*"4)$f1Qg4
YgcFj$>G+k7Ft4l=8e(`5eMc=-QDFJG"b,D8!7$,r6UQPL>_Xb),?/ggrSPmH!Ikb;RbJI4k
3ho^8]A6pTELbR15,'5[ZY.GkMrGeHB?VU]Ais',OaI`h%%K7k*,c2[&Z4,p$[9-9Xh6<ch5RR
@GfB1P93tNf51_lfj\>m<Bc:P;ibe+&.Gui_T^h@)ZG'5ErNiD^bOkZJ"53fa#RM2:mOu56k
$D',60eV)Va1g'-Hdq;NmUcZpd>jM2=\^i9/>p7Pp+G,17pfXnhVO@%"TYfe7/@1VVV:Zrd4
37IQM:Mf!=@J]A,e]A/T3MZ$YN;g:Mrgj#"<<hTnn40R=-p8kG(%jHeDH5h%opBJsN[oI+R]AmP
`-R6\bs[Te@*WlqU;$56W\i_;-DKI3$InlIlAXuN`7+&f%L)`;ts.$L*(da4.<qRL209M^A)
OhJ+*")M4.!Oc/P0hDiM,roV_`M'tDEp/QUnr56R"jQ#l\2r-$IBDk96K;G_qcbF5[-'4BeR
ha#\I9+8[df5mAKb[-UE)qLq4E,9G5,&B[dflZ%u0.l4-fP3th(+5[4KA'/2F.(56]ATE:(%n
Ldn"BIsJo?2@AH<<Ih$NHPgM6$WlGTij1bPOsRnjJB6i$s4%<Yg6*k5uFP[lIL&#Ptt-a-nk
!_I!:&[.$IH2CT2QaS+u/+)i;dcEpAo#\tE@rFP\44(-,!lH[B8[ud>K?/Oct'f`kf.`*r!Q
"`Y^,eDlV4]AhF+1XAkPfkA-K5Ihb',0*K5@L4n)00f*cak!#?nV&=p^6R0qB*I`gp@j^qmJ2
\c>k9%bUWK+^b'7>A?hTmSIV)BtHHFl0\siNB^nL(PfW^#^nJDk<q,1qZNq>pq::(nLd>-t`
2ejR"51XP>/J(c`[</)3lV/EhW:n.)n8_3N9nI&"=pBpBm9>&[Y/"n_IY"iCPZi=@"Yc?KE!
&GQ6ji]ACgNt5r`>iR?%`L=a1^.>=5hJWX8F%#X^f4M9?d![qE'@q"i8%")F-`G_9$pb&)o8#
k(st2>=-=*.I>Hg;cq!Q#J&'=*gco*&7A/n%$1@hiq=n#`DkBmQN3LJ_,Lt;2B(Mo-Js#no$
29FUYRY[21B?QLN,2W"6lsa__rFA06ZE)UlWo_-D"+Fl'7cCIY"IeI5$4j:Y<C/[H4b/U`I+
CP&EN<o;c1+I^*A.3Vg;rM3T=.6,]A5@SRifpfRSO:\dY3\mC4+Yii_*#[>lF/-l0Rp'+aanD
o7:@MQt"e:eCe!cimNCr-fj8:DA/b'@"u(ss(i/<S+=`RMB=3t4@;<X'hVQ^>]Ar9l*R%]A32k
Jb\8jiYA8QXpQ>)@3kP1`+.n#5.klf4AT"@11BOEqWSNB`b$P`</Q#:o16!=,52c0nHr;&6L
"<Io1*N=AQ[K7,!V7B/B4I\DG[;Z@G+5e"A*o5Yd'Hn'l$9Ng%r"4e7PF[GBf62rq<X$C80I
^q")s4r61NW)NNco57P*:75*ou)EDj?4,T<7&?)P?_lmVoRBMo(hG[/qH7I?0A4HDC2a%X4m
M!H#A3ZcV"6A'JjET1>5_iL8pp:5r?h+Q"eA^(idgQ@qnd9qo/Gi:Q_EjEV4bV5s@J((HKc4
<u[TnC8G1!O.kE$+qQ7+`ke-l49;5?NAs`?<0:tu1'T,+WMLS5KRi7dXC7-<[g$<\;6n!9DK
#P.1<7L[38-2s0I_YccYd8i-MS5=?j2Dq&f%i$HC?hBWf""-Ckm6/(>S.CE<D)05q+STn%$^
@++U]ALVrRhl4BX+Wc.HlJQMmRr$Sr"D<K5Qt;HX'D0G^m`6rN@pZlAsRB=+/T0&*!&(YjGjc
SC!7q6')1\XQ%U;:<ZTP#dXR,QXc%hWuX$^*0o++<Od3,D:EV_Uj\%$#:FkfocT=j]A[`td!#
P*]A+=N!>FO)j5S5K7hqC<Of\`AR7PDTIlHJ]ApQ.2SOS6/YKW5k@*VjN]AQIG#GuX1B"r1jmnQ
/4"h-*r1[E`d#tRg-mP+`f-nJ6me28_Ncj4`)`^D9&GX1in9";rtT'c(Oa0&#dfh*4t,ci8>
f.[[;m<iEL'UogFo)'7X]A0(,FLk&E[g_554EGPQ/:H?2?YW=.)q+`Yf>+_Z\_%<[_;kVh.g1
A1E1W*NQDOm5aRkWC[Fo'P0c:sM/j!l)A/2A(sa>>,iS'_Y2SmodK7t:7G#?P5r.,&Fum/\?
A+Bk'5Sh]AD.*R(ZHGs;nlpdOFGZc0L7pnB60m4<No-TKG`CZ*Gp<480Mk8e`Z`O'IG#&nClG
6_^`T:2(`YNB(3sK^NWTVl1_4CW==G$EGS=p<#VG:pG=VAU:N3WVW/O,TTF3[Y4)?<.E%R/s
0@Wg"An_Y^_FDqSFCoh"]A_cN;Ok:Y(m@0"u,h>9K?1k&QC3++AJ"g,4$RV/V'P<?4dT0@m=j
iVGrVT'@Mr5R?FEgtSR:.S2#U;q4-u)ID''!mb>Y0m/k"D!E-8ljtZqXLp,k8gs@7CWGn6(j
HYE:,gM[@<j]A$:CPU_\a>V1'r<_EUTT;^IdHRdOrQqmq#'i@oMaa:TnT"#6BHai,$m\Lq(39
5=mhR5M"J^QFj=-=l&lMDj-cX87ZrR]AkfR\\fqar\VPHDTXO=ho8U_^YO)X7%,&:[^>SE=Rt
GPbJN[4amHEPEf>DKfR$GY*/*E#J0aIW%2=/b!.:Dq;$_s%JYPV)ieE9T>&P9J+HCFEdb0.3
&gp"_I`,sBS5=,^rr5)ScBMrTG@aRmZ\Pe+)jR`sg^FY;I/&p1)_[/q<S^@1(2j&\Ebefp'.
<d)l`n]AUi7K^9atc@Vn%&AW8.;#le7ZO2pRQPJoXu1k8?EP7_6h.d9Y#'dfTo*kAQEmHi89$
S7$ZgYAB=9M(#cmm*ftje8+gjc/U2pY:a2,iiHN4!/#Z?e-M`&JE?I_Y*uZ@fQio/keE5bd6
)%c.I7Fmr5V&0sC$PV8YU90^/.^NVeaF/MXbpX0_Z6,:k'LG)WT5tsKVtZQ:ZfE4PE)Qa*@\
ZA!l)"#\Q7i`"?b42N[7od!&mo`Wf<hn\a-9Mb4]A6r<VeVdH[']A6f60`,r?aQ;,HC3X,;)?V
SY`7?AQljR&W@0U9q[n^jk)>j4c'7#>5PEgRu`9#6dW1e`AF5"W\^cZ1!Ehj1;VCM.oZO?mm
>S:DqnA3N/]A"Xf8,3tntqk5)G:L#]A4mG+dh=$WTUju"'$H$@%beK6@SQ!uG>gMicI2g7@lVV
h\aaaf:pOB&(J\fV)VAsmSZ!:hBp2`-&H"`>4Dka+j/@\F!*#DR>:\+GTSNKQj86<Y6"3-3n
n8clL:!-U[SfqGgsXN]A6pA$I6%[-9?CRfBK1!0"9stVR:\`S'=d,[,0a0W@X/#L@PG&oS\1>
Uj.7S)'a/4Y4RINSsCo?KZ'1G4cQbaT+a]A:B/)-tJi8Q/g>b#50P)T>gQQ=dda#<*FL>RdKC
ab=Waf"OS=qY_[8]Ak^<hB4(4o%8\u:/gl4B^.#$[q;2KP,cQTp;2Sr/M?j__`@/(4VFm6M`3
H&03KU?5@>cr97E:=^qD4!5E'uG:?r9V,.SQbXYCOOLp)Y1,R\!UdV@-,R$*]AS#Q_C:"-CPK
&M`oP7V2X3i2OgZ/oQq!cirE3h`2/-3`=nLNao:OIbb:TfmJGY`*oI`u7&Q(um&lSGn0fFQ-
\T:lH]A57u3Z:1OeE,5pa&HY]A1,CT.G2p)e>X)a]A2rJbFmo"oi1^9cC!QYGBHkOL2Um&h*"82
`u\AXPD3[hWHIOffU!b!]ANK$cD1=@P*aI=qe.3'spNY'Q4">Xk"f1kRR`1\,r%L,tS,Mb?eG
8r7!Y=s1;uU8^7frff["Og\/&i`C0g'3gmJA-%t$0;!6Io'&Tp84Y:K7[EB9/#FC.dk[lNd2
MM*`hp0UbT'e5aL%Fu[!a8IfI<m*D<S(+S%T*8#??`g$'EeM.O7G!\e&^.5hJ^AA8N_hF^Dt
J/nS1S9"-GlF*S>^ETA^oq'7%?.Hj9\QD_?1.Yh4YUFD6-)^3?kBS(b3m9K7JGdI"ZX%;I+-
5A@SUi6TR;`h3DXNB$q_!.tQ*7JX0!-5jrU$[1GP&D/<Aq4f6iq3O6+PinLn';M'+>k8TSB<
[i"t++H_8?E)IbT+AnWr!d2?K*Ll>1Fu:,'drQY9SIa%3J3Ah+1mL2^AM8Lmb:aZW?C7($4O
WMF<-@OUE)<,7@B!38*j1r+$OOZiZYPJhHQO,WFu41s8/h)i-NRq98`jFMl=L;Pp$h1p<#D<
<9;4Kqd%^ht$lQ"i90bQMi6$pKOq<>%>-B2R"s;?Sn;M&T.mKp*n3!g#_6A+e5cBJW4U)^3k
;*!VARD)?)h<GA@.f,Qt6=F?c0l+=<M:DKl@`-?Y8KORSS`%`6'Wp!p[3=j('9]A`U6S0W#rj
rJ$:qi2qd(d7Kt]AZONF3la%[\T3_a=Z1p"1>4L6!C@=H?@ttU1B.W]AAU&Z&:0\IdU[/^:("T
^jEjB>GjWrXj5B`=N$ZL,;W&jAl?D'GTV]A\Io!+mcsr;G=2gXQ/4\19+Y-!@?8+_\<jk:@4i
[*_esPoeh*:kJPC;Tcq>"Q^0_An=LK+"#[s`>ftCU,q!"ESO1!$-jkE&k>NlpMVRGkFa$0H(
chFpJD2+kN:XF96h>mQp]AI[[epfMgQ*H6!d]A$F(V?:W,0hpj2UQ/u'bDmYi\!GL`]A]AMX^E;`
3DH5,Mo]ADnNhZ,b\cVO]ASaM.U9M-D'=$Xb6mo7_g3dX@,YSk/:cXdGS-oi/<K"2&PZrg>LsP
XZL11"1@'F'rN&M4W*RkaE+66)f\UQ()plo]Ab]Agn/F*@aWr-Q,+(T!5]AVAcS!Z4t-oqUR"Xt
R%og#k"_0j)O7_QZt&J@>BQQ0p99CcGBTJ_'K"dk3&?0Yr*P<orXKCX,F^,ejqAc7lB"Bn`2
$@$n>_9abSL_>U,jM5TP8($;O,g%g!T8BlpA46c'3!URke5;_:D-p$WZ>6QA-8_;`RYK4tIC
.R!Wi8$f'<7\mboSXEZ7To^pnT#`K+;-3aZj?S^Cneh9p"B.]AZ[BG@V+XEQn->5f%pk'3P%X
-h"T5d$!V+5#:$s,HR&;aM8Xl*3_MAA9Z+f*2Z(1j5?U0$+6^j?)*;E"<0iXt`VCgLFJ71@*
Ro65Z+#sg7@st9\i([oB2@:#?mTJ'V,q)TGOUUQf%pJmB?JZRHd[K&m5Vrr#M=qua\Q19["U
-olMj_*-PUd%E5]A!R=-.A`;CZh6LrZ9?.Io3eW2E)^PE,ANehh2jg>DmTbTY5Ga8Ym]AA?8d[
]A1/>UO;qd-UqNM@Zi4%$NtW>=OpH4q3.&q&n5np>+_7Rt?fY1DUDWDK_;qd9m\&LUh"4`,a^
K&R:5>=r(qesPTY*HIe1F&OF=['o8%tT?SMQ!!1A63kbt%1]ANs4f>VD0+aAuNo4*KRh7g%Q8
*pH%,4!-Z>b-@"=DWV2mThS%V@Gf.!QcKL]AFV_dma@&,q+qs!]AM$#nZa0.RCp/aX''QuXU]A5
Ue9o1_f9#[Tn#/j7+R*p<Gs:mht^mD#NOa'2gh(_c8H^:#Y[)PFhWl_-h*-$SeQS>&s$:2$p
"9VLB%"UeQYh<p?nZ0BVu3Ft.M_]AXrKRa7_3bK:CdHns9iZSW;NWGK1i?q#Dn97-D5^%sJb2
?5T=4o<e+?CpRYD6;Q=a/FglbTC:@i3dh:09j>:pXG6kpVS:>jM<m(Ke1V6;O9"crO7dNpR(
'f%oFPCprU-qM>MqJ<f?8kP*'[MqdH!/OLW[$Io>tKFUQ%?b"-ou3eIqCUMK;pr0?UY^lIYh
=guOjd>u5hG7@@rJGj++MFZI>9^:?J#K'ljI=8d0G`1<=f!=K[X)bM&,^#tD1C+sc'MfM5Jn
jnfW=,=L/Sb(TYn8=`E*%OfhT^(lR'LUgf\Q0!Di+nPKq/XISRGJqH8C3(?>PBc4o/`RCf_l
!<HYt`:gJ]A6$\9@C7GW4`VPQ0WaIl^Op%mmFq0qH&!=T'HSZESRNDDQ41T,\DgY.=)@fEiY0
EACiMmZ`@,SA$cUG=2XE23^:Lli$#`@LB\kP3<IUB;@1Blp5OIr72B'&ie<al?PpL1%B]AoE:
J;hcV"f<)9>5F!&E&6kn>Q?*jQK7$%JrHO-g"7;kqS*k"GVB5(Rb0j%DE`Q]A8IY`6a/G-ORX
-N]AOAAns:\:C\&^+^eK&taE%Vkp/JlB\3?ja'4D3d6ABYq<J(,/A@p-30e)("<2`KE%klC[r
@6%+YV<9Z+W/BKPG-K3hOL)6qB3akWceNSq.Ue?+DQ@29R0s_#@L9R:),<_dMZ<\.L&"l!E.
WY-n7b8]A_U\,)dA'-34>RnZFdQX$q@hXii9K59.5(,DBr3_oi<ol9qMS,`[Ce.aLO0Q@p9^'
[=:1>a[Ai&g@`V^5MJ@(OUXWmq5/JF1G=1N]AeDRE903tKFJ7=HojKXe1i\nth`NpV)F<$Y_!
5qbO\TuF(099M^o[oh8U\uFYH#*&Wk.W4QYUkCi>Y0G&I"HSU[`i9TO/7G0VWT@;d51`@q>]A
2c\W$#XFFQBF4MAF?%gQ'h&pf_J,><d>BtYRoZsa^*<7<]AS]A]AEJd/NMn:qM/?rDgoBSt*3ur
V_TK:\ZmdoZQ>A]ALt%TR_iZ?`#Zp8Y><no3QGl!4$;@(ktpFEWntV6pEA:i$)3kjJ`f[-3Uo
kpddlcF#8',cFL^44GN9Lbqu9R>B>"dpk#M80lhOWKm[mkF6)Ku0VV>0+;M+MA&GY$)J\9nB
b'jZ&IWt:nkX^\$d\^.7FQMI?a%j>UnMB7NOl?0c.qN_Ic&g;L&'MC?N_L,KXg"pi*id>VSZ
jGm;\RJ^9g'nEeMfR<fdH=UU%Y$Rfpuac`@?MM&0*>a#V.6^m<Dsrs7K4P.ffJKJ-o8q-HJH
D;%T&/p(u0HmtO1BJV`-dE1NO)I@LsqC[E<8Jb'.H&B<N@/"1_+H,$Ul?c;GTlH1TR>K4/i!
GUjZd4o413!cf%.4`#mZXLRl"TCo_Z_p!eoia[!bWSdR=$"7mCDs<po=e2/"b;;J^W_.T;!U
5Nb>4DTOo6E)=Fe&I+rRO3INAhcTjuSG7#58*P?p-Brc^W@5P#,qW"V`gBLlJ`m6A!=0L":q
mHl.dWck3\jS?Sb@d#?]AIesZZ'2LX8=T;s2gN,-fi+dFQj9k'?Nt.goo%[6u&/Yp2O$Q$4s)
GV7p]AA'7<WA+bVQ#()5cA*(ZM"NLhAj_uL$8a..ML;H[`ITAW(O\%garWC\1T_gq<a[;DiPP
;Ih%=P3:ag(,;KmQp)eoN3uCoY7d>e+_omJ\;7OVD8F^#KKP*hB:q43N&lRC4I9Q6NaCa/t>
(Md;L-6jGo9Udhk+*Xm?Q&J9!304iaUXM-[Y`.V$O)0g-92dhjQ2\i":SjZ^[ln_130ko<GI
n&C(N0D]A7I6VDWlFO>P^B2lOk>PJNg,a,Q_A@@<)VdK+>1(f@U.9l)eV0Q$aFKVRYlnb1]ANd
5o.;T^8Tqarco=#TGG=+q?J?97$g,&\HJS=ZC'J;Eao[Lna3I(SRP"^F0JJibblrJ:roShc6
06L,#E:gRbX7AkrYNd>E"dG6Q3JjRr,^u1o_Dmi#?Ou*dV.AkVl<"5:8bXn?V$/c;,\F\EbB
cbkl&ToI/L;HUZ2rSHiC>?QZE-]AWUB]AY^-6X~
]]></IM>
<ElementCaseMobileAttrProvider horizontal="1" vertical="1" zoom="true" refresh="false" isUseHTML="false" isMobileCanvasSize="false" appearRefresh="false" allowFullScreen="false"/>
</InnerWidget>
<BoundsAttr x="0" y="0" width="863" height="243"/>
</Widget>
<body class="com.fr.form.ui.ElementCaseEditor">
<WidgetName name="report0"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<Margin top="1" left="1" bottom="1" right="1"/>
<Border>
<border style="0" color="-16744448" borderRadius="0" type="0" borderStyle="0"/>
<WidgetTitle>
<O>
<![CDATA[订单明细]]></O>
<FRFont name="宋体" style="0" size="72"/>
<Position pos="0"/>
</WidgetTitle>
<Alpha alpha="1.0"/>
</Border>
<Background name="ColorBackground" color="-3342388"/>
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
<![CDATA[1104900,838200,838200,723900,723900,723900,723900,723900,723900,723900,723900]]></RowHeight>
<ColumnWidth defaultValue="2743200">
<![CDATA[2743200,2743200,2743200,2743200,2743200,2743200,2743200,2743200,2743200,2743200,2743200]]></ColumnWidth>
<CellElementList>
<C c="0" r="0" cs="6" s="0">
<O>
<![CDATA[订单明细]]></O>
<PrivilegeControl/>
<CellGUIAttr/>
<CellPageAttr/>
<Expand/>
</C>
<C c="0" r="1" s="1">
<O>
<![CDATA[订单ID]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="1" r="1" s="1">
<O>
<![CDATA[产品ID]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="2" r="1" s="1">
<O>
<![CDATA[单价]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="3" r="1" s="1">
<O>
<![CDATA[数量]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="4" r="1" s="1">
<O>
<![CDATA[进价]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="5" r="1" s="1">
<O>
<![CDATA[折扣]]></O>
<PrivilegeControl/>
<Expand/>
</C>
<C c="0" r="2" s="2">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="订单ID"/>
<Condition class="com.fr.data.condition.ListCondition"/>
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
<Attributes name="ID"/>
<O>
<![CDATA[A3]]></O>
</Parameter>
</Parameters>
<Content>
<![CDATA[location="/WebReport/ReportServer?reportlet=/Details_3.cpt&ID="+ID]]></Content>
</JavaScript>
</NameJavaScript>
</NameJavaScriptGroup>
<Expand dir="0"/>
</C>
<C c="1" r="2" s="2">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="产品ID"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand dir="0"/>
</C>
<C c="2" r="2" s="2">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="单价"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand dir="0"/>
</C>
<C c="3" r="2" s="2">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="数量"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand dir="0"/>
</C>
<C c="4" r="2" s="2">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="进价"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
<Expand dir="0"/>
</C>
<C c="5" r="2" s="2">
<O t="DSColumn">
<Attributes dsName="ds2" columnName="折扣"/>
<Complex/>
<RG class="com.fr.report.cell.cellattr.core.group.FunctionGrouper"/>
<Parameters/>
</O>
<PrivilegeControl/>
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
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="SimSun" style="1" size="108" foreground="-16737895"/>
<Background name="NullBackground"/>
<Border/>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="SimSun" style="0" size="72"/>
<Background name="ColorBackground" color="-1577999"/>
<Border>
<Top style="1" color="-6697729"/>
<Bottom style="1" color="-6697729"/>
<Left style="1" color="-6697729"/>
<Right style="1" color="-6697729"/>
</Border>
</Style>
<Style horizontal_alignment="0" imageLayout="1">
<FRFont name="SimSun" style="0" size="72"/>
<Background name="NullBackground"/>
<Border>
<Top style="1" color="-6697729"/>
<Bottom style="1" color="-6697729"/>
<Left style="1" color="-6697729"/>
<Right style="1" color="-6697729"/>
</Border>
</Style>
</StyleList>
<heightRestrict heightrestrict="false"/>
<heightPercent heightpercent="0.75"/>
<IM>
<![CDATA[m94@/;cgEYTcI`9#MRIRg&bt0iq42b&uhueO>uJQZs&lX'au54U;dNDj[0=\8^UG:;Nf%/Yb
`>))*:kA$:=Lp&Q(7aSl,]AKJOCap,X<Uu#t[[.cNuWi\oXM;cKLnJ?[29QYJ&Q"f"9eH%Yt%
p52pc=YIMfG2t(s/8,hUgoB&'lkKWl=mPhmMSqtZHS`\0)X*XXrIssV_G[_dXA_W"4U;?/T0
*GVXCY3O>MdQ*madR^S4<F*'[^0&T#HQ-G?.n[d@QWW2mgm(Y3r79i5=u[0heh!cLeW-chNg
ro".L6*T2t)bD3>F=l;IfDYH/ZA8EjO*5rU><l,Hkn@Pu/=RdVC1i6JnfV3C%OJb`gS\E'16
p+/2$`-bcKpN,MCNaF2E#5O\@EBO-+Q's.CT4$t=\cfF(.S%mQgn5D3Z/"+$Xa7#6dmDOib8
VZiAM_Bj.6ce)58Yo'EaFb!-89%DBm]AgK/?>@R23$eG!_9;qn(XGk)lsr\(]AIn6$M;C2$pVB
^21X<0Q.f.'gk]Abc_\6_',un<gf@TfCPjPLI%Xr%"UBWl[\b3b^Wt89S9Ya]AF9tsW?)ne@7g
hKl'(7!e.8EDL4.@")N#?U\TD[?3t5h)i5K>D"cTC[Nqi5\DibP7_WKFsbMm\I!<h8m*7Z*q
2a=_7\^3S_!NO`cehqe5-0oEcBLNnBVh56]AM/$QGiuAFZQO!@i263nrU[:jjCeNkIbb_/mqZ
IQdC^@\WaX%87AKM,Q<j]A(KC]APtS^[*EB'jfB6HT[ot4W(U^L/io-p9E)^Oq;u_ls&@;X%^9
=MPkCpfmT9YRL#jeVQN,-KT4.h98_kO&CW>E(X]A*Q-!p\GS(QaYa/2fC--d,dUXbqI24,:Dd
/^)D%l4F1a<Sp\7VQ7p]A3AMJkpO5*E7b]A_<p^03.m4pA^M6C"40,6E_ddJ%=RQ`-(<Kk.IUn
pYgB`l5I"c"u$'.(RH9s3(qH1SVYLG(#D9m;c\[!G_GpNdm#A`VK[oSs850^:RAB%`,WW9Wj
M<p'J12_!7U]AK(#H)&HoGI%Ro9k>_2KokL1OC$B(\0jG>d9[(9#1nnh`+86*>pm6B5[9r_/W
#c0Y]Ak3GQ_;>'!5n&:+u\.K8>$<nq'P_EpmH]AC^3,+@@:$U`plT\1%DiUp%:(hP>nUK@OEil
Dun[M\un=M&>BaH-]A3!&[&QkABO4O:=.>RZH2)`tpUA#nmL%i?FD`_7DEekUN@a0HlN4+joX
qi73O<l\jJs#VFLpSl%E#EFiQf^>XK7I=<D>n$Q;ph0kGLe2;CCZnX*:B2Gh"6-(\jY&&usq
)WjqW%Ysp9)4L<G8^4Q^(:hC`+e\7)i(1l^\rI0&Vn*2[ifTn_\qXd<Hi8+Cl1W^(O_L'lUr
,=]Aj!CY_5KRcn9?rJ5A5i3d4L9Z-rR0G'IJtFY)2t"gS-U9XeT4uG,X_4m<R!ooK-KnBXKmb
KeX]A\8L6-GH$5/&<Rd!Rn%_Yq0(RNJR>_S8Ie]At_@1fY73q%$N8t^t:@TO1O1CBKXXSJ-i,K
F/@oY_tp_p1EQMPZYdQD\TCrR"_!OB0:3f-_3BlqRe0@)P[[<TN'AE-]AYH;UOR-2S,_>2PVT
fel,_RLR4!"fjDDl!iOGO3Z52!;`D@tI]AV/l?(Ut_$8K*-rl"?J/"b1+rr*NM+'DN>Rlk'b(
W"XbD7H76=!,0qHW-`C>tS(]A"SU["cmK:=q1c2qS@cLG,G,WF2rr.]A'?V#0;8-HZi12>.Y"q
^oZ^Xpn*KI%%?UuFj+%,+fi[)h'k$&P%-^QEmhYQFUVs'*<<r6o^jn*%9@h'LiV1qDa_CBW)
7)80Y8V-Fb1CDHLP2Fbqb_Tka&dI45&f5^84.<W:8eXUY@t"%/FQj:rp-\Ol@1EGmJ\s4/Ub
Yl\K[p>:Y,uE!n\U+Vg4t<l(cbP1CI0MG-G=Wcm*Z0RFJ5T#0pg.V$5qRB]AK0^dQ8_befadR
&itQe)ae05QpA[3ps.*]AY@:^Wk=JA7$Wgb;:B8@8oSZ!Yp43jiPR]AZUOCU\-%%iV_"DRjh87
5q?;<9rHrb<4#Fg/hdspe\47dI'kDiXjNX8oS!B>^??cgH,)AFrM_8mA'D>;W'Ch7Rh;[EcQ
2TkAP0j;YUMOi_r4F/u!0Wr7p^Hq;b))0%F^I5Y5lmAa7.^X3TsbkW'j\N_4PYrhr$2e@e4[
>ZI[D.Q?2E2l<%16>:eJIJYF@-AuQ(+("MUpp+hnTn94%]A;b0C[4Z[ig/^Y7gFO?@ij`EnB^
AWV,#Pp694o<(_:B6YMYD?;@`0V%QrH(C<F&!HWN^Qn;>25oAj.uF.(d:bUs8e#qY2YN<-Jc
m0?JM,8'R:-_,&s`1A<LMpIL#sPd$'(/u\='+2Wh\EpfNaYmN%.RBaTT\_bU\kug!7k`c#B0
?_WaHdZ<`%E<2RK1WK;"PiOpFHq-@gAU'Y(FEhu?S#4]A)j:LLh(3>fUP_U/>(,0[@a.86nla
g-Ab1/GF#fei&S>WlRTd+'5(@`4GL(_?W'=JBnjB$"XJ8pN;U'-;[Ps\u#ecEcEE49YgB=^Y
1:!(tmX68B[=`KTgJtnE;OON^1C\5s-g8[TrTsB@%?(uE'`Y)Pon;-FCQZD.g*@'g(X0SqeI
rf<ZC,q/O:QmpCF,rm+1e>(PQieE]AM;?@<cH%f=YafD^59BB%Sqp(N4eP*4a,@.>_lQXe^\@
?di0ZkWgjuZY$>o$\AmB0R\R>kj>G>S,&_!ZE8#.qRRG15faG8T@`>oZIb'A/dEDqm1&^o">
e&KK&r3:kXo.:G%gO''!52BXLK(7_c&a#bQ9'p2h>0:EP4hHj`$f^GNc;^1cIU%__HNm1bJ!
<Igk_A$(SAaBJEZ<[(D'ViRi!%;ZK9TL`%KL/B(Q?H-c1i*RDZa`\dCg8CY=7"kK,T"r+,a6
ikh[)cMs^&SCWtRFJMNDF4TU9H/$!)qKJgKq4.!!R;;B"r@At!*%Q^<(:r-.O>[%4?LM&<@F
_srOTiti#X4$K(TR%-^)2/48V4AY]A2%M\CueL<J%(`MXhI]A!<-GJgI]AF_5MNI81]A>Gg9LG;+
:FS;\!<PkCUs(<Z(W[=6cL$AtbWa0qE8pBBT2SR6:dSRd^DD*U)Ftd+k>8des_>q6iXHTTQS
Ijf0_]A/B@fa_/4K#I^e&hJZ;MqUSc&9TClA2$Y2-Uc[R6cXTE"3NnB[e2geqh;UFB@Ab:qkC
Z1!S;(KYtY$+Pt/J7A>YfqQlRJ.V0:BPl1XL@>hPKRq)Y(_*MosjI(L>PR9dbR"8soJkL<@'
UT_$A<"Z8tW$h`G3K#6Z9-hkR>A:*1\j_Pj</B#Wm4G@n@OYQ822iKNP]AV2T=\G*X\Sk@,DK
1Gb`*>>B#mUk'UdTRX/8=+f1;6!=r,K9rR"#OI@^BL>OmZr17\gNB_&l>f:lJ-\&?.`[)sLE
/8[C?N"<0K5=fT_]Ain%%M[FXjPrcjIRa56?%rK%R2m5N=#[,oSn(4KCd_.!6[$MVWs=Za9MG
$,CZ$en,e`Gc+gi#\UBdl^Bu>KpfWX9u;57u#PM:Yj:&K33+S:Tb/>")4q"a_s2IpG?YY>,H
X?rTV'/.9sg@WP6_j`?E-!qp*\##:h$ZFi>BuJN^Oh_Q=AaVCE5c`[#`BN-I0oJCe<g.n4)#
kS@sKg+Mfd(5.)PbBs5n/I<4K'RV#)qdg5#?g@QMdY")WkPag/3_!VZ>=:j\M[t"Qk]AflJ'I
c(;5DD78]A5n>UM$<i%SV>Tj&,V9\k&7Ac%==dQRQX!g2tm*i]AJrZNNMDnZVbPK=>rs_k`/+@
ll,qd5cU5NBX,fff-S-35b@X3KC!(K5oV*kc.>0QI/1B/G&KXS8J5BLX\>tG!m:4`=V&g]A5T
ne"POsf]Ad(fOb+)rYDW':)@G/=cKiSK\H^Lk?Smj@DW$[6as51E>gFRe1Chb2)tm9kUe(qRi
iNFORl;[_C:g,"=8.:$aufnP?f!2=Ab$H]ARG1;dcLU#ni0fmrc4ldTrJ,CIIJXGd1o;!7pJ1
Y+JVMGlgW#&MO.7K-Skf'GCVtK2'tB$F=GEpb#T\m=D-Vg[1AYS;eb3eIes0)00idf4DiE[o
tRDE$=m)-P/Q7]AuX>6(=PN[OgbmjrQ]A+:3+je+lBcXX;./)T]A"sOn+Yo9Q"P\.[6GEE?_g\J
tlel>rf,K=GQ)oqr2J"(3L%QW(Gj[-P/ul1@PmU4:Epm>P)9L1Uh&-CE:PFBLUpc]A+lLs08Q
9_?EmDG;;On$>^%rl-biYHDRXOMO`OBUqU:&_+$3eDl"D6B<nilITO8SEW#]AMrpeBr'DT6b4
Vs44ru$L-HgAlW\lN16Occ15'Vmi'3VRpeL\(]AR#"V\A$?14O]Ap'4bs[4*<5jW3Vk0$I8fA'
S8UK33i%r!Bh6fPV[]AEq@bScKj*/p5P*A>rV0Y\95NrjQ@uZ_QKW?2+<Qu_@Y^4ZN/8W?Or:
r*7(PetD'k'u15*V7H%D"fl3L]AHa!>rlKjJ@Eq58r#'<3LV62YU^k$tU*)``T%e\K!YgmsU"
M\e]A66iR[6AWt.XlePT@$HDV.#.-79MCb>Ktf6AX[W`/*0ba8F<@s^LOg`DqWZ.SoahNhD72
4@"a]AcrAXG`g"U^`\3,+'?a.]AkHPa*ko=5WY;+^a,^_T!>ZCdH$XrHH7bAYVs6nF[S\B.?4Y
2s:;e#V%i4Wj=23P@p]A'j6RZ633H2,A*\SH%O3i64C2U_KsJ469)JsT/p_2Ib+MlSLpe?sIS
rZtdPIf%20k2]A[_-^u<n(P$>@6qWSTRK`&ti0Aq4<(BGiFO28Y;%.'*56KS/2"U&,hKf`)J3
B"`r7q:5s+ec>PiY,ZNqO.^5nnYC'=.js2l)QL+2B+M%ea:&Ch,Yg`q\6!eX>">pu0n]A*^>l
uE_/.E<Le<sB1LSSN'#>lqk(p"!I\7ia`8+,!UNT&G\P"/lOiW+crLP4TE&F7Mb^n<\Gm9H4
TrVK?0r<3jWHRp8835:QA$0KD\7452j4eDNW:3$aLfYh%M&PbGeqRf9'q\tLq#0<=aoLdNQr
V/Mk67Dc?]A^s@Rt%1T>>cEj6GV+=Kc,N#!epW?f8klp0km^TJc,r3"KmW#S((RpAqG#i+`%.
G0Atpj<H>h6Z$Y)/>4>FJ&4[K=,Zk4'i2u<"!0qj5tLVt8R2HQi#7DQnMkMN/i[Pb=JAbqK)
k`Y>\tklr7K[Mi2M%iJ`:s(`>iiUM*4YY(:[8:bu@m&C_2anQbfuF2AKEiI(8X[CM?\_f`]Ak
n"1%<2i4qou,(5!:,m0m7BgQt-R=;CU3*Y[=jdSS!\/IU5lk=F!j$IMoC,l1K+;l+3#qh66N
ZVP0]A^hl+T;A"?9Rm0+Z9(k';\!?hgo&buR(ppH^@kn%QmZIgO[K':]AXHefQ2Z"olf5fc7E<
e6LK=1s@tdfY)Wf(;i\/Fc:J3sCMT9<VUuLY@!P_'.\EE+^R!Qh!i)/6Ws#HF!,=u]AYr6sbY
K-&gViA>BuZ'CQ>!*F/A^eJ"eg=,3#Q%6FMV9>Ppq&W@@2(st'q"]A/R-NFW^:Q?t3E3r+3S#
LK+AQ#?@+QUkASOG93R2f1+CA7^nAu[ML)>>^',sUGBrrC(LfJjYr'7Pcr+Q$Q-ann^4(i&P
b3GK?\*Yas8[[ud'Qd[0tYQ6q,>8.$9rE)!?A!n0?UiG(!UY:+5XW\MNdq/E?W8Qp4IKLgd!
bBR45Wg.;)R21efKi,f"5)<t_&3ZTi','[3E>.^-]Aku:#K>5tMcbRA,,ejJJ`SNl-s?7Pd^.
`9b>"^MQKa0+>R$M?\shHHjAg[(eiTOU%8+=,=]Ahp@D(@p:?C-<Q1%*#:/O."\*D8mN5QPUs
B,ZrF23D;Pjc.Si8Xm5GN==aQFn_=f0k)&/I68[Y_VZl/;Ssr4's)$U!cT2c1C2B#c4%0e".
k>"C"mAD*Z.+H/h*(?E?TnJ80;8]AqMm"T7q?-$CS1$*`@tkhZiuN#hm?h':fH38c@*94obL"
ZS7^u";^(^F]A`WP5BpJ2?Nhjs24fM?ZOU$(9%'/RR21Bel'-`gsbr$78=G.$Q%I.cgZkFJ0`
DH3k?q.I7DFUoc)-7UadOGtOn:qEq?sbI@-=ZsQ&E6==8pf-/51FS4.@C?b^q,0^T\a/^jZI
KPRbmB01.FCuo=nfqmPb>(LO:+5@p_>Xj_S=ZVd:.+_hl^.chm(^2QUd:V[;tU9cu:k&MuN$
aQbET/2JIE<1YTWAjg\dqnE=N7j6?2f9KeTkK.k>JR5c8U:-r7AR,XE$bQm_5'T]At?T=UQl>
9n:MNUl<^g[O_/^0QYFMmHTJ&$k]A5iVqiVq/[XSp1f\4j@>baT:_rm3)39FQ9/YE-;/QO(K\
VI/s7KMF=C,IGuJj`;CG&:p`^3#I)oTHK-1s!Q.uR0.H:`hk!,8ffsrj"hgc#r*aP]Abmb4YI
8<K$EUYDNnbpj>E3'-FeN`HCV=S$1M"`sGFTZ!dl,Q!:\S)0UfQ;#*Y0k(]A[_[TcZo/Pfj0C
qf"b1oiM@,YD/MO3)*4.@W55(uVQe7KpWhCl[lT#Hj/VX/LF$/,@qGB%!KH9<>2i^!>*hfa,
SGQKE'b33jnp59JD-*bMfq\Ve-fRp]AbeY2qDR'16*/o_,E5q5Cp&QdV$)k7hg1;;T`^OGFJ0
6=:.ldJs!k9CCMJc/--afbWP\7;s^?e:!0tU1^Y=D3&rrNEOpXGF>fE_"NSp]A!?kWh8@7]Ant
#Uu<11=`_e%#*'NsI#12r$^j84W4O5J3&H%Lr/4$[WT$Gaphu1a'jV&5QY+JHO*?Ltd-4E="
)sH5<\qZW"u*WACs+\c9$I_;kq\@W$9s`Lih_cg[3!S"UgJ:qY;r3R[/rnrs2ENt69&\Fpu1
n=fgHI5-JCK'0UU>W\,^TT^RC?;]AKo/bK*><0<JMKMV!bn%'c01>kHJV:;83_K3UFS!"b6;1
PH%4VDY_K0>RbI4ISk_[q,JXr&,GtnlLfY++Dog3^A~
]]></IM>
<ElementCaseMobileAttrProvider horizontal="1" vertical="1" zoom="true" refresh="false" isUseHTML="false" isMobileCanvasSize="false" appearRefresh="false" allowFullScreen="false"/>
</body>
</InnerWidget>
<BoundsAttr x="0" y="0" width="864" height="243"/>
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
<FRFont name="微软雅黑" style="0" size="88"/>
</Attr>
</TextAttr>
<TitleVisible value="false" position="0"/>
</Title>
<Plot class="com.fr.chart.chartattr.CustomPlot">
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
<![CDATA[#0.##%]]></Format>
</PercentFormat>
</AttrContents>
</newHotTooltipStyle>
<ConditionCollection>
<DefaultAttr class="com.fr.chart.chartglyph.CustomAttr">
<CustomAttr>
<ConditionAttr name=""/>
<ctattr renderer="1"/>
</CustomAttr>
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
<AxisLineStyle AxisStyle="1" MainGridStyle="0"/>
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
<CustomTypeConditionCollection>
<ConditionCollection>
<DefaultAttr class="com.fr.chart.chartglyph.CustomAttr">
<CustomAttr>
<ConditionAttr name="">
<AttrList>
<Attr class="com.fr.chart.base.AttrBarSeries">
<AttrBarSeries>
<Attr seriesOverlapPercent="-0.25" categoryIntervalPercent="1.0" axisPosition="LEFT"/>
</AttrBarSeries>
</Attr>
</AttrList>
</ConditionAttr>
<ctattr renderer="1"/>
</CustomAttr>
</DefaultAttr>
<ConditionAttrList>
<List index="0">
<CustomAttr>
<ConditionAttr name="系列设置1">
<AttrList>
<Attr class="com.fr.chart.base.AttrLineSeries">
<AttrLineSeries>
<Attr isCurve="false" isNullValueBreak="true" lineStyle="5" markerType="NullMarker" axisPosition="RIGHT"/>
</AttrLineSeries>
</Attr>
</AttrList>
<Condition class="com.fr.data.condition.ListCondition">
<JoinCondition join="1">
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
<ctattr renderer="2"/>
</CustomAttr>
</List>
</ConditionAttrList>
</ConditionCollection>
</CustomTypeConditionCollection>
</CategoryPlot>
</Plot>
<ChartDefinition>
<MoreNameCDDefinition>
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<TableData class="com.fr.data.impl.NameTableData">
<Name>
<![CDATA[ds1]]></Name>
</TableData>
<CategoryName value="產品名稱"/>
<ChartSummaryColumn name="庫存量" function="com.fr.data.util.function.NoneFunction" customName="庫存量"/>
<ChartSummaryColumn name="成本價" function="com.fr.data.util.function.NoneFunction" customName="成本價"/>
<ChartSummaryColumn name="單價" function="com.fr.data.util.function.NoneFunction" customName="單價"/>
</MoreNameCDDefinition>
</ChartDefinition>
</Chart>
</Chart>
<ChartMobileAttrProvider zoomOut="0" zoomIn="2" allowFullScreen="true"/>
</InnerWidget>
<BoundsAttr x="0" y="0" width="863" height="242"/>
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
<FRFont name="微软雅黑" style="0" size="88"/>
</Attr>
</TextAttr>
<TitleVisible value="false" position="0"/>
</Title>
<Plot class="com.fr.chart.chartattr.CustomPlot">
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
<![CDATA[#0.##%]]></Format>
</PercentFormat>
</AttrContents>
</newHotTooltipStyle>
<ConditionCollection>
<DefaultAttr class="com.fr.chart.chartglyph.CustomAttr">
<CustomAttr>
<ConditionAttr name=""/>
<ctattr renderer="1"/>
</CustomAttr>
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
<AxisLineStyle AxisStyle="1" MainGridStyle="0"/>
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
<CustomTypeConditionCollection>
<ConditionCollection>
<DefaultAttr class="com.fr.chart.chartglyph.CustomAttr">
<CustomAttr>
<ConditionAttr name="">
<AttrList>
<Attr class="com.fr.chart.base.AttrBarSeries">
<AttrBarSeries>
<Attr seriesOverlapPercent="-0.25" categoryIntervalPercent="1.0" axisPosition="LEFT"/>
</AttrBarSeries>
</Attr>
</AttrList>
</ConditionAttr>
<ctattr renderer="1"/>
</CustomAttr>
</DefaultAttr>
<ConditionAttrList>
<List index="0">
<CustomAttr>
<ConditionAttr name="系列设置1">
<AttrList>
<Attr class="com.fr.chart.base.AttrLineSeries">
<AttrLineSeries>
<Attr isCurve="false" isNullValueBreak="true" lineStyle="5" markerType="NullMarker" axisPosition="RIGHT"/>
</AttrLineSeries>
</Attr>
</AttrList>
<Condition class="com.fr.data.condition.ListCondition">
<JoinCondition join="1">
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
<ctattr renderer="2"/>
</CustomAttr>
</List>
</ConditionAttrList>
</ConditionCollection>
</CustomTypeConditionCollection>
</CategoryPlot>
</Plot>
<ChartDefinition>
<MoreNameCDDefinition>
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<TableData class="com.fr.data.impl.NameTableData">
<Name>
<![CDATA[ds1]]></Name>
</TableData>
<CategoryName value="产品名称"/>
<ChartSummaryColumn name="库存量" function="com.fr.data.util.function.NoneFunction" customName="库存量"/>
<ChartSummaryColumn name="成本价" function="com.fr.data.util.function.NoneFunction" customName="成本价"/>
<ChartSummaryColumn name="单价" function="com.fr.data.util.function.NoneFunction" customName="单价"/>
</MoreNameCDDefinition>
</ChartDefinition>
</Chart>
</Chart>
<ChartMobileAttrProvider zoomOut="0" zoomIn="2" allowFullScreen="true"/>
</body>
</InnerWidget>
<BoundsAttr x="0" y="243" width="864" height="242"/>
</Widget>
<Sorted sorted="false"/>
<MobileWidgetList>
<Widget widgetName="report0"/>
<Widget widgetName="chart0"/>
</MobileWidgetList>
<WidgetZoomAttr compState="0"/>
<AppRelayout appRelayout="true"/>
<Size width="864" height="485"/>
<ResolutionScalingAttr percent="1.0"/>
<BodyLayoutType type="0"/>
</Center>
</Layout>
<DesignerVersion DesignerVersion="KAA"/>
<PreviewType PreviewType="0"/>
<TemplateIdAttMark class="com.fr.base.iofile.attr.TemplateIdAttrMark">
<TemplateIdAttMark TemplateId="65043973-1944-4593-a7f5-773e8d065e12"/>
</TemplateIdAttMark>
</Form>
