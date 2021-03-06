# Guidelines for interpreting the licenses

The licenses are interpreted only by using the information provided in the `rights` field of the dataset metadata. If a link is provided, the linked document is also used in the interpretation. No contact is made with the data publisher or owner.

*Note: All examples below are actual provided licenses.*

## Standard license

The license is interpreted as a standard license ([Creative Commons](http://creativecommons.org/licenses/) or [Open Data Commons](http://opendatacommons.org/licenses/)) if a link to such license is provided or if the license name or abbreviation is used.

> * Este trabajo está licenciado bajo una licencia Creative Commons Zero (CC0) 1.0  http://creativecommons.org/publicdomain/zero/1.0/legalcode
> * http://creativecommons.org/publicdomain/zero/1.0/ & http://www.canadensys.net/norms
> * cc-by-nc-nd
> * The Tree of Life Project owns the copyright for the ToL Tree Structure XML File. This file is made available to the public under the terms of the Attribution-NonCommercial Creative Commons License. This license allows people to copy, modify, and redistribute the ToL tree structure, subject to some restrictions.

For those standard licenses, the standard URL of the license is provided. If the license mentions a specific version or region, the corresponding URL is provided, otherwise the URL of the current version is provided.

rights | standard license
--- | ---
CC-BY | [http://creativecommons.org/licenses/by/3.0/](http://creativecommons.org/licenses/by/3.0/)
Tall Timbers data is governed by the Creative Commons Attribution 3.0 license (http://creativecommons.org/licenses/by/3.0/legalcode). Any use of data or images must be attributed to Tall Timbers Research Station and Land Conservancy. | [http://creativecommons.org/licenses/by/3.0/](http://creativecommons.org/licenses/by/3.0/)
Data supplied is licensed under the Creative Commons Attribution 3.0 Australia License. | [http://creativecommons.org/licenses/by/3.0/au/](http://creativecommons.org/licenses/by/3.0/au/)
Tela Botanica a choisi de publier par défaut son contenu sous licence libre Creative Commons (by-sa) afin d'en faciliter la divulgation : http://creativecommons.org/licenses/by-sa/2.0/fr/ | [http://creativecommons.org/licenses/by-sa/2.0/fr/](http://creativecommons.org/licenses/by-sa/2.0/fr/)

## License characteristics

The licenses are interpreted using the following parameters, which can be set to `true`, `false`, or `?` (= unclear). These parameters are not entirely independent from each other:

    - use
        ↳ (re)distribution
        ↳ derivatives
        ↳ commercial (use)
        ↳ attribution
        ↳ share alike
    - notification

Some licenses are too unclear to set those parameters (see last section).

For the analysis and [charts](http://datafable.com/gbif-data-licenses/charts/index.html), those parameters are interpreted as:

parameter | open | restricted/required | unclear
--- | --- | --- | --- 
use | true | false | ?
distribution | true | false | ?
derivatives | true | false | ?
commercial | true | false | ?
attribution | false | true | ?
share alike | false | true | ?
notification | false | true | ?

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

Data use is interpreted as false if all rights are reserved or if contact is explicitly required before using the data.

> * These data are Copyright by the California Academy of Sciences, with all rights reserved.
> * Data may not be used without permissionContact info@mantamatcher.org
> * Terms of use Ghana Herbarium data: all rights on this data file belong to the University of Ghana / Ghana Herbarium. Please contact the Herbarium data manager before secondary usage of data in electronic or printed form.
> * Contact us before using the data

### Unclear

Data use is interpreted as unclear if it is only allowed for parts of the data or if the scope of the use is unclear.

> * Data records made available from Tiira Bird Observation System for the GBIF Data Portal may be used by individual researchers or research groups for scientific non-commercial purposes only. […] If this data **comprises an essential part of the work**, a priori consent must be obtained, and the possibility of joint work negotiated. Any other purposes of use are forbidden in any form without the explicit written consent of BirdLife Finland. […] BirdLife Finland has the right of use to these data records.
> * […] Except as otherwise expressly stated herein, material from the Databases may not be reproduced, distributed, publicly displayed or otherwise used , in whole or in part, without the express written permission of the Academy.Subsets of the records in one or more of the Databases may be used, downloaded, reproduced, publicly displayed, distributed or reprinted by persons affiliated with academic and/or non-profit organizations for scientific and scholarly purposes only, provided however, that the following attribution appears in all copies: "Information provided with the permission of The Academy of Natural Sciences, Philadelphia, PA." Nevertheless, the Academy does not grant permission for anyone to use, download, reproduce, publicly display, distribute or reprint **all or substantially all** of the records in one or more of the Databases. […]
> * […] Not to use data contained in OBIS-SEAMAP **in any publication** without the written consent of the original data provider. […]
> * Please contact Dr. G.M. Dirkse gerard.dirkse@natuurmuseum.nl before use of the data in **electronic files or printed publications**.
> * Owner **grants GBIF** a worldwide, non-exclusive right to: (i) use,        reproduce, perform, display, archive, transmit and distribute the        Content (including any trademarks, tradenames and logos in the        Content) in electronic form in connection with the Site, (ii) allow        **users of the Site** to use, search, copy, download and transmit the        Content, and (iii) modify and reformat the Content, but solely to the        extent necessary and for the purposes of: (a) conforming to the format        and "look and feel" of the Site, and (b) creating snippets, headlines        or teasers consisting of selected lines or sections from the Content        to be displayed on the Site (or displayed on other websites owned by        GBIF for the purposes of directing traffic to the Site).

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
> * […] No part of this data base may be copied or **reproduced** without written permission from the legal owner. […]

### Unclear

Data distribution is interpreted as unclear if use is unclear or if there are conflicting or dubious statements in the license.

> * […] These records are intended for use in education and research and **may not be** repackaged, **redistributed**, or sold in any form without prior written consent from the collection(s) holding such data. […] For Terms of Use specific to the Museum of Vertebrate Zoology, see **http://mvz.berkeley.edu/PDFs/MVZ_terms_of_use.pdf**
> * For scientific and noncommercial purposes, the database can be **consulted** freely. […]

## Derivatives

### True

Creating derivatives is interpreted as true for applicable standard licenses, if no restrictions are imposed, if it is explicitly allowed for all data, or if the GBIF use agreement is referenced.

### False

Creating derivatives is interpreted as false for standard licenses with a non-derivatives clause (such as [CC BY-ND](http://creativecommons.org/licenses/by-nd/3.0/)), if it is explicitly forbidden, if all rights are reserved, or use is set to false.

> * These data are copyright by the California Academy of Sciences, with all rights reserved.
> * UCMP data records may be used by individual researchers or research groups, but they may not be **repackaged**, resold, or redistributed in any form without the express written consent of the UCMP director or designate. […]
> * Use of the data for commercial or for-profit applications are permitted only via written permission from Instituto de Investigação Científica Tropical. Data are provided to users, but should not be passed on to third parties or redistributed. It is explicitly **forbidden to incorporate these data** into other databases of free or restricted access.

### Unclear

Creating derivatives is interpreted as unclear if use is unclear or if there are conflicting or dubious statements in the license.

> * […] No part of this data base may be **copied or reproduced** without written permission from the legal owner. […]
> * For scientific and noncommercial purposes, the database can be **consulted** freely. […]

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

Attribution required is interpreted as true for standard licenses with an attribution clause (such as [CC BY](http://creativecommons.org/licenses/by/3.0/)), if it is explicitly required, or if the GBIF use agreement is referenced.

> * The data in this dataset is free to share, modify and use on the only condition that the data creators are attributed in citation and acknowledgement.
> * […] If any of these records are used in an analysis or report, **the provenance of the original data must be acknowledged** and the PSM notified. […]
> * Acknowledge the use of records from this dataset in the form appearing in the 'Citation' field and acknowledge this use of the OBIS facility. Recognise the limitations of data in OBIS.
> * The copyright for any material created by the DSMZ is reserved. The duplication or use of information and data such as texts or images is only permitted with the indication of the source or with prior approval by the DSMZ.
> * Data may be used for non-commercial purposes only, with appropriate credit given to the Atlas project partners. […]
> * Proper citation of web resource.
> * No restrictions (Dataset must be cited)
> * When using the data please refer to the 'Dutch Vegetation Database' as managed by Alterra, Wageningen, The Netherlands.

### False

Attribution required is interpreted as false if a standard public domain waiver is used (such as [CC0](http://creativecommons.org/publicdomain/zero/1.0/)), if there are no restrictions, or if attribution is not required, nor hinted at.

> * Este trabajo está bajo una licencia Creative Commons Zero (CC0) 1.0  http://creativecommons.org/publicdomain/zero/1.0/legalcode
> * ITIS data is in the public domain
> * The use of the data is allowed only for non-profit scientific use and for non-profit nature conservation purpose.
> * Use of the data for commercial or for-profit applications are permitted only via written permission from Instituto de Investigação Científica Tropical. Data are provided to users, but should not be passed on to third parties or redistributed. It is explicitly forbidden to incorporate these data into other databases of free or restricted access.

### Unclear

Attribution required is interpreted as unclear if use is unclear, if it is only hinted at, or only required for substantial or special use of the data.

> * free according to the standards of scientific publications
> * Data are freely available through GBIF and through the AADC web site. If **substantial parts** of the database is used for other data or information products, please acknowledge the source.
> * Please contact R.M. Lopes for additional details on proper dataset citation
> * Please acknowledge NIWA if used for commercial purposes.

## Share alike

### True

Share alike required is interpreted as true for standard licenses with a share alike clause (such as [CC BY-SA](http://creativecommons.org/licenses/by-sa/3.0/)).

> * Los datos de este recurso están sujetos a la licencia CC BY-NC-SA 3.0 (http://creativecommons.org/licenses/by-nc-sa/3.0/)

### False

Share alike required is interpreted as false for standard licenses without a share alike clause (such as [CC BY-NC](http://creativecommons.org/licenses/by-nc/3.0/)), if a standard public domain waiver is used (such as [CC0](http://creativecommons.org/publicdomain/zero/1.0/)), or if there are no restrictions or requirements (optionally with a liability disclaimer only).

> * CC-BY
> * cc0 Creative Commons No copyright
> * ITIS data is in the public domain
> * Commercially available
> * free
> * The dataset enclosed within this package/transmission are only as good as the quality assurance and quality control procedures outlined by the enclosed metadata reporting statement. The user bears all responsibility for its subsequent use/misuse in any further analyses or comparisons. The Federal Government does not assume liability to the Recipient or third persons, nor will the Federal Government indemnify the Recipient for its liability due to any losses resulting in any way from the use of this dataset.

### Unclear

Share alike required is interpreted as unclear in all other cases, as it is unclear if distributed or derivative data should use the same or similar license.

> * Open data [does not exclude share alike]
> * A copy of final article paper, book, etc to be forwarded to data provider. [notification requirement]
> * Any data gained from the results of the European Moth Nights and the full text or shortened version of the relevant scientific balance complete with maps may be freely used for further scientific, nature conservancy or educational purposes. Only the indic

## Notification

### True

Notification is interpreted as true if it is explicitly required.

> * […] If any of these records are used in scientific analysis or report, the provenance of the original data must be acknowledged and the publication or report sent to BirdLife Finland […]
> * […] If any of these records are used in an analysis or report, the provenance of the original data must be acknowledged and the PSM notified. […]
> * […] If these data comprise a significant part of data used in publication, the creator of this resource must be given the possibility to comment a manuscript, and offered the possibil

### False

Notification is interpreted as false if use is allowed, but notification is not explicitly required.

### Unclear

Notification is interpreted as unclear if contact is required, either because the license is unclear or data use is not allowed.

## License unclear

If the license is unclear for any of the reasons below, then all field are set to `?` except for `standard license` which is left empty.

The license is not indicated or the link to the license is broken.

> * [empty, not supplied]
> * none
> * No information
> * http://www.zoo.cam.ac.uk/museum/collections.archives/academic.use/

The license is unclear or is not a license at all

> * No
> * Not available until published
> * Freely available after moratorium period
> * BfN/NetPhyD
> * Usage of Taiwan Forestry Research Institute.
> * Alpha version! Use at own risc.
> * The Borror Laboratory of Bioacoustics provides high-quality copies of recordings for research, education, management, and other uses. Please contact us at borrorlab.osu.edu 01 614 292 2176 to make requests or inquiries.
> * The MNCN does not guarantee the accuracy of these data. Individual researchers should verify individual records by making direct reference to corresponding museum specimens.
> * Contact Metafro team
> * RGM_GERTH version 2008-05-03Contact Dr. W. Renema
> * RGM_MIJNWEZEN version 2008-05-07Richtlijnen / voorwaarden onder welke de database kan worden gebruikt, eventueel naam van contactpersoon voor meer info.

The license only indicates the (copyright) owner, but does not specify how the data can be used. Chances are high it is "All rights reserved".

> * Staatliches Museum für Naturkunde Karlsruhe
> * Copyright of the Corvids Literature Database: Gabriele Droege.
> * Copyright © 2012 The President and Fellows of Harvard College
> * Copyright to this data is asserted by the State of Western Australia on behalf of the Western Australian Herbarium, Department of Environment and Conservation. Please review the copyright before using the data.

The license applies to something other than the data.

> * All commercial use of images must be cleared with Dr. Patterson. dpatterson@mbl.edu
> * http://www.fieldmuseum.org/linking_policy.htm
> * http://www.fonozoo.com/eng/faq.php
