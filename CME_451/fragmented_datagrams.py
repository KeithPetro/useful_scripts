#CME 451 - Lab 5 -Exercise 2.1 V2.0

def createHTMLOutput(packetData):
    htmlFile = open('results.html', 'a')
    htmlData = ('<table>'
               '<tr>'
               '<td colspan="32"> IP Packet </td>'
               '</tr>'
               '<tr>'
               '<td colspan="4"> Version = ' + str(packetData['Version']) + '</td>'
               '<td colspan="4"> HLEN = ' + str(packetData['HLEN']) + '</td>'
               '<td colspan="8"> TOS = ' + str(packetData['TOS']) + '</td>'
               '<td colspan="16"> Total Length (Bytes) = ' + str(packetData['Total Length']) + '</td>'
               '</tr>'
               '<tr>'
               '<td colspan="16"> Identification = ' + str(packetData['ID']) + '</td>'
               '<td colspan="3"> Flags = ' + str(packetData['Flags']) + '</td>'
               '<td colspan="13"> Fragmentation Offset = ' + str(packetData['Fragmentation offset']) + '</td>'
               '</tr>'
               '<tr>'
               '<td colspan="8"> TTL = ' + str(packetData['Maximum Routers Left']) + '</td>'
               '<td colspan="8"> Protocol = ' + str(packetData['Protocol']) + '</td>'
               '<td colspan="16"> Header Checksum = ' + str(packetData['Checksum']) + '</td>'
               '</tr>'
               '<tr>'
               '<td colspan="32"> Source IP Address = ' + str(packetData['Source IP']) + '</td>'
               '</tr>'
               '<tr>'
               '<td colspan="32"> Destination IP Address = ' + str(packetData['Destination IP']) + '</td>'
               '</tr>'
               '<tr>'
               '<td colspan="32"> Option (If Any) = ' + str(packetData['Option']) +  '</td>'
               '</tr>'
               '<tr>'
               'Data = ' + str(packetData['Data']) + ''
               '</tr>'
               '</table>')
    htmlFile.write(htmlData)
    htmlFile.close()
    
def fragmentDatagram(packetData, fragSize):
    fragments = []
    length_remaining = packetData['Total Length']

    while(length_remaining >= fragSize):
        if(length_remaining == fragSize):
            if(packetData['Flags'] == 0):
                flags = 0
        else:
            flags = 1
        fragments.append({'Version': 'IPv4', 'Total Length': fragSize, 'Protocol': 'TCP/IP', 'Maximum Routers Left': 128, 'HLEN': 5, 'TOS': '', 'ID': 45678, 'Flags': flags, 'Fragmentation offset': packetData['Fragmentation offset'] + len(fragments)*(fragSize-packetData['HLEN']*4)//8, 'Checksum': 0, 'Source IP': '127.0.0.1', 'Destination IP': '127.0.0.1', 'Option': '', 'Data': (packetData['Data'])[len(fragments)*(fragSize-packetData['HLEN']*4) * 2:(1+len(fragments))*(fragSize-packetData['HLEN']*4) * 2]})
        length_remaining = length_remaining - fragSize + packetData['HLEN'] * 4

    #grab another fragment if there is data left
    if(packetData['Flags'] == 0):
        flags = 0
    else:
        flags = 1
    if(length_remaining != 0):
        fragments.append({'Version': 'IPv4', 'Total Length': length_remaining, 'Protocol': 'TCP/IP', 'Maximum Routers Left': 128, 'HLEN': 5, 'TOS': '', 'ID': 45678, 'Flags': flags, 'Fragmentation offset': packetData['Fragmentation offset'] + len(fragments)*(fragSize-packetData['HLEN']*4)//8, 'Checksum': 0, 'Source IP': '127.0.0.1', 'Destination IP': '127.0.0.1', 'Option': '', 'Data': (packetData['Data'])[len(fragments)*(fragSize-packetData['HLEN']*4) * 2:(1+len(fragments))*(fragSize-packetData['HLEN']*4) * 2]})
    
    return fragments

MTU_ETHER = 1500
MTU_X25 = 576
packetData = {'Version': 'IPv4', 'Total Length': 5020, 'Protocol': 'TCP/IP', 'Maximum Routers Left': 128, 'HLEN': 5, 'TOS': '', 'ID': 45678, 'Flags': 0, 'Fragmentation offset': 0, 'Checksum': 0, 'Source IP': '127.0.0.1', 'Destination IP': '127.0.0.1', 'Option': '', 'Data': '84538fe87e168e95d3e636cb3cad77fe4c34ab09bee17e9482e93fd15a2f3e15c9d0ba37aa14460632d29991af16d06fca491e1ff56e44db2f2e43324e7d4b2cee1ad15dc9522cb4b2cdf15f402294864a96184cf1fb7dff60d09afee5613efc4584b213a036b4c408d12aa005d2392df2d1b726be741cb98a8224f49eb1251e6b06a3dc40566943a427e16012d0789b5d61f3f3379249ca9f068d3a89422607bb82e521d181f326450d49a89053d6e23afbe286b5006335f20697b2147afad5a7272e2ec943c5708fac71e26be1f7ff7dc42b70664feb78994913b4deabb24a1f1edcd468bf34f25699db82754c1dedbb7cea5f77a21b739da54354f43f8e9189d8d27ca3b14d9e28fdbf70202b55787c67255c953f84d81e391006ad8094e509de576791bf4fc45db832a77c32829bdfe4a3ac019837b42ae754569c184e5234f31a9eb3e75b2e2a908da881361646d6dd68a8d63714408a43f5b89e1ffdfcdf9b7d2d3c674ab40b9118bbeb08eed266e1934a4c39f2fc73985bf3af6b4defb470818b3c9c76e1541263acdc10e4af00b65904b74c09758e8b692857915d4f7782ae8d6fafa779926097ac971f770746178d439fdddd9914b947d0e180f467de4ff609d9a72ae1ef6546132fb2db1de4f44969478e3e28351ba666a11f726448522e808dd37b2106830e46111cb087d29e62153becd1847d05d1eeb9a2a998ac7b41fae72347d2a771262edd035fae8592fe1ce0a706108b1fc59f0bbf999aeed9dea6fea53adfe201f83517ef427c262d4522f52054aedee8811fd976e650ec2a5af145aeba6a739380bc3a383aee45cdd995fd5ad28f877a2e9ac9c4eaa4c44f02473c4fd931c23c1b13e54abaa2f8c778052c17fea32322c439f3d8aae592810465e790e25a073878bbb59e11fe6a66c9c0ffb7da647cf59c59f5865dcff10ee6bd000d54151874d89f72e9aef2b0cd50f8d3ca691d2aa54d82b29f046b9141ee25f4098fdc177fe67a06b9cc6744113889875593ec08541b5dc844b18dafb75004814eee831251db3278963e8c0b2dc50fc55ca7f79da17b948400b0a6301fb77ea5059be1e1b0884f62d280f02b6b6e4e4c974c6fd9e74561ac2ab63c5894a52dd1ac1aa7d817b6b6bdbb0d58fa5dec8502fc88d2a2f3f48a6a8d331b7c2911484a7b0c2b4fe372c2e9f7f4a04c714ea083d4f164b57a2d3cc2ee5b5b6d2f05d8fef9b1b734783f147f7e294a6e15dfb94b5ffc03b18258e7fef3f23d2a86f0bd417561b4d6e098edf944f28c1bf40ba31ebe45096e28010c0be7a741ef1eb245074d80bc4e93b9113ef99b50fed63b48eb33ea5b6d707f25d122255091fb8220782244fe4adcf34ef0427975714a7573e01a582a1a6aa920f0b5904099416d273f476ed366c58a8b671096b71e698b75e0b227c4b4238e698a463782988679c39621f4962f586ed3ffb1570fb48c34cf880559f4b381cfefc0155f356e34038bf0509783f26578f352a219600d307926c138b0da85939ea3e3b2c15615b41a2540cc276524b29a7999cd6d075d0b9153756243b25f0683016e5337c0901f3240345c8c65dbc337fe1301bc75ec0c35536c88cb3c19f6759d951e73b6bc2f6e859eadc2a9f9268e61245a3fc4a7a0b5f75968d1151b347c89611f87afe48fef92bddc112e12f660eda737041c5905dabecca445c61823bdb55179e668878c0f82a3746e27e002b15b0dea0cb300936767a39fdbb8d83cbeea17b40f395182343c3e0be6089b2c1d89ff3330ec0ba1753e4468955cdf215d1ea89f9089874a3376aee1270a352e0071f8f0f36025fed0810d135262f4c25340d5a17c234d70e1fb32932c2f54a59a7e25074eedc58062dfb1a66aa0dff300856a60c765b26d95bef60518912212d9209e235a739726a5052278b12e0d1ddf5402defa041c057aaa8c44e9e45ad33563aa43a41e0fdb88d3e43c09360ecfc2594ec88db18d3fe11577e9979e3a4b0eb765ec2a7d2e3245145e29f23831e9eff0d6771824864015429f852b786dff1fd2bb7f9ca2f042c25c4f5b1f732351cb56bf4059afbf830cf3258972b462317d1ae6ae7ac8bfaae04ace24c9850f69d8cf8b68d1a1033af58335b5fd05157075981cd2739d4b60bc14f25a4132b711e75ff37268ddff36ca0247f0a23b779b50fd136041be1939780d26d76e574f151340395e30424e978b278b967fe49a2317b157350767d71074ef097f1ba211b539649fec5b02b5a81565917db3f3292edf5f1e1830a7e8ac7ddb36e800da5d606e3229d02a231b211e665c354d5b2e30b4a5d1668754b9fc5f778d260ed51780897b22eb0c02d463bf6a4bd5fe4145a92018df458e0349981a928933c5e1c16461bbf3a9e34bb29c226ec53d58c052850509a5c485a6cb0f64ab7770d1e68a072e4259aea61009d085c6c89a36c7bcbd3d4e89382e70142b4b02a455f21d9bfe4410d9fda31f02365af8895ca367566fc77ce93a42b45835f5a76d440d2a451b25971e3cd6d5e223269deacfd4a6f600ac9caf03db5ccd814a61ddf3e221175ff5c67ff48c90f68eff46cd47ace1d334caea839ae5d4d5635eea18b850e3a39be3e1fd22e46bfec0fbfe37905c2b351008ae441879e1712132e6788aae5865a68f1b437492210d8810e6e7497e0b519127fd9223c79a0f763a404f13167a55df2e42a9dd3fe2fb255aaf4c5e9996e18ff1553bf9fa16bd883f9629cf677ba8f8355cf749523c0cd6312506d5394a401fb2c34f5528b6416930039ac970d5cb43458411511e29b81c0beca6b21e1546835876f47f8df26c25c75f0f379b87c8ff10a5665ab6af5c884c19760212dbdb6e7ee24fb06920081515b9051e6ce4c0794714d22dd65b2b4b1c0a65542dcbd852e5565fd6b7c6f7ad9c95065746637ad315598c7f2bb243f1c8a17cf77700a2e894b3a3eac1a06670d62a82f4013551643c9bf623d28098f47475bd7de6cf567854cef7786935fb9c24552d85191465370f98d8c3bf62d9a8348f78f358891f19eed0962e3eabc200de9b10102fd1dc5896d682afc9418968bb0be4be424262db1f7a0c77f2ae29b40c7c96a6926c3afd64d3844443d4528f937d1fcef2b6a59c51f0787b9c5bcd5e53bf18b1b01f60b2d7a954800eb7e26c9e01c701895eacc78cd6c49a89562b952a87e394d1d96203c04d141f4dc9d00782eb6ead62b81ac6d004886c829e86c438ac592132ab251cc5eb909ccf32a01424ceeef8857d19f530ba3c7f432c95e4a6cf9fc0c53e9a74c234505d1eee9252f534549187dae9090afe9e70b0196423a462bf21c7a02a2da20bf0d1fc92175b1277c5de99d5311f0fe71d2faa7e96e6e5e9fd9b067499b53958ffd3cfaa121cd78d2ec3e4132749ea5502a1063861f5c3ddbbbad95562947c74812eac8f86c1d4df748c640f1d22bd80b9001e74a3431dfb46cc7f07790b2dccbba06dc61cc920c8554d1b3472f6be85559ba4c11fb9b4c312bac4160e9c79af5ce29eaab5318dbf7ccf5c6652fa8363538a01e190a6e184ffd34ef427022de603ed33da0bf01f3af3f4fe7f5db87a99d577e2d56784c97b64d90f4b4b1aa3d44f9e13aaa56d72dfc8b46de0b0d8db8cd7ef6606fb353099c68bc5e82f942b36313b9fe768de3ed692b919ed5315407e255e993dedd197121e3820565fd941efa0ee4e0ba5ca15247b34291a608b0479ad3bc761ff1caa61be206556ea00f9afb5a56e9774485448bf6f9f9f98dacbc816439d859a2d214c09ecc6a4f86fc265859eea057fa105cd57bde4f5f3b53e8d60055f9e953e3c5eb2a24c87ed89cbfc300ad0f543f31f840092217d5ce78fd4e5de404be00efd65695283d3df7afea084cd28cc30d5f444f08650b4770957411e44351fc1f528b4f0ecc048cf4c0376ad643a64e325cd6955afceb05791d23dbb28371fdaa40dc2215402a228e3347f2980e37ac6bac013bd01b165e7e083fd7ef5b756600522e820752e1fbd503d7592cdaaf3f126753aa7dc68a8dd4621b1e85a30298aa18de5b31889421f76f8bac389a1a61e843f7f5ae57c326a3ae82349d60afd4cb6b535694c4a2cc2bb3df8f472ba5fb7b2edc2afca78fb207c6986f793093817170edbe2ffdb765599d295de688b5a065e8adcb4b419b97db53834d1175fd3727f8c851698e2f77c2efde1d4cf6c3119de44a4b375bdc0cdc936a59b3aca87aa2aa22523d57b47b5ceda27ae97d82ea08e1291c79d3b466c1104552faddab6790b7ce3b8405e9919818c46ea5c84c778609a7c93f79873eb64479c5dc635d23f89285a64949c3c9d6242ed82caaf66660f15bf3a6586e87de6ae202d7236b46ffc20c4ad0de61205d16bf26be3085e48f0c400762e52960acc79742996f898ad619431c25133a1dcba848076cc42cd67e06649c6ddfa205ae885775d047f40ef465f425173227bae083ac89e3796d2ea0a9d491396eaccada2ada3563458a53848f4ffbe3a199e03ddfc6b400bedf6a60150c9ab6585c29e3337f48be95db2e3d5c1670372b2f073cfe6bea254879161578c3ba90aa58266de10065f226e236506b62687b2bde59027a1bcbdc9dfae95df984b89a53cbfea77ee287b72e2c73a00c558453cc7ea8edb8504d1cc579885460dd6d4d3ba3a2ac9f50796bddc7d8bda3b59c148da5d072a553159cbf1e9620719eea418da759af88508ee88505fcc3bbe68cde3280e8d447575b9891586aba0ce2b7b600d3a0f3a1674c32880538b81334c1df172f9d8d5510a99ed96aafd5ebdbdc66d42e3c2c861f174fe27a56d2f390d871aa9a0fb68f4d600bae611baa2424defc0ea0c750e4ce4bab5e1a55217db740c91e16e2117774fee138d77b8594f3f8004417ecde25bea3246d70d0960ec8ffac5cd3a752894d68c22a7aad1fad4e112276aa324ccb58daa3b03259aef232e105b983b19eb17f39e2923e20ee15c8f80f857800bfacbfe653d28b7379c91beb203f8637dfc45a3fc92a5dc9888d6f014344ec0d63b95c62a8606c378c2848fa5ef334ad28b579605430a8cb4605ca48ce4139275e6876d6ce0b25773bee559b5079559dee0a47ddc95c7b6853f52e8881690e468d2817640408337718c3948e82db2efcca851cba6bd8f867e6a64968e47a772b83d6ebb8d586849f044ef31ff75438116e0f878805503d6bc61ae842972f9cccf5e12e24b6bcfde142dd67cd73eb20fae9cd05a4873c311930055251b705e3250942b74f32f04520a6208eb1e510245f700bf1dc37a7122ee4615afb3ff23d19c90d72c575e9dc316201c8bf48c5214efdb7ee127b1ef1ce3f6491f06189e5117c34354990800326e58b02b11ccd887981222efcae172d0c8bd244e8c77b575e320655366e1c34fbba84a27d682237d1e650542652f9c35b00bd7e405157c2423c253f765434fc44162f5cb4903e0fb0abaf1c01be108186ebc3099dbb9cdc48f9eb0eaffe034b9303d8a3e0553f4a1cb747454de8827399d9d24e91ba9d43abf2b1e8fe5685d413e0c5d34fe94ffb7e87dd3a20a2cd00233c7b88bae407a6d00a31d24838b168ebda93e7d55b7d6a3a9aa158af35bbd439fefa045aa8b8d32b4b4d00d2b434aa68373b0611ddf23feccf23ea1bb7737799e96c85385178c04ae0e4f9ed6404575dda0c903c88f7e1e8afb620716801418bc70ebd359aa24adfa759430b4cc2c8d22c89f0750953bdacd84337567e055f1d7fe9fd7369bdd0f02bfbb8576d1e23e3de04be3a9c11cd6769f367e03f534e7ac0936e2905ad761f9517237ef5974b9396388eca0a949b00aa4d1d300b58246a85213f933a9377b4250f8719f112abb40fcbe836265f76f05487fc23860c4ef595b276929216e71dd46109b7c103e2ad7157f0a83d2b2f61875a0f1935ca53d19bb2a3517e9004731ac723f78fad1589bf18c534cb4bd7d957137d08b43f3abe3b831b837e92101f5e766d4562cceca9405aeeed6dd7acabbfd6bcbf298409e5c0f9fb3b4b64b7f05c36ba4c03bf7af3b08ddcf0a23d3fa5491c4a66d8797ccc20e7900d53bde6cf07e69beb95967910eedf5058cf454a4859a58387a8f5957aab3e7386486a4d7550b6ef84179b3017f6b85ccd39a71e55989488da3d594212c145b21d14bf6b355726b58bd6b851d0fddd30bb9ab742d19f92f585e27f7940f052721d4bf1c8bc47148e2d1e8de74dc0925857dc41d68c850e989656ad4bcc9f703e48712f586b860b314eba83d7c8d54420b6dbf216719531d19d7c4b18015157f79c1c73a4e82268ea19bce03f69c542352fb570ae10a4ff1239380c10a94909dd969957b4ff08f16587d237050f486c9f603b0a58b0b50e92d55a007e314ee1d52b41f262983bb016cd398baa5aabfef01ef061c65bb1b048b4fff13a2c52c1b791473c66bc4fee27d7fd8da3e15b63ace86b6b55df63b336fe7fb3da907250f3e992f85cc53b2106d484fc66b17c74cfd30fa20753f9c081f4bb38a6f893c0f845cffc895bc1170e941ab30435fb99a6b81787d9a7f08ebe79c937f4d46a0a3963057708c399f01e390728b7178274b2e7a4ad4319c2bb61b42fb6739b53811e9b3b3eb10503ea9302cf71fc04402f19bb8eb44cd3e697bc4719185d49afad84912e848aca7f8b2e67bc194cb539bc54c6bca6c3ab36b2ea6b11b9ae70dc97c3f9da9c102e8471770b26b326127d3b26c375cf97401a23d558e34f6e3f79ae7b10bb1f4092c1c9a477d51a915d464fab0fc6a936be1e9e0206232a2df9723700dac72b96afb89871f9031f16ff190f2f6426d5608697abe4c7aa8f1829c84ede9409702df2c06a218b8c40067c33f2c2b48b7b67b312b23ea983861bb561bfe96fb48a92184285e2ac36cb82957e7657e1bdf6e35c557d54dd1bb22fb380246979474bf5083d337909a5523a372e7bb047819267052d02347a7ab44aaf11f1439d5935e2b1027b10901665ed5f6253b2f58be7bdf95558ccd0cfcd99082744b5ed04fff2e57bc31d9ed1da332b939e7a0c0ff562a42848ab8c264ac5275814fb32432af88'}
fragments = fragmentDatagram(packetData, MTU_ETHER)

htmlFile = open('results.html', 'w')
htmlHeader = ('<!DOCTYPE html>'
              '<html>'
              '<head>'
              '<style>'
              'table, th, td{'
              'border: 1px solid black;'
              'border-collapse: collapse;'
              'text-align: center;'
              '}'
              '</style>'
              '</head>'
              '<body>'
              '<b>First level (Ethernet):</b><br>')
htmlFile.write(htmlHeader)
htmlFile.close()

for x in fragments: createHTMLOutput(x)

print('First level fragments: ' + str(len(fragments)))

#fragment fragment 2 to go into X25 server
fragments_2 = fragmentDatagram(fragments[1], MTU_X25)

htmlFile = open('results.html', 'a')
htmlFile.write('<b>second level (X25):</b><br>')
htmlFile.close()
for x in fragments_2: createHTMLOutput(x)

print('Second level fragments (X25): ' + str(len(fragments_2)))

#write footer
htmlFile = open('results.html', 'a')
htmlFooter = '</body>'
htmlFile.write(htmlFooter)
htmlFile.close()
