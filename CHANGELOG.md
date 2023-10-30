# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [1.12.0] - 2023-10-11
- feature/integrity-pajak [abdur.rasyid@majoo.id]
### Changed
- configs
    - prod
        - laporan-pajak.json ``config process group etl pajak``
        - dashboard-penjualan.json ``add nifi config stream``
    - beta
        - laporan-pajak.json ``config process group etl pajak``
        - dashboard-penjualan.json ``add nifi config stream``

## [1.11.1] - 2023-10-10
- feature/change-default-state [muhammad.muzakki@majoo.id]
### Changed
- configs
    - prod
        - datamart-busiest-item-time-postgres.json
        - datamart-busiest-selling-postgres.json
        - laporan-order-type-postgres.json
        - laporan-product-v2.json
        - laporan-promo-kupon-poin-postgres.json
        ``change default state from RUNNING to STOPPED``

## [1.11.0] - 2023-10-06
- feature/integrity-pajak [wikan.kuncara@majoo.id]
### Changed
- configs
    - prod
        - integrity-pajak.json ``feature: integrity pajak``

## [1.10.0] - 2023-10-05
- feature/add-promo-stream [akbar.noto@majoo.id]
### Changed
- configs/*/laporan-promo-kupon-poin-postgres.json `` Add nifi for promo stream ``

## [1.9.2] - 2023-10-04
- feature/akunting-v2 [akbar.noto@majoo.id]
### Changed
- configs/*/laporan-akunting-postgres.json `` Add v2 nifi group processor ``

## [1.9.1] - 2023-09-19
- feature/recovery-promo-klopos [wikan.kuncara@majoo.id]
- maintenance/validity-recovery [abdur.rasyid@majoo.id]
### Added
- configs
    - beta
        - validity.json `config validity etl`
        - recovery.json `config recovery etl`
    - prod
        - validity.json `config validity etl`
        - recovery.json `config recovery etl`
        - recovery-promo-klopos.json ``feature: recovery promo klopos``
### Changed
- main.py `remove config validity & recovery on beta & prod`

## [1.9.0] - 2023-09-14
- feature/recovery-product-sales-hourly [wikan.kuncara@majoo.id]
### Added
- configs/beta/recovery-product-sales-hourly.json ``feature: recovery product sales hourly``
- configs/prod/recovery-product-sales-hourly.json ``feature: recovery product sales hourly``

## [1.8.0] - 2023-09-13
- coldfix/turnoff-all-beta [akbar.noto@majoo.id]
- feature/recovery-promo [muhammad.muzakki@majoo.id]
- feature/payment-type [muhammad.muzakki@majoo.id]
- feature/etl-payment-type [muhammad.muzakki@majoo.id]
- feature/hutang-piutang [akbar.noto@majoo.id]
### Added
- configs/beta/laporan-payment-type.json
- configs/beta/recovery-promo-komplimen.json
- configs/beta/recovery-promo-produk.json
- configs/beta/recovery-promo-promo.json
- configs/prod/laporan-payment-type.json
- configs/prod/recovery-promo-komplimen.json
- configs/prod/recovery-promo-produk.json
- configs/prod/recovery-promo-promo.json
``add promo recovery configuration for komplimen, jenis bayar, produk, and promo report``
- configs/*/laporan-akunting-hutang-piutang.json `` add for hutang piutang on staging & prod ``
### Changed
- configs/beta/*.json ``turning off (change to STOPPED) all beta configs ``

## [1.7.0] - 2023-08-30
- feature/etl-dashboard [abdur.rasyid@majoo.id]
### Added
- configs
    - beta
        - dashboard-penjualan.json ``config process group etl dashboard``
    - prod
        - dashboard-penjualan.json ``config process group etl dashboard``
### Changed
- main.py ``chane location process group ``

## [1.6.2] - 2023-08-30
- Ahmad-Irsyadur-Roziqin/jenkinsfile-edited-online-with-bitbucket-1693313015249 [ahmad.roziqin@majoo.id]
### Changed
- Jenkinsfile ``Edit sleep dan scale 0 set image k8s staging dan prod, utk improv nifi config bs auto set ketika ui restart``

## [1.6.1] - 2023-07-31
- feature/delete-outlet-v2 [wikan.kuncara@majoo.id]
- maintenance/validity-recovery [abdur.rasyid@majoo.id]
### Changed
- configs
    - beta
        - laporan-penjualan-outlet-postgres.json
        ``feature: delete etl outlet v1``
    - prod
        - laporan-outlet-postgres.json
        ``feature: delete etl outlet v1``
- Controller
    - Beta_NiFiValidity
    ``change name and config``
    - NiFiValidity
    ``change name and config``
- main.py
``state validity from STOPPED to RUNNING``

## [1.6.0] - 2023-07-14
- maintenance/validity-recovery [abdur.rasyid@majoo.id]
### Changed
- Controller
    - Beta_NiFiRecovery.py
    ``Add recovery Busiest Item Time``
    ``Add recovery Compliment``
    ``Add recovery Outlet Sales``
    ``Add recovery Product Sales``
    ``Add recovery Summary Reservation``
    ``Add recovery Transaction Type``
    ``Add recovery Utilization``
    - Beta_NiFiValidity.py
    ``Add validity Busiest Item Time``
    ``Add validity Compliment``
    ``Add validity Outlet Sales``
    ``Add validity Product Sales``
    ``Add validity Summary Reservation``
    ``Add validity Transaction Type``
    ``Add validity Utilization``
    - NiFiRecovery.py
    ``Add recovery Busiest Item Time``
    ``Add recovery Compliment``
    ``Add recovery Outlet Sales``
    ``Add recovery Product Sales``
    ``Add recovery Summary Reservation``
    ``Add recovery Transaction Type``
    ``Add recovery Utilization``
    - NiFiValidity.py
    ``Add validity Busiest Item Time``
    ``Add validity Compliment``
    ``Add validity Outlet Sales``
    ``Add validity Product Sales``
    ``Add validity Summary Reservation``
    ``Add validity Transaction Type``
    ``Add validity Utilization``
- Main.py
``Add execution config prod Busiest Item Time``
``Add execution config prod Compliment``
``Add execution config prod Outlet Sales``
``Add execution config prod Product Sales``
``Add execution config prod Summary Reservation``
``Add execution config prod Transaction Type``
``Add execution config prod Utilization``
``Add execution config beta Busiest Item Time``
``Add execution config beta Compliment``
``Add execution config beta Outlet Sales``
``Add execution config beta Product Sales``
``Add execution config beta Summary Reservation``
``Add execution config beta Transaction Type``
``Add execution config beta Utilization``

## [1.5.0] - 2023-07-11
- feature/etl-harian [akbar.noto@majoo.id]
- feature/etl-outlet-v2 [wikan.kuncara@majoo.id]
### Added
- configs
    - beta
        - laporan-harian.json
    - prod
        - laporan-harian.json
        - laporan-outlet-v2.json

## [1.4.0] - 2023-07-10
- feature/etl-utilisasi [abdur.rasyid@majoo.id]
### Added
- configs
    - beta
        - laporan-utilisasi.json
    - prod
        - laporan-utilisasi.json

## [1.3.0] - 2023-06-23
- feature/etl-snbn [muhammad.muzakki@majoo.id]
- coldfix/akunting-prod-specs [akbar.noto@majoo.id]
### Added
- configs
    - beta
        - laporan-batch-serial-number-postgres.json
    - prod
        - laporan-batch-serial-number-postgres.json
### Changed
- configs
    - beta
        - laporan-order-type-postgres.json
        ``change the state : STOPPED TO RUNNING``
    - prod
        - laporan-order-type-postgres.json
        ``change the state : STOPPED TO RUNNING``
        - laporan-akunting-jurnal-postgres.json
        ``change config deafult resource usage``
        - laporan-akunting-postgres.json
        ``change config deafult resource usage``

## [1.2.0] - 2023-06-13
- feature/subextras [akbar.noto@majoo.id]
- feature/etl-order-type [muhammad.muzakki@majoo.id]
- feature/etl-outlet-v2 [wikan.kuncara@majoo.id]
### Added
- configs
    - beta
        - laporan-order-type-postgres.json
        - laporan-outlet-v2.json
    - prod
        - laporan-order-type-postgres.json
        - laporan-subextra.json

## [1.1.0] - 2023-06-08
- hotfix/deploy-prod [akbar.noto@majoo.id]
### Changed
- main.py
``remove print()``

## [1.0.0] - 2023-05-31
- inisiasi tbd [grandis@majoo.id]
