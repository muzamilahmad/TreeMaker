import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/100000/04A18B6F-B193-E611-9BB0-0025907B4FC0.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/100000/060D7204-7D93-E611-A349-001E67792592.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/100000/06940EBF-F195-E611-860E-0CC47A78A418.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/100000/08A47D1C-F595-E611-AE0F-0CC47A4D769E.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/100000/0E47B9F8-7C93-E611-86A5-0090FAA597B4.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/100000/0EBE13D6-F895-E611-BD3F-0CC47A78A414.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/100000/1A087F72-EB95-E611-884A-0025905B860C.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/100000/1A7061B2-0696-E611-AE02-0CC47A4D75F4.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/100000/1CC7599C-2D93-E611-826E-848F69FD2925.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/100000/1E46B47E-3F96-E611-8BA0-0CC47A4DEE0C.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/100000/2085AFB2-8F94-E611-916A-008CFAFBF6CC.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/100000/2AA94AF2-8793-E611-8397-001E67E7187B.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/100000/2C10BF58-A096-E611-8CF4-002590DB928E.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/100000/2C33B3E9-7393-E611-8E58-001E67E71381.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/100000/2CB14DCD-E395-E611-91FD-0025905A612E.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/100000/2EC37DC1-9993-E611-9696-002590AC4C6C.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/100000/30A44672-2493-E611-A592-008CFAF74A86.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/100000/3671BA27-9693-E611-829A-001E677924C6.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/100000/388A2685-6A94-E611-AF04-0242AC110003.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/100000/44E02B2E-A896-E611-A6F8-0CC47A7452D8.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/100000/4AF09863-E195-E611-8979-0CC47A7C3404.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/100000/4AF67792-8993-E611-943C-002590D0B096.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/100000/542F5729-E795-E611-8303-0CC47A4D76D2.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/100000/5AB5CDA6-A093-E611-ADF2-001E677924B2.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/100000/5C96D7F5-E495-E611-90A3-0025905B8590.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/100000/6427671B-D895-E611-8112-0CC47A745284.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/100000/6C5B35ED-DE94-E611-B4DD-C4346BC8C638.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/100000/781EAE99-2D93-E611-9928-0CC47A4DEEDE.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/100000/7A044BE6-7696-E611-821E-00266CF9B318.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/100000/7E8E7501-8D93-E611-80D4-0CC47A4DEE0C.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/100000/841BE243-9693-E611-A083-7845C4FC39C5.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/100000/84B83EF1-8F93-E611-B018-008CFAFBEC9A.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/100000/88BB0813-7F93-E611-9AD5-848F69FD4553.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/100000/8A07120F-A493-E611-9DB1-6CC2173BBE90.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/100000/8ADD7863-8193-E611-94B8-0090FAA57C60.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/100000/8AEB7428-0A96-E611-A63E-0CC47A7C34A0.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/100000/907F19FB-E193-E611-BA1C-00266CFF090C.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/100000/9093E0EF-DD95-E611-9814-0CC47A7C345E.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/100000/924F2B98-C093-E611-8B10-848F69FD4ED1.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/100000/9458D482-9F93-E611-B3A3-20CF3019DF0F.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/100000/96D79C5F-A896-E611-BD12-0CC47A4C8ECE.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/100000/9C8D2660-AF94-E611-A581-00266CFFCC50.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/100000/9CB95718-EE95-E611-AB8A-0CC47A4C8E16.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/100000/A44E7031-E395-E611-827D-0025905A6056.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/100000/AC59CE04-9C93-E611-B5FF-008CFAFBF52E.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/100000/AE7632AB-A295-E611-8307-008CFAF73190.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/100000/B8CD418D-E195-E611-8119-0CC47A4D76C0.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/100000/BCF276E0-F895-E611-BA74-0CC47A7C3422.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/100000/D21AF52B-E795-E611-8B43-0025905B85CC.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/100000/D45EFCF1-DD95-E611-B34B-0CC47A4C8E34.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/100000/DE7F58A9-A693-E611-A8F8-7845C4FC35B7.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/100000/E672926D-9493-E611-8C7D-0CC47A4DEE88.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/100000/F0884E36-E395-E611-BCBC-0CC47A78A2EC.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/100000/F2AA033A-8693-E611-AF19-7845C4FC36E0.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/100000/FA7973C1-6B94-E611-85F1-001E677926A2.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/100000/FCEA5099-7F94-E611-BEE6-002590D0B06A.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/110000/38F652EC-6797-E611-A1D7-0CC47A7E6AA2.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/00245E1E-C895-E611-B147-0CC47A78A30E.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/005D7FBC-B695-E611-9CB6-0CC47A4D76D2.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/02396269-BC95-E611-8BBC-F8BC1234F309.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/02951EA5-C295-E611-82C5-00259029E84C.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/06F70A25-7796-E611-A5D8-0025905A60FE.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/0A3C02B3-D195-E611-B100-0CC47A7C3404.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/0A3F75B0-A995-E611-B714-003048FFD72C.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/10C9D3B5-CE95-E611-9FFE-00259055C83A.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/1295A288-CD95-E611-A801-0CC47A745298.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/1457EFB0-AD95-E611-B9DA-0CC47A4C8E46.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/16B76D89-B895-E611-B144-0CC47A78A418.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/181257E6-BA95-E611-BC08-0242AC130004.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/1CE7A797-C695-E611-B63B-008CFA1974DC.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/1E3DE6D3-D595-E611-8007-0CC47A4C8EE2.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/2C6A2FCE-C595-E611-877E-0025905B85BE.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/36750A8A-BA95-E611-BC5B-0CC47A78A4B8.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/36A9473D-C895-E611-8254-0CC47A7C3430.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/3CFAF3E7-B095-E611-A01D-0025905B85D8.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/44394F50-D895-E611-AEE3-0CC47A4C8ECE.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/44E6A9A7-BF95-E611-8035-0025905A60EE.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/4881453C-C895-E611-8B7E-0CC47A78A41C.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/4EA9B653-C195-E611-A60F-0CC47A78A418.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/5010761F-CD95-E611-AC33-0242AC130003.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/50BE53E8-C395-E611-9131-0CC47A4D7666.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/56DEDE64-A595-E611-8388-0CC47A4D7600.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/56ED51EA-BB95-E611-8138-00259048AC9A.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/58893987-B295-E611-B387-0242AC130002.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/58E44D7F-7796-E611-82C8-00259073BBF6.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/5EA0FA39-BD95-E611-BB8F-0CC47A4D76BE.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/5EF308FF-B995-E611-8807-008CFA197C70.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/607FFA80-B895-E611-8EC8-0CC47A7C3422.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/62474DB7-7896-E611-BEBF-008CFA002634.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/72E8B283-A595-E611-875D-0025905AA9CC.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/74D80F52-1996-E611-B796-0025905746AC.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/76264C7C-7696-E611-A807-001C23C0D109.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/7EE334E4-CA95-E611-8E00-0CC47A745298.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/82228995-CD95-E611-AF24-00304867FD03.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/8480BBFC-C995-E611-BD7C-00259055C83A.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/88BBFB22-BB95-E611-86EA-0CC47A78A3B4.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/8A020721-7796-E611-8129-0CC47A74527A.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/8AF9D5CD-B495-E611-806A-0025905A6132.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/8C366BE0-C395-E611-AE61-0025905A6060.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/90D65D91-C295-E611-B633-003048FFD72C.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/9663B49C-D295-E611-A00F-00259055C83A.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/98CE59A8-D795-E611-B205-008CFA197C80.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/9A6A1FF4-BE95-E611-B891-0242AC130003.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/A09D5B0C-C895-E611-9E12-00304867FEBB.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/A2D269D5-C895-E611-B390-B083FED02AD1.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/A4DB8D10-C895-E611-865D-0CC47A7C3444.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/AAE0E27E-BD95-E611-ACA5-0CC47A4C8E46.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/AE9BEB95-B695-E611-80FE-0CC47A78A360.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/AEB1E943-B395-E611-93BD-0CC47A4D760A.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/BC09108F-C295-E611-A4C8-0CC47A7C3430.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/C2A4C5C7-BA95-E611-9C87-0242AC130003.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/C6494FEE-B695-E611-B7E5-0CC47A4C8E1E.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/C8EEC764-C695-E611-AC60-0242AC130002.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/CE7DBFBE-A895-E611-B5BC-0CC47A4C8EC8.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/D27189D5-CA95-E611-8EC9-0CC47A7C346E.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/D450BA8A-B395-E611-8A59-00259075D702.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/D461F5D6-CA95-E611-9819-0CC47A4C8F0C.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/D4CBDD18-F095-E611-A1E9-0CC47A78A414.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/D64778F9-BF95-E611-9355-0CC47A7C346E.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/DEB218FE-B695-E611-BEF8-0CC47A4D7604.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/E0045580-7696-E611-A276-00259029E66E.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/E0576BE9-AE95-E611-9198-0CC47A4C8E1E.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/E091C24E-B395-E611-9D35-C81F66B7ED99.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/E098F643-E795-E611-8B26-0CC47A57CDD2.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/E88D3F56-C195-E611-8897-0025905B858E.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/E8ABA67E-CD95-E611-BA4E-0CC47A78A3EE.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/EA7C2B3A-5096-E611-8A09-6CC2173BC350.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/ECA5CA59-B295-E611-A5FA-0CC47A78A3F4.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/F4C15E61-D495-E611-BA71-003048FFD734.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/F8869110-CF95-E611-8439-003048FFD72C.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/FAC4EF7E-7696-E611-9EC3-0242AC130003.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/50000/FE1E215C-B595-E611-891A-0242AC130006.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/70000/02EAC6DD-E591-E611-806F-20CF3027A5D5.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/70000/06DE0605-D395-E611-8D9A-0CC47A7FC700.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/70000/102146AD-AD95-E611-A045-008CFA0014EC.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/70000/14992CB0-E895-E611-BAC2-001E67E6F8D2.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/70000/1A463CE6-B395-E611-AA09-0CC47A7FC7B2.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/70000/20596C57-1B92-E611-9AE5-0CC47A1DF7EE.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/70000/2A405D91-B595-E611-9BD4-F04DA275BFA7.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/70000/2EE5ECDA-A195-E611-AE1A-008CFAF0842A.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/70000/36D1E4B8-D295-E611-AB03-0242AC130003.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/70000/4CBE7B41-C792-E611-AEF1-0CC47A7FC46A.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/70000/5E1F71C9-8D95-E611-A530-0025907B4F6C.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/70000/5E89D723-6895-E611-8DB3-0CC47A7E010A.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/70000/60F80C34-9895-E611-829A-00259073BBF6.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/70000/6411921A-C792-E611-AA92-F04DA23BCE4C.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/70000/702985F9-D295-E611-89F4-848F69FD4EB6.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/70000/78F74FD1-3894-E611-BDE2-848F69FD2925.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/70000/8A5C6577-B495-E611-960D-0CC47A1DF7EE.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/70000/8CC0593B-7895-E611-BDEF-7845C4FC39AD.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/70000/96C7EB67-7695-E611-BBB1-E41D2D08E0B0.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/70000/96EE2609-2E94-E611-86E5-001E677924B2.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/70000/9A3D9B7E-9095-E611-8052-F04DA275C013.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/70000/A84B0B80-A395-E611-BD11-00266CFEFE08.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/70000/A8782B84-A592-E611-819A-00266CFEFCE8.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/70000/AC221470-4A93-E611-AEBD-7845C4FC35B7.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/70000/AE5D8A04-D395-E611-951B-0025905B8594.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/70000/B2A4C3A1-C095-E611-87E7-848F69FD29FA.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/70000/B46AC632-BA95-E611-A9EE-008CFAFBE5CE.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/70000/B649A4FB-D295-E611-A07E-0CC47A4D9A6E.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/70000/C20B6EC7-D395-E611-B232-00266CFFBF88.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/70000/C8EE04F2-A695-E611-A96B-001D09FDD7C8.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/70000/CC40983B-8692-E611-9AD8-008CFAFBF1EC.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/70000/CEDB77FC-EE91-E611-90FD-0CC47A4DEDD2.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/70000/D28438C7-E792-E611-A5F5-0090FAA58204.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/70000/D88E6715-8A95-E611-B559-008CFA002184.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/70000/E00CD4CE-8D95-E611-971F-0025905B85EE.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/70000/E4B275CB-9A95-E611-B9EB-002590A83136.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/70000/E60DB8EB-7B95-E611-A231-0025907B4F50.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/70000/EA180BEC-E591-E611-A8BE-848F69FD3FAA.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/70000/EA19516E-6E95-E611-8EF1-0CC47A1DF5FA.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/70000/ECB18503-D395-E611-8066-0CC47A78A408.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/70000/F4378EE7-8A95-E611-9570-0CC47A7FC844.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/70000/F6F6E8B3-6695-E611-AAD2-00266CFEFE08.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/70000/F8CCAED0-BA95-E611-92C8-0025907B4FAE.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/70000/FCE0810F-CD95-E611-B6AD-0025907DCA0C.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/90000/06162E27-4192-E611-A6DF-0025907B50D6.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/90000/1C262180-E995-E611-B7B9-002590D0AF6E.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/90000/2C886E84-E995-E611-B6C6-00266CFFC4D4.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/90000/2E9572D2-8D95-E611-BD6C-0CC47A7E6A8E.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/90000/32F80278-8D94-E611-BC15-002590AC4CEC.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/90000/36D6DD05-8D95-E611-B545-002590D0B0D8.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/90000/3AC22C83-E995-E611-8E12-0025905A60A6.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/90000/3C022614-0793-E611-B122-001E67E340DE.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/90000/4646491B-4195-E611-A320-7845C4FC39A7.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/90000/609ACFA2-9295-E611-856F-00266CFFBF88.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/90000/687C1C5C-8995-E611-9D6C-0CC47A4DED4E.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/90000/8C169AD4-3792-E611-9D72-001E67E6F5D0.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/90000/92FCD2C4-F992-E611-8BB9-0025907DC9F2.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/90000/94A50107-F792-E611-9AFB-00266CFFBE14.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/90000/9E93B01C-D692-E611-85A9-7845C4FC3B0F.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/90000/A2AEE55D-8995-E611-ACD8-002590D0AF9A.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/90000/A2C3DF62-8995-E611-9D27-848F69FD4ED4.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/90000/A6FB3BF8-DD95-E611-B51B-0CC47A78A408.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/90000/BA8C98AF-E895-E611-946D-002590A83192.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/90000/CE8DA2C3-0893-E611-B2F8-20CF3027A5AD.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/90000/D426AB92-E995-E611-A03A-00266CFFA7C0.root',
       '/store/data/Run2016F/HTMHT/MINIAOD/23Sep2016-v1/90000/E0299068-E895-E611-8A7A-008CFAFC043A.root',
] )
