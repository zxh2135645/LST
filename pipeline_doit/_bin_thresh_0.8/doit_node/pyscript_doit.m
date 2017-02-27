fprintf(1,'Executing %s at %s:\n',mfilename(),datestr(now));
ver,
try,
        %% Generated by nipype.interfaces.spm
        if isempty(which('spm')),
             throw(MException('SPMCheck:NotFound', 'SPM not in matlab path'));
        end
        [name, version] = spm('ver');
        fprintf('SPM version: %s Release: %s',name, version);
        fprintf('SPM path: %s', which('spm'));
        spm('Defaults','fMRI');

        if strcmp(name, 'SPM8') || strcmp(name(1:5), 'SPM12'),
           spm_jobman('initcfg');
           spm_get_defaults('cmdline', 1);
        end
        
        jobs{1}.spm.tools.LST.doit.bin_thresh = 0.800000;
        
            jobs{1}.spm.tools.LST.doit.data_ref{1, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4627/ms1236-mse4627-008-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{2, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4561/ms1110-mse4561-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{3, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4516/ms925-mse4516-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{4, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4488/ms875-mse4488-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{5, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4540/ms1073-mse4540-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{6, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4346/ms548-mse4346-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{7, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4475/ms865-mse4475-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{8, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4502/ms903-mse4502-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{9, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4496/ms889-mse4496-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{10, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4601/ms1195-mse4601-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{11, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4530/ms1054-mse4530-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{12, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4397/ms714-mse4397-008-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{13, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4379/ms692-mse4379-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{14, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4304/ms175-mse4304-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{15, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4639/ms1249-mse4639-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{16, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4416/ms758-mse4416-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{17, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4325/ms494-mse4325-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{18, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4715/ms577-mse4715-051-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{19, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4665/ms1298-mse4665-015-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{20, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4424/ms773-mse4424-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{21, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4360/ms592-mse4360-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{22, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4457/ms839-mse4457-008-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{23, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4624/ms1230-mse4624-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{24, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4653/ms1277-mse4653-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{25, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4586/ms1147-mse4586-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{26, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4562/ms1111-mse4562-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{27, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4534/ms1060-mse4534-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{28, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4498/ms898-mse4498-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{29, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4708/ms172-mse4708-011-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{30, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4338/ms534-mse4338-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{31, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4495/ms888-mse4495-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{32, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4406/ms727-mse4406-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{33, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4471/ms862-mse4471-008-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{34, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4097/ms1784-mse4097-039-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{35, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4533/ms1059-mse4533-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{36, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4434/ms798-mse4434-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{37, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4611/ms1210-mse4611-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{38, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4666/ms1304-mse4666-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{39, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4462/ms842-mse4462-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{40, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4512/ms919-mse4512-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{41, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4213/ms1711-mse4213-032-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{42, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4417/ms759-mse4417-028-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{43, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4589/ms1157-mse4589-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{44, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4452/ms835-mse4452-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{45, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4522/ms929-mse4522-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{46, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4656/ms1281-mse4656-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{47, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4316/ms248-mse4316-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{48, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4509/ms908-mse4509-008-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{49, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4473/ms863-mse4473-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{50, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4095/ms1738-mse4095-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{51, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4305/ms176-mse4305-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{52, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4648/ms1267-mse4648-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{53, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4391/ms706-mse4391-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{54, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4347/ms558-mse4347-012-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{55, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4490/ms882-mse4490-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{56, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4403/ms720-mse4403-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{57, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4651/ms1276-mse4651-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{58, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4366/ms627-mse4366-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{59, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4428/ms786-mse4428-034-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{60, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4489/ms880-mse4489-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{61, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4564/ms1113-mse4564-006-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{62, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4725/ms714-mse4725-027-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{63, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4628/ms1237-mse4628-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{64, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4622/ms1227-mse4622-008-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{65, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4521/ms927-mse4521-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{66, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4577/ms1127-mse4577-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{67, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4298/ms165-mse4298-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{68, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4535/ms1062-mse4535-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{69, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4392/ms707-mse4392-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{70, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4301/ms173-mse4301-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{71, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4398/ms716-mse4398-008-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{72, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4594/ms1179-mse4594-008-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{73, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4570/ms1122-mse4570-019-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{74, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4604/ms1200-mse4604-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{75, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4456/ms838-mse4456-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{76, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4421/ms765-mse4421-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{77, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4381/ms693-mse4381-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{78, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4625/ms1231-mse4625-029-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{79, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4419/ms762-mse4419-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{80, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4413/ms736-mse4413-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{81, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4710/ms198-mse4710-027-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{82, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse3727/ms1624-mse3727-077-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{83, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4754/ms1206-mse4754-011-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{84, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4751/ms1136-mse4751-011-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{85, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4739/ms779-mse4739-011-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{86, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4482/ms870-mse4482-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{87, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse4348/ms563-mse4348-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{88, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse5390/ms843-mse5390-050-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{89, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse5702/ms816-mse5702-008-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{90, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse5651/ms695-mse5651-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{91, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse5630/ms249-mse5630-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{92, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse5789/ms1168-mse5789-014-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{93, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse5793/ms1207-mse5793-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{94, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse5771/ms1053-mse5771-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{95, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse5801/ms1233-mse5801-012-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{96, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse5806/ms515-mse5806-012-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{97, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse6645/ms1234-mse6645-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{98, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse6662/ms542-mse6662-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{99, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse6691/ms1105-mse6691-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{100, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse5790/ms1199-mse5790-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{101, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse6715/ms1157-mse6715-010-FLAIR_bin_lesion_map.nii';
        
            jobs{1}.spm.tools.LST.doit.data_ref{102, 1} = '/data/henry1/tristan/LST/FLAIR-MPRAGE/mse6714/ms1201-mse6714-010-FLAIR_bin_lesion_map.nii';
        
                    spm_jobman('run', jobs);
                    
,catch ME,
fprintf(2,'MATLAB code threw an exception:\n');
fprintf(2,'%s\n',ME.message);
if length(ME.stack) ~= 0, fprintf(2,'File:%s\nName:%s\nLine:%d\n',ME.stack.file,ME.stack.name,ME.stack.line);, end;
end;