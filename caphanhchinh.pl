country(vietNam).
region(dongNamBo).
region(tayNguyen).
region(bacTrungBo).

province(dongNai).
province(binhDuong).
province(giaLai).
province(lamDong).
province(quangTri).
province(quangBinh).

city(longKhanh).
city(bienHoa).
district(camMy).
city(thuDauMot).
city(diAn).
city(thuanAn).
city(pleiku).
district(dakDoa).
district(kbang).
city(daLat).
city(baoLoc).
district(diLinh).
city(dongHa).
district(camLo).
district(vinhLinh).
city(dongHoi).
district(minhHoa).
district(tuyenHoa).

ward(bauSen).
ward(xuanLap).
ward(hoaAn).
ward(buuLong).
commune(baoBinh).
commune(lamSan).
ward(chanhMy).
ward(hoaPhu).
ward(dongHoa).
ward(anBinh).
ward(anPhu).
ward(binhChuan).
ward(dongDa).
ward(chiLang).
commune(kongGang).
commune(haDong).
commune(dakHlo).
commune(dakRong).
ward(tramHanh).
ward(xuanTho).
ward(locPhat).
ward(locTien).
commune(baoThuan).
commune(dinhLac).
ward(dongGiang).
ward(dongLe).
commune(camChinh).
commune(camHieu).
commune(hienThanh).
commune(kimThach).
ward(bacLy).
ward(dongHai).
commune(chauHoa).
commune(caoQuang).
commune(danHoa).
commune(hoaHop).

include(vietNam,dongNamBo).
include(vietNam,tayNguyen).
include(vietNam,bacTrungBo).
include(dongNamBo,dongNai).
include(dongNamBo,binhDuong).
include(tayNguyen,giaLai).
include(tayNguyen,lamDong).
include(bacTrungBo,quangTri).
include(bacTrungBo,quangBinh).
include(dongNai,longKhanh).
include(dongNai,bienHoa).
include(dongNai,camMy).
include(binhDuong,thuDauMot).
include(binhDuong,diAn).
include(binhDuong,thuanAn).
include(giaLai,pleiku).
include(giaLai,dakDoa).
include(giaLai,kbang).
include(lamDong,daLat).
include(lamDong,baoLoc).
include(lamDong,diLinh).
include(quangTri,dongHa).
include(quangTri,camLo).
include(quangTri,vinhLinh).
include(quangBinh,dongHoi).
include(quangBinh,minhHoa).
include(quangBinh,tuyenHoa).
include(longKhanh,bauSen).
include(longKhanh,xuanLap).
include(bienHoa,hoaAn).
include(bienHoa,buuLong).
include(camMy,baoBinh).
include(camMy,lamSan).
include(thuDauMot,chanhMy).
include(thuDauMot,hoaPhu).
include(diAn,dongHoa).
include(diAn,anBinh).
include(thuanAn,anPhu).
include(thuanAn,binhChuan).
include(pleiku,dongDa).
include(pleiku,chiLang).
include(dakDoa,kongGang).
include(dakDoa,haDong).
include(kbang,dakHlo).
include(kbang,dakRong).
include(daLat,tramHanh).
include(daLat,xuanTho).
include(baoLoc,locPhat).
include(baoLoc,locTien).
include(diLinh,baoThuan).
include(diLinh,dinhLac).
include(dongHa,dongGiang).
include(dongHa,dongLe).
include(camLo,camHieu).
include(camLo,camChinh).
include(vinhLinh,hienThanh).
include(vinhLinh,kimThach).
include(dongHoi,bacLy).
include(dongHoi,dongHai).
include(minhHoa,chauHoa).
include(minhHoa,caoQuang).
include(tuyenHoa,danHoa).
include(tuyenHoa,hoaHop).

belongto(X,Y) :- include(Y,X).
includes(X,Z) :- include(X,Z).
includes(X,Z) :- include(X,Y), includes(Y,Z).
belongsto(X,Z) :- belongto(X,Z).
belongsto(X,Z) :- belongto(X,Y), belongsto(Y,Z).
sibling(X,Y) :-  belongto(X,Z),belongto(Y,Z),X\=Y.
