# Guidelines for interpreting the licenses

The licenses are interpreted only by using the information provided in the `rights` field of the dataset metadata. If a link is provided, the linked document is also used in the interpretation. No contact is made with the data publisher or owner.

The licenses are interpreted using the following parameters, which can be set to `true`, `false` or `?` (= unclear):

* is a `standard license`?
* data `use` allowed?
* data (re)`distribution` allowed?
* `derivatives` allowed?
* `commercial` use allowed?
* `attribution` required?
* `share alike` required?
* `notification` required?

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

Data use is interpreted as unclear if it is only allowed for parts of the data.

> * Data records made available from Tiira Bird Observation System for the GBIF Data Portal may be used by individual researchers or research groups for scientific non-commercial purposes only. […] If this data **comprises an essential part of the work**, a priori consent must be obtained, and the possibility of joint work negotiated. Any other purposes of use are forbidden in any form without the explicit written consent of BirdLife Finland. […] BirdLife Finland has the right of use to these data records.
> * […] Except as otherwise expressly stated herein, material from the Databases may not be reproduced, distributed, publicly displayed or otherwise used , in whole or in part, without the express written permission of the Academy.Subsets of the records in one or more of the Databases may be used, downloaded, reproduced, publicly displayed, distributed or reprinted by persons affiliated with academic and/or non-profit organizations for scientific and scholarly purposes only, provided however, that the following attribution appears in all copies: "Information provided with the permission of The Academy of Natural Sciences, Philadelphia, PA." Nevertheless, the Academy does not grant permission for anyone to use, download, reproduce, publicly display, distribute or reprint **all or substantially all** of the records in one or more of the Databases. […]

## Distribution

### True

Data distribution is interpreted as true for all standard licenses, ...

### False

Data distribution use is interpreted as false if it is explicitly forbidden.

> * Release with permission of the appropriate parties.

### Unclear

## Derivatives

### True

### False

### Unclear

## Commercial

### True

### False

### Unclear

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
