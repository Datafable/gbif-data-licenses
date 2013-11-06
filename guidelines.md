# Guidelines for interpreting the licenses

The licenses are interpreted only by using the information provided in the `rights` field of the dataset metadata. If a link is provided, the linked document is also used in the interpretation. No contact is made with the data publisher or owner.

## License parameters

The licenses are interpreted using the following parameters, which can be set to `true`, `false` or `?` (= unclear). These parameters are not entirely independent from each other:

    - (is a) standard license
    - (data) use (allowed) 
        ↳ (re)distribution (allowed)
              ↳ share alike (required)
        ↳ (creating) derivatives (allowed)
        ↳ commercial (use allowed)
        ↳ attribution (required)
    - notification (required)

Some licenses are too unclear to set those parameters (see last section).

## Standard license

### True

The license is interpreted as a standard license ([Creative Commons](http://creativecommons.org/licenses/) or [Open Data Commons](http://opendatacommons.org/licenses/)) if a link to such license is provided or if the license name or abbreviation is used.

> * Este trabajo está licenciado bajo una licencia Creative Commons Zero (CC0) 1.0  http://creativecommons.org/publicdomain/zero/1.0/legalcode
> * http://creativecommons.org/publicdomain/zero/1.0/ & http://www.canadensys.net/norms
> * cc-by-nc-nd
> * The Tree of Life Project owns the copyright for the ToL Tree Structure XML File. This file is made available to the public under the terms of the Attribution-NonCommercial Creative Commons License. This license allows people to copy, modify, and redistribute the ToL tree structure, subject to some restrictions.

### False

All other licenses.

### Unclear

n/a

## Use

### True

Data use is interpreted as true for all standard licenses (see above), if no restrictions are imposed, if use (even with some restrictions) is explicitly allowed for all data, or if the GBIF use agreement is referenced.

> * Data from this dataset may be used and shared freely when the creators of the data are attributed correctly.
> * Open data
> * Unrestricted
> * The use of the data is allowed only for non-profit scientific use and for non-profit nature conservation purpose.
> * PSM data records may be used by individual researchers or research groups, but they may not be repackaged, resold, or redistributed in any form without the express written consent of a curatorial staff member of the PSM. […]
> * […] These records are intended for use in education and research and may not be repackaged, redistributed, or sold in any form without prior written consent from the collection(s) holding such data. […]
> * Data are provided for personal research only. Data may not be used for commercial purposes. Data may not be transferred to another database for distribution to others without prior written permission from the Canadian Museum of Nature.
> * GBIF Data Sharing Agreement is applied.  GBIF Data Use Agreement is applied.

### False

Data use is interpreted as false if all rights are reserved or if use (without contact) is explicitly forbidden.

> * These data are Copyright by the California Academy of Sciences, with all rights reserved.
> * Data may not be used without permissionContact info@mantamatcher.org
> * Terms of use Ghana Herbarium data: all rights on this data file belong to the University of Ghana / Ghana Herbarium. Please contact the Herbarium data manager before secondary usage of data in electronic or printed form.

### Unclear

Data use is interpreted as unclear if it is only allowed for parts of the data or if the scope of the use is unclear.

> * Data records made available from Tiira Bird Observation System for the GBIF Data Portal may be used by individual researchers or research groups for scientific non-commercial purposes only. […] If this data **comprises an essential part of the work**, a priori consent must be obtained, and the possibility of joint work negotiated. Any other purposes of use are forbidden in any form without the explicit written consent of BirdLife Finland. […] BirdLife Finland has the right of use to these data records.
> * […] Except as otherwise expressly stated herein, material from the Databases may not be reproduced, distributed, publicly displayed or otherwise used , in whole or in part, without the express written permission of the Academy.Subsets of the records in one or more of the Databases may be used, downloaded, reproduced, publicly displayed, distributed or reprinted by persons affiliated with academic and/or non-profit organizations for scientific and scholarly purposes only, provided however, that the following attribution appears in all copies: "Information provided with the permission of The Academy of Natural Sciences, Philadelphia, PA." Nevertheless, the Academy does not grant permission for anyone to use, download, reproduce, publicly display, distribute or reprint **all or substantially all** of the records in one or more of the Databases. […]
> * […] Not to use data contained in OBIS-SEAMAP **in any publication** without the written consent of the original data provider. […]

## Distribution

### True

Data distribution is interpreted as true for all standard licenses, if no restrictions are imposed, if it is explicitly allowed for all data, or if the GBIF use agreement is referenced.

> * No release restrictions
> * The use of the data is allowed only for non-profit scientific use and for non-profit nature conservation purpose.
> * The GRIN Taxonomy is public data with free and open access with no restrictions.
> * Data from this dataset may be used and shared freely when the creators of the data are attributed correctly.
> * Copyright 2013, National Biodiversity Data Centre, Waterford, Ireland. The information is free to use by individuals provided the owners of the data are acknowledged in any use of publication, or that the use of the data is cited in the following format […]
> * GBIF Data Use Agreement and GBIF Data Sharing Agreement apply.

### False

Data distribution is interpreted as false if it is explicitly forbidden, if all rights are reserved, or if use is set to false.

> * Release with permission of the appropriate parties.
> * Oregon State University data records may be used by individual researchers or research groups, but they **may not be** repackaged, resold, or **redistributed** in any form without the express written consent of a curator of the appropriate collection. […]
> * Data are provided for personal research only. Data may not be used for any commercial purposes. Data **may not be transferred** to another database for distribution to others without prior, written permission from the Canadian Museum of Nature.

### Unclear

Data distribution is interpreted as unclear if use is unclear or if there are conflicting statements in the license.

> * […] These records are intended for use in education and research and **may not be** repackaged, **redistributed**, or sold in any form without prior written consent from the collection(s) holding such data. […] For Terms of Use specific to the Museum of Vertebrate Zoology, see **http://mvz.berkeley.edu/PDFs/MVZ_terms_of_use.pdf**

## Derivatives

### True

Creating derivatives is interpreted as true for applicable standard licenses, if no restrictions are imposed, if it is explicitly allowed for all data, or if the GBIF use agreement is referenced.

### False

Creating derivatives is interpreted as false for standard licenses with a non-derivatives clause (such as [CC BY-ND](http://creativecommons.org/licenses/by-nd/3.0/)), if it is explicitly forbidden, if all rights are reserved, or use is set to false.

> * These data are copyright by the California Academy of Sciences, with all rights reserved.
> * UCMP data records may be used by individual researchers or research groups, but they may not be **repackaged**, resold, or redistributed in any form without the express written consent of the UCMP director or designate. […]
> * Use of the data for commercial or for-profit applications are permitted only via written permission from Instituto de Investigação Científica Tropical. Data are provided to users, but should not be passed on to third parties or redistributed. It is explicitly **forbidden to incorporate these data** into other databases of free or restricted access.

### Unclear

Creating derivatives is interpreted as unclear if use is unclear or if there are conflicting statements in the license.

## Commercial

### True

Commercial use is interpreted as true for applicable standard licenses, if no restrictions are imposed, if it is explicitly allowed for all data, or if the GBIF use agreement is referenced.

> * Commercially available
> * Copyright 2013, National Biodiversity Data Centre, Waterford, Ireland. The information is free to use by individuals provided the owners of the data are acknowledged in any use of publication, or that the use of the data is cited in the following format […]
> * Público
> * GBIF Data Use Agreement and GBIF Data Sharing Ageement apply

### False

Commercial use is interpreted as false for standard licenses with a non-commercial clause (such as [CC BY-NC](http://creativecommons.org/licenses/by-nc/3.0/)), if it is explicitly forbidden, if all rights are reserved, if use is restricted to non-profit or scholarly use, if contact is required, or use is set to false.

> * The use of the data is allowed only for non-profit scientific use and for non-profit nature conservation purpose.
> * Data are provided for personal research only. Data may not be used for commercial purposes. […]
> * […] Copying or redistributing MVZ Content in any manner for 
commercial use, including commercial publication, or for personal gain, is strictly prohibited. […]
> * Use of the data for commercial or for-profit applications **are permitted only via written permission** from Instituto de Investigação Científica Tropical. […]
> * The University of Texas at Arlington makes its records available for **scholarly research**. […]

### Unclear

Commercial use is interpreted as unclear if use is unclear, if the use clause can be commercial or non-commercial (e.g. `intended for use of individual researchers` or `for use in education`), or if data `may not be resold` (commercial use has a wider scope than selling data).

> * Data records from the Division of Ornithology of the University of Kansas Biodiversity Institute (KUBI) are provided for the **use of individual researchers or research groups**.
> * The data and media available through Arctos are the property of the originating institution, with all rights reserved. These records are intended for **use in education and research** […]
> * This work is licenced under a CreativeCommons Licence.
> * MHP data records may be used by individual researchers or research groups, but they **may not** be repackaged, **resold**, or redistributed in any form without the express written consent of a curatorial staff member of the MHP Mammal Collection. If any of these records are used in an analysis or report, the provenance of the original data must be acknowledged and MHP notified. The Sternberg Museum of Natural History and its staff are not responsible for damages, injury or loss due to the use of these data.

## Attribution

### True

### False

### Unclear

## Share alike

### True

### False

### Unclear

## Notification

### True

Notification is interpreted as true if it is explicitly required.

> * […] If any of these records are used in scientific analysis or report, the provenance of the original data must be acknowledged and the publication or report sent to BirdLife Finland […]
> * […] If any of these records are used in an analysis or report, the provenance of the original data must be acknowledged and the PSM notified. […]

### False

Notification is interpreted as false if use is allowed, but notification is not explicitly required.

### Unclear

Notification is interpreted as unclear if contact is required, either because the license is unclear or data use is not allowed.

## License unclear

If the license is unclear for any of the reasons below, then all field are set to `?` except for `standard license` which is set to `false`.

The license is not indicated or applies to something other than the data.

> * not supplied
> * none
> * No information
> * All commercial use of images must be cleared with Dr. Patterson. dpatterson@mbl.edu
> * Alpha version! Use at own risc.
> * http://www.fieldmuseum.org/linking_policy.htm

The license is unclear.

> * No
> * Not available until published
> * BfN/NetPhyD
> * Usage of Taiwan Forestry Research Institute.

The license only indicates the (copyright) owner, but does not specify how the data can be used. Chances are high it is "All rights reserved".

> * Staatliches Museum für Naturkunde Karlsruhe
> * Copyright of the Corvids Literature Database: Gabriele Droege.
> * Copyright © 2012 The President and Fellows of Harvard College
> * Copyright to this data is asserted by the State of Western Australia on behalf of the Western Australian Herbarium, Department of Environment and Conservation. Please review the copyright before using the data.
