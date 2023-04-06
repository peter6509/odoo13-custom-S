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
<![CDATA[SELECT * FROM [銷量]A where 地區 ='${地區}']]></Query>
<PageQuery>
<![CDATA[]]></PageQuery>
</TableData>
<TableData name="ds2" class="com.fr.data.impl.DBTableData">
<Parameters>
<Parameter>
<Attributes name="product"/>
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
<![CDATA[SELECT * FROM [銷量]A where 地區 ='${地區}' and 1=1 ${if(len(product)==0,"","and 產品類型='"+product+"'")}]]></Query>
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
<Margin top="10" left="10" bottom="10" right="10"/>
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
<InnerWidget class="com.fr.form.ui.ElementCaseEditor">
<WidgetName name="report0"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<Margin top="0" left="0" bottom="0" right="0"/>
<Border>
<border style="1" color="-6908266" borderRadius="0" type="0" borderStyle="0"/>
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
<![CDATA[723900,495300,1181100,990600,990600,723900,723900,723900,723900,723900,723900]]></RowHeight>
<ColumnWidth defaultValue="2743200">
<![CDATA[2743200,3390900,3733800,2743200,2743200,2743200,2743200,2743200,2743200,2743200,2743200]]></ColumnWidth>
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
<![CDATA[m<]A.=PNTAt,"at/83L!NJPb[3<`*gDL*X0+;(5?-!&=[)6tDN:&<^Eu;,JN;7%'c)W<bdU_N
Y'M6:D.kRE<5]A6@^b#!0WF.fUd.!$2:lXs/rub?ba!ZBth7;hX>peZ_+qgO/q0mgLtu?mLoR
#TWs"([m'im.T?CUM;*&N`W+#>6(S/Y*g-?7h0g-.1<`Q&p@1C<ac8MALb%8$D9ne858\"(M
r"-omFr_L4aG\!/lCi!H2'iZbsh=X0K2U>bF3>[s6R&YMq,FF[dAK^7I*miRL@N(;N<iVQS(
.&^17P*g+>DHYk+41cT1afSRr@ATAs)"r%C0VhRdF^?ZT$"*ouFHP%7qJRVBn_)1$H8f'4#?
ddMU5rd$e&^e\SQ=2'/I)5MbI-Ql;X)`e'%Tn'e3G-b8$H8FQ5rh:(p?^ar(=3Y=Q]A:9A+[9
Z9Q5=`I_7c/Xo;@1]A@['"YU^A8+.2,UZ-T:YP2hYYn)^pUKJqu!#4H^]Ad+r@mmk)cD%,qj0=
928K-rVf.S;'`&#uJ>3:_f*&"`^o>%P%Xtt#jlOdfm(MWgVgY+RW!"s>"s$")md-J@hG=HY"
8;-Gg2=fs;-;AVQa!ULi(YK+H%,d@HnYX\.i#.7EUY02@5hH\I3JT]A]Ad?aCHGYf.s/BqPRa_
(nAk]AWGVp>f>6M)>EDRGm1Hes8W5sLKJ='YQ.Tg+Ae/_i.(kXs$"#P@*JPOV5\TBlUjRUa&Y
b59YC3kGFS'6DHk.&h!1H0mWe+SJRACt[MS_ZQ)"jlhK>gs7$$<*0XQp'`g\IdF;q3W1J8<;
,H_LmOQ>Q)Y;COc!0^P&"q5F3G(fM`G/4FHd;Yk-#P%!:T>Ahn>"m\d3(F$GP)QrTSQNcD;'
<_4R")^Xt?L10u86-(o*TaOrGe^Nnl+FAT>nL_a)`q)hrka%L@D",HSAQh7h"fIPU\?\E[C^
<QX6pY]Ao@/ETW9C#Pnr;6<"4pWMXB08;N7!ThYj\Kk,NWBFk>+J#e-LRdJi:Gf'>qkFgIXO+
cWKIZjfjO.L/mh<ar&!"EOe;2[TJECmeM>I`OqPa'kI/arJm_(Ea4&=l1I3H2up,-[P!W4ko
#/9U`T05$Fel46!35*:C"9[r6UnM2]A_9;2KXERSq<,_ht/FlX#o@9T.'=>Q5Pg@MuhbMceq_
Zp@BZ3[(*ZrB#L*c7\rBbaO8q-+bbX9_=dnBuVbq9+ui%4_u%)2QH!"fUQ&6J^^qD*!]A7sV=
Jk$)\8M`l\Cn,3u/:XGc'\!g3lm1O43"%ul.hYl*dI\Y*+pmQ[0^NO!*GJ:uN^T[Pe1M-XA*
rrWmVrq^;:PTJZ&-'*X`9sTLl:-3d-'5_:nf^kX"/]A+YnGlefLJO36oV"(-+ApK3Xt$o,F.j
0CE;3uhQit)$#1IXl\@A9ie:3D4ofC^X[\")RCXYi/qAjcfO55&(p#j8ZnKTP['dQt[SM:D@
76uZ5mZliP'tknuWc`#;,Ec<]A^['E4MtnoTU47)&e`8qL[KMEZ[Xb`k/7RIBE"$bZp!J#'lE
OI)ldT!RgSmSjhJiL-Gb4$f0_N$,6tkm4^I.BgFdgg3<_KqQNUZ:;<H]ABDYOD.!n=Z6MY$?q
`dJ\.8oA)/,j>`4e-3SbcPM-)#hD#&X1k*T\O?`+!Bb8hqbRM;NKD+C`\;8Gj4.2;UVhV/rp
.F/ZG2AlN%Tlu+S#U+'?@K((Q^3Hs'+7/bAtUu*hcS_b%fa=lYWP&re;<ILmeocN\A\L?R[Y
n5RBigbYB*JBNhY)aoSuoG#Ds_Fce%B4q%0@,+_h>%K]As$:981cG,6P.9%e9FfY;<7!j_-Xr
(#)$pO2S'(Qe?&!`m@=1'L`cJR01=aT9Zd(^[/0gh/85HN6A5&J"E[ghr^^?O6%&,5]AVeX?p
lbBYKd-]AI);j'?tG0OKq#O?Q\Q.,djIpWJ;BHuJKm%R:H,<Hd01)n.VF#%?k%qjPLbG`P.3K
sZm\7^lnb2DIV8q+Sbq`G4!<TJiK(U-&oUSGeu@-XplUCpZ"3D"5P18'p+?KN`6p7=Hgns,<
V^7(!/I[;(mjI8P!P.C[RCE4.11PBM_I1>>(2dtRu5oI36e:_"'!aR)#hFu:7fC<lid\p4.?
.0(9c/_'?Wm.<OY[1.OI&<Q'Bc+68Y[$$cZI(::(q?j02G5d**@+I4/&9g'53j3m'9:\.Rjq
45@!R-W.?^FIZ=nG,G+DX2=*\I_&W5/4=\$*YlQ(Ub[[hF>rO.QZ$g'q8QU6iLl/sSXp4'KO
KC+dR&1r%Ts]A**mc)-_T>uF]A&BjsJ0*V"">#jr1^aOf3tU<XUWAnGY"9<TB&L5[F,738Gul2
HSNsDYos%'1/cI.@3`/CfT<F;G/G3l\,#<AXqK$*QnnMIMY0fgq"AXE8pdc/k3spXDDT#r6A
&#XVCTdo$/F-T97G7B1Vm2Q*P88n<5br?]Am)oJ"qc=?ek_h\[2>2(N<="sL+qJ(GE#Maj]AcI
re`"=TQ$!4@k2EZi84*4&e5?>P![UlIbD7tK.dkaKfD*J-uOb9.76Zs4T2t-h/1K+Zu4;u.m
n.RAM<j8K3%)kc(bd9a.dTHB-0QiQB2&^JT$m8"[bR#q!n`)]A/P/:]AbR`%IDn;<`I2L,p:q2
`HbkK)]AoGQ'qP+5$ti<sU&B`+8ErFXo]Aoq<[&_G1'IEIA;E;p9_=_eTG]AOlN3@>SU*pG6.D8
H-;1b&k6I`u$,GQWZU'bjM)OG+(e8KIEbT6[<=m?:E^-gA$c]AID2fbKD^]AD*9&%*n4JVj=T@
kS/B`rQI^Fq01E>lBbB\FKt3YpXqWecrH,<]A/J(h,%'eB1&k9/$_774U+R/gBa'7%Sgs;3Au
W4D!dJOoLq7,M%]A5pR%,7MS;/r$8cU6=#>j7i%">,oh=Pu7mr3LS)>X!'9bb\H>W_cXZZ2-,
<^XDXFi2o]A/S<6_@Q*6\-@[:]AG&4'+4"m/1=h$'kqM!5.q+u0J!u@X9FjDTLV5No/bL/.'id
tu?b/fsji(@?87(\`rR@I9_qu!*(L^;:PWY3[i8^#8?kQ='Q]A@a]AMPY+XYc`nfi.^-Nr-+ne
WDulM[)O'9"cRXCe]At:&nVp!gBP"Upf;2juQ";!r#Zdk$bMd]A>%G"eXjb1nY8onC,"43B(]A`
/TUHlCM6f^f'7R8qK\7dDN?`EY?RT&T<N+jn%O=SHgB0-QXHYX[abeE0aVt!10)B&?d>Oo*s
D'"]Au5K.qm<PTj/$60_C_>!Skeqpm@+aUCo/S('**disX6WUDE(ce)'ANSi.!*:[-32r;leF
<M1#TWS6$.L['qVUaP:i[gc3r^>rAj\`Q?G93/9DlktT,->j&%:^hd96p0m!>!u"L;^Z?]A,l
#=ZZP+qN\NA1&FKaC[g[nq'3O!;oMP;fqAEkZ,:D(5ld'b`V8#;P-R3/jC"^e3eeX<^@@%q;
Db\0_/Y8Hh5Z%M.W^3.A`;ik2pEH-,u>A3o#\Lp8PW8I^/%Qg5;]An_^CBOu+<1]A%70ZP($6P
D8WYSTq84+/hhU[(=!'GNTF*6TrF=@H5@e>*5NA:ARr.k<HTT38Q5XI/KX`L#u$V)A(LA'+X
m/rU%pJ#8VN0,eDfg1EX,2-t]A3Z,tp%]A]A9\3,)pqj/9Rt6_C"ZV!)!bQ3#sW:SGLO,0,8j(+
N*ih=<:*<fA"#cqq]A-.`7Pr+CSVY[1=nd_ac:K`G2GP)@T<)B'cE7H(/37og"BXFOF5Pq%k5
b'Q,PXJD9L+#cRadH)7$Lcf)1.-L49+UWe5qDd2:\mpRh\''c-D=R_p"d+]A>4_kki#J4A<q<
[Ql42KK,R2J>&q/LEq0\g_EjuE_C"^T$Q<lf'?Pi"0=adC%t.Wmk%7_N=*@6$n40VOcUf@qr
jJ<cOb#;/XlMQh`BDh)X*)=OIVUIhBcR.&=iGS)\#S_//(h,R467pmRpoL_(:)1fPF=O9_FY
,QgnXQ%nh$$'6_D38Li$iC;1T*LM_+/_7Ub(qI.!"12KO@I1YA%b(3,@YG,!Q9G+p8g-Q`H6
o7bV!&:CL0Hds;1A-?s//Q!02BF&M0^F>@s&a"&=iA.T7RAeT3nV8bV<bjqV@?S(h<OK12l[
r5l,pCR3XL=rnDk^$M.2iFNd0^(5;[$;QKTGQlpN=h[M'B<Jb6>Z;S=RKIbGTDA)Z46u&FNX
HfRYnc+6ICa^ON@p-HS?q$dJ1`:;*F,7%>tq4t_)L%5T%SjlLcQN>1&t,M=P!f&@gbUe>Z^=
T0UmW`%1"IJU?]A'+QP[%IWj7DOX*Y.f8>m<?l!pfOP?\Q`G$Vnh$?-r2tsD#od6B\]Ac&^.F1
_dX=U:i40*Z/'YC4MoT?Zd!;03pA2JOSRR;`^b9`opfcVe'OF,)'nc\Cg?c06$s(STdC7erO
'=h[*RGU[S#F<G1^bs;t4H[F=;UO9T_[+[r<$pTU8+3=7?/1Z1O\7,%cu15]AH8FG_n=CCPc.
rrTb9b1$Tj2(d`]AbN6Nu0#"F.QYp12k0;R?X_B[&_fO*n&"O@*5RX]A%F?\VC/"9VR'eA<os[
M72CmmUrQVSEJkg?b.SA_2Qpr(<$:42.Dj/TXK3.P7u1j(BqjX#"YE#aY^A0[@!n0A!)RQl%
u"f^Im?fP#14)5df(">$mW!"gBJ!AVfI$oV*p)%]An(L1%TnZb'<P["X$Ak:I*ch)PNmQr663
3[=/kskU*Moh->2se]A616M_!IkT'oRlQ`SFO4Q7cG@Sc/_%Ym?:+Mf-p,VM?(=`\f)rgKBJ4
<Tnc"EP60&9>\n!@^eU/\u?5;8+p]AHs04$7jt)QKX7$h?c.!9SG')kPb"\ns4&pK>LZI:?WZ
8n.B(T%chi"eifm5D=:JjKr56"H5NEq\;jg4s!orkDsF@[+^i[Pd$0LG<.6j&<g@MNIDDmG5
g!P#KU9Y]AbYG#&^X@Y#^X9k8AtWEk94Ol8u]AL9)Ls_e7$#pLo\%+r"RGO+YbR$1RM"4SL4-K
Dh$;+[Nl%iOt_S)N/&"\&7qU3[PEO+1oDq\\YRDK]AkU+D_D3&+4L6u(fs3-7a#`7TE1gCb?k
I5T0-;bU-1tS$24Q>ji!W8<E7nm8ig*F,<@CnaPIlH1&fhq=Ebk8o!^`7\5Y`38r29o30Yq3
4gRcOV3[]ARp*r0s/n*_\A![T3a]AVQf_P9F9HdF>F(AW#u0(/)^&`Ydo?,NZ*[XW8"X^DS1%p
M]A>/Ig/TL!TQ\%0d5(qK0r'f+2D]AKLsFb+4O%Y5T#kfWF!t3qKA,glEJP;L-J,hCkKN]A$F=)
)iZe75*06iYhiD8rWG5u<4:4%i4Jh"tZrWEjZt>5;Xu]AA]AE[#o-(48>;2u%aV@,O"d[7tZm0
u8,lp0qp<3CX_d#oFs-Vj>``XV>3mXesgZI(,.-1s[]AfnMZVN4I>qE7I6[iV^q.[Vph&C]A&@
iGrqXVYfuDLg/jliI!;t)9pi(Tk-CYJfIFa3ogtOo/X$Zo_VOnL,JAm;`HOa,ZBMB`]AHZ7Sh
_tW\odBPEPGdOE?>AqW53]A!FkM1ggpf$J<'A+5efh5tA08Fe`hQA[D*Ie*^<+KoFhVJ>ZLGM
/'&&b8_NQ$Wh#))s89J$HDI`brm!Q$,<H><4iC,Il`fqb@Mr@.$\M?424YL7h4CC#LgS4U^Q
b&XLt>!;2Z:Ho$/dX=h%Sr2aZ9Pscs0l:gO;m0d`KA0>%pq1@E:)r\HZ?]A>(/DLaB*p7B#I<
"OL\7+89F[h1L\`rgYNBP"=X4djFGk-AK!Mm1OP8g*qTV8ILt.8AY6;)QjeO;$rI5KclBL>Z
sW<L0kZgTr@_f!0<4-_J6^8:7f'.RFguWIJN^c>]AF@A86k=H4[8_&l"jKo@@mdJc9C&V9r>!
,FA`%BV\W-2Sbk=E3sq*Ya[3'[[SA:2$Ej",I&e26U_JDb[]A0cDKlJbHB0W7^,aHcV0p`/>Z
qFeA?$=gOlJ(<M*$;oJ$_BaUt+i<X#s^\=^-iDcgN%5Lt2?$T?3QXVhNmO'Yl!u/RnHpXhaI
&3if>h\W:*=/7e%4$m$l/Rs<><8FFgKhWp:)O63_8M:t,8$>X')L;dH'RaA6KN@IA?Sa]A1?i
&2K>cJYruiFI.p3UKcYLE$&s,i?TsET$D<a)LjD=sp1iF=eBF>AkO(hlTTF6BXY-#&6-g6c!
4A!5/Zs[C!k2KU);sErY*Kr._]AJ`jP4hf'E\.BO,*mQPaGDNUn>=<_H^RNl.`1gpDoU".P*b
JZDt295&LIOVa#i%FL9lUEKb>VHXnT(b0q"@+X/fS%F60QOS;ikO_ttST3t(MpHAVSn$-Yg5
,/7(]A",m;Sip&,t9/f"k[ud8=I(BeVXdF1O:WRXK4CuB'k?bL,=]ArRjO(ZqQ4&tYOI(f_d#G
CO(T-?'R<btd,2J4kp9A^q)ehX&AVj"AuQ!"EUA<Z;'^b,QQ'2tmQ'fY<Ih-]AU.<h7h\22bR
O1]A>`:JENF-Ei:VT'*%A+UP,@*:FJ:'8H)i>d'p3=B`EXX4k89T)0YJ]A"2A<ulZZL-[mbLCY
ED*LNloN/2dg),ln=4S1TpCQ\mWbBgND2''E?iR)+a`)2BJ5:m;_H,AplFE"kR83!*j"KH[<
MJV0EOM>4LAN1=m9N:>IT^-Xug6\!PbuV1l?RA*Tip.17;"!#Ql_foO';/hIB!pbo^6<IcPF
dTB%\<YR$19=+R"R+M"4%WXq21JR&f\.mdlIWqHAjZg*mYq8#"&cPC#l;:9C?k!QYp`PmH;c
[$lOJVNe5H<#Ad'inW]Aa(3]ASHC[&ebSYgR<n*G)/mcVY*.e."Gsc>q6MZ&)FZOl!Ubo=_>2e
?5]A=:Ai!%ogcP\<2^sXcLr+#4qoV0X\b"c\B)AnoN;KMNa-0Tl\<&8aM!#CIfGq"FJ2\_FNB
+NB&1d?@9$G>j\N"`Tq39Ubn?@28PZli-]A0JTWK:>FC3$(NRlXr(Ufot2qg"<\5+="_b=m"U
>"6BS,`uYPL&I>EM6'R^:l!=11HB?@$rV#5%CQ936dI+rNn3j?LU$!)#4MHWoi1NKTr8A,!@
$)M0-#JV6[8Z@BBGI7*p[0^d;u;FRT@<A`4d5PmbFCOC6b76OV:#HIc]A$\YoW3Kp<:b.8Qn#
t[&7m:-c[c9hX#+fEDQOcJKhq;$N;(tb\hg,Q*S/`m,d3p3W>iGd%Nh^Pb@mOn"`X$N*[Dhn
5/Gib_STok5n;<H5s;Z@B(8KZ^tC-!U$5)a`'.bHCBSJ;jgJK$8G9MUemeK7-ll,1g#Ar4DU
cPonIUW(q2d1Fb:r+WTBE@Qt`n:`gM\9g(M-%@Cs"EYh)["QQ4[=ng14$-[V.=8g'%mjce.3
+i%6>`GsldIC+/%_O[FZ@tqV[TQM/3#Qh*2[f#d8^))')oB"Dap[spX6tC+GcT[Akqb32=Tb
8FQT=iS?c3hGF2+\CQ\?R$rVHaATXAgNgEbAr#K!L$i6R64!;n6\47>Mq`H9D0dVb,NuLc7n
fpB_n>R1qE;EZ_Fe4&DFKY&;Ah13&;o*&C1[-k)^f&/=&6>>nCo-/=d\WGaA7Y&&&8r4ZjI>
Ddt<*omC#_6[rsdk/5>06jQ"PWdX$GsQ9mg8q8Tl_J=>GNrYlb]A@cVh8LGg@asrK0fuc!"_X
<LA+1o7,TnW"$ZM1Mj=[[Hp$47!#.L;G_&))R$g2e+:rpAR"@kk,"HM0!E1=%-iu*^a_,*(l
lTBA)I!U8SYH(Lj-+Ci_2fWs9NVo)6<bqCUGu$<,-PkJ!lMb':)DtpQ8s#\6#jaZB&'E2pmZ
=l.SMm4h^GNi5MC@cH`LZ#YmFCn;-X/D"Rg+IUDa!B!VQDk[pnPp\"tr)Rmhe?aWJX;R/pQ`
5INhH':+Yl2dS!HPNtoI*UNL+YViU-Lf"Xp4-.u%[@\RL"#NHB!/+9-ag7mH['F3Se;S)d]AN
Rd[#5,hl^`f3]A@06^ud,Jm?Y2poD:N:96XP06t_"@AnSLS?qS[P;lr9PVfp7/#s0C>E3?[E^
Uma2At(3%<ts`XQJu1\lL/lCG0BSQX72%*,S/Z*)_#?9TXDKmRNsnVkkn/WD;cR"W8';VrBl
g7&[:hMo!gFN&q)[bW^#2th;'=h;J63g1')i%*@^/gt?Cge6>0o$HF/O`]AYpo]A';-0mYROmW
EP8h((0U[-Q'jYJ>4=?f(Qqa7j+.RW"*!3b"R1/>Rl63&DB'F#>m>aYoBd9t-PXV)5U29C,<
t<j(El5V:I=,aVusOS\@Vo>"8YdR&!U6D:p"f5JXJ^th)JP=57m:1t!d>&:C5=16TF3<gK<K
tnXhVg8L?E9JtKkZtEa<H#FY?pijs?jFK`aDmaCb=PD6c_@d_67!aYd6=%?YOAJU956OF^A=
<ZksA0X$F3h^h.&Gu%@[1,rQiU(7CM^HNKEDK9DHRt%/6%"ZXMZMcPCTi'n053?<L')8V*q4
:!D+.1R[T=QO#bMqe[d/oJcEiNbal0'l!MAeh2<E;0M5hf2GiO^pC'DO"?cC,0E1;qFQI$<C
p;p@SRia=bYUDUR1g,M&7i_+Zd7TZrFq2c[pkqNeZRYptNX.IChGM[gg]Ap'06'dcj-2W/>0=
98GNp_ic:EfB@AIeRN*b;dD-9ZVV7>Ok\oaZ*Ht`?R`rW.WJM)UEVfrTDTp^@?tu6PbJ$og/
%l"V9TMsmK8r<8=!%1?6J'/bj0h*Mpf?l^MnE=RbEl^"'X[)@IuI:4WJ3N5TOF`sq+eb7B,5
<?oR_![Jm/+u]A:$B,a,F+*=i23E9GcQH_5r5VM/L)ZKP1;G"Zslt+3reEX;%eCjO:rG7PNu=
hV8@T+dZC5>nL"$]AEbeFRu<go?-SRSduKc0L-DCd)^)*<ps?G_0nOEUe1`cLok(?OAYsai5j
E#$,!BqEFCIQi,DZtX?tRWHg_A_1_4@rW^m>Kp$t`8qH0i'i?2J`WpqfP=+EIN+lBh%4'(X0
HS$6XfSgq,6Q1N/G@=T*:6p*B[;S=5_fq<+%8_!9Jp]AZqie*P&2<kJ`i)G+=3f8!q^[Bd=t5
8Z0D1`[dUqsOndh;)F<jkW$,Nt1E0D4a$cfa_J0cUq*'E8k.0(dHALAW:o]AF,2WKi5\&LWM^
af2]AO\$O5CKWQr;/%U1ZHt\Ocq;!i2/l&!mTSl#rpj8efWhU*/=[YY!-9B>DUaO#+6s8LI+M
fij^I4R*0<:Xe0W_;L((TZjr<QPZ8>[T=_*b(\2DhI>pF1]A(Z4o+.e*D]AGKijueLAGMSS6./
_pLZ1\IbM"F@6Db#YfM<beBO^YFdSj9_Feo(;Bf%N6r.f.R,Naf9k*lG*%*+p>KK3tGqV5B)
K;s^tS.!EkQ@;F00?s)t?<&+f?DW`(2q0$)VH8HMl[bH9b!S@TLmm"P'qDNY]AXQtH1,BWt>@
&b(UIFq]A0a!pUcLIB*Fa<MS!#6B]A%@%+-?W!=)mgaA@Z>(T93UIViKBp?h:bF7Z_*D,o>!V5
.^4mU9p4f3g;ImbU>YCK.S1T-ia_Xr]Ascj%EHg#-f`0tf5<73h!If#l?up3EJgT9tg$n&m9a
J87ET9+C&cDcLrY,\>qqTHh<L3R;EtLl96i1NH:#%D#AZ8>9<04F:DCqUC(qN>b*<cTDEp%)
7Jt#cfK!o,ZPqdBLq`gX7R>bU7`k40n^ZY$dK;dnEjZ3jd^Nj>j>HXZi]AR!@SU&5qVYj`:2g
9T$qF?AP[l&AWs(i[;/4S`tX]A%d1E%qW1/>V3KlYPL#QgKVjl3g!T;hn9)F$s_5Tj8WpEDO^
4V)>WIDA*aH1%3e%2H.00q:kk+u7ZL;]AV<UAMj@%OU"(G)>C#QV<JOr&AuX(nUG-a.O;t/@t
0<mMOMm:hu2QWC,@F^;(#`4I`::H&Zmm(0,O=IE,D3p'!W!4T<e$;JostD1q-485gK8[S+)s
n*@g#MlK=Jmqe/Xk?q/GA%KS$gFmioTlCRETd`(\!-B8%U80k?CDN^5Q]Ar<Xnlo=D1Qj,FYr
fto[p[#aDLUEJF`a]Ah?s6\@r_=I"1r#,nJRGNkL7S6'dC;XoerGp7-nLrKD'jD/72@ICdE$8
kDCn@0J(t$0P1"^!*ts)aio`Fn/2]Ab@M?teXO%&LmJpV$3T%6gnG8kNZ.;ju3d*GKX7Sd`FF
]ANPX2;jRmB)AlXK3jL3C7;lebV&LaF>c5;E51i63')Wm*=R-`Ai<c5)Xr]A47BXM\Q>fM'm1!
-rriX?$KeoGl3i/!NA_Ffk?);?f7dd$nQ0n0U.Sp*W`/4du]Ac&FVd?LoIBhP4uojM@h(@M!$
_jXmGb=@hD$2Q^-d]AQ?jXO49FrLD9E]AMN`MG+'MR8TisS>>,@6+)M6O>kcC]AZFcf_ZB3>F:u
2d;1$GSg(gDJcc*(/T']AC#TNU+f7<>q(kX;+)6'SWZY;oGdaKm_4kEh*1/Cd..MRFtA?qZ0`
0o-btQK=]AW^lATsq)Um!:8i:^bUSf!W!UW4kOnp5\3^RKSW.Ts3on%m:h3&YqA%a\m8&@<&i
KS`HEVDgR'j-taQGpY-d25pQJTV#WO38cPhUfTl':c1:XR1u/j:@)Vm[Pb?:q%=(13pt`nln
=_7VD:YH)p4"eW-q(OFN^45QNe@\$?gU\;d4<[&l63Ff=`DN5bG2mmsf\^4g*.2kT#KN.enB
RV"RuisNVpf942j@ipc<?udIUN[92hfq#b`RiRPt?p<grgI:-n.<uo@;"AV<pAQbM%VbR78A
bD(g;j;U%2eqH,p:)h)FLHVf]Aeo/^*Z5+B#.cj=%;cN1&:AIeCUeg1Mua,fd01R%=4uk:Q=I
GAsV2nIq+.t5eUnig^P^1g4_a0kH<L`2Y_rM&W#LRmE>j@@2^X/=I":m2*rNh#0Nmsl7k.Ql
5Y+'HE?E"$u5ht1K&3WnW9[4`&qV&Es;WD>/<rgN'((ph^-QA*.EJ,3)@JAk>!'1r=j@CEa1
sVT;:1"9$l2eMN$/')ejZ7;Vc^QgPCiMd6/EN=6-6fS?SCp]A0f-?,hL?lgqeL,:@9t^ZH`/=
NXhc\T%;Au_4RTC3%mpmD!>g-E6HgoCh[S^7Jme\iGSI'lq#;-<lhb0I*\_.Kba09j'7g?NU
Ms+%7EA+]AL3dsi4.b=aHbBK<KYt'dWDOYe0.N<=[sCG._Si0\0Y(iF[k]Anp'p-t/X&r.')K4
P:PaE;n@ZuJX=YRgM-5Pjg6A<2SFr]ACMqO?.4nH(@l`M47!$YKWlcCY=!FbbtWCa3CRFmJB[
k>(f_]AKflpjPr;IV$J7Qa_cG4LQ^"_i!H3TTMN"gU]A)*q5D!-&l<67>7&g\6ADCP2T?5/e16
k%G<`)ODh,f>'S?+#oH*ZFhO]A,0ZYALBCFo@DHP0Cq-F]A$/C<+f9%FepZW9Ea^nJ_VPMm#pS
R(TS%f[q1LFR&8of7kt:EnGj_.(gc)U"a[@Fe]Ar:'[Jli3cVLtRIFkHVU>p$k6ioS$kM8<c"
#0RCSOSjmBTZ2L/.+#fePT:Z=*;02M\EOrhK8G8)h(_6<`47JU(%#lE92)n:GR$FuVXB(f`!
bld*<CiIb4'NX1)b!DqHp.4Si2a$$o4/h$I1f1t^:'>7fBOJsj<HbBK/r$/Ra;L_N6<I_to8
Bi14XFaG8[I@nG]A&k!jMdrqp+/RJX<-CcY'N=*O3R3)M94qPe!BjQ20T_%C58.4[YD3Qo%,M
Yar3gXE4m$!I?5fp@@qJ<^nCFC)F(]A,IYuu0%ZTJpRe#BFO.'#V>$guS(K=%2c=5r7Qcc5b.
UVj;@ApA!=Qf(`q1tFiE,2i-4KeopPf57!f40)1)B9n.N9V=.$FI0)9Y:JG,e7.S0]AQqFr!F
U-U4-L%<euCLjkoc.SL0pKC)02ct*!nLLCC&_tSa;No&q*A1q3%Y^\Suc?bU!a/lAgC!:`Ar
bp?8[[T=ib*FlXE"eW/Pd[^=>EnRAi.=a(%9C#aOKa]Ar9>[L0^En"[<W2*n]A\Rs$(O6k^fmZ
po;+Gp%3Ghh.'`M0BWnG+=1$JqcXh9b%KhE)MnDT[dH=c+;0]A2uIC+C0JpG@\4n\&Q#[blYr
qknU$7m6Fm!/8#IVi"s0rejXH!f5.M^#4)2@V$m8lI=h?$cEdMs@fU4Uk8%+8!%5[WPD3<f.
Vs7.SL1(<J@DbG",<.Ts=j2(H-nVV\U'4O,=6"Z^OXM31&cCcRGG$=pl,:[)JWQ#b2gh7bk+
_O?oLm,:d6P*N?#!QSf53WuIX\rZUt1uai@;8E&UZY7>[@PgLmI3o`&@ER%Cb,+de-NN',+8
)p1*Nn9n"A&=]A$3@YNU>4\1?6R<c62)d'fdhbc.`9U>?_33&tXHJA:o+P%:F1B,gHZ/gg]Ash
]ACS?9?s(LceG:?k1mOsNmX/RRMFjQ_s;"l`8D;0^R*V>a:`U\%)&VpAiNe$2&=&/iV4Y;N#?
q`ps$ZTU#h9l2oF2F,O;oF,/m@@L@!c08<inrY@^YP3,@Qe&>DW)GOn(@aHG$Sm`W_u^_^V9
Ddr,\c,`Tp3W^e_Uo$*AVorKkUs[*<p.8CrL0YYfen>\T*1i[4(,iKLM9&cVb`9Q-WbCoK@<
fgCSP,$%$gXt`Z@VQkAL:Yf*l3D@.PIC=dVm!#7P@e^%*b>9IO-:ES1`)E%UIP$`7PfHHRc)
A1s=GNF1,TP,&/tVHdOHOR^0F&j+A?\,bG9oFPR1W)b?,GGTMf#RZ"c2e@u=oh$1htq]A7f;Y
\n4IVO3+_0_AJ5N3H&R(*"i@cbuq'Pk)S/C#V`-2p&.h.1S9=/"J5eL[po!;.LoY?mr2Y0pX
>'2BB>n(>2[(F\2#RKRrIOG<X3<n\#fRiesoH[2clT)-O#jjBkNckfGlAYtq"e8E^qG1s>5a
BtuiCLL7!8`GC"M*C0b)>Z_tn9O;\uNA<Bu![+4MFR)E5^23rrVgVVG2'eT>qZ8m+8+Anj$`
DTUI)WrMdT\le[,^Fm<FBj]A'6eV[/^41nIX0+66Lo1r<0sVT.9l(UDoO.!HbfNmGJ+nli.*P
=Hfs7@f+GiE5i,f=7)A\C:S%MX>MaZtT4dUS><dFnf37g)U:@r/&2oS>]A;E?r<Z+0;Ve"Vo/
C5XkZG6Pqp!J%$Nt8Fh<<0)%VQ&sPi7c`M2ZCT1HH0"U_&"4j-)Spah,*3]A7dq9AX+(5K$9W
[@G5VHnL&kQql2K)>0.HKdJ^T54qVbZR)o'8LUYc2NifetVeid(I,>G3.BdKo1]A(m8sFM$3f
>^Z/boh?`5k*uW0c&>R'o6QT"o)c>Z8'Xs2$MH>gRm-Q^[H!b6s0+pWUnA_mUNNgnpU_3!Q%
pFUV4FOTLm56rFJ<SX/$\H(?;uk97a98Ri31kj`>lkt&>(Aioj<T-7BAWJ$_[Fq3K&@<.b"C
knDW#)]A7IQY0.)jg7KY6sQ,>s4,T,,1mFM)_,j4;b/pZ&W9.eYXj&<<I!2d[s73?RG%mLb=V
R?bYD>>+qs%>&OfRBFmZ!5d_VPst+X=TU*=3ch+d*jLVoE:#VN'W!HNR*hOU`4EGV<T@'@_'
r1&G]AG=l[O65(Q$'Sl/;31b1Nc8gtP,q=L[2bSK6<,L,e9@j[`l=Yk[:ORsR(o!n*]A8D6<@I
BuVSjK2XM/fV`=LbjeV<1qH[%U">,Nptq0jX8N$n_GD2W7akb7'#+NJ`kEqb^A2+9KuKeXn$
AE6jN[/nC=a+%"K7PBEZX4>!il7T]ANu+XmnK-d-/%kpP_qlJVAie.HG5m$b4SkiH8MS2]A9#\
1o`(pS>g+c'Ajn`,0Q7oOhQV2Y`urS)/jKBbo$aKb5?hR)kFGJe7JG:s4&@+O8R@X'6<$8;V
b0-kHa4t*,]Acu"5hhKF;4t=T$/N/FG4=!>jZG4UQ+l!IA2!3QW[tiTXr=JC0BMTShe_n2g#g
fZZ"rul*50>b1naeZ-_JERDobDP2F'2NZ!(:`T)dVT^;aGZih"=*Q*L5]A0Vs3p,4R,9U3bUC
WH[;Fn8@XCSMo/fIS.0Hl0LX_PlLPQ\HnDtB<jaeoj<]A"D?#fUn>/arb0t,[:$&JKa(Y(-:6
bG]AVWS'8M\;kSG"FbF(.`8TBoD0I/XFk7W=MbUpu2MYjcR<-Ms#o<;Eh2[]A08a7W?ZKmXn,.
nj^P;Hp,Utk8GTp>'Hji3c!/$P?UTqq%/;'WrC_/'TANM(4S0\<!frGEQFQ?Z<pB>AJWpXUr
ZI$3dA5XOH`@Zb[Ra4/H_.05/5p-Z?`;nnMBh>^.@1_D7s4mJP41[]A2f_Xp+<pE77BJr(KL0
bFhj!`q;,3D>Ap\FtB$i*h@I;+O/#j.T3A7pf7KJXD/tu@k!CZ5mdSD9\&(^i`hCLSE<S['a
G')XQc$6i#?+c<08F6iI4o*uOoDaJ\;R*!odaeAW_P,iI/QQ[EW6smp^TrDfTUD8gV\<W?WV
csi$Ddjk^Q_>+ET99]A8E4m^*=:4:&PalYWd((8Tlm+%s4lRsRQ80*>qGAuPSSqRGVNo2HasN
j=Gjj,2AJKR^%^;DGp4oodKlU:PRV_kQ1LX&Fsr#+JMT*W_u?-2r\SeDePks?p'XCcU0?LNH
6N`([]A!AQnI,EI^]A+2!F]AkOR+=Z**#7W1PA'm;:p'DRcdEh.C3m(YcKm>*1Rs*fZFh3&uDZ5
U::"QQR#G5WV/lJ!o'kN49*+AVtNXrnPTW6PWh9fj9^thl5G%,<am\4-n^$Gf02_'aA",4mW
c;b`D]A*RAO[n'a?8Ii]AP#LEEE3<-mp.R]A(ZcM/]AYrB=M/91OQO8K-i6cd"s,EX%[L_aTnpju
K]A\TtO1rJHfP,.hHEjI-u%LZE"$jq9#=[;9;bPVsSEtr0?d!#`Mld]AIj+h-(qrf2I$+"?;c%
V-te#7^$Mc.KG:D5DI&k)hi)jnULPnWMbt_ejC6SK"`orCV(uPGO1ZP8Ob`s#]ADN\d0tm+[9
6:O#Q1DCmh?$qV"AN.LU-noheo^.#3bVf`<m'IO28VfYDh[D<?$=0f$usGe3H3nF"Yk]Aa')V
roe7-fO_?eJ%M]AJjg"$focIj0+_o$4Q5[m`acML(X8='muMe24T19rrDkM=2&--_B),g36_T
Ciql/iI]ABrTP&?1!j<Idd+AN<^$K`5;8_2(cq,q'h`fP`JsngN?<O^>s81C)5'.)5Yl'<eE0
67E'L?+$Q4O$hO,0:e"(l!*!O)'-kkck\DChRl!+ogATJ80FQU@tEn:M7c:=%4nLls"I[na=
3V<F=+F<h-7G36[goYG?qeNXK10Gh137@,L*-,:eLN_tfc2\Olkc.bWtA^d_uK]AU8Pf;?3mU
M(>q41q2Yr:;'3AsKLu_WGR<<>P;P4:7U`i,So"fM1"o&[MQ0_+lFC<13UZG<Wqs&0RU6(3p
-?.@X+=hskH@iidp,nYK/3(LG0[JL(!YnDW^.a2&i]A)cd3&r-Z<l.S#M.mtmS[V]A_d3q$W[o
,c)+8K0*4Vq(S<!agM"ocRq<]A)Un;mLAMndW[W50:$[&+10(QPPm5%`(B1sGAP1h\WCpg!.h
-B0)be]A*p/L=.AJAHO:;?rd\k7t+;3i@k!53f1ep]A-o<2C*Cq+5.tRRVD62*#H]Ap>5ji`,25
`/So:W6_'#hm/2=..h[canC*k#B[qGVaATVJ_#brp<&oLX55IZMp>otniCj:L0`h#+jg%d3[
+"(iaUD/%,!8T.:%_$XDD1pP&q'O6"/Wp2+TTY*V&7*8cm-/eOjm66.cKIW`VuKd"6Bi$X3&
qFZS6Rq&lXkKnF=X9R\l#i7]AsQafs-#Bj3;FGBGpY@HKutJF=#C8BmRlr80i4qopF/IQ)t+I
GnLqtb$d3_CFAQkQdd\*,OH"d!0"q77YH9nFA"IDXURlq9ISX>b2%APr%NZ(f[1V1FIc;H4"
AF85I4VmJI$Z1)T1P4.2t:QjIO&[A'Lu8LdREc_UaGkR\[3g57=oWI>]AXd^]AsE;n<8d+k29W
b/,jb]A?cNhF.@fYpEl"2u,G(PnPX?]A13"&T<Lp?U/(80/[BhU["E`JuC.'9'"a['kC@`8&Nk
YNlma:g?K(84r;*&Bpip35u_YB#j?k6`.!<cWsqPb)ctI!4msKr,kiVACWo[Wsol8<1@*,1o
--1hBpfTZ))D<8#uaeja4m6b0(I0)q*?U&6&<k##5pUr:oUcas'Z3E["@6nX>OZ#CKCc^60A
P!=J"74I[F&aaNJQ`X@X1>(7SP@h!O;Jr_77\J9j$hI(W0N*AHF"r'XR=kMV>Q-_Y9n?Hk5?
d,&8uW/934!C-YL8p`*<4jK>(9!K69!;@RL0Be!#0qVn$2mNn!i?%rZ;~
]]></IM>
<ElementCaseMobileAttrProvider horizontal="1" vertical="0" zoom="true" refresh="false" isUseHTML="false" isMobileCanvasSize="false" appearRefresh="false" allowFullScreen="false"/>
</InnerWidget>
<BoundsAttr x="0" y="0" width="960" height="237"/>
</Widget>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.ui.ChartEditor">
<WidgetName name="chart0"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<Margin top="0" left="0" bottom="0" right="0"/>
<Border>
<border style="1" color="-4144960" borderRadius="0" type="0" borderStyle="0"/>
<WidgetTitle>
<O>
<![CDATA[新建标题]]></O>
<FRFont name="宋体" style="0" size="72"/>
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
<OneValueCDDefinition seriesName="產品" valueName="銷量" function="com.fr.data.util.function.SumFunction">
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<TableData class="com.fr.data.impl.NameTableData">
<Name>
<![CDATA[ds2]]></Name>
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
<BoundsAttr x="414" y="237" width="546" height="303"/>
</Widget>
<Widget class="com.fr.form.ui.container.WAbsoluteLayout$BoundsWidget">
<InnerWidget class="com.fr.form.ui.ChartEditor">
<WidgetName name="chart1"/>
<WidgetAttr description="">
<PrivilegeControl/>
</WidgetAttr>
<Margin top="0" left="0" bottom="0" right="0"/>
<Border>
<border style="1" color="-4144960" borderRadius="0" type="0" borderStyle="0"/>
<WidgetTitle>
<O>
<![CDATA[新建标题]]></O>
<FRFont name="宋体" style="0" size="72"/>
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
<NameJavaScriptGroup>
<NameJavaScript name="动态参数1">
<JavaScript class="com.fr.js.ParameterJavaScript">
<Parameters>
<Parameter>
<Attributes name="product"/>
<O t="XMLable" class="com.fr.base.Formula">
<Attributes>
<![CDATA[=SERIES]]></Attributes>
</O>
</Parameter>
</Parameters>
</JavaScript>
</NameJavaScript>
</NameJavaScriptGroup>
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
<OneValueCDDefinition seriesName="產品型別" valueName="銷量" function="com.fr.data.util.function.SumFunction">
<Top topCate="-1" topValue="-1" isDiscardOtherCate="false" isDiscardOtherSeries="false" isDiscardNullCate="false" isDiscardNullSeries="false"/>
<TableData class="com.fr.data.impl.NameTableData">
<Name>
<![CDATA[ds1]]></Name>
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
<ChartMobileAttrProvider zoomOut="0" zoomIn="2" allowFullScreen="true"/>
</InnerWidget>
<BoundsAttr x="0" y="237" width="414" height="303"/>
</Widget>
<Sorted sorted="false"/>
<MobileWidgetList>
<Widget widgetName="report0"/>
<Widget widgetName="chart1"/>
<Widget widgetName="chart0"/>
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
<TemplateIdAttMark TemplateId="099f746c-b357-4e9c-a26f-773769fe570d"/>
</TemplateIdAttMark>
</Form>
